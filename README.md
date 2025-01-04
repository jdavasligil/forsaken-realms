[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# The Forsaken Realms
[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

**Forsaken Realms** is a dark fantasy adventure roleplaying game based on [Cairn](https://cairnrpg.com/) about exploring  mysterious ruins and forsaken realms filled with strange folk, hidden treasure, and unfathomable horrors. Powerful factions vie for power in lawless realms of ruin. Character generation is quick and narrative driven, adventures are tense and reward careful exploration, and combat is frantic and deadly. The game was written by [Julian Davasligil](https://github.com/jdavasligil), derivative of the work written by [Yochai Gal](https://newschoolrevolution.com/).

## Status
In development! There is much work to be done.

## Roadmap
- [ ] System Reference Document
- [ ] Player's Guide
- [ ] Referee's Guide

## License
The following files, directories, and their children (recursively) are not included in the MIT License:
* public/
* src/assets/
* src/content/
* src/fonts/

All text (.md, .mdx, or otherwise) is licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)


## Project Structure

Inside of this Astro + Starlight project, you'll see the following folders and files:

```
.
├── public/
├── src/
│   ├── assets/
│   ├── content/
│   │   ├── docs/
│   ├── fonts/
│   ├── styles/
│   └── content.config.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

Starlight looks for `.md` or `.mdx` files in the `src/content/docs/` directory. Each file is exposed as a route based on its file name.

Images can be added to `src/assets/` and embedded in Markdown with a relative link.

Custom fonts can be added to `src/fonts/`. We only accept [OFL](https://openfontlicense.org/open-font-license-official-text/) licensed fonts.

Static assets, like favicons, can be placed in the `public/` directory.


## Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`             | Installs dependencies                            |
| `pnpm dev`                 | Starts local dev server at `localhost:4321`      |
| `pnpm build`               | Build your production site to `./dist/`          |
| `pnpm preview`             | Preview your build locally, before deploying     |
| `pnpm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm run astro -- --help` | Get help using the Astro CLI                     |

## Documentation

Check out [Starlight’s docs](https://starlight.astro.build/), read [the Astro documentation](https://docs.astro.build), or jump into the [Astro Discord server](https://astro.build/chat).


## Attribution
This game is a heavily modified hack of [Cairn RPG](https://cairnrpg.com/) by [Yochai Gal](https://newschoolrevolution.com/), and would not be possible without their incredible work.

### Inspiration
* [Cairn](https://cairnrpg.com/)
* [Old School Essentials](https://necroticgnome.com/pages/about-old-school-essentials)
* [Forbidden Lands](https://freeleaguepublishing.com/games/forbidden-lands/)
* [Into the Odd](https://freeleaguepublishing.com/shop/into-the-odd/remastered/)
* [Mausritter](https://mausritter.com/)
