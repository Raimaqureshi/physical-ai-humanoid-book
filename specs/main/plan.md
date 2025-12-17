# Implementation Plan: AI-Native Textbook Platform

**Branch**: `main` | **Date**: 2025-12-17 | **Spec**: [specs/001-ai-textbook-platform/spec.md](specs/001-ai-textbook-platform/spec.md)
**Input**: Feature specification from `/specs/001-ai-textbook-platform/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The project aims to create an AI-native technical textbook platform for "Physical AI & Humanoid Robotics". This platform will deliver modular, university-grade content via a web interface, augmented by a conversational AI for Q&A, and support user authentication, personalization, and Urdu translation. The technical approach involves leveraging Docusaurus for the frontend, FastAPI for backend services, Qdrant Cloud for vector storage, Neon Serverless Postgres for user data, and OpenAI/ChatKit for AI functionality, all deployed on GitHub Pages.

## Technical Context

**Language/Version**: Python (for backend), JavaScript/TypeScript (for frontend)  
**Primary Dependencies**: Docusaurus, React, FastAPI, Qdrant Cloud, Neon Serverless Postgres, OpenAI Agents / ChatKit SDK, better-auth.com  
**Storage**: Neon Serverless Postgres (user data, metadata), Qdrant Cloud (vector embeddings)  
**Testing**: Pytest (Python unit/integration/API), Playwright (Python E2E), Jest (JS/TS unit/integration), React Testing Library (React components), Playwright (JS/TS E2E)  
**Target Platform**: Web browsers  
**Project Type**: Web application (frontend + backend)  
**Performance Goals**:
-   Page load times under 2 seconds.
-   Conversational AI response time under 3 seconds.
-   Urdu translation display within 5 seconds.
-   System availability: 99.9% uptime.
**Constraints**:
-   Content strictly follows course document.
-   Modular structure (4 modules, 4 chapters each).
-   No content hallucination.
**Scale/Scope**: Educational platform for "Physical AI & Humanoid Robotics" textbook, supporting individual users with personalization and translation features.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

-   **I. Modular, Structured, University-Grade Content**: PASSED. The spec defines a modular structure (4 modules, 4 chapters) and implies university-grade content.
-   **II. Course Document Adherence**: PASSED. The spec states content must strictly follow the provided course document.
-   **III. Consistent Module Structure**: PASSED. The spec mandates 4 modules and 4 chapters per module.
-   **IV. Comprehensive Chapter Content**: PASSED. The spec details chapter content (concept explanation, examples, ROS/Gazebo/Isaac, learning objectives, exercises).
-   **V. AI-Native Features & Accessibility**: PASSED. The spec includes conversational AI (RAG), personalization, Urdu translation, and content explanation based on background.
-   **Guiding Personas & Alignment**: PASSED. The spec implicitly considers these through the feature set.
-   **Content Integrity**: PASSED. The spec includes an edge case that the conversational AI must not answer outside the book's scope.

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-textbook-platform/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/           # Data models for users, content metadata, etc.
│   ├── services/         # Business logic for conversational AI, auth, personalization
│   └── api/              # FastAPI endpoints
└── tests/                # Backend tests

frontend/
├── src/
│   ├── components/       # React components for UI
│   ├── pages/            # Docusaurus pages
│   └── services/         # Frontend API clients, state management
└── tests/                # Frontend tests
```

**Structure Decision**: The project will adopt a decoupled frontend and backend architecture, with the frontend residing in `frontend/` and the backend in `backend/`. This aligns with the "Web application" option, allowing for clear separation of concerns and independent development.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|

## Execution Plan Phases

This plan outlines the execution in a phased approach, prioritizing core functionality to achieve a Minimum Viable Product (MVP) suitable for a hackathon timeframe, while also structuring for future expansion.

### Phase 1: Book Content Generation & Structure

**Goal**: Establish the foundational textbook content, its modular structure, and tools for management.

**Tasks**:
-   **Content Ingestion Strategy**: Define a process for converting raw course material into the structured format required by the platform (Markdown, potentially with custom Docusaurus components).
-   **Module & Chapter Creation**: Develop a template or script for generating the Docusaurus-compatible file structure for 4 modules, each with 4 chapters.
-   **Initial Content Population**: Populate a sample module/chapter to validate the structure and display.
-   **Metadata Definition**: Define comprehensive metadata for chapters (learning objectives, examples, references, exercises) to support AI features.
-   **Version Control Integration**: Ensure content is managed effectively within Git.

