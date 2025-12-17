// frontend/src/components/ChapterDisplay.tsx

import React, { useState } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import ChapterActions from './ChapterActions'; // Import ChapterActions
import { PersonalizationService } from '../services/personalization_service'; // Import PersonalizationService
import { TranslationService } from '../services/translation_service'; // Will be created later

// Assuming a way to get the current user's authentication status and token
// This is a placeholder for actual auth context
const useAuthStatus = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // Default to false
  const [accessToken, setAccessToken] = useState<string | null>(null); // Store token

  // In a real app, this would check localStorage, context, etc.
  React.useEffect(() => {
    // Mock authentication check
    const token = localStorage.getItem('mockAccessToken'); // Example
    if (token) {
      setIsAuthenticated(true);
      setAccessToken(token);
    }
  }, []);

  return { isAuthenticated, accessToken };
};


interface ChapterDisplayProps {
  chapterId: string;
  chapterTitle: string;
  // This would typically fetch content from an API or Docusaurus context
  content: string;
  metadata?: {
    learningObjectives?: { objective: string }[];
    realWorldExamples?: { title: string; description: string; url?: string }[];
    rosGazeboIsaacReferences?: { title: string; type: string; url?: string }[];
    practicalExercises?: { title: string; description: string }[];
  };
}

const ChapterDisplay: React.FC<ChapterDisplayProps> = ({
  chapterId,
  chapterTitle,
  content,
  metadata,
}) => {
  const { siteConfig } = useDocusaurusContext();
  const { title: siteTitle } = siteConfig;
  const { isAuthenticated, accessToken } = useAuthStatus();

  const [displayContent, setDisplayContent] = useState(content);
  const [displayTitle, setDisplayTitle] = useState(chapterTitle);
  const [isContentPersonalized, setIsContentPersonalized] = useState(false);
  const [isContentTranslated, setIsContentTranslated] = useState(false);

  // Reset display content when chapterId or initial content changes
  React.useEffect(() => {
    setDisplayContent(content);
    setDisplayTitle(chapterTitle);
    setIsContentPersonalized(false);
    setIsContentTranslated(false);
  }, [chapterId, content, chapterTitle]);

  const handlePersonalize = async (id: string) => {
    if (!accessToken) {
      alert("Please log in to personalize content.");
      return;
    }
    try {
      const personalized = await PersonalizationService.personalizeChapter(id, accessToken);
      setDisplayContent(personalized.personalized_content);
      setDisplayTitle(personalized.title);
      setIsContentPersonalized(true);
      setIsContentTranslated(false); // Personalization resets translation
      alert("Chapter personalized!");
    } catch (error: any) {
      alert(`Failed to personalize chapter: ${error.message}`);
      console.error(error);
    }
  };

  const handleTranslate = async (id: string, language: string) => {
    if (!accessToken) {
      alert("Please log in to translate content.");
      return;
    }
    try {
      const translated = await TranslationService.translateChapter(id, language, accessToken);
      setDisplayContent(translated.translated_content);
      setDisplayTitle(translated.title);
      setIsContentTranslated(true);
      setIsContentPersonalized(false); // Translation resets personalization
      alert(`Chapter translated to ${language.toUpperCase()}!`);
    } catch (error: any) {
      alert(`Failed to translate chapter: ${error.message}`);
      console.error(error);
    }
  };


  // Placeholder for rendering metadata dynamically
  const renderMetadataSection = (title: string, items: any[]) => {
    if (!items || items.length === 0) return null;
    return (
      <div className="margin-top--md">
        <Heading as="h2">{title}</Heading>
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              {item.objective || item.title || item}
              {item.description && <span>: {item.description}</span>}
              {item.url && <a href={item.url} target="_blank" rel="noopener noreferrer"> (Link)</a>}
            </li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <Layout
      title={displayTitle}
      description={`Read ${displayTitle} from the ${siteTitle}`}
    >
      <div className="container margin-top--lg margin-bottom--xl">
        <div className="row">
          <div className="col col--10 col--offset-1">
            <Heading as="h1">{displayTitle}</Heading>

            {/* Chapter Actions */}
            <ChapterActions
              chapterId={chapterId}
              onPersonalize={handlePersonalize}
              onTranslate={handleTranslate}
              isUserAuthenticated={isAuthenticated}
            />

            {/* Display Metadata */}
            {metadata && (
              <div className="metadata-section">
                {renderMetadataSection('Learning Objectives', metadata.learningObjectives)}
                {renderMetadataSection('Real-World Examples', metadata.realWorldExamples)}
                {renderMetadataSection('ROS/Gazebo/Isaac References', metadata.rosGazeboIsaacReferences)}
                {renderMetadataSection('Practical Exercises', metadata.practicalExercises)}
              </div>
            )}

            <article dangerouslySetInnerHTML={{ __html: displayContent }} />
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ChapterDisplay;