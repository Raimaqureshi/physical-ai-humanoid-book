# Tasks: AI-Native Textbook Platform

**Feature**: AI-Native Textbook Platform  
**Branch**: `main`  
**Date**: 2025-12-17  
**Plan**: [specs/main/plan.md](specs/main/plan.md)  
**Spec**: [specs/001-ai-textbook-platform/spec.md](specs/001-ai-textbook-platform/spec.md)

## Overall Implementation Strategy

The project will be developed iteratively following the outlined phases, prioritizing core user stories first to achieve an MVP. Parallel execution will be leveraged where task dependencies allow, primarily within feature-specific implementations.

## Phase: Setup (Project Initialization & Core Structure)

**Goal**: Establish the basic project structure and initialize core components.

- [x] T001 Initialize Docusaurus project in `frontend/`
- [x] T002 Initialize FastAPI project in `backend/`
- [x] T003 Create `backend/src/models/` directory
- [x] T004 Create `backend/src/services/` directory
- [x] T005 Create `backend/src/api/` directory
- [x] T006 Create `backend/tests/` directory
- [x] T007 Create `frontend/src/components/` directory
- [x] T008 Create `frontend/src/pages/` directory
- [x] T009 Create `frontend/src/services/` directory
- [x] T010 Create `frontend/tests/` directory

## Phase: Foundational (Blocking Prerequisites)

**Goal**: Configure essential infrastructure and environment settings required across the application.

- [x] T011 Set up Python virtual environment for `backend/`
- [x] T012 Configure `backend/requirements.txt` for FastAPI and other core Python dependencies
- [x] T013 Set up Node.js environment for `frontend/`
- [x] T014 Configure `frontend/package.json` for Docusaurus and React dependencies
- [x] T015 Define and document `.env.example` for `backend/`
- [x] T016 Define and document `.env.example` for `frontend/` (if needed)
-   [ ] T017 Initial commit of project boilerplate

## Phase: Book Content Generation & Structure (User's Phase 1)

**Goal**: Establish the foundational textbook content, its modular structure, and tools for management.

-   [ ] T018 Define content ingestion strategy (e.g., Markdown conversion guidelines) in `docs/content_strategy.md`
-   [ ] T019 Develop script/tool for Docusaurus module/chapter structure generation in `scripts/generate_content_structure.py`
-   [ ] T020 Generate initial 4 modules and 16 chapter placeholder markdown files in `frontend/docs/`
-   [ ] T021 Define comprehensive metadata schema for chapters (learning objectives, examples, references, exercises) in `backend/src/models/content_metadata.py`
-   [ ] T022 Populate sample content for one module (4 chapters) with rich metadata in `frontend/docs/sample_module/`

## Phase: Frontend Setup & Core UI (User's Phase 2) [US1]

**Goal**: Set up the Docusaurus frontend, establish basic navigation, and integrate a placeholder for the conversational AI, enabling basic textbook access.

-   [ ] T023 Configure Docusaurus sidebar navigation for 4 modules, 4 chapters per module in `frontend/sidebars.ts`
-   [ ] T024 Configure Docusaurus routing and theme in `frontend/docusaurus.config.ts`
-   [ ] T025 Implement Docusaurus pages for displaying generated textbook content in `frontend/src/pages/`
-   [ ] T026 Implement core UI components for chapter display (e.g., handling metadata, exercises) in `frontend/src/components/ChapterDisplay.tsx`
-   [ ] T027 [P] Create placeholder UI element for conversational AI (floating button/sidebar) in `frontend/src/components/AIChatPlaceholder.tsx`
-   [ ] T028 Apply basic styling for clean documentation layout in `frontend/src/css/custom.css`
-   [ ] T029 Implement frontend service to fetch textbook content from `backend/api/content` (initially mocked) in `frontend/src/services/content_service.ts`

## Phase: Backend Services & Conversational AI Integration (User's Phase 3) [US2]

**Goal**: Develop the core backend services, implement the RAG pipeline, and integrate the conversational AI with the frontend, enabling interactive Q&A.

-   [ ] T030 [P] Implement `Content` models based on `data-model.md` in `backend/src/models/content.py`
-   [ ] T031 [P] Implement basic CRUD operations for `Content` in `backend/src/services/content_service.py`
-   [ ] T032 Configure Qdrant Cloud connection in `backend/src/config/qdrant.py`
-   [ ] T033 Develop vector ingestion script for textbook content to Qdrant in `backend/scripts/ingest_vectors.py`
-   [ ] T034 Implement RAG pipeline core logic (embedding creation, similarity search) in `backend/src/services/rag_service.py`
-   [ ] T035 Integrate OpenAI Agents / ChatKit SDK for conversational AI in `backend/src/services/ai_agent.py`
-   [ ] T036 Implement `/ai/query` endpoint based on `contracts/ai.yaml` in `backend/src/api/ai.py`
-   [ ] T037 [P] Implement `/books`, `/modules/{module_id}/chapters`, `/chapters/{chapter_id}` endpoints based on `contracts/content.yaml` in `backend/src/api/content.py`
-   [ ] T038 Connect frontend `AIChatPlaceholder` to `backend/ai/query` endpoint in `frontend/src/components/AIChat.tsx`

## Phase: Authentication & Personalization Features (User's Phase 4) [US3, US4]

