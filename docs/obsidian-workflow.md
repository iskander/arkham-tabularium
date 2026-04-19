# Obsidian Workflow

## Setup — one time

### 1. Open the project as an Obsidian vault

In Obsidian: **Open folder as vault** → select the `arkham-tabularium/` folder.

Obsidian will create a `.obsidian/` config folder at the root alongside
`hugo.toml`. This is intentional — it stays completely out of Hugo's way.

### 2. Verify key settings (already pre-configured)

These settings are committed in `.obsidian/app.json` and should be active
automatically, but confirm them in Obsidian → Settings:

| Setting | Location | Required value |
|---|---|---|
| Use [[Wikilinks]] | Files & Links | **OFF** |
| New link format | Files & Links | Relative path |
| Default location for new attachments | Files & Links | **Same folder as current file** |

The wikilinks and attachment settings are the critical ones.
If wikilinks is ON, your links will break in Hugo.
If attachment folder is wrong, pasted images will land outside the Page Bundle.

### 3. Enable the Templates core plugin

Settings → Core plugins → **Templates** → enable.
The template folder is already set to `.obsidian/templates/`.

---

## Daily writing workflow

### Creating a new article

**Option A — Obsidian (recommended for writing)**

1. In the file explorer, navigate to the right game + type folder
   (e.g. `content/arkham-lcg/scenarios/` or `content/call-of-cthulhu/scenarios/`)
2. Create a new folder for the article (for Page Bundle support):
   right-click → New folder → `the-midnight-masks`
3. Inside that folder, create `index.md`
4. Open the file, then: **Cmd/Ctrl+P** → "Templates: Insert template"
   → select the right template (**Scenario Review**, **Adventure**,
   **Supplement Review**, **Deck Guide**, **Campaign Log**,
   **Investigator Analysis**, or **Article**)
5. Fill in the title and front matter fields using the Properties panel
   (the structured UI above the document body)

**Option B — Hugo CLI (for the front matter scaffold)**

```bash
# AH:LCG scenario
mkdir -p content/arkham-lcg/scenarios/the-midnight-masks
hugo new --kind scenarios arkham-lcg/scenarios/the-midnight-masks/index.md

# Call of Cthulhu scenario
mkdir -p content/call-of-cthulhu/scenarios/dead-light
hugo new --kind scenarios call-of-cthulhu/scenarios/dead-light/index.md

# AH:RPG adventure
mkdir -p content/arkham-rpg/adventures/hill-manor
hugo new --kind adventures arkham-rpg/adventures/hill-manor/index.md
```

Hugo picks the archetype based on the content type (the segment after the
game name). `arkham-lcg/scenarios/...` uses `archetypes/scenarios.md`;
`call-of-cthulhu/supplements/...` uses `archetypes/supplements.md`; etc.

Then open the file in Obsidian — the front matter is pre-filled from
the archetype, and Obsidian's Properties panel displays it as a form.

### Writing the article

Write normally in Obsidian. A few things to keep in mind:

**Links between articles** — use standard Markdown links, not wikilinks
(wikilinks are disabled in the vault settings):
```markdown
As discussed in [The Gathering](../the-gathering/), the core loop…
# (use relative paths — your article and the link target live in
# the same GAME/TYPE/ folder)
```

**Card images** — you can reference ArkhamDB cards two ways:

*As a plain image (renders correctly in Obsidian preview):*
```markdown
![Agnes Baker](https://arkhamdb.com/bundles/cards/02003.jpg)
```

*As the full shortcode (renders as raw text in Obsidian, correctly in Hugo):*
```
{{< card "02003" name="Agnès Baker" >}}
```

For writing/drafting, using plain image links is often easier. You can
convert to shortcodes before publishing if you want the faction colours
and ArkhamDB link behaviour.

**Your own screenshots** — paste directly into Obsidian. Because the
attachment folder is set to "same folder as current file", the image
lands in the article's Page Bundle folder automatically. Then reference
it in the article:

*Simple (renders in Obsidian and Hugo):*
```markdown
![The encounter deck](encounter-deck.jpg)
```

*With caption and resizing (Hugo shortcode, raw text in Obsidian):*
```
{{< figure src="encounter-deck.jpg" alt="The encounter deck"
    caption="Three cultists and a ghoul in the opening hand." >}}
```

**Callouts** — Obsidian has its own `> [!note]` callout syntax which is
incompatible with Hugo. Use Hugo's HTML callout divs instead:
```html
<div class="callout tip">
  <p class="callout-title">Tip</p>
  <p>Your tip here.</p>
</div>
```
These render as raw HTML in Obsidian's source view but display correctly
in Hugo. The pre-build check will warn you if you accidentally use
Obsidian-style callouts.

### Publishing an article

1. In Obsidian's Properties panel, change `draft` from `true` to `false`
2. Run the pre-build check locally (optional but recommended):
   ```bash
   python3 scripts/pre-build-check.py
   ```
3. Preview locally:
   ```bash
   hugo server
   ```
   (without `-D` flag — shows only published articles)
4. Commit and push:
   ```bash
   git add content/
   git commit -m "Publish: The Midnight Masks review"
   git push
   ```
5. GitHub Actions runs the pre-build check, then builds and deploys.

### Adding discussion links after publishing

After posting your BGG/Reddit thread, come back to the article in
Obsidian and fill in the Properties panel:

- `bgg_thread`: paste the BGG thread URL
- `reddit_thread`: paste the Reddit post URL

Then commit and push — the discussion buttons appear at the bottom
of the article.

---

## What renders differently in Obsidian vs Hugo

| Feature | Obsidian | Hugo |
|---|---|---|
| Standard Markdown | ✓ | ✓ |
| YAML front matter | ✓ (Properties panel) | ✓ |
| Standard images `![alt](file)` | ✓ | ✓ |
| HTML blocks (stat blocks, callouts, rating bars) | Source only | ✓ Rendered |
| `{{< card >}}` shortcode | Raw text | ✓ Rendered |
| `{{< figure >}}` shortcode | Raw text | ✓ Rendered (with WebP processing) |
| Wikilinks `[[…]]` | ✓ (disabled in settings) | ✗ Never use |
| Obsidian callouts `> [!note]` | ✓ | ✗ Never use |
| Dataview queries | ✓ (plugin) | ✗ Renders as code block |

**The key insight:** Obsidian is your writing environment; `hugo server`
is your rendering preview. Run both in parallel while working on an article.

---

## Recommended Obsidian plugins (optional)

**Core plugins** (built-in, just enable):
- Templates — already configured
- Word count — useful for tracking article length

**Community plugins** worth considering:
- **Linter** — auto-formats front matter on save (ensures consistent YAML)
- **Dataview** — query your content like a database inside Obsidian
  (e.g. list all published scenario reviews, all articles tagged "dunwich")
  Note: Dataview output is Obsidian-only, never put Dataview blocks in
  articles that Hugo will render.
- **Templater** — more powerful templating with dynamic date insertion
  and per-folder templates; can replace the core Templates plugin

**Do not install:**
- Wikilinks-to-MDLinks converter (the vault is already set to standard links)
- Any plugin that modifies link format globally

---

## Keeping Obsidian settings in sync across devices

The `.obsidian/app.json` and `.obsidian/templates/` folder are committed
to Git, so your settings and templates stay in sync across machines
automatically when you pull.

The following are **not** committed (they're in `.gitignore`) because
they're personal/device-specific:
- `workspace.json` — open tabs, cursor position
- `plugins/` — installed plugins (each machine installs its own)
- `themes/` — visual theme
