import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/module1-ros-nervous-system-chapter1">
            Start Reading 📖
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>AI-Native Approach</h3>
              <p>Learn cutting-edge techniques that integrate artificial intelligence directly into robotic systems, focusing on humanoid robotics applications.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>Hands-On Learning</h3>
              <p>Each concept is paired with practical exercises and real-world examples using industry-standard tools like ROS 2, Gazebo, and NVIDIA Isaac.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className="text--center padding-horiz--md">
              <h3>Comprehensive Coverage</h3>
              <p>From ROS fundamentals to advanced vision-language-action systems that enable autonomous humanoid behavior.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function BookOverview() {
  return (
    <section className={clsx('hero hero--secondary', styles.bookOverview)}>
      <div className="container">
        <div className="row">
          <div className="col col--6">
            <h2>About This Book</h2>
            <p>"Physical AI & Humanoid Robotics" is a comprehensive textbook designed for engineers, researchers, and students interested in the intersection of artificial intelligence and robotics.</p>
            <p>Our AI-native approach emphasizes:</p>
            <ul>
              <li>Modern ROS 2 architecture as the nervous system for robots</li>
              <li>Digital twins using Gazebo and Unity simulation environments</li>
              <li>NVIDIA Isaac as the robot brain for AI processing</li>
              <li>Vision-language-action systems for autonomous behavior</li>
            </ul>
          </div>
          <div className="col col--6">
            <h2>Why Choose This Book?</h2>
            <p>This book stands out due to its:</p>
            <ul>
              <li><strong>Practical Focus</strong>: Every chapter includes hands-on exercises</li>
              <li><strong>Up-to-Date Content</strong>: Covers the latest tools and frameworks</li>
              <li><strong>Easy to Follow</strong>: Step-by-step explanations with clear examples</li>
              <li><strong>Industry Relevant</strong>: Addresses current challenges in humanoid robotics</li>
            </ul>
            <p>Whether you're a beginner or experienced developer, this book provides the knowledge needed to build next-generation AI-powered robots.</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics`}
      description="An AI-Native Technical Textbook on Physical AI & Humanoid Robotics">
      <HomepageHeader />
      <main>
        <FeatureSection />
        <BookOverview />
      </main>
    </Layout>
  );
}
