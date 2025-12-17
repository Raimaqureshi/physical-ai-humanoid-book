// frontend/src/components/AIChatPlaceholder.tsx

import React, { useState } from 'react';
import styles from './AIChatPlaceholder.module.css';
import { AIService } from '../services/ai_service'; // Import the new service

interface AIChatPlaceholderProps {
  // Add any props for initial state or behavior if needed
  currentChapterId?: string; // To provide chapter context
}

const AIChatPlaceholder: React.FC<AIChatPlaceholderProps> = ({ currentChapterId }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<{ sender: 'user' | 'ai'; text: string; sources?: string[] }[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleQueryChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleSubmitQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    const userMessage = { sender: 'user' as const, text: query };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setQuery('');
    setIsLoading(true);

    try {
      const payload = {
        query_text: userMessage.text,
        context_type: currentChapterId ? "chapter_specific" : "entire_book",
        context_reference: currentChapterId,
      };
      const aiResponse = await AIService.queryAI(payload);
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: 'ai', text: aiResponse.response_text, sources: aiResponse.source_references },
      ]);
    } catch (error: any) {
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: 'ai', text: `Error: ${error.message || 'Failed to get response.'}` },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.chatContainer}>
      <button className={styles.chatToggleButton} onClick={toggleChat}>
        {isOpen ? 'Close Chat' : 'Open AI Chat'}
      </button>

      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h3>Conversational AI</h3>
            <button className={styles.closeButton} onClick={toggleChat}>X</button>
          </div>
          <div className={styles.chatBody}>
            {messages.length === 0 ? (
              <p>Ask me anything about the textbook content!</p>
            ) : (
              messages.map((msg, index) => (
                <div key={index} className={msg.sender === 'user' ? styles.userMessage : styles.aiMessage}>
                  <strong>{msg.sender === 'user' ? 'You' : 'AI'}:</strong> {msg.text}
                  {msg.sources && msg.sources.length > 0 && (
                    <small className={styles.sources}>
                      (Sources: {msg.sources.join(', ')})
                    </small>
                  )}
                </div>
              ))
            )}
            {isLoading && <p>AI is thinking...</p>}
          </div>
          <form onSubmit={handleSubmitQuery} className={styles.chatFooter}>
            <input
              type="text"
              placeholder="Type your question..."
              value={query}
              onChange={handleQueryChange}
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading || !query.trim()}>
              Send
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default AIChatPlaceholder;