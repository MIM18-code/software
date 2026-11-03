# Troubleshooting

Cold Open leaves state readable on purpose: errors stay in a place you can open and act on, not in a toast that vanishes.

## First addresses

1. Tools > Operation Error History…: the Activity dialog lists persistent errors with retry where one exists.
2. The status bar and the panels' own headers carry per-feature state (model, sync, phone) with their retry paths.
3. Tools > Command Palette… lists any command with the reason it is currently unavailable.

## The AI provider is not ready

1. Settings > AI: read the status line. "Provider reports ready" means the server answered; requests can still fail or hit a usage limit afterward.
2. Local (Ollama): choose Tools > Set up AI… > Set up local AI for me, or Download writing model if Ollama is already running. Earlier beta 8 builds show separate install/start buttons. If using a custom model, check Settings > AI > Advanced; its name must exist in Ollama (`ollama list` in a terminal shows what is pulled).
3. ChatGPT: sign in again from Settings > AI if the status is stale; the browser opens, then the connection resumes. Usage limits are your plan's, not Cold Open's.
4. API keys: check the key and its remaining balance with your provider.

Nothing switches from local to cloud (or the reverse) by itself; if a provider is down, the feature that used it is down until you pick another provider.

## Format Draft says it has no model

1. Tools > Manage Local Formatting Models….
2. Choose Set up formatting on this Mac… and confirm Download model. In earlier beta 8 builds, install and open Ollama first, then choose Refresh model status.
3. Wait for the formatter download, then choose Pin and use this version for Format Draft. The model manager displays 3.10 GB for the model alone.
4. A broken or partial download resumes rather than restarting; Pause cancels Cold Open's request only.

Format Draft for pasted text needs no microphone, only this model.

## Dictation does not start

1. Settings > Dictation: choose Prepare engine. The app includes Parakeet and loads it locally. Apple speech requires macOS 26 or later and may download the system speech asset for your language; prepare it before going offline.
2. macOS needs microphone permission the first time. Check System Settings > Privacy & Security > Microphone.
3. The speech helper path is found automatically; if it is not, Choose… points at it manually.

## Voice packs fail to download

1. Tools > Settings… > Local features: Refresh voice packs.
2. In the packs dialog, cancel and resume the download; a resumed pack continues rather than restarting.
3. Neural packs need macOS 15. On macOS 14, use installed Apple Premium or Enhanced voices (System Settings > Accessibility > Spoken Content > System Voice > Manage Voices). Quick Read uses a neural pack and also needs macOS 15.
4. Clearing the speech cache never removes weights; if disk space is tight, clear the cache, not the packs.

## Co-writing will not connect

1. Open the Connection diagnostics in the Co-writing panel: it separates what your Mac reports from whether a live connection exists.
2. Same-network share: both Macs need the same Wi-Fi. On a hotel or captive network this may fail; use Tailscale.
3. With no network at all, the invite only works on this Mac; Cold Open says so when you share.
4. Tailscale: both Macs signed in, MagicDNS on, and the same tailnet.
5. A self-hosted relay: check the relay address in Settings > Co-writing and that the relay is running.
6. Folder sync: the shown status is local truth. Confirm the file actually arrived on the other Mac before you trust it.

## One scene number, two scenes

1. Production > Scene Number Conflicts….
2. Cold Open shows each conflict; resolve by renumbering or accepting which scene keeps which.
3. Coordinate anything already published with your production team before renumbering.

## Someone's typing ended up in the wrong place after a scene move

1. Production > Scene Move Conflicts….
2. Cut the flagged text and paste it into the moved scene. Cold Open never deletes it for you. The watch has limits (moves older than the last eight per writer, and typing left by an Undo of a move can go unnoticed); nothing is lost either way, it just may not be flagged.

## An FDX export refuses to run

A script note is detached from the text it was pinned to. Reattach it from the Script Notes panel and export again. Cold Open blocks the export instead of saving a changed note.

## The file changed while Cold Open was saving

The app pauses autosave rather than overwriting an externally changed file; Settings > Native autosave offers Save / resolve file conflict… to settle it. External-change detection covers ordinary edits; make a backup copy before you trust a conflicted merge by hand.

## Cold Open crashed

Recovery is separate from autosave and from history. On the next launch, accept the recovery prompt; the recovered snapshot is per document and explicit. File > Draft History / Named Snapshot… (`⌘⇧H`) holds up to 64 versions (128 MB) per document with up to 20 named snapshots protected from pruning.

## Gatekeeper will not open the app

Cold Open ships signed and notarized. "Cold Open is an app downloaded from the Internet" needs one click on Open, once. If macOS shows "damaged" instead, the download is broken: delete the app and download the `.dmg` again, or reinstall the Homebrew cask.
