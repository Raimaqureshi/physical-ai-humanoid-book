# Data Model: AI-Native Textbook Platform

## Entities

### User

Represents an individual interacting with the platform.

**Attributes**:
-   `id`: (string, UUID, primary key) Unique identifier for the user.
-   `email`: (string, unique, required) User's email address.
-   `password_hash`: (string, required) Hashed password for authentication.
-   `software_background`: (string, optional) User's background in software engineering (e.g., "beginner", "intermediate", "expert"). Used for personalization.
-   `hardware_robotics_background`: (string, optional) User's background in hardware/robotics (e.g., "none", "hobbyist", "professional"). Used for personalization.
-   `personalization_preferences`: (JSON object, optional) Stores user-specific preferences for content adaptation.
-   `created_at`: (datetime, required) Timestamp of user creation.
-   `updated_at`: (datetime, required) Timestamp of last update.

**Validation Rules**:
-   Email must be a valid email format.
-   Password must meet defined complexity requirements (e.g., minimum length, special characters).
-   `software_background` and `hardware_robotics_background` should be selected from a predefined list of options or allow custom input with validation.

### Textbook Content (Hierarchical: Book -> Module -> Chapter)

Represents the educational material provided in the textbook.

**Attributes**:
-   `book_id`: (string, UUID, primary key) Unique identifier for the book ("Physical AI & Humanoid Robotics").
-   `book_title`: (string, required) Title of the book.
-   `module_id`: (string, UUID, primary key, unique per book) Unique identifier for each module.
-   `module_title`: (string, required) Title of the module.
-   `chapter_id`: (string, UUID, primary key, unique per module) Unique identifier for each chapter.
-   `chapter_title`: (string, required) Title of the chapter.
-   `textual_content`: (string, required) The main body of the chapter content (Markdown or similar format).
-   `learning_objectives`: (array of strings, optional) Key learning goals for the chapter.
-   `real_world_examples`: (array of objects, optional) Structured data for real-world robotics examples.
-   `ros_gazebo_isaac_references`: (array of objects, optional) Structured data for references to ROS 2, Gazebo, and NVIDIA Isaac.
-   `practical_exercises`: (array of objects, optional) Structured data for practical exercises.
-   `metadata`: (JSON object, optional) Additional information (e.g., difficulty, tags, topics, keywords for RAG).
-   `created_at`: (datetime, required) Timestamp of content creation.
-   `updated_at`: (datetime, required) Timestamp of last update.

**Relationships**:
-   A Book contains multiple Modules.
-   A Module contains exactly 4 Chapters.

### Query

Represents a user's question posed to the conversational AI.

**Attributes**:
-   `query_id`: (string, UUID, primary key) Unique identifier for the query.
-   `user_id`: (string, UUID, foreign key to User) The ID of the user who made the query.
-   `query_text`: (string, required) The actual question text from the user.
-   `context_type`: (string, required) Indicates the scope of the query (e.g., "entire_book", "chapter_specific", "selected_text").
-   `context_reference`: (string, optional) Reference to the specific content if `context_type` is not "entire_book" (e.g., `chapter_id`, `selected_text_hash` or `start_char_idx-end_char_idx`).
-   `timestamp`: (datetime, required) Timestamp when the query was made.

**Relationships**:
-   Each Query is associated with one User.
-   Each Query may be associated with a specific piece of Textbook Content.

### Conversational AI Response

Represents the answer provided by the conversational AI in response to a user's query.

**Attributes**:
-   `response_id`: (string, UUID, primary key) Unique identifier for the response.
-   `query_id`: (string, UUID, foreign key to Query) The ID of the query this response answers.
-   `response_text`: (string, required) The generated answer text.
-   `source_references`: (array of strings, optional) References to sections of the Textbook Content used to generate the answer (e.g., "Chapter 1.2 Introduction", "Module 3, Page 45").
-   `timestamp`: (datetime, required) Timestamp when the response was generated.

**Relationships**:
-   Each Conversational AI Response is associated with one Query.
