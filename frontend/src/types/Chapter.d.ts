// frontend/src/types/Chapter.d.ts

export interface LearningObjective {
  objective: string;
}

export interface Example {
  title: string;
  description?: string;
  url?: string;
  codeSnippet?: string;
}

export interface Reference {
  title: string;
  url?: string;
  type?: string;
}

export interface Exercise {
  title: string;
  description?: string;
  difficulty?: string;
  solutionHint?: string;
}

export interface ChapterMetadata {
  learningObjectives?: LearningObjective[];
  realWorldExamples?: Example[];
  rosGazeboIsaacReferences?: Reference[];
  practicalExercises?: Exercise[];
  keywords?: string[];
  difficulty?: string;
  estimatedReadingTimeMinutes?: number;
  prerequisites?: string[];
  relatedChapters?: string[];
  authors?: string[];
  version?: string;
  additionalMetadata?: Record<string, any>;
}

export interface Chapter {
  id: string;
  title: string;
  moduleId: string;
  textualContent: string;
  metadata?: ChapterMetadata; // Embed metadata directly or fetch separately
}
