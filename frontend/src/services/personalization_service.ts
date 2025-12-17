// frontend/src/services/personalization_service.ts

const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL || "http://localhost:8000";

interface PersonalizePayload {
  // Potentially send current user background or let backend derive from token
}

interface PersonalizedChapterResponse {
  chapter_id: string;
  title: string;
  personalized_content: string;
}

export const PersonalizationService = {
  async personalizeChapter(chapterId: string, accessToken: string): Promise<PersonalizedChapterResponse> {
    try {
      const response = await fetch(`${BACKEND_API_URL}/personalization/chapters/${chapterId}/personalize`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
        body: JSON.stringify({}), // Body might be empty or contain user context if not derived from token
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to personalize chapter');
      }

      return await response.json();
    } catch (error: any) {
      console.error("Error personalizing chapter:", error);
      throw error;
    }
  },
};
