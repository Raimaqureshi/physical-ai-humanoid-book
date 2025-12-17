# backend/src/models/content_metadata.py

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import uuid

class LearningObjective(BaseModel):
    objective: str = Field(..., description="A specific learning objective for the chapter.")

class Example(BaseModel):
    title: str
    description: Optional[str] = None
    url: Optional[str] = None
    code_snippet: Optional[str] = None

class Reference(BaseModel):
    title: str
    url: Optional[str] = None
    type: Optional[str] = None # e.g., "ROS 2", "Gazebo", "Isaac"

class Exercise(BaseModel):
    title: str
    description: Optional[str] = None
    difficulty: Optional[str] = None # e.g., "easy", "medium", "hard"
    solution_hint: Optional[str] = None # For practical exercises

class ContentMetadata(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the content metadata entry.")
    chapter_id: str = Field(..., description="ID of the chapter this metadata belongs to.")
    learning_objectives: Optional[List[LearningObjective]] = None
    real_world_examples: Optional[List[Example]] = None
    ros_gazebo_isaac_references: Optional[List[Reference]] = None
    practical_exercises: Optional[List[Exercise]] = None
    keywords: Optional[List[str]] = Field(None, description="Keywords for RAG and search.")
    difficulty: Optional[str] = Field(None, description="Overall difficulty of the chapter (e.g., 'beginner', 'intermediate', 'advanced').")
    estimated_reading_time_minutes: Optional[int] = Field(None, description="Estimated reading time in minutes.")
    prerequisites: Optional[List[str]] = Field(None, description="List of prerequisite chapter IDs or topics.")
    related_chapters: Optional[List[str]] = Field(None, description="List of related chapter IDs.")
    authors: Optional[List[str]] = None
    version: Optional[str] = None
    additional_metadata: Optional[Dict[str, Any]] = None # For any other arbitrary metadata
