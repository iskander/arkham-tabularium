# Image Handling Guide

## Three types of images, three strategies

### 1. Card images — link to ArkhamDB

Never store FFG card images in your repo. ArkhamDB hosts them at stable URLs,
keeps them up to date, and redistributing them raises copyright questions.

Use the `{{< card >}}` shortcode — it fetches and displays them automatically.

### 2. Screenshots and original images — Page Bundles

Screenshots, photos, diagrams, maps, custom charts — anything you created that
belongs with a single article goes in the article's Page Bundle folder
alongside the Markdown files.

Hugo processes them at build time: converts to WebP, generates srcset variants,
strips EXIF, adds width/height to prevent layout shift.

### 3. Illustrations, banners, and composite images — external assets repo

Larger images that aren't individual cards (class banners, stylised composite
card spreads, multi-image illustrations) are stored in a separate public repo:
**`iskander/arkham-tabularium-assets`**, served via the jsDelivr CDN.

Reasons for keeping them out of the main repo:

- The main Hugo repo stays under GitHub's 1 GB soft limit
- Build times stay fast (no image processing on every deploy)
- Git history stays focused on text changes

Access these images via the `{{< figure >}}` shortcode's `asset=` parameter:

```
{{< figure asset="arkham-lcg/articles/c2-guardian/Guardian.jpg"
           alt="Guardian class banner — Chapter 2 Core"
           width="900" >}}
```

The shortcode prepends `Site.Params.assets_cdn` from `hugo.toml` automatically,
so article content never hard-codes the CDN URL. Migrating to a different CDN
or pinning to a specific release tag becomes a one-line edit in `hugo.toml`.

**Important trade-off:** external images bypass Hugo's build-time processing.
No WebP conversion, no srcset, no automatic dimension inference. They're served
as-is from the CDN. For most illustrations this is fine — the CDN is fast,
jsDelivr handles caching — but you should optimise the image *before* uploading
it to the assets repo (compress to reasonable dimensions, strip EXIF manually).

**Naming convention:** lowercase, hyphen-separated, no spaces (same as the main
repo). A few early files in the assets repo (`Vicious Blow.jpg`, etc.) predate
this convention and use spaces; those work but should not be imitated for new
uploads.

---

## Where to put images

**Wrong — global static folder:**
```
static/img/the-gathering-setup.jpg    ← hard to manage, shared namespace
```

**Right — Page Bundle:**
```
content/arkham-lcg/scenarios/the-gathering/
  index.md
  index.fr.md
  setup.jpg                           ← lives with its article
  encounter-deck.jpg
```

All translations of an article share the same image files. You only store
each image once regardless of how many language versions you write.

---

## Supported formats

Hugo can process: **JPEG, PNG, GIF, WebP, TIFF**

Recommended input format: **JPEG** for photos, **PNG** for screenshots with
text or UI elements. Hugo converts everything to WebP at build time for optimal
delivery while keeping your source files in their original format.

---

## Naming conventions

Use lowercase, hyphen-separated names with no spaces:

```
encounter-deck.jpg          ✓
ghoul-priest-hp.png         ✓
Setup Photo.JPG             ✗
```

---

## Build-time processing

The `{{< figure >}}` shortcode automatically:
- Converts to WebP
- Resizes to the requested `width` (default 800px)
- Generates a half-width srcset variant for mobile
- Adds `loading="lazy"` and `decoding="async"`
- Preserves aspect ratio

You never manually resize images — just drop the full-resolution file in the
bundle and Hugo handles optimisation at build time.

---

## Multilingual alt text and captions

Image files are language-neutral. The text describing them lives in the
article, written naturally in each language:

**English (index.md):**
```
{{< figure src="setup.jpg" alt="Initial board setup for The Gathering" caption="Roland's starting position." >}}
```

**French (index.fr.md):**
```
{{< figure src="setup.jpg" alt="Mise en place initiale pour La Réunion" caption="Position de départ de Roland." >}}
```

Same `src`, different `alt` and `caption` — no extra files needed.

---

## Repo size management

A text article with 3–4 screenshots will typically add 1–3 MB to your repo.
For dozens of articles this is fine. If you ever approach GitHub's 1 GB soft
limit, the options are:

1. **Optimise before committing** — use Squoosh or ImageMagick to compress
   images before adding them to the bundle. Even large screenshots are usually
   under 500 KB after compression.

2. **External hosting for heavy assets** — if you have many large images
   (e.g. full campaign photo diaries), consider Cloudflare Images (€5/month)
   and reference them via URL in the `{{< figure >}}` shortcode's fallback path.
