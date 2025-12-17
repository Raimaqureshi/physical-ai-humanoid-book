# backend/src/config/qdrant.py

import os
from qdrant_client import QdrantClient, models

# Configuration for Qdrant connection
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None) # Optional, if using Qdrant Cloud

COLLECTION_NAME = "ai_textbook_chapters"
VECTOR_SIZE = 1536 # Example for OpenAI embeddings, adjust if using other models
DISTANCE_METRIC = models.Distance.COSINE # Or DOT, EUCLID, etc.

def get_qdrant_client() -> QdrantClient:
    """Initializes and returns a Qdrant client."""
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        prefer_grpc=True # Recommended for performance
    )
    return client

def create_qdrant_collection(client: QdrantClient):
    """Creates the Qdrant collection if it does not already exist."""
    collections = client.get_collections().collections
    if COLLECTION_NAME not in [c.name for c in collections]:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=DISTANCE_METRIC),
            # You might want to add payload_schema for filtering on metadata
            # payload_schema=models.PayloadSchemaType.KEYWORD
        )
        print(f"Created Qdrant collection: {COLLECTION_NAME}")
    else:
        print(f"Qdrant collection '{COLLECTION_NAME}' already exists.")

# Example usage (for local development/testing)
if __name__ == "__main__":
    client = get_qdrant_client()
    create_qdrant_collection(client)
