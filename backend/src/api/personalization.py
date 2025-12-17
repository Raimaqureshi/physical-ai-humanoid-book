# backend/src/api/personalization.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional

from backend.src.services.personalization_service import personalization_service
from backend.src.services.content_service import content_service
from backend.src.models.content import Chapter
from backend.src.models.user import User # Assuming User model is available
from backend.src.api.auth import get_current_user # Dependency for authentication

router = APIRouter()

@router.post("/chapters/{chapter_id}/personalize", response_model=Chapter, status_code=status.HTTP_200_OK)
async def personalize_chapter(
    chapter_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Retrieves and personalizes a chapter's content based on the authenticated user's background.
    """
    chapter = await content_service.get_chapter(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID: {chapter_id} not found"
        )
    
    # current_user contains software_background and hardware_robotics_background
    personalized_chapter = await personalization_service.personalize_chapter_content(chapter, current_user)
    return personalized_chapter

# You would need to include this router in your main FastAPI application
# Example:
# from fastapi import FastAPI
# from .personalization import router as personalization_router
# app = FastAPI()
# app.include_router(personalization_router, prefix="/personalization", tags=["Personalization"])
