import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  "docs": [
    {
      "type": "category",
      "label": "ROS 2 as the Robotic Nervous System",
      "link": {
        "type": "generated-index",
        "title": "ROS 2 as the Robotic Nervous System Overview"
      },
      "items": [
        {
          "type": "doc",
          "id": "module1-ros-nervous-system-chapter1"
        },
        {
          "type": "doc",
          "id": "module1-ros-nervous-system-chapter2"
        },
        {
          "type": "doc",
          "id": "module1-ros-nervous-system-chapter3"
        },
        {
          "type": "doc",
          "id": "module1-ros-nervous-system-chapter4"
        }
      ]
    },
    {
      "type": "category",
      "label": "Gazebo & Unity as the Digital Twin",
      "link": {
        "type": "generated-index",
        "title": "Gazebo & Unity as the Digital Twin Overview"
      },
      "items": [
        {
          "type": "doc",
          "id": "module2-gazebo-unity-digital-twin-chapter1"
        },
        {
          "type": "doc",
          "id": "module2-gazebo-unity-digital-twin-chapter2"
        },
        {
          "type": "doc",
          "id": "module2-gazebo-unity-digital-twin-chapter3"
        },
        {
          "type": "doc",
          "id": "module2-gazebo-unity-digital-twin-chapter4"
        }
      ]
    },
    {
      "type": "category",
      "label": "NVIDIA Isaac as the AI-Robot Brain",
      "link": {
        "type": "generated-index",
        "title": "NVIDIA Isaac as the AI-Robot Brain Overview"
      },
      "items": [
        {
          "type": "doc",
          "id": "module3-nvidia-isaac-ai-robot-brain-chapter1"
        },
        {
          "type": "doc",
          "id": "module3-nvidia-isaac-ai-robot-brain-chapter2"
        },
        {
          "type": "doc",
          "id": "module3-nvidia-isaac-ai-robot-brain-chapter3"
        },
        {
          "type": "doc",
          "id": "module3-nvidia-isaac-ai-robot-brain-chapter4"
        }
      ]
    },
    {
      "type": "category",
      "label": "Vision-Language-Action for Humanoid Autonomy",
      "link": {
        "type": "generated-index",
        "title": "Vision-Language-Action for Humanoid Autonomy Overview"
      },
      "items": [
        {
          "type": "doc",
          "id": "module4-vision-language-action-humanoid-autonomy-chapter1"
        },
        {
          "type": "doc",
          "id": "module4-vision-language-action-humanoid-autonomy-chapter2"
        },
        {
          "type": "doc",
          "id": "module4-vision-language-action-humanoid-autonomy-chapter3"
        },
        {
          "type": "doc",
          "id": "module4-vision-language-action-humanoid-autonomy-chapter4"
        }
      ]
    }
  ]
};

export default sidebars;