**Goal**: Implement user authentication, personalized content delivery, and Urdu translation capabilities.

-   [ ] T039 [P] Implement `User` model based on `data-model.md` in `backend/src/models/user.py`
-   [ ] T040 [P] Implement basic user management (CRUD) in `backend/src/services/user_service.py`
-   [ ] T041 Integrate better-auth.com for external authentication in `backend/src/services/auth_external.py`
-   [ ] T042 Implement `/auth/signup`, `/auth/signin`, `/auth/me` endpoints based on `contracts/auth.yaml` in `backend/src/api/auth.py`
-   [ ] T043 Update signup logic to store `software_background` and `hardware_robotics_background` in `Neon Serverless Postgres` via `backend/src/services/user_service.py`
-   [ ] T044 Implement `personalization_logic` to adapt chapter content based on user background in `backend/src/services/personalization_service.py`
-   [ ] T045 Implement `/chapters/{chapter_id}/personalize` endpoint based on `contracts/personalization.yaml` in `backend/src/api/personalization.py`
-   [ ] T046 Implement `translation_logic` to provide Urdu translation of chapter content in `backend/src/services/translation_service.py`
-   [ ] T047 Implement `/chapters/{chapter_id}/translate` endpoint based on `contracts/translation.yaml` in `backend/src/api/translation.py`
-   [ ] T048 [P] Implement "Personalize content" button in `frontend/src/components/ChapterActions.tsx`
-   [ ] T049 Connect "Personalize content" button to `backend/personalization` API and update `ChapterDisplay.tsx`
-   [ ] T050 [P] Implement "Translate content to Urdu" button in `frontend/src/components/ChapterActions.tsx`
-   [ ] T051 Connect "Translate content to Urdu" button to `backend/translation` API and update `ChapterDisplay.tsx`
-   [ ] T052 Implement frontend authentication flow (login, signup, session management) in `frontend/src/services/auth_service.ts`
-   [ ] T053 Update `ChapterDisplay.tsx` to conditionally show personalization/translation based on user authentication status

## Phase: Deployment & Demo Preparation (User's Phase 5)

**Goal**: Deploy the platform, conduct final testing, and prepare for presentation.

-   [ ] T054 Configure Docusaurus for GitHub Pages deployment in `frontend/docusaurus.config.ts`
-   [ ] T055 Set up CI/CD for frontend deployment to GitHub Pages (e.g., GitHub Actions workflow) in `.github/workflows/frontend_deploy.yml`
-   [ ] T056 Configure FastAPI backend for cloud deployment (e.g., Dockerfile, `Procfile`) in `backend/`
-   [ ] T057 Set up CI/CD for backend deployment to chosen cloud platform (e.g., Vercel, Render) in `.github/workflows/backend_deploy.yml`
-   [ ] T058 [P] Develop E2E tests using Playwright for core user flows (textbook access, AI query, auth) in `e2e_tests/`
-   [ ] T059 Execute performance tests against deployed platform and document results in `docs/performance_report.md`
-   [ ] T060 Prepare demo script highlighting key features and AI-native aspects in `docs/demo_script.md`
-   [ ] T061 Create presentation slides/materials in `docs/presentation/`

## Dependency Graph (User Story Completion Order)

1.  **US1 (Accessing Textbook)** depends on:
    *   Setup Phase
    *   Foundational Phase
    *   Book Content Generation & Structure Phase
    *   Frontend Setup & Core UI Phase

2.  **US2 (Interacting with Conversational AI)** depends on:
    *   US1
    *   Backend Services & Conversational AI Integration Phase

3.  **US3 (User Authentication)** depends on:
    *   Setup Phase
    *   Foundational Phase

4.  **US4 (Personalizing and Translating Content)** depends on:
    *   US1
    *   US3
    *   Authentication & Personalization Features Phase

*Note: US3 and US4 are bonus features and can be deprioritized if time constraints are severe.*

## Parallel Execution Opportunities

-   **Frontend vs. Backend Development**: Many frontend UI components and backend API implementations can proceed in parallel, especially once API contracts are defined.
-   **Content Generation**: Initial content population (T022) can happen concurrently with early frontend setup.
-   **Testing**: E2E tests (T058) can be developed alongside feature implementation, but full execution requires deployed services.

## Independent Test Criteria per User Story

-   **US1 (Accessing Textbook)**: Can be fully tested by browsing the published site and verifying all modules and chapters are accessible and correctly structured.
-   **US2 (Interacting with Conversational AI)**: Can be fully tested by asking questions and verifying the AI's responses are accurate, contextual, and sourced only from the textbook content.
-   **US3 (User Authentication)**: Can be fully tested by completing the signup process, logging in, and verifying the background information is collected.
-   **US4 (Personalizing and Translating Content)**: Can be fully tested by selecting personalization options and verifying content changes, and selecting translation and verifying Urdu content.

## Suggested MVP Scope

For a hackathon with time constraints, the MVP should focus on User Story 1 and User Story 2 to deliver the core textbook content and the mandatory conversational AI functionality. User Stories 3 and 4 (Authentication, Personalization, Translation) would be considered stretch goals.

-   **MVP Core**: US1 (Accessing Textbook) + US2 (Interacting with Conversational AI)
-   **Stretch Goals**: US3 (User Authentication), US4 (Personalizing and Translating Content)
