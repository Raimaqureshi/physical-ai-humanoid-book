# backend/src/api/content.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from backend.src.services.content_service import content_service
from backend.src.models.content import Book, Module, Chapter

router = APIRouter()

@router.get("/books", response_model=List[Book])
async def get_all_books():
    """
    Retrieves a list of all available books.
    """
    return await content_service.get_all_books()

@router.get("/books/{book_id}/modules", response_model=List[Module])
async def get_modules_for_book(book_id: str):
    """
    Retrieves a list of modules for a specific book.
    """
    modules = await content_service.get_modules_by_book_id(book_id)
    if not modules:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No modules found for book ID: {book_id}"
        )
    return modules

@router.get("/modules/{module_id}/chapters", response_model=List[Chapter]) # Returning full chapter for simplicity in mock
async def get_chapters_for_module(module_id: str):
    """
    Retrieves a list of chapters for a specific module.
    """
    chapters = await content_service.get_chapters_by_module_id(module_id)
    if not chapters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No chapters found for module ID: {module_id}"
        )
    return chapters

@router.get("/chapters/{chapter_id}", response_model=Chapter)
async def get_chapter_content(chapter_id: str):
    """
    Retrieves the full content of a specific chapter.
    """
    chapter = await content_service.get_chapter(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID: {chapter_id} not found"
        )
    return chapter

# You would need to include this router in your main FastAPI application
# Example:
# from fastapi import FastAPI
# from .content import router as content_router
# app = FastAPI()
# app.include_router(content_router, prefix="/content", tags=["Content"])
