# backend/scripts/ingest_vectors.py

import os
import re
import asyncio
import markdown
from bs4 import BeautifulSoup
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import PointStruct
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Configuration from backend/src/config/qdrant.py
from backend.src.config.qdrant import get_qdrant_client, COLLECTION_NAME, VECTOR_SIZE, create_qdrant_collection
from backend.src.models.content import Chapter
from backend.src.models.content_metadata import ContentMetadata

# OpenAI Embedding Model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")
openai.api_key = OPENAI_API_KEY

EMBEDDING_MODEL = "text-embedding-ada-002"

async def get_embedding(text: str) -> List[float]:
    """Generates an embedding for the given text using OpenAI."""
    try:
        response = await openai.Embedding.acreate(
            input=text,
            model=EMBEDDING_MODEL
        )
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return []

def extract_metadata_from_markdown(md_content: str) -> Dict[str, Any]:
    """Extracts frontmatter metadata from markdown content."""
    match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', md_content, re.DOTALL)
    if match:
        frontmatter_str = match.group(1)
        # Simple YAML parsing, could use a proper YAML library for robustness
        metadata = {}
        for line in frontmatter_str.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if value.startswith('[') and value.endswith(']'):
                    metadata[key] = [item.strip().strip("'"") for item in value[1:-1].split(',')]
                else:
                    metadata[key] = value.strip("'"")
        return metadata, match.group(2) # Return metadata and remaining content
    return {}, md_content

def chunk_text(text: str, chapter_metadata: ContentMetadata, max_tokens: int = 500, overlap: int = 50) -> List[Dict[str, Any]]:
    """
    Chunks text into smaller pieces for embedding, attempting to preserve semantic meaning.
    Adds chapter metadata to each chunk's payload.
    """
    # Convert markdown to plain text for more accurate token counting
    html = markdown.markdown(text)
    plain_text = BeautifulSoup(html, "html.parser").get_text()

    chunks = []
    current_chunk = []
    current_token_count = 0

    words = plain_text.split() # Simple split by word
    
    for word in words:
        word_token_count = len(word.split()) # Estimate token count by word count
        if current_token_count + word_token_count <= max_tokens:
            current_chunk.append(word)
            current_token_count += word_token_count
        else:
            chunks.append(" ".join(current_chunk))
            # Start new chunk with overlap for context
            current_chunk = current_chunk[-overlap:] + [word]
            current_token_count = len(" ".join(current_chunk).split())

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    # Prepare payload for each chunk
    chunked_data = []
    for i, chunk in enumerate(chunks):
        payload = chapter_metadata.model_dump() if chapter_metadata else {}
        payload.update({
            "chunk_id": f"{chapter_metadata.chapter_id if chapter_metadata else 'unknown'}_chunk_{i}",
            "text": chunk,
            "source_chapter_id": chapter_metadata.chapter_id if chapter_metadata else "unknown",
            "source_module_id": chapter_metadata.module_id if chapter_metadata else "unknown",
            "keywords": chapter_metadata.keywords if chapter_metadata and chapter_metadata.keywords else [],
            "learning_objectives": [obj.objective for obj in chapter_metadata.learning_objectives] if chapter_metadata and chapter_metadata.learning_objectives else [],
        })
        chunked_data.append(payload)
    return chunked_data

async def ingest_chapter_to_qdrant(client: QdrantClient, chapter_file_path: str):
    """Reads a Docusaurus markdown chapter, chunks it, embeds, and uploads to Qdrant."""
    with open(chapter_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    metadata_dict, content_text = extract_metadata_from_markdown(md_content)
    
    if not metadata_dict:
        print(f"Skipping {chapter_file_path}: No frontmatter metadata found.")
        return

    # Assuming 'id', 'title', 'module_id' are always present from metadata extraction
    # and mapping to ContentMetadata Pydantic model
    try:
        chapter_metadata = ContentMetadata(
            chapter_id=metadata_dict.get('id'),
            module_id=metadata_dict.get('module_id'),
            keywords=metadata_dict.get('keywords', []),
            learning_objectives=[LearningObjective(objective=obj) for obj in metadata_dict.get('learning_objectives', [])]
            # Add other fields from metadata_dict as needed, ensuring they match ContentMetadata
        )
    except Exception as e:
        print(f"Error parsing metadata for {chapter_file_path}: {e}")
        return

    # Combine content text with potentially useful metadata for embedding
    text_to_chunk = f"{chapter_metadata.title}. {content_text}"
    
    chunks = chunk_text(text_to_chunk, chapter_metadata)
    
    points_to_upsert = []
    for chunk_payload in chunks:
        chunk_text = chunk_payload["text"]
        embedding = await get_embedding(chunk_text)
        if embedding:
            points_to_upsert.append(
                PointStruct(
                    id=str(uuid.uuid4()), # Unique ID for each vector point
                    vector=embedding,
                    payload=chunk_payload
                )
            )
    
    if points_to_upsert:
        client.upsert(
            collection_name=COLLECTION_NAME,
            wait=True,
            points=points_to_upsert
        )
        print(f"Ingested {len(points_to_upsert)} chunks from {chapter_file_path} into Qdrant.")
    else:
        print(f"No chunks to ingest from {chapter_file_path}.")

async def main():
    qdrant_client = get_qdrant_client()
    create_qdrant_collection(qdrant_client)

    docs_base_path = "frontend/docs"
    
    # Iterate through all markdown files in the Docusaurus docs directory
    for root, _, files in os.walk(docs_base_path):
        for file in files:
            if file.endswith((".md", ".mdx")):
                chapter_file_path = os.path.join(root, file)
                await ingest_chapter_to_qdrant(qdrant_client, chapter_file_path)

if __name__ == "__main__":
    asyncio.run(main())
