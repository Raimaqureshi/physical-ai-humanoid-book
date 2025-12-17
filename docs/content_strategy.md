# Content Ingestion Strategy for AI-Native Textbook Platform

This document outlines the strategy and guidelines for ingesting and structuring content for the "Physical AI & Humanoid Robotics" AI-Native Textbook Platform.

## 1. Content Source and Format

**Source**: Raw course material, academic papers, existing textbook excerpts, and newly generated content.
**Preferred Format**: Markdown (`.md` or `.mdx` for Docusaurus). This allows for easy version control, readability, and compatibility with Docusaurus.

## 2. Content Structure (Book, Modules, Chapters)

The content MUST adhere strictly to the following hierarchical structure:

-   **Book**: "Physical AI & Humanoid Robotics" (top-level)
    -   **Module**: Exactly 4 modules per book. Each module represents a major thematic area.
        -   **Chapter**: Exactly 4 chapters per module. Each chapter covers a specific topic within the module.

### File System Mapping

-   The Docusaurus `docs` folder (`frontend/docs/`) will house all textbook content.
-   Each module will be a sub-directory within `frontend/docs/`.
    -   Example: `frontend/docs/module1-ros-nervous-system/`
-   Each chapter will be a Markdown file within its respective module directory.
    -   Example: `frontend/docs/module1-ros-nervous-system/chapter1-ros-intro.md`
-   Sidebar configuration (`frontend/sidebars.ts`) will reflect this structure.

## 3. Chapter Content Components

Each chapter Markdown file MUST include the following sections to ensure richness for both human readers and AI agents:

### a. Introduction

-   Brief overview of the chapter's topic and its relevance.
-   `# Introduction`

### b. Core Concepts

-   Detailed explanation of fundamental theories, principles, and algorithms.
-   Use clear headings and subheadings.
-   `## Core Concepts`

### c. Tools & Technologies

-   Discussion of relevant tools, libraries, and technologies (e.g., ROS 2, Gazebo, NVIDIA Isaac).
-   Provide code snippets and configuration examples where applicable.
-   `## Tools & Technologies`

### d. Real-World Humanoid Robotics Examples

-   Practical application scenarios and case studies related to humanoid robotics.
-   Include diagrams, images, or links to external resources.
-   `## Real-World Humanoid Robotics Examples`

### e. Practical Exercises

-   Hands-on exercises or thought experiments for learners to apply concepts.
-   May include coding challenges, simulation tasks, or critical thinking questions.
-   `## Practical Exercises`

### f. Chapter Summary

-   Concise recap of the key takeaways from the chapter.
-   `# Chapter Summary`

## 4. Metadata Definition

Each chapter Markdown file will include a frontmatter section (YAML format at the top of the Markdown file) for structured metadata. This metadata is crucial for AI-powered features (RAG, personalization).

```yaml
---
id: chapter1-ros-intro
title: Introduction to ROS 2 as the Robotic Nervous System
module_id: module1-ros-nervous-system
learning_objectives:
  - Understand the core concepts of ROS 2.
  - Identify key ROS 2 components and their functions.
  - Learn how ROS 2 facilitates communication in robotics.
keywords: [ROS 2, robotics, middleware, nodes, topics, services, actions]
difficulty: intermediate
estimated_reading_time_minutes: 30
prerequisites: [basic-python, linux-fundamentals]
related_chapters: [chapter2-ros-communication, chapter3-humanoid-sensors]
---
```

**Required Metadata Fields**:
-   `id`: Unique identifier for the chapter (string, e.g., `chapter1-ros-intro`).
-   `title`: Chapter title (string).
-   `module_id`: Identifier of the parent module (string, e.g., `module1-ros-nervous-system`).
-   `learning_objectives`: (Array of strings) Specific learning outcomes for the chapter.
-   `keywords`: (Array of strings) Important terms for RAG and search.
-   `difficulty`: (string, e.g., "beginner", "intermediate", "advanced").
-   `estimated_reading_time_minutes`: (integer).

**Optional Metadata Fields**:
-   `prerequisites`: (Array of strings) IDs of chapters or external knowledge required.
-   `related_chapters`: (Array of strings) IDs of other relevant chapters.
-   `authors`: (Array of strings).
-   `version`: (string).

## 5. Content Ingestion Pipeline (for AI)

-   **Extraction**: Docusaurus Markdown files will be read by the backend.
-   **Chunking**: Content will be chunked into smaller, semantically meaningful units (e.g., paragraphs, sections) for vector embedding.
    -   Chapter-wise chunking for broad context.
    -   Semantic chunking within chapters for granular retrieval.
-   **Embedding**: Text chunks will be converted into vector embeddings using a chosen embedding model (e.g., OpenAI Embeddings).
-   **Storage**: Vector embeddings will be stored in Qdrant Cloud for efficient similarity search.
-   **Metadata Association**: Original chapter metadata and chunk metadata (e.g., source chapter ID, section heading) will be stored alongside vectors to enable contextual retrieval.

## 6. Version Control

All content (Markdown files, scripts, metadata schemas) MUST be managed in the project's Git repository. Changes to content should follow standard version control practices (branches, pull requests, reviews).

## 7. Quality Assurance

-   **Automated Checks**: Implement linters for Markdown and frontmatter.
-   **Manual Review**: Content will undergo peer review for accuracy, clarity, and adherence to guidelines.
-   **AI Validation**: Periodically validate conversational AI responses against the content to ensure accuracy and prevent hallucination.
