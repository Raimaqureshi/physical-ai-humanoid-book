# backend/src/models/user.py

from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
import uuid
import datetime

class UserBase(BaseModel):
    email: EmailStr
    software_background: Optional[str] = Field(None, description="User's background in software engineering (e.g., 'beginner', 'intermediate', 'advanced').")
    hardware_robotics_background: Optional[str] = Field(None, description="User's background in hardware/robotics (e.g., 'none', 'hobbyist', 'professional').")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserInDB(UserBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    hashed_password: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    # Example for personalization preferences - can be more detailed
    personalization_preferences: Optional[Dict[str, Any]] = None

    class Config:
        json_encoders = {
            datetime.datetime: lambda dt: dt.isoformat() + "Z", # Ensure datetime is ISO formatted
        }
        from_attributes = True

class User(UserBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        json_encoders = {
            datetime.datetime: lambda dt: dt.isoformat() + "Z",
        }
        from_attributes = True

# JWT Token models (for authentication response)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None
