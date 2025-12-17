// frontend/src/components/ChapterActions.tsx

import React from 'react';
import Link from '@docusaurus/Link';

interface ChapterActionsProps {
  chapterId: string;
  onPersonalize?: (chapterId: string) => void;
  onTranslate?: (chapterId: string, language: string) => void;
  isUserAuthenticated: boolean; // Assume this prop is passed to determine button visibility/enabled state
}

const ChapterActions: React.FC<ChapterActionsProps> = ({
  chapterId,
  onPersonalize,
  onTranslate,
  isUserAuthenticated,
}) => {
  const handlePersonalizeClick = () => {
    if (onPersonalize) {
      onPersonalize(chapterId);
    }
  };

  const handleTranslateClick = () => {
    if (onTranslate) {
      onTranslate(chapterId, "ur"); // Hardcode Urdu for now
    }
  };

  return (
    <div style={{ marginTop: '20px', display: 'flex', gap: '10px' }}>
      <button
        className="button button--primary"
        onClick={handlePersonalizeClick}
        disabled={!isUserAuthenticated}
        title={!isUserAuthenticated ? "Login to personalize content" : "Personalize content"}
      >
        Personalize Content
      </button>
      <button
        className="button button--secondary"
        onClick={handleTranslateClick}
        disabled={!isUserAuthenticated}
        title={!isUserAuthenticated ? "Login to translate content" : "Translate content to Urdu"}
      >
        Translate to Urdu
      </button>
    </div>
  );
};

export default ChapterActions;
