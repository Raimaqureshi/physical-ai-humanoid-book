# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a "Book + RAG Chatbot on Physical AI & Humanoid Robotics" project that combines a Docusaurus-based book with a RAG chatbot powered by FastAPI. The content covers ROS 2, Digital Twins (Gazebo/Unity), NVIDIA Isaac, Vision Language Models (VLAs), and humanoid robotics.

## Architecture

The project consists of:
- **Frontend**: Docusaurus website for book content (`website/` directory)
- **Backend**: FastAPI application for RAG chatbot (`chatbot_backend/` directory)
- **Storage**:
  - Neon (PostgreSQL) for RAG metadata
  - Qdrant (vector database) for semantic search
- **Content Generation**: Spec-Kit Plus for generating book content from feature specifications

## Development Commands

### Docusaurus Website
```bash
cd website/
npm install                    # Install dependencies
npm start                      # Start development server (localhost:3000)
npm run build                  # Build static site
```

### FastAPI Backend
```bash
# From chatbot_backend/ directory
python -m venv venv            # Create virtual environment
source venv/bin/activate       # Activate (Linux/Mac) or venv\Scripts\activate (Windows)
pip install -r requirements.txt # Install dependencies
uvicorn main:app --reload      # Start development server (localhost:8000)
```

### Docker Services
```bash
docker-compose up -d           # Start Qdrant and Neon services
docker-compose down            # Stop services
```

### Testing and Linting
```bash
cd chatbot_backend/src/
pytest                         # Run Python tests
ruff check .                   # Run Python linter
```

## Project Structure

```
specs/002-ros2-nervous-system/ # Feature specifications and plans
├── spec.md                    # Feature specification
├── plan.md                    # Implementation plan
├── tasks.md                   # Task breakdown
├── research.md                # Research findings
├── data-model.md              # Data models
├── quickstart.md              # Quickstart guide
└── contracts/openapi.yaml     # API contract

chatbot_backend/              # FastAPI backend (to be created)
├── src/
│   ├── models/               # Pydantic models
│   ├── services/             # Business logic
│   └── api/                  # FastAPI endpoints
└── tests/

website/                      # Docusaurus frontend (to be created)
├── docs/                     # Markdown content
├── src/
│   ├── components/           # Custom React components
│   └── pages/                # Custom pages
└── docusaurus.config.js
```

## Content Development Workflow

1. Create or update a feature specification in the `specs` directory
2. Use Spec-Kit Plus commands (`/speckit.specify`, `/speckit.plan`, `/speckit.implement`) to generate content
3. Review and edit the generated Markdown files in the `docs` directory
4. The generated content will be manually reviewed by a subject matter expert

## API Endpoints

The RAG chatbot exposes:
- `POST /query` - Accepts a question and returns an answer with source citations

## Key Technologies

- Python 3.11
- ROS 2 Humble (for robotics content)
- FastAPI (backend framework)
- Docusaurus (documentation site)
- Qdrant (vector database for semantic search)
- Neon (PostgreSQL for metadata)
- Spec-Kit Plus (specification-driven development)

## Project Constitution

All contributions must adhere to the project constitution which emphasizes:
- Technical accuracy based on official documentation
- Spec-driven writing approach
- Clear, instructional content for advanced learners
- No hallucinations - all content must be verifiable
- Structured, modular writing approach