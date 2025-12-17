// frontend/src/services/content_service.ts

import { Chapter } from '../types/Chapter'; // Assuming a Chapter type will be defined later

// Mock data for initial development
const mockChapterContent: Chapter = {
  id: "mock-chapter-id",
  title: "Mock Chapter Title",
  moduleId: "mock-module-id",
  textualContent: "This is **mocked** chapter content. Replace with actual API call.",
  learningObjectives: ["Understand mocking", "Learn service integration"],
  realWorldExamples: [{ title: "Mock Example", description: "This is a mocked real-world example." }],
  rosGazeboIsaacReferences: [{ title: "Mock ROS Ref", type: "ROS 2" }],
  practicalExercises: [{ title: "Mock Exercise", description: "Complete the mock." }],
  metadata: { keywords: ["mock", "test"] }
};

export const ContentService = {
  async getChapter(chapterId: string): Promise<Chapter> {
    console.log(`Fetching chapter: ${chapterId} (mocked)`);
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 500));
    return Promise.resolve(mockChapterContent);
  },

  async getBookList(): Promise<any[]> {
    console.log("Fetching book list (mocked)");
    await new Promise(resolve => setTimeout(resolve, 300));
    return Promise.resolve([
      { id: "mock-book-id-1", title: "Mock Book 1" },
      { id: "mock-book-id-2", title: "Mock Book 2" },
    ]);
  },

  async getModulesForBook(bookId: string): Promise<any[]> {
    console.log(`Fetching modules for book: ${bookId} (mocked)`);
    await new Promise(resolve => setTimeout(resolve, 300));
    return Promise.resolve([
      { id: "mock-module-id-1", title: "Mock Module 1" },
      { id: "mock-module-id-2", title: "Mock Module 2" },
    ]);
  },

  async getChaptersForModule(moduleId: string): Promise<any[]> {
    console.log(`Fetching chapters for module: ${moduleId} (mocked)`);
    await new Promise(resolve => setTimeout(resolve, 300));
    return Promise.resolve([
      { id: "mock-chapter-id-1", title: "Mock Chapter 1" },
      { id: "mock-chapter-id-2", title: "Mock Chapter 2" },
    ]);
  }
};
