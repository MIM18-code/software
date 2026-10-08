# MindInMotion software

Download page for [Backlot](https://github.com/MIM18-code/homebrew-backlot) and [Dumptruck](https://github.com/MIM18-code/dumptruck), served by GitHub Pages at https://mim18-code.github.io/.

The page is one static file, `index.html`. When it loads, it asks the GitHub API for the newest release of each app and updates the version, size, download link and checksum. The links written into the HTML are the fallback if that request fails.

New releases show up on their own as long as each release:

- attaches a `.dmg` (Backlot's name starts with `Backlot-`)
- ends its notes with a line like ``SHA-256: `<64-character hash>` ``

Update the hard-coded fallback links in `index.html` now and then, so the page still points at a recent build when the API can't be reached.
