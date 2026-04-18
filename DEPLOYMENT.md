# Deployment Checklist

Follow this in order. Each section is independent — once complete, you have
a live, monitored, multilingual Hugo site with discussion integration.

---

## 1. Local setup

**Install Hugo Extended** (required for image processing and remote fetching):

```bash
# macOS
brew install hugo

# Linux
sudo apt install hugo            # may be older; prefer the GitHub binary
# OR download the latest from https://github.com/gohugoio/hugo/releases

# Verify
hugo version
# Must say "hugo.Extended" and v0.120.0 or newer
```

**Install Python 3** (for the pre-build check script — already on macOS/Linux).

**Clone / open the project:**

```bash
cd ~/Documents              # or wherever you keep projects
# If starting fresh:
unzip ~/Downloads/arkham-tabularium.zip
cd arkham-tabularium

# Or if already in Git:
git clone git@github.com:YOURUSERNAME/arkham-tabularium.git
cd arkham-tabularium
```

**Test local build:**

```bash
python3 scripts/pre-build-check.py
hugo server -D
```

Open http://localhost:1313 — should show the home page with the sample
scenario review. Test the language switcher in the header.

---

## 2. Configuration — replace placeholders

Five values need replacing before first deployment. All are currently set
to obvious placeholders that would break the site if left as-is.

### `hugo.toml`

```toml
baseURL = "https://yourdomain.com/"          # ← your actual domain
```

If you don't have a custom domain yet, use your GitHub Pages URL:
`https://yourusername.github.io/arkham-tabularium/`

### `hugo.toml` → `[params]`

```toml
[params]
  author = "Alexandre"
  goatcounter = ""                            # ← see step 4 below
```

Leave `goatcounter` empty for now — fill it in after you create the
GoatCounter account.

---

## 3. GitHub setup

### Create the repository

```bash
# On github.com, create a new empty public repo named "arkham-tabularium"
# Then locally:
git init
git add .
git commit -m "Initial commit — Arkham Tabularium"
git branch -M main
git remote add origin git@github.com:YOURUSERNAME/arkham-tabularium.git
git push -u origin main
```

### Enable GitHub Pages

1. Go to repo → **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. That's it — the existing workflow (`.github/workflows/hugo.yml`) will
   handle deployment on every push to `main`.

### First deployment

After the first push, go to the **Actions** tab and watch the workflow run.
It should complete in 1–2 minutes. If it fails:

- Check the "Pre-build validation" step output for Obsidian artifacts
- Check the "Build" step for Hugo template errors
- Verify Python is available (the workflow uses `actions/setup-python@v5`)

When green, your site is live at `https://yourusername.github.io/arkham-tabularium/`.

---

## 4. Analytics — GoatCounter

