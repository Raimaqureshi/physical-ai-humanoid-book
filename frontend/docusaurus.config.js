const config = {
  title: 'Physical AI & Humanoid Robotics Textbook',
  tagline: 'An AI-Native Technical Textbook',
  url: 'https://speckit-ai.github.io',
  baseUrl: '/speckit/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'Raimaqureshi',
  projectName: 'physical-ai-humanoid-book',

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/speckit-ai/speckit/tree/main/frontend/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/speckit-ai/speckit/tree/main/frontend/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'AI-Native Textbook Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'module1-ros-nervous-system/module1-ros-nervous-system/module1-ros-nervous-system-chapter1',
          position: 'left',
          label: 'Textbook',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/speckit-ai/speckit',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Textbook',
              to: '/docs/module1-ros-nervous-system/module1-ros-nervous-system/module1-ros-nervous-system-chapter1',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/speckit-ai/speckit',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. Built with Docusaurus.`,
    },
  },
};

module.exports = config;