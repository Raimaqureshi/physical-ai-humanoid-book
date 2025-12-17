# backend/src/main.py

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

# Import routers from your API modules
from backend.src.api import auth, content, personalization, translation, ai

# Initialize FastAPI app
app = FastAPI(
    title="Physical AI & Humanoid Robotics Textbook API",
    description="Backend API for the AI-Native Textbook Platform.",
    version="0.0.1",
)

# CORS Configuration
# Adjust origins in a production environment
origins = [
    "http://localhost",
    "http://localhost:3000",  # Frontend Docusaurus development server
    "https://speckit-ai.github.io" # Frontend GitHub Pages deployment (TODO: Adjust to actual URL)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(content.router, prefix="/content", tags=["Content"])
app.include_router(personalization.router, prefix="/personalization", tags=["Personalization"])
app.include_router(translation.router, prefix="/translation", tags=["Translation"])
app.include_router(ai.router, prefix="/ai", tags=["Conversational AI"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Native Textbook API!"}

# Example of a protected endpoint (requires authentication)
# from backend.src.api.auth import get_current_user
# @app.get("/protected-route")
# async def protected_route(current_user: User = Depends(get_current_user)):
#     return {"message": f"Hello, {current_user.email}! This is a protected route."}
