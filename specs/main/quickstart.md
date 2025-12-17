# Quickstart Guide: AI-Native Textbook Platform

This guide provides a rapid overview of how to set up and run the AI-Native Textbook Platform locally.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

-   **Git**: For version control.
-   **Python 3.9+**: For the backend services.
-   **Node.js (LTS recommended)**: For the frontend Docusaurus application.
-   **Docker (Optional but Recommended)**: For easily running database services like Qdrant and Neon Postgres locally if not using cloud instances.

## 2. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone [REPOSITORY_URL]
cd speckit
```

## 3. Backend Setup

Navigate to the `backend/` directory to set up the FastAPI services.

```bash
cd backend
```

### Install Dependencies

```bash
pip install -r requirements.txt # (assuming requirements.txt will be generated later)
```

### Configure Environment Variables

Create a `.env` file in the `backend/` directory with necessary configurations (e.g., database connection strings, API keys for OpenAI/ChatKit, better-auth.com credentials).

```
# Example .env content
DATABASE_URL="postgresql://user:password@host:port/database"
QDRANT_URL="http://localhost:6333" # Or your Qdrant Cloud URL
OPENAI_API_KEY="your_openai_api_key"
CHATKIT_API_KEY="your_chatkit_api_key"
BETTERAUTH_CLIENT_ID="your_betterauth_client_id"
BETTERAUTH_CLIENT_SECRET="your_betterauth_client_secret"
```

### Run Backend Services

```bash
uvicorn main:app --reload # (assuming main:app will be the entry point)
```

## 4. Frontend Setup

Open a new terminal and navigate to the `frontend/` directory to set up the Docusaurus application.

```bash
cd frontend
```

### Install Dependencies

```bash
npm install # or yarn install
```

### Run Frontend Application

```bash
npm start # or yarn start
```

This will typically open the Docusaurus site in your browser at `http://localhost:3000`.

## 5. Content Ingestion (Initial Setup)

Before the Conversational AI can function, you'll need to ingest the textbook content into Qdrant. This usually involves a separate script or a dedicated endpoint.

```bash
# Example command (details to be provided in further documentation)
python scripts/ingest_content.py --source ../book_content --qdrant-url http://localhost:6333
```

## 6. Accessing the Platform

Once both the backend and frontend services are running:

-   Open your web browser and go to `http://localhost:3000`.
-   You should see the "Physical AI & Humanoid Robotics" textbook.
-   You can now navigate chapters, sign up/in (if implemented), personalize content, and interact with the conversational AI.

This is a basic quickstart. More detailed documentation for specific features, deployment, and testing will be available in the respective `specs/` and `docs/` directories.
