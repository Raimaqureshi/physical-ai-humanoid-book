# backend/src/models/content.py

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import uuid

# Re-using the ContentMetadata schema for embedding within Chapter
from .content_metadata import LearningObjective, Example, Reference, Exercise, ContentMetadata

class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the book.")
    title: str = Field(..., description="Title of the book.")

class Module(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the module.")
    book_id: str = Field(..., description="ID of the book this module belongs to.")
    title: str = Field(..., description="Title of the module.")
    order: int = Field(..., description="Order of the module within the book.")

class Chapter(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the chapter.")
    module_id: str = Field(..., description="ID of the module this chapter belongs to.")
    title: str = Field(..., description="Title of the chapter.")
    order: int = Field(..., description="Order of the chapter within the module.")
    textual_content: str = Field(..., description="The main body of the chapter content (Markdown format).")
    metadata: Optional[ContentMetadata] = Field(None, description="Comprehensive metadata for the chapter.")

class Query(BaseModel):
    query_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the query.")
    user_id: Optional[str] = Field(None, description="ID of the user who made the query (if authenticated).")
    query_text: str = Field(..., description="The actual question text from the user.")
    context_type: str = Field(..., description="Indicates the scope of the query (e.g., 'entire_book', 'chapter_specific', 'selected_text').")
    context_reference: Optional[str] = Field(None, description="Reference to the specific content if context_type is not 'entire_book'.")
    timestamp: str = Field(..., description="Timestamp when the query was made (ISO 8601 format).")

class ConversationalAIResponse(BaseModel):
    response_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the response.")
    query_id: str = Field(..., description="ID of the query this response answers.")
    response_text: str = Field(..., description="The generated answer text.")
    source_references: Optional[List[str]] = Field(None, description="References to sections of the Textbook Content used to generate the answer.")
    timestamp: str = Field(..., description="Timestamp when the response was generated (ISO 8601 format).")
