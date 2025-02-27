// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://jdavasligil.github.io',
  base: 'forsaken-realms',
	integrations: [
		starlight({
			title: 'Forsaken Realms',
			social: {
				github: 'https://github.com/jdavasligil/forsaken-realms',
			},
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
				{
					label: 'First Edition',
					autogenerate: { directory: 'first-edition' },
				},
			],
      customCss: [
        './src/fonts/font-face.css',
        './src/styles/custom.css',
      ],
		}),
	],
});
