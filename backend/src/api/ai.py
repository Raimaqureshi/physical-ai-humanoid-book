# backend/src/api/ai.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from backend.src.services.ai_agent import ai_agent_service
from backend.src.models.content import Query, ConversationalAIResponse

router = APIRouter()

# Placeholder for dependency to get current user ID
# In a real app, this would decode a JWT or session token
async def get_current_user_id() -> Optional[str]:
    # For now, return None (unauthenticated) or a fixed ID for testing
    return "mock_user_id" 

@router.post("/query", response_model=ConversationalAIResponse, status_code=status.HTTP_200_OK)
async def query_ai(
    user_query: Query,
    user_id: Optional[str] = Depends(get_current_user_id)
):
    """
    Sends a query to the conversational AI and returns its response.
    """
    if not user_query.query_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query text cannot be empty."
        )
    
    # Pass the user_id (even if mock) to the AI agent service
    response = await ai_agent_service.process_user_query(
        user_query_text=user_query.query_text,
        user_id=user_id,
        context_type=user_query.context_type,
        context_reference=user_query.context_reference
    )
    return response

# You would need to include this router in your main FastAPI application
# Example:
# from fastapi import FastAPI
# from .ai import router as ai_router
# app = FastAPI()
# app.include_router(ai_router, prefix="/ai", tags=["AI"])
