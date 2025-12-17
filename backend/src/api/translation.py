# backend/src/api/translation.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional

from backend.src.services.translation_service import translation_service
from backend.src.services.content_service import content_service
from backend.src.models.content import Chapter
from backend.src.models.user import User # Assuming User model is available
from backend.src.api.auth import get_current_user # Dependency for authentication

router = APIRouter()

@router.post("/chapters/{chapter_id}/translate", response_model=Chapter, status_code=status.HTTP_200_OK)
async def translate_chapter(
    chapter_id: str,
    target_language: str, # Currently only 'ur'
    current_user: User = Depends(get_current_user) # Translation can be a premium feature
):
    """
    Retrieves and translates a chapter's content to the target language (currently only Urdu).
    """
    chapter = await content_service.get_chapter(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID: {chapter_id} not found"
        )
    
    # In a real app, you might check user's subscription or credits here
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required for translation."
        )

    try:
        translated_chapter = await translation_service.translate_chapter_content(chapter, target_language)
        return translated_chapter
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# You would need to include this router in your main FastAPI application
# Example:
# from fastapi import FastAPI
# from .translation import router as translation_router
# app = FastAPI()
# app.include_router(translation_router, prefix="/translation", tags=["Translation"])
