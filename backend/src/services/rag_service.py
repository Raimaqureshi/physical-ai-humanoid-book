# backend/src/services/rag_service.py

import os
from typing import List, Dict, Any, Optional
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from openai import OpenAI
from dotenv import load_dotenv

from backend.src.config.qdrant import COLLECTION_NAME, get_qdrant_client, VECTOR_SIZE
from backend.src.models.content import Query, ConversationalAIResponse

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

class RAGService:
    def __init__(self):
        self.qdrant_client: QdrantClient = get_qdrant_client()
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)
        self.embedding_model = "text-embedding-ada-002"
        self.llm_model = "gpt-3.5-turbo" # or gpt-4, etc.

    async def _get_embedding(self, text: str) -> List[float]:
        """Generates an embedding for the given text using OpenAI."""
        response = self.openai_client.embeddings.create(
            input=text,
            model=self.embedding_model
        )
        return response.data[0].embedding

    async def _retrieve_context(self, query_vector: List[float], limit: int = 3, context_filter: Optional[Filter] = None) -> List[Dict[str, Any]]:
        """Retrieves relevant text chunks from Qdrant based on the query embedding."""
        search_result = self.qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            query_filter=context_filter,
            limit=limit,
            with_payload=True # Ensure payload is returned for context reconstruction
        )
        return [hit.payload for hit in search_result]

    async def _generate_response_with_llm(self, user_query: str, context: str) -> str:
        """Generates a conversational AI response using the LLM with retrieved context."""
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant specialized in 'Physical AI & Humanoid Robotics' textbook content. "
                                          "Answer questions truthfully and accurately ONLY from the provided context. "
                                          "If the answer is not in the context, state that you don't know or that the information is not available in the textbook. "
                                          "Do not make up answers."},
            {"role": "user", "content": f"Based on the following textbook content, answer the question:\n\nContext: {context}\n\nQuestion: {user_query}"}
        ]
        
        response = self.openai_client.chat.completions.create(
            model=self.llm_model,
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content

    async def process_query(self, query: Query) -> ConversationalAIResponse:
        """
        Processes a user query through the RAG pipeline.
        
        Args:
            query: The user's query including text and context.
        
        Returns:
            A ConversationalAIResponse object with the generated answer and source references.
        """
        query_vector = await self._get_embedding(query.query_text)
        
        context_filter = None
        source_references = []

        if query.context_type == "chapter_specific" and query.context_reference:
            context_filter = Filter(
                must=[
                    FieldCondition(
                        key="source_chapter_id",
                        match=MatchValue(value=query.context_reference)
                    )
                ]
            )
            source_references.append(f"Chapter ID: {query.context_reference}")
        elif query.context_type == "selected_text" and query.context_reference:
            # For selected_text, the reference might be a chunk ID or a specific text segment identifier.
            # This is a simplification; in a real scenario, you'd search for the specific text chunk.
            context_filter = Filter(
                must=[
                    FieldCondition(
                        key="chunk_id", # Assuming context_reference is a chunk ID
                        match=MatchValue(value=query.context_reference)
                    )
                ]
            )
            source_references.append(f"Selected Text Context: {query.context_reference}")

        retrieved_chunks = await self._retrieve_context(query_vector, context_filter=context_filter)
        
        context_text = "\n\n".join([chunk["text"] for chunk in retrieved_chunks])
        
        # Populate source references from retrieved chunks
        for chunk in retrieved_chunks:
            if "source_chapter_id" in chunk:
                ref = f"Chapter ID: {chunk['source_chapter_id']}"
                if ref not in source_references:
                    source_references.append(ref)
            # You could add more granular references if available in payload
        
        response_text = await self._generate_response_with_llm(query.query_text, context_text)
        
        return ConversationalAIResponse(
            query_id=query.query_id,
            response_text=response_text,
            source_references=source_references if source_references else None,
            timestamp=query.timestamp
        )

# Initialize RAGService
rag_service = RAGService()
