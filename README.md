# The Mythos Files — AH:LCG Site

A static site built with [Hugo](https://gohugo.io/) for writing about Arkham Horror: The Card Game.

## Quick start

### 1. Install Hugo

```bash
# macOS
brew install hugo

# Windows (Scoop)
scoop install hugo-extended

# Linux
sudo apt install hugo
# or download the binary from https://github.com/gohugoio/hugo/releases
```

Requires Hugo **v0.120+**.

### 2. Run locally

```bash
cd arkham-tabularium
hugo server -D
```

Open http://localhost:1313 — the site hot-reloads as you write.

The `-D` flag shows draft articles. Remove it to preview only published content.

### 3. Build for production

```bash
hugo
```

Output goes to `public/`. That folder is your entire website — upload it anywhere.

---

## Writing articles

### Create a new article

```bash
# Scenario review
hugo new scenarios/the-midnight-masks.md

# Deck guide
hugo new decks/agnes-baker-spell-spam.md

# Campaign log
hugo new campaigns/dunwich-ep3.md

# Investigator analysis
hugo new investigators/patrice-hathaway.md

# General article
hugo new articles/on-fail-forward-mechanics.md
```

Hugo uses the matching archetype template from `archetypes/` and pre-fills the front matter.

### Publish an article

Change `draft: true` to `draft: false` in the front matter.

### Front matter fields

Every article type has its own archetype. Common fields:

| Field | Type | Notes |
|---|---|---|
| `title` | string | Article title |
| `date` | date | Publication date (YYYY-MM-DD) |
| `draft` | bool | `true` = hidden from production |
| `description` | string | Shown in card previews and SEO |
| `tags` | list | Free-form tags |
| `cycle` | string | AH:LCG cycle name |
| `difficulty` | string | `easy` / `standard` / `hard` / `expert` |

Scenario-specific:

| Field | Type | Notes |
|---|---|---|
| `fun_factor` | int 0–10 | Shown in rating bar |
| `replayability` | int 0–10 | |
| `thematic_coherence` | int 0–10 | |
| `mechanical_design` | int 0–10 | |
| `standalone` | bool | Playable without campaign? |

Deck-specific:

| Field | Type | Notes |
|---|---|---|
| `investigator` | string | Primary investigator |
| `class` | string | Guardian / Seeker / Rogue / Mystic / Survivor |
| `xp_budget` | int | Total XP in the deck |
| `taboo` | bool | Taboo list applied? |

---

## Callout boxes in Markdown

Use raw HTML in your `.md` files for callout boxes:

```html
<!-- Tip -->
<div class="callout tip">
  <p class="callout-title">Tip</p>
  <p>Your tip text here.</p>
</div>

<!-- Spoiler warning -->
<div class="callout spoiler">
  <p class="callout-title">Spoiler</p>
  <p>Major plot beat ahead.</p>
</div>

<!-- General note -->
<div class="callout note">
  <p class="callout-title">Note</p>
  <p>Worth knowing.</p>
</div>
```

## Rating bars

In scenario reviews, paste this block and adjust the `width` percentages and score numbers:

```html
<div class="rating-bar">
  <h4>Ratings</h4>
  <div class="rating-row">
    <span class="rating-label">Fun factor</span>
    <div class="rating-track"><div class="rating-fill" style="width: 80%"></div></div>
    <span class="rating-score">8/10</span>
  </div>
</div>
```

## Stat blocks

```html
<div class="stat-block">
  <div class="stat-item"><strong>Cycle</strong> Dunwich Legacy</div>
  <div class="stat-item"><strong>Players</strong> 1–4</div>
  <div class="stat-item"><strong>Difficulty</strong> Standard</div>
</div>
```

---

## Deployment

### GitHub Pages (free, recommended)

1. Push the repo to GitHub.
2. Create `.github/workflows/hugo.yml` (see below).
3. In the repo settings → Pages → Source: `gh-pages` branch.

```yaml
# .github/workflows/hugo.yml
name: Deploy Hugo site

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
      - name: Build
        run: hugo --minify
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

### Cloudflare Pages (free, fast CDN)

1. Connect your GitHub repo in the Cloudflare Pages dashboard.
2. Build command: `hugo`
3. Output directory: `public`
4. Environment variable: `HUGO_VERSION` = `0.124.0`

### Neocities (free, indie-web)

Run `hugo`, then drag and drop the `public/` folder into the Neocities dashboard.

---

## Redundancy & archiving

For maximum persistence:

1. **Mirror the source repo** to both GitHub and [Codeberg](https://codeberg.org/) (open-source Git host):
   ```bash
   git remote add codeberg git@codeberg.org:yourusername/arkham-tabularium.git
   git push --all codeberg
   ```

2. **Submit to the Wayback Machine** after publishing new articles:
   https://web.archive.org/save/

3. **Enable GitHub Arctic Vault** — public repos are automatically included.

4. Consider a periodic **offline backup** of `public/` as a ZIP archive.

---

## Customization

### Change site name / author

Edit `hugo.toml`:
```toml
title = "Your Site Name"
[params]
  author = "Your Name"
  tagline = "Your tagline"
```

### Change colors

All design tokens are CSS variables in `layouts/_default/baseof.html`, in the `:root { }` block. The key ones:

```css
--gold:    #c9a84c;   /* Accent color */
--crimson: #8b2636;   /* Campaign/danger color */
--teal:    #2a6b7c;   /* Scenario color */
--paper:   #111318;   /* Background */
--body:    #c8c2b4;   /* Body text */
```

### Add a new section

1. Create `content/newsection/_index.md`
2. Add an entry in `hugo.toml` under `[[menu.main]]`
3. Create an archetype at `archetypes/newsection.md` if needed

---

## File structure

```
arkham-tabularium/
├── hugo.toml                   ← Site configuration
├── archetypes/
│   ├── default.md              ← Template for general articles
│   ├── scenarios.md            ← Template for scenario reviews
│   ├── decks.md                ← Template for deck guides
│   └── campaigns.md            ← Template for campaign logs
├── layouts/
│   ├── _default/
│   │   ├── baseof.html         ← Base HTML + all CSS
│   │   ├── list.html           ← Section listing pages
│   │   └── single.html         ← Individual article pages
│   ├── index.html              ← Home page
│   └── partials/
│       ├── header.html
│       ├── footer.html
│       └── card.html           ← Article card component
└── content/
    ├── scenarios/              ← Scenario reviews go here
    ├── investigators/          ← Investigator analyses
    ├── decks/                  ← Deck guides
    ├── campaigns/              ← Campaign logs
    └── articles/               ← General articles
```

---

## Multilingual content

The site supports multiple languages out of the box. English is the default (served at `/`), French at `/fr/`.

### Writing a translated article

Add the language code before `.md` in the filename:

```
content/scenarios/the-gathering.md       ← English (default)
content/scenarios/the-gathering.fr.md    ← French translation
```

Hugo links them automatically. A "also available in" notice appears on each article that has a translation, and the language switcher in the header activates.

Articles with no translation simply appear in their own language only — no placeholder needed.

### Adding a new language

1. Add a `[languages.xx]` block in `hugo.toml` (Portuguese and Dutch are already configured; follow the same pattern for others).
2. Create `i18n/xx.toml` with translated UI strings (copy `i18n/en.toml` as a starting point).
3. Add `_index.xx.md` files for each section you want translated.
4. Write articles as `filename.xx.md`.

### URL structure

| Language | URL |
|---|---|
| English | `iskander.github.io/arkham-tabularium/scenarios/the-gathering/` |
| French | `iskander.github.io/arkham-tabularium/fr/scenarios/the-gathering/` |
| Dutch | `iskander.github.io/arkham-tabularium/nl/scenarios/the-gathering/` |
| Portuguese | `iskander.github.io/arkham-tabularium/pt/scenarios/the-gathering/` |

English lives at the root (no `/en/` prefix). All other languages are prefixed.

---

## Analytics (GoatCounter)

GoatCounter is a privacy-first, cookie-free analytics tool. It's free for public non-commercial sites and open-source.

### Setup

1. Create a free account at [goatcounter.com](https://www.goatcounter.com/)
2. Choose a site code (e.g. `arkhamt` → `arkhamt.goatcounter.com`)
3. Add it to `hugo.toml`:

```toml
[params]
  goatcounter = "arkhamt"
```

Analytics are automatically skipped during local development (`hugo server`). To disable tracking on a specific article, add `analytics: false` to its front matter.

---

## Discussion links

Each article can link to its BGG thread and/or Reddit post. Add the URLs to the article's front matter after publishing and starting the community discussion:

```yaml
bgg_thread: "https://boardgamegeek.com/thread/XXXXXXX"
reddit_thread: "https://www.reddit.com/r/arkhamhorrorlcg/comments/XXXXX"
```

If neither URL is set, the block shows links to the general BGG and Reddit community forums instead — always giving readers a place to go.

To hide the discussion block entirely on an article:

```yaml
comments: false
```

### Workflow

1. Publish the article (`draft: false`, `git push`)
2. Post links on BGG and/or Reddit
3. Copy the thread URLs back into the article's front matter
4. `git push` again — the links now appear at the bottom of the article

---

## Images

### Card images — `{{< card >}}`

Never store FFG card art in the repo. The `{{< card >}}` shortcode fetches
images from ArkhamDB at build time:

```
{{< card "02003" >}}
```

In non-English articles, supply the translated card name via `name=`:

```
{{< card "02003" name="Agnès Baker" >}}
{{< card "03006" name="Le Domaine de la Sorcière" >}}
```

For side-by-side cards:

```
{{< cardgroup caption="Investigators used in this run" >}}
  {{< card "02003" name="Agnès Baker" >}}
  {{< card "02004" name="Skids O'Toole" >}}
{{< /cardgroup >}}
```

### Your own images — `{{< figure >}}`

Articles with images should be **Page Bundles** — a folder instead of a
single file, with images stored alongside the Markdown:

```
content/scenarios/the-gathering/
  index.md            ← English
  index.fr.md         ← French translation
  index.pt.md         ← Portuguese translation
  setup.jpg           ← shared image (used by all translations)
  encounter-deck.jpg
```

Reference images in articles:

```
{{< figure src="setup.jpg" alt="Initial setup" caption="Board state at start." >}}
{{< figure src="map.jpg" alt="Location map" float="right" width="300" >}}
```

Hugo converts images to WebP, generates srcset variants, and adds
lazy loading automatically at build time.

**Multilingual alt text:** write `alt` and `caption` directly in each
translation file in the correct language — the image file itself is shared.

See `docs/shortcodes.md` and `docs/images.md` for full reference.

---

## Writing with Obsidian

Open the `arkham-tabularium/` folder as an Obsidian vault. The key settings
are already pre-configured in `.obsidian/app.json`:

- **Wikilinks disabled** — Obsidian uses standard `[text](path)` links,
  which Hugo understands natively
- **Attachments in same folder** — pasted images land in the article's
  Page Bundle automatically
- **Templates folder** — five templates in `.obsidian/templates/` mirror
  the Hugo archetypes (Scenario Review, Deck Guide, Campaign Log,
  Investigator Analysis, Article)

### Quick start

1. Obsidian → Open folder as vault → select `arkham-tabularium/`
2. Settings → Core plugins → enable **Templates**
3. Write articles in `content/` subfolders
4. Use **Cmd/Ctrl+P → Insert template** to scaffold new articles
5. Use the **Properties panel** to manage front matter visually
6. Run `hugo server` in a terminal alongside Obsidian for live preview

### Pre-build validation

Before pushing, the script `scripts/pre-build-check.py` catches
Obsidian artifacts that would break the Hugo build:

```bash
python3 scripts/pre-build-check.py
```

It detects: wikilinks, Obsidian image embeds (`![[…]]`), Obsidian
callouts (`> [!note]`), Dataview blocks, and empty alt text.

This check also runs automatically in GitHub Actions before every build —
a push with wikilinks in an article will fail the build with a clear
error message pointing to the exact file and line.

See `docs/obsidian-workflow.md` for the full workflow documentation.