1. Go to [goatcounter.com](https://www.goatcounter.com/)
2. Click **Sign up** → choose a site code (e.g. `arkhamt` for
   `arkhamt.goatcounter.com`) and enter your email
3. Confirm the email, log in
4. In your dashboard, note your site code
5. Back in `hugo.toml`:

   ```toml
   [params]
     goatcounter = "arkhamt"          # ← your code, no URL prefix
   ```

6. Commit and push:

   ```bash
   git add hugo.toml
   git commit -m "Enable GoatCounter analytics"
   git push
   ```

Analytics are suppressed during local development automatically.
Dashboard at `https://arkhamt.goatcounter.com` — free forever for non-
commercial sites.

---

## 5. Codeberg mirror (redundancy)

1. Create a free account at [codeberg.org](https://codeberg.org/)
2. Create a new empty repo named `arkham-tabularium`
3. Add it as a second remote:

   ```bash
   git remote add codeberg git@codeberg.org:YOURUSERNAME/arkham-tabularium.git
   git push --all codeberg
   ```

4. Set up a push-to-both alias for convenience:

   ```bash
   git config alias.pushall '!git push origin main && git push codeberg main'
   # Now: git pushall   →   pushes to both hosts
   ```

Your source code is now mirrored to two independent hosts (GitHub/Microsoft
and Codeberg non-profit). If either disappears, the other is intact.

---

## 6. Custom domain (optional)

### Buy a domain

Registrars worth considering: Gandi, Namecheap, Porkbun. €10–15/year for
a `.com` or `.net`. Consider a shorter brandable domain — `at.games`,
`arkhamtab.com`, etc.

### Point it at GitHub Pages

1. In your domain registrar's DNS settings, add these records:

   ```
   Type   Name    Value
   ────   ────    ─────
   A      @       185.199.108.153
   A      @       185.199.109.153
   A      @       185.199.110.153
   A      @       185.199.111.153
   CNAME  www     YOURUSERNAME.github.io
   ```

2. In the GitHub repo: **Settings** → **Pages** → **Custom domain** →
   enter your domain → **Save**.

3. Wait for DNS propagation (minutes to 24 hours), then check
   **Enforce HTTPS**.

4. Update `hugo.toml`:

   ```toml
   baseURL = "https://yourdomain.com/"
   ```

5. Commit and push.

---

## 7. Wayback Machine archiving

Once the site is live:

1. Submit the home page once: https://web.archive.org/save/
2. The Wayback crawler will pick up the rest over time automatically.
3. After publishing any significant article, manually submit that URL
   too — takes 10 seconds, guarantees the article is archived.

You can also use the [Wayback Machine browser extension](https://archive.org/details/wayback-machine) to submit pages with one click.

---

## 8. Obsidian setup (writing environment)

1. Open Obsidian → **Open folder as vault** → select the `arkham-tabularium/` folder
2. Settings → **Core plugins** → enable **Templates**
3. Verify Settings → **Files & Links**:
   - Use `[[Wikilinks]]`: **OFF**
   - Default location for new attachments: **Same folder as current file**
   - New link format: **Relative path**

These are already pre-configured in `.obsidian/app.json`, but Obsidian may
occasionally need a restart to pick them up on first open.

---

## 9. First article — end-to-end test

Before writing real content, run through the full workflow once with a
throwaway article to make sure everything works:

1. In Obsidian: create `content/articles/test-article/index.md`
2. Insert the "Article" template (Cmd/Ctrl+P → Insert template → Article)
3. Fill in the title in Properties panel, leave `draft: true`
4. Check `hugo server -D` in terminal — article appears
5. Change `draft: false` — article remains (since `-D` was showing drafts too)
6. Stop and restart `hugo server` without `-D` — article still appears
7. Commit and push:

   ```bash
   git add .
   git commit -m "Test article"
   git push
   ```

8. Watch GitHub Actions build → site updates
9. Delete the test article:

   ```bash
   rm -rf content/articles/test-article
   git add .
   git commit -m "Remove test article"
   git push
   ```

If all seven steps worked, the full pipeline is verified.

---

## 10. Post-launch hygiene

### Weekly

- [ ] Check GoatCounter for traffic patterns and referrers
- [ ] Submit any new articles to Wayback Machine manually

### Monthly

- [ ] Run `hugo --gc` locally to clean build caches
- [ ] Mirror push to Codeberg (if not using the `pushall` alias)
- [ ] Review GitHub Actions history — any failed builds to investigate?

### When adding translations

- Add language files to all `content/*/` sections (not just the ones
  with translated articles — the section indexes are needed too)
- Keep the i18n files (`i18n/*.toml`) in sync: all four should have
  the same set of keys

---

## Reference — what to edit for what

| You want to… | Edit… |
|---|---|
| Change site title | `hugo.toml` → `title = "…"` |
| Change tagline | `hugo.toml` → `[languages.XX.params] tagline = "…"` |
| Change menu labels | `hugo.toml` → `[[languages.XX.menu.main]]` |
| Change colours | `layouts/_default/baseof.html` → `:root { --… }` |
| Change fonts | `layouts/_default/baseof.html` → `<link href="…fonts.google">` |
| Add UI string | `i18n/XX.toml` for all four languages |
| Change footer text | `layouts/partials/footer.html` |
| Change discussion block | `layouts/partials/comments.html` |

---

## If something goes wrong

**GitHub Actions build fails on "Pre-build validation":**
An Obsidian artifact slipped through. Read the error message — it names
the exact file and line and suggests the fix. Fix it, commit, push again.

**GitHub Actions build fails on "Build":**
Hugo template error. Most common cause: invalid front matter YAML in a
new article. Run `hugo` locally to see the full error, fix, push.

**Site builds but looks broken:**
Usually a `baseURL` mismatch. Verify `hugo.toml` `baseURL` matches where
the site is actually served from.

**Language switcher shows wrong link:**
A section `_index.XX.md` is missing. Make sure every section has index
files in every configured language.

**Card shortcode shows "image unavailable":**
ArkhamDB API timeout or card code doesn't exist. Verify the code on
arkhamdb.com directly. Hugo caches API responses — run `hugo --gc` to
clear the cache and retry.
