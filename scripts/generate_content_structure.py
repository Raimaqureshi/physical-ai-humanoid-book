# scripts/generate_content_structure.py

import os
import uuid
import json

def generate_chapter_content(chapter_title, module_id, chapter_id, chapter_number):
    """Generates placeholder Markdown content for a chapter."""
    return f"""---\nid: {chapter_id}
title: {chapter_title}
module_id: {module_id}
learning_objectives:
  - Understand the core concepts of {chapter_title}.
  - Identify key components and their functions related to {chapter_title}.
keywords: [{chapter_title.lower().replace(" ", ", ")}, robotics, AI]
difficulty: intermediate
estimated_reading_time_minutes: 30
---\n
# {chapter_title}

## Introduction
This chapter provides an introduction to {chapter_title}. It aims to lay the foundational understanding necessary for subsequent topics in this module.

## Core Concepts
Here we delve into the core concepts related to {chapter_title}. We will explore theoretical underpinnings and key principles.

## Tools & Technologies
This section discusses relevant tools and technologies that are integral to {chapter_title}. Examples might include specific software libraries, hardware components, or development environments.

## Real-World Humanoid Robotics Examples
Practical applications of {chapter_title} in the context of humanoid robotics will be presented. Case studies and real-world scenarios will illustrate the concepts.

## Practical Exercises
Engage with hands-on exercises designed to reinforce your understanding of {chapter_title}. These exercises may involve simulations, coding challenges, or analytical problems.

## Chapter Summary
A concise summary of the key takeaways and important points covered in this chapter.
"""

def generate_module_structure(base_path, module_name, module_id, num_chapters=4):
    """Generates a module directory and its chapters."""
    module_dir = os.path.join(base_path, module_name)
    os.makedirs(module_dir, exist_ok=True)
    print(f"Created module directory: {module_dir}")

    chapter_summaries = []
    for i in range(1, num_chapters + 1):
        chapter_title = f"{module_name.replace('-', ' ').title()} - Chapter {i}"
        chapter_id = f"{module_id}-chapter{i}"
        
        # Override titles based on user's request from the prompt for modules
        if "ros-nervous-system" in module_name:
            if i == 1: chapter_title = "ROS 2 Fundamentals: The Robotic Nervous System"
            elif i == 2: chapter_title = "ROS 2 Communication: Nodes, Topics, Services"
            elif i == 3: chapter_title = "Advanced ROS 2: Actions, Parameters, Transforms"
            elif i == 4: chapter_title = "ROS 2 Best Practices for Humanoids"
        elif "gazebo-unity-digital-twin" in module_name:
            if i == 1: chapter_title = "Introduction to Robotic Simulation: Gazebo"
            elif i == 2: chapter_title = "Building Digital Twins in Gazebo: URDF & SDF"
            elif i == 3: chapter_title = "Unity for Robotics: Advanced Visualization & Physics"
            elif i == 4: chapter_title = "Humanoid Simulation & Testing with Digital Twins"
        elif "nvidia-isaac-ai-robot-brain" in module_name:
            if i == 1: chapter_title = "Introduction to NVIDIA Isaac ROS"
            elif i == 2: chapter_title = "AI Navigation & Perception with Isaac ROS"
            elif i == 3: chapter_title = "Humanoid Manipulation with Isaac Gym & Isaac Sim"
            elif i == 4: chapter_title = "Deploying AI Models to Humanoid Robots with Isaac ROS"
        elif "vision-language-action-humanoid-autonomy" in module_name:
            if i == 1: chapter_title = "Foundations of Vision-Language Models for Robotics"
            elif i == 2: chapter_title = "Perception for Humanoids: Object & Scene Understanding"
            elif i == 3: chapter_title = "Action Planning & Execution with LLMs in Robotics"
            elif i == 4: chapter_title = "Integrated Vision-Language-Action Systems for Humanoids"


        chapter_file = os.path.join(module_dir, f"{chapter_id}.md")
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write(generate_chapter_content(chapter_title, module_id, chapter_id, i))
        print(f"  Generated chapter: {chapter_file}")
        
        chapter_summaries.append({
            'id': chapter_id,
            'title': chapter_title
        })
    return chapter_summaries

def generate_sidebar_config(module_data):
    """Generates sidebar configuration for Docusaurus."""
    items = []
    for module in module_data:
        module_item = {
            'type': 'category',
            'label': module['title'],
            'link': {
                'type': 'generated-index',
                'title': f"{module['title']} Overview"
            },
            'items': [{'type': 'doc', 'id': chapter['id']} for chapter in module['chapters']]
        }
        items.append(module_item)
    
    return { 'docs': items }

def main():
    frontend_docs_path = "frontend/docs"
    os.makedirs(frontend_docs_path, exist_ok=True)

    modules_config = [
        {"name": "module1-ros-nervous-system", "title": "ROS 2 as the Robotic Nervous System"},
        {"name": "module2-gazebo-unity-digital-twin", "title": "Gazebo & Unity as the Digital Twin"},
        {"name": "module3-nvidia-isaac-ai-robot-brain", "title": "NVIDIA Isaac as the AI-Robot Brain"},
        {"name": "module4-vision-language-action-humanoid-autonomy", "title": "Vision-Language-Action for Humanoid Autonomy"},
    ]

    module_data_for_sidebar = []

    for module in modules_config:
        module_id = module['name']
        module_title = module['title']
        
        # Create a directory for the module within frontend/docs
        current_module_docs_path = os.path.join(frontend_docs_path, module_id)
        os.makedirs(current_module_docs_path, exist_ok=True)
        
        print(f"Generating structure for Module: {module_title}")
        chapters = generate_module_structure(current_module_docs_path, module_id, module_id)
        module_data_for_sidebar.append({
            'title': module_title,
            'chapters': chapters
        })

    # Generate sidebar.js
    sidebar_content = generate_sidebar_config(module_data_for_sidebar)
    
    # Docusaurus sidebars.js export format
    js_content = f"module.exports = {json.dumps(sidebar_content, indent=2)};"
    with open("frontend/sidebars.js", 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("\nGenerated frontend/sidebars.js")

if __name__ == "__main__":
    main()
