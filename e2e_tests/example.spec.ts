// e2e_tests/example.spec.ts

import { test, expect } from '@playwright/test';

test.describe('AI-Native Textbook Platform E2E Tests', () => {
  const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
  const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000';

  test('should navigate to the textbook and display content (US1)', async ({ page }) => {
    await page.goto(frontendUrl);
    await expect(page).toHaveTitle(/Physical AI & Humanoid Robotics Textbook/);

    // Navigate to the first chapter
    await page.getByRole('link', { name: 'Textbook' }).click();
    await page.getByRole('link', { name: 'ROS 2 Fundamentals: The Robotic Nervous System' }).click();

    await expect(page.getByRole('heading', { name: 'ROS 2 Fundamentals: The Robotic Nervous System' })).toBeVisible();
    await expect(page.locator('article')).toContainText('This is the **mock content** for ROS 2 as the Robotic Nervous System - Chapter 1.');
  });

  test('should interact with the AI chat placeholder (US2 - UI only)', async ({ page }) => {
    await page.goto(frontendUrl);
    
    // Open the AI chat
    await page.getByRole('button', { name: 'Open AI Chat' }).click();
    await expect(page.getByRole('heading', { name: 'Conversational AI' })).toBeVisible();

    // Verify input and send button are present but disabled (as it's a placeholder)
    const chatInput = page.getByPlaceholder('Type your question...');
    await expect(chatInput).toBeVisible();
    await expect(chatInput).toBeDisabled();
    await expect(page.getByRole('button', { name: 'Send' })).toBeDisabled();

    // Close the AI chat
    await page.getByRole('button', { name: 'X' }).click();
    await expect(page.getByRole('heading', { name: 'Conversational AI' })).not.toBeVisible();
  });

  // TODO: Add more E2E tests for authentication, personalization, translation once implemented
  // and mock/actual backend is available for these features.
});
