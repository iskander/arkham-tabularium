# Shortcodes Reference

Arkham Tabularium provides three custom shortcodes for use in articles.

---

## `{{< card >}}` — ArkhamDB card widget

Fetches card data from ArkhamDB at build time and renders a card image with
faction-coloured border and a link to the card's ArkhamDB page.

```
{{< card "02003" >}}
```

| Parameter | Default | Notes |
|---|---|---|
| (positional) | — | ArkhamDB card code, required |
| `name` | API English name | Translated card name for non-English articles |
| `size` | `medium` | `small` (120px) · `medium` (180px) · `large` (300px) |

### Multilingual usage

ArkhamDB's API returns English card names. In French, Portuguese, or Dutch
articles, supply the translated name via the `name` parameter:

```
{{< card "02003" name="Agnès Baker" >}}          ← same in all languages
{{< card "60301" name="Nathaniel Cho" >}}

{{< card "02003" name="Agnès Baker" >}}          ← French article
{{< card "03006" name="Le Domaine de la Sorcière" >}}
```

If you omit `name` in a non-English article, the English name is shown with a
small note "(name in English)" — the card is still correctly linked and displayed.

---

## `{{< cardgroup >}}` — horizontal card row

Wraps multiple `{{< card >}}` calls in a flex row for side-by-side display.

```
{{< cardgroup caption="Investigators used in this playthrough" >}}
  {{< card "02003" name="Agnès Baker" >}}
  {{< card "02004" name="Skids O'Toole" >}}
{{< /cardgroup >}}
```

| Parameter | Default | Notes |
|---|---|---|
| `caption` | — | Optional caption below the row |

---

## `{{< figure >}}` — responsive image

Renders an image from the article's **Page Bundle** (see below), processed
at build time into WebP with a `srcset` for mobile.

```
{{< figure src="encounter-deck.jpg" alt="The encounter deck" >}}
{{< figure src="setup.jpg" alt="Initial setup" caption="Board state at start." >}}
{{< figure src="portrait.jpg" alt="Agnes" float="right" width="300" >}}
```

| Parameter | Default | Notes |
|---|---|---|
| `src` | — | Filename in the page bundle, required |
| `alt` | `""` | Alt text — write in the article's language |
| `caption` | — | Optional caption — write in the article's language |
| `width` | `800` | Max display width in px |
| `float` | — | `left` or `right` to float beside text |
| `link` | — | Optional URL to wrap the image |

**The `alt` and `caption` parameters carry the multilingual responsibility.**
Since you write them directly in the article's `.md` file, they are naturally
in the correct language for each translation. There is no centralised alt text
to translate — just write naturally.

---

## Page Bundles — how to structure articles with images

A regular article is a single `.md` file:
```
content/arkham-lcg/scenarios/the-gathering.md
```

An article with images should be a **Page Bundle** — a folder with `index.md`
inside it, and images alongside:

```
content/arkham-lcg/scenarios/the-gathering/
  index.md                  ← English article
  index.fr.md               ← French translation
  encounter-deck.jpg        ← shared image (language-neutral)
  setup-photo.jpg
  ghoul-priest-hp-chart.png
```

Images in the bundle are shared across all translations of that article —
you only store the file once. The `alt` and `caption` text you write in each
`index.XX.md` file provide the language-specific descriptions.

### Creating a new Page Bundle article

```bash
# Instead of:
hugo new arkham-lcg/scenarios/the-midnight-masks.md

# Do this:
mkdir -p content/arkham-lcg/scenarios/the-midnight-masks
hugo new --kind scenarios arkham-lcg/scenarios/the-midnight-masks/index.md
# Then copy images into content/arkham-lcg/scenarios/the-midnight-masks/
```

Or just create the folder and file manually — Hugo treats any folder
containing an `index.md` as a Page Bundle automatically.

---

## ArkhamDB card codes

Find card codes in the ArkhamDB URL:
```
https://arkhamdb.com/card/02003  →  code is "02003"
```

Or via the API:
```
https://arkhamdb.com/api/public/card/02003
```

The API response includes `faction_code` (used for the border colour),
`type_name`, and `name` — all used by the shortcode automatically.