**Artifacts**:
-   Sample Docusaurus content files (`frontend/docs/`, `frontend/blog/`)
-   Content generation scripts/guidelines

### Phase 2: Frontend Setup & Core UI

**Goal**: Set up the Docusaurus frontend, establish basic navigation, and integrate a placeholder for the conversational AI.

**Tasks**:
-   **Docusaurus Project Initialization**: Set up the Docusaurus project within the `frontend/` directory.
-   **Basic Navigation**: Configure sidebar and routing to reflect the 4-module, 4-chapter structure.
-   **Content Display**: Ensure the generated textbook content is rendered correctly in Docusaurus.
-   **Conversational AI Placeholder**: Integrate a basic UI element for the conversational AI within chapter pages (e.g., a floating button or sidebar component) with no backend integration yet.
-   **Styling**: Apply basic styling consistent with a clean documentation layout.

**Artifacts**:
-   Initialized Docusaurus project (`frontend/`)
-   Basic Docusaurus configuration (`frontend/docusaurus.config.ts`, `frontend/sidebars.ts`)
-   Frontend components for content display and AI placeholder.

### Phase 3: Backend Services & Conversational AI Integration

**Goal**: Develop the core backend services, implement the RAG pipeline, and integrate the conversational AI with the frontend.

**Tasks**:
-   **FastAPI Backend Initialization**: Set up the FastAPI project within the `backend/` directory.
-   **Vector Database Setup (Qdrant Cloud)**: Configure Qdrant Cloud instance and develop a vector ingestion pipeline to load textbook content.
-   **RAG Pipeline Development**: Implement the Retrieval-Augmented Generation (RAG) pipeline using OpenAI Agents / ChatKit SDK to process queries and retrieve relevant textbook content from Qdrant.
-   **Conversational AI API Endpoint**: Create a FastAPI endpoint (`/ai/query`) that receives user queries, processes them through the RAG pipeline, and returns AI responses.
-   **Frontend-Backend AI Integration**: Connect the frontend conversational AI placeholder to the `backend/ai/query` endpoint, displaying responses and source references.
-   **Content API**: Implement basic FastAPI endpoints for fetching book, module, and chapter details (`/books`, `/modules`, `/chapters`).

**Artifacts**:
-   FastAPI application (`backend/`)
-   Qdrant Cloud configuration and ingestion scripts
-   RAG pipeline implementation
-   OpenAPI definitions for AI and Content APIs.

### Phase 4: Authentication & Personalization Features

**Goal**: Implement user authentication, personalization logic, and Urdu translation.

**Tasks**:
-   **User Authentication Integration**: Integrate better-auth.com for user signup and signin. Develop FastAPI endpoints for user management (`/auth/signup`, `/auth/signin`, `/auth/me`).
-   **User Profile Management**: Store user background information (software/robotics) in Neon Serverless Postgres during signup.
-   **Personalization Logic**: Develop backend logic to adapt chapter content based on user's background, using `personalization_preferences` from `data-model.md`.
-   **Personalization API Endpoint**: Create a FastAPI endpoint (`/chapters/{chapter_id}/personalize`) to deliver personalized content.
-   **Frontend Personalization Integration**: Connect the "Personalize content" button to the API and dynamically update chapter display.
-   **Urdu Translation API**: Implement a FastAPI endpoint (`/chapters/{chapter_id}/translate`) to provide Urdu translations of chapter content.
-   **Frontend Translation Integration**: Connect the "Translate content to Urdu" button to the API and dynamically display translated content.

**Artifacts**:
-   Authentication and Personalization API implementations
-   Database schemas for user profiles and preferences
-   Frontend integration for auth, personalization, and translation.

### Phase 5: Deployment & Demo Preparation

**Goal**: Deploy the platform, conduct final testing, and prepare for presentation.

**Tasks**:
-   **GitHub Pages Deployment**: Configure Docusaurus for deployment to GitHub Pages.
-   **Backend Hosting**: Deploy the FastAPI backend to a suitable cloud platform (e.g., Vercel, Render, AWS Lambda).
-   **End-to-End Testing**: Perform comprehensive E2E tests using Playwright to ensure all features work across the integrated system.
-   **Performance Testing**: Verify performance goals (page load, AI response times) are met.
-   **Demo Script & Presentation**: Prepare a script and materials for demonstrating the platform's features, highlighting the AI-native aspects.

**Artifacts**:
-   Deployed frontend and backend applications
-   E2E test reports
-   Demo materials.
