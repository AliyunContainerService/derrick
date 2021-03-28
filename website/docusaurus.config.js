/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: "Derrick",
  tagline: "一个帮助你快速容器化应用的工具",
  url: "https://alibaba.github.io/",
  baseUrl: "/derrick/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "alibaba", // Usually your GitHub org/user name.
  projectName: "derrick", // Usually your repo name.
  themeConfig: {
    navbar: {
      title: "Derrick 官网",
      logo: {
        alt: "My Site Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          to: "docs/",
          activeBasePath: "docs",
          label: "Docs",
          position: "left",
        },
        { to: "blog", label: "Blog", position: "left" },
        {
          href: "https://github.com/alibaba/derrick",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Introduction",
              to: "docs/",
            },
            {
              label: "Design",
              to: "docs/design",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/alibaba/derrick",
            },
            {
              label: "Wechat",
              href: "https://github.com/alibaba/derrick",
            },
            {
              label: "DingTalk",
              href: "https://github.com/alibaba/derrick",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "Blog",
              to: "blog",
            },
            // {
            //   label: "GitHub",
            //   href: "https://github.com/alibaba/derrick",
            // },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl: "https://github.com/alibaba/derrick/edit/master/website/",
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            "https://github.com/alibaba/derrick/edit/master/website/blog/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
