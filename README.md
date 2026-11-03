# MindInMotion software

Public downloads for Cold Open, Backlot, Dumptruck, Lacquer and Writers Block, served by GitHub Pages at [mindinmotionsoftware.com](https://mindinmotionsoftware.com/).

The landing page is `index.html`. It checks the public GitHub releases for current versions, sizes, download links and checksums. Its built-in links remain available when the API cannot be reached. Update those fallback links when publishing an app release.

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
