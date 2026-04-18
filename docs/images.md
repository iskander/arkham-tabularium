# Image Handling Guide

## Two types of images, two strategies

### 1. Card images — link to ArkhamDB

Never store FFG card images in your repo. ArkhamDB hosts them at stable URLs,
keeps them up to date, and redistributing them raises copyright questions.

Use the `{{< card >}}` shortcode — it fetches and displays them automatically.

### 2. Your own images — Page Bundles

Screenshots, photos, diagrams, maps, custom charts — anything you created or
own goes in the article's Page Bundle folder alongside the Markdown files.

Hugo processes them at build time: converts to WebP, generates srcset variants,
strips EXIF, adds width/height to prevent layout shift.

---

## Where to put images

**Wrong — global static folder:**
```
static/img/the-gathering-setup.jpg    ← hard to manage, shared namespace
```

**Right — Page Bundle:**
```
content/scenarios/the-gathering/
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
