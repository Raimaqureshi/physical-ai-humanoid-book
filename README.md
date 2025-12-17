# Speckit: Book and RAG Chatbot

This project contains the source code and specifications for a technical book and an integrated RAG (Retrieval-Augmented Generation) chatbot.

## Overview

- **Frontend**: A Docusaurus-based website that hosts the technical book.
- **Backend**: A FastAPI application that provides a RAG-based chatbot API over the book's content.

## Getting Started

### 1. Root Directory Setup
- Clone the repository.
- Ensure you have Node.js (for frontend) and Python 3.11+ (for backend) installed.

### 2. Frontend Setup (Docusaurus Book)
```bash
cd frontend
npm install
npm start
```
This will start the Docusaurus development server.

### 3. Backend Setup (FastAPI RAG Chatbot)
```bash
cd backend
# Create and activate virtual environment
# Use the appropriate command for your system (e.g., `python -m venv .venv` or `python3 -m venv .venv` or `py -m venv .venv`)
# The path to your python executable is: C:\Users\HASSAN COMPUTER\AppData\Local\Programs\Python\Python314\python.exe
# Example:
"C:\Users\HASSAN COMPUTER\AppData\Local\Programs\Python\Python314\python.exe" -m venv .venv
# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install Poetry (if not already installed)
pip install poetry

# Install backend dependencies using Poetry
poetry install

# Create a .env file from the template and fill in your details
cp .env.template .env
# Open .env and add your DATABASE_URL, QDRANT_HOST, QDRANT_PORT, OPENAI_API_KEY etc.

# Run database migrations (if any - not yet implemented)
# python -m alembic upgrade head

# Run the FastAPI application
poetry run uvicorn app.main:app --reload
```
This will start the FastAPI development server.
