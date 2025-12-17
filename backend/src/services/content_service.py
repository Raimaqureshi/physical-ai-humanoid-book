# backend/src/services/content_service.py

from typing import List, Optional
from backend.src.models.content import Book, Module, Chapter, ContentMetadata
import uuid

class ContentService:
    def __init__(self):
        # Initial mock data (in-memory for now)
        self.books: Dict[str, Book] = {}
        self.modules: Dict[str, Module] = {}
        self.chapters: Dict[str, Chapter] = {}
        self._initialize_mock_data()

    def _initialize_mock_data(self):
        # Create a mock book
        mock_book = Book(id="book-physical-ai-humanoid-robotics", title="Physical AI & Humanoid Robotics")
        self.books[mock_book.id] = mock_book

        # Create mock modules and chapters
        module_titles = [
            "ROS 2 as the Robotic Nervous System",
            "Gazebo & Unity as the Digital Twin",
            "NVIDIA Isaac as the AI-Robot Brain",
            "Vision-Language-Action for Humanoid Autonomy"
        ]

        chapter_templates = [
            lambda m_id, m_title, i: Chapter(
                id=f"{m_id}-chapter{i}",
                module_id=m_id,
                title=f"{m_title} - Chapter {i}",
                order=i,
                textual_content=f"This is the **mock content** for {m_title} - Chapter {i}. "
                                 f"It contains an introduction to the core concepts of this chapter, "
                                 f"some real-world examples, and practical exercises. "
                                 f"This content will eventually be loaded from actual Markdown files.",
                metadata=ContentMetadata(
                    chapter_id=f"{m_id}-chapter{i}",
                    learning_objectives=[{"objective": f"Understand {m_title} concept {i}"}],
                    keywords=[m_title.lower().replace(' ', '-'), f"chapter-{i}"]
                )
            )
        ]

        for i, m_title in enumerate(module_titles):
            module_id = f"module{i+1}-{m_title.lower().replace(' ', '-')}"
            mock_module = Module(id=module_id, book_id=mock_book.id, title=m_title, order=i+1)
            self.modules[mock_module.id] = mock_module

            for j in range(1, 5): # 4 chapters per module
                mock_chapter = chapter_templates[0](mock_module.id, m_title, j)
                self.chapters[mock_chapter.id] = mock_chapter
    
    async def get_book(self, book_id: str) -> Optional[Book]:
        return self.books.get(book_id)

    async def get_all_books(self) -> List[Book]:
        return list(self.books.values())

    async def get_module(self, module_id: str) -> Optional[Module]:
        return self.modules.get(module_id)

    async def get_modules_by_book_id(self, book_id: str) -> List[Module]:
        return sorted([m for m in self.modules.values() if m.book_id == book_id], key=lambda x: x.order)

    async def get_chapter(self, chapter_id: str) -> Optional[Chapter]:
        return self.chapters.get(chapter_id)

    async def get_chapters_by_module_id(self, module_id: str) -> List[Chapter]:
        return sorted([c for c in self.chapters.values() if c.module_id == module_id], key=lambda x: x.order)

    async def create_chapter(self, chapter: Chapter) -> Chapter:
        if chapter.id in self.chapters:
            raise ValueError("Chapter with this ID already exists.")
        self.chapters[chapter.id] = chapter
        return chapter

    async def update_chapter(self, chapter_id: str, updated_chapter: Chapter) -> Optional[Chapter]:
        if chapter_id not in self.chapters:
            return None
        self.chapters[chapter_id] = updated_chapter
        return updated_chapter

    async def delete_chapter(self, chapter_id: str) -> bool:
        if chapter_id in self.chapters:
            del self.chapters[chapter_id]
            return True
        return False

content_service = ContentService()
