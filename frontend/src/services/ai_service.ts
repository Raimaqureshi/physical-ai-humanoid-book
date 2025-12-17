// frontend/src/services/ai_service.ts

interface QueryPayload {
  query_text: string;
  context_type: "entire_book" | "chapter_specific" | "selected_text";
  context_reference?: string;
}

interface AIResponse {
  response_text: string;
  source_references?: string[];
}

const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL || "http://localhost:8000";

export const AIService = {
  async queryAI(payload: QueryPayload): Promise<AIResponse> {
    try {
      const response = await fetch(`${BACKEND_API_URL}/ai/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Add Authorization header if authentication is implemented
          // 'Authorization': `Bearer ${yourAccessToken}`,
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to query AI');
      }

      return await response.json();
    } catch (error: any) {
      console.error("Error querying AI:", error);
      throw error;
    }
  },
};
