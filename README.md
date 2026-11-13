# MindInMotion software

Public downloads for Cold Open, Backlot, Dumptruck, Lacquer and Writers Block, served by GitHub Pages at [mindinmotionsoftware.com](https://mindinmotionsoftware.com/).

The landing page is `index.html`, and each app has a page of its own (`cold-open/`, `writers-block/`, `backlot/`, `dumptruck/`, `lacquer/`). They are generated, so edit the source and rebuild:

```sh
python3 scripts/build-site.py   # needs Python 3 with Pillow
python3 scripts/check-guides.py
```

- The words, page titles and descriptions are in `scripts/build-site.py`.
- Release facts (version, size, download link, checksum) are in `releases.json`. The pages also read the newest GitHub release when they load, so `releases.json` is only what shows when GitHub cannot be reached. After an app release, edit that app's entry, rebuild and commit.
- The look is `assets/site.css`. It uses system fonts, so the pages load nothing from another site except the release lookup. `assets/site.js` holds the copy buttons and that lookup.
- The build also writes `sitemap.xml`, `robots.txt`, `404.html` and the share images in `assets/og/`.
- Each app's main screenshot is in `assets/shots/` as WebP at two widths, `<app>-1600.webp` and `<app>-800.webp`.
- The extra screenshots (`assets/shots/<app>-<name>-1440.webp` and `-720.webp`) and the walkthrough clips (`assets/video/`) are made from the guide images and recordings by `python3 scripts/build-media.py`, which needs ffmpeg. Run it when those sources change, then list the new file under the app's `gallery` or `clips` in `scripts/build-site.py`.

Each app page has its own title, description, canonical link and `SoftwareApplication` data for search engines. The sitemap is at `/sitemap.xml`; submit it once in Google Search Console and Bing Webmaster Tools.

## User guides

Cold Open and Backlot have browsable guides under `guides/`, with screenshots, captioned videos and sample scripts. `downloads/` holds complete offline ZIP bundles and `GUIDE-SHA256SUMS`. Unzip a bundle and open its `index.html`; page navigation and videos work offline. Account sign-in and external support/download links still need internet access.

The reviewed Markdown and media are checked in alongside generated HTML. `guides/sources.json` records the source revisions. Public copies use public support links and keep the two Backlot technical references inside its guide. Clean screenshots from the public Cold Open build replace earlier captures with a baseline-restore error. The Recent dialog image was omitted because it exposed a temporary file path. One outdated credential sentence in the AI reference was corrected to describe the provider connection used by requests.

To update the HTML and bundles, use Node 20.11 or later and Python 3:

```sh
npm ci
npm run build:guides
npm run check:guides
python3 -m http.server 8766
```

Check the local preview at `http://localhost:8766` in desktop and mobile layouts before merging. GitHub Pages serves the checked-in files from `main`; visitors do not need Node, Python, JavaScript or a GitHub account to read the guides. Each guide includes its GPL-3.0 license.

Publishing guide updates does not rebuild the signed app DMGs. App versions, release source archives and DMG checksums continue to identify the original app builds. Attach the guide ZIP and its checksum as separate documentation assets when adding them to a public release.
