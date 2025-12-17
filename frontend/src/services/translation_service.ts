// frontend/src/services/translation_service.ts

const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL || "http://localhost:8000";

interface TranslatePayload {
  target_language: string;
}

interface TranslatedChapterResponse {
  chapter_id: string;
  title: string;
  translated_content: string;
  language: string;
}

export const TranslationService = {
  async translateChapter(chapterId: string, targetLanguage: string, accessToken: string): Promise<TranslatedChapterResponse> {
    try {
      const response = await fetch(`${BACKEND_API_URL}/translation/chapters/${chapterId}/translate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
        body: JSON_stringify({ target_language: targetLanguage }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to translate chapter');
      }

      return await response.json();
    } catch (error: any) {
      console.error("Error translating chapter:", error);
      throw error;
    }
  },
};
