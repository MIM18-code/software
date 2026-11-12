#!/usr/bin/env python3
"""Build the landing page, one page per app, the sitemap and robots.txt.

    python3 scripts/build-site.py

The words live in this file. Release facts (version, size, links, checksum)
live in releases.json, so a release only edits that file and runs this.
Output is plain HTML checked in beside it; GitHub Pages serves it as is.
"""
import datetime
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://mindinmotionsoftware.com"
RELEASES = {k: v for k, v in json.loads((ROOT / "releases.json").read_text()).items()
            if not k.startswith("_")}
TODAY = datetime.date.today().isoformat()

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800'
         '&family=IBM+Plex+Mono&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">')

# The stages of a film, in order, and the apps that belong to each.
STAGES = [
    ("Write", "Get the script on the page", ["cold-open", "writers-block"]),
    ("Plan", "Budget it, break it down, schedule it", ["backlot"]),
    ("Shoot", "Back up every card before it is cleared", ["dumptruck"]),
    ("Deliver", "Put the finished film on a disc", ["lacquer"]),
]

APPS = {
    "cold-open": {
        "name": "Cold Open",
        "color": "green", "tape": "var(--green)",
        "icon": "assets/cold-open-512.png",
        "macos": "macOS 14 Sonoma or later", "license": "GPL-3.0",
        "category": "DesignApplication",
        "title": "Cold Open: free screenwriting app for Mac, Final Draft compatible",
        "description": "Cold Open is a free, open-source screenwriting app for Mac. It opens and saves Final Draft .fdx files, reads Fountain, and has templates for film and TV.",
        "what": "A free screenwriting app for Mac that opens and saves Final Draft files",
        "tagline": "A screenwriting app that opens and saves Final Draft files.",
        "summary": "Cold Open types like Final Draft: Tab and Return move through scene headings, action, characters and dialogue, and pages break where Final Draft breaks them. It opens and saves .fdx and keeps the Final Draft data it doesn't edit.",
        "points": [
            "Templates for features, one-hour, half-hour, multi-camera and stage plays",
            "Co-writers type in the same script at once",
            "Reads and writes Fountain too",
        ],
        "shot_alt": "Cold Open with a script open: the scene list on the left, the screenplay page in the middle, and the table-read panel on the right.",
        "lede": "Cold Open writes screenplays with Final Draft's elements and keys, paginates the way Final Draft does, and opens and saves .fdx files, keeping the Final Draft data it doesn't edit. It also reads and writes Fountain.",
        "features": [
            ("Writes like Final Draft.", "Tab and Return move through scene headings, action, characters and dialogue. Scene numbers lock and take A-numbers, revisions get their page colors, and script notes and breakdown tags survive a trip through FDX."),
            ("Templates for the format you're in.", "Features, one-hour drama, half-hour single-camera, multi-camera and stage plays, with act breaks and page breaks where those formats put them."),
            ("Write together.", "Co-writers on the same network, or through a relay, type in the same script at once and see each other's cursors."),
            ("Dictate scenes.", "The default speech recognizer is included and works offline. Dictate rough text, then use Format Draft to make screenplay elements after its one-time local model setup."),
            ("Hear the table read.", "Download local voices and Cold Open reads the script with a cast picked from what the script says about each character."),
            ("AI only if you want it.", "Proofreading suggestions, an assistant that reads the whole script before it answers and proposes edits you approve, casting help and an optional sentence completion that stays off until you turn it on. It runs on a local Ollama model, your own API key, or your ChatGPT plan, and nothing changes in the script until you accept it."),
            ("Use your ChatGPT plan.", 'Sign in with ChatGPT and Cold Open\'s AI features use your ChatGPT plan. Cold Open itself is free. <a href="https://help.openai.com/en/articles/20001542">Learn more</a>'),
        ],
        "install_note": "Open the disk image and drag Cold Open to Applications. Needs an Apple Silicon Mac with macOS 14 Sonoma or later; local table-read voices need macOS 15.",
        "brew": "cold-open",
        "brew_note": "Homebrew asks you to trust a third-party tap once, which is the second line. Update later with <code>brew upgrade --cask cold-open</code>.",
        "guide": ("guides/cold-open/index.html", "downloads/ColdOpen-user-guide.zip"),
        "repo": "https://github.com/MIM18-code/cold-open",
        "faq": [
            ("Is Cold Open free?", "Yes. It is free and open source under GPL-3.0. The AI features are optional and run on a local model, your own API key or your ChatGPT plan."),
            ("Can it open my Final Draft scripts?", "Yes. It opens and saves .fdx files and keeps the Final Draft data it doesn't edit, so a script can go back to Final Draft afterwards. It reads and writes Fountain as well."),
            ("Does it run on Intel Macs or Windows?", "No. Cold Open needs an Apple Silicon Mac with macOS 14 Sonoma or later."),
        ],
    },
    "writers-block": {
        "name": "Writers Block",
        "color": "teal", "tape": "var(--teal)",
        "icon": "assets/writers-block-512.png",
        "macos": "macOS 14 Sonoma or later", "license": "MIT",
        "category": "DesignApplication",
        "title": "Writers Block: dictate a screenplay into Final Draft on a Mac",
        "description": "Writers Block is a free Mac app that turns a scene you say out loud into formatted Final Draft paragraphs. The speech recognition runs on your Mac.",
        "what": "Screenplay dictation for Final Draft that runs on your Mac",
        "tagline": "Say a scene out loud and get Final Draft paragraphs.",
        "summary": "Click an empty paragraph in Final Draft, press Command-Option-D and talk through the scene. Press it again and the scene lands at your cursor with the heading, action, character names and dialogue each in its own element.",
        "points": [
            "Speech recognition and formatting both run on your Mac",
            "Understands “scratch that” and corrections mid-sentence",
            "Exports Fountain, FDX or plain text for other writing apps",
        ],
        "shot_alt": "Writers Block: the dictated words on the left and the same scene formatted as a screenplay page on the right.",
        "lede": "Click an empty paragraph in Final Draft, press Command-Option-D and talk through the scene: where you are, what happens, who says what. Press it again and the scene lands at your cursor as real Final Draft paragraphs, with the scene heading, action, character names, parentheticals and dialogue each in its own element. The speech recognition and the formatting both run on your Mac.",
        "note": "This is a beta. The formatting model gets most takes right, not every one. Read what it pasted the way you'd read any dictated draft. Every recording and transcript is saved, so a take that goes wrong can be fixed or run again.",
        "features": [
            ("Your words, labeled.", "The model decides which of your sentences is action and which is dialogue. It isn't asked to rewrite them. When a take drops or changes words, Writers Block pastes it anyway and tells you which words to check."),
            ("Talk the way you think.", "“Scratch that”, “no wait” and corrections partway through a sentence are handled. So is a heading you say in the middle of a sentence, like “she walks in, interior kitchen, night”."),
            ("Nothing is uploaded.", "Parakeet transcribes your recording and a writing model running in Ollama formats it, both on your Mac. On first launch, Writers Block walks you through installing Ollama and downloading the two models, about 6 GB in all."),
            ("Other writing apps too.", "In the Writers Block workspace you can record or paste a transcript, check the scene, then copy it, send it to any open app, or export Fountain, FDX or plain text."),
            ("Use the dictation app you have.", "If you already dictate with another app, paste its text into the workspace and Writers Block formats it the same way."),
        ],
        "install_note": "Open the disk image and drag Writers Block to Applications. Needs an Apple Silicon Mac with macOS 14 Sonoma or later and about 8 GB free for the models. On first launch it asks for the microphone, and for Accessibility so it can paste into Final Draft. It also helps you install Ollama, the free app that runs the writing model.",
        "faq": [
            ("Do I need Final Draft?", "No. Writers Block pastes into Final Draft if you have it, and its own workspace exports Fountain, FDX or plain text for any other writing app."),
            ("Is my voice sent anywhere?", "No. The speech recognition and the formatting model both run on your Mac."),
            ("How much disk space does it need?", "About 8 GB free. The two models it downloads on first launch are about 6 GB together."),
        ],
    },
    "backlot": {
        "name": "Backlot",
        "color": "blue", "tape": "var(--blue)",
        "icon": "assets/backlot-mark.svg",
        "macos": "macOS 13 Ventura or later", "license": "GPL-3.0",
        "category": "BusinessApplication",
        "title": "Backlot: free film budgeting and scheduling software for Mac",
        "description": "Backlot is a free, open-source production office for Mac: film budgets, script breakdowns, a stripboard, day out of days, call sheets and daily reports.",
        "what": "Free film budgeting, breakdown and scheduling for Mac",
        "tagline": "A production office on your Mac.",
        "summary": "Backlot keeps the budget, script breakdown, stripboard, day out of days, call sheets and daily reports in one project file on your own disk, and prints them the way a production office expects to see them.",
        "points": [
            "Budgets with fringes, globals, purchase orders and actuals",
            "Breakdowns from a Final Draft or Fountain script",
            "Call sheets sent as PDFs, with who confirmed",
        ],
        "shot_alt": "Backlot's stripboard: colored scene strips for interior and exterior scenes, split by black end-of-day bars across three shoot days.",
        "lede": "Backlot keeps the budget, script breakdown, stripboard, day out of days, call sheets and daily reports in one project file on your own disk, and prints them the way a production office expects to see them.",
        "features": [
            ("Budgets that track the money.", "Fringes, globals and budget alternatives, plus purchase orders, invoices and petty cash posted against each line, so every account shows committed, spent and variance."),
            ("Breakdowns from your script.", "Import a Final Draft or Fountain draft. When a revised draft comes in, Backlot shows what changed before it touches anything and marks the pages in the standard revision colors."),
            ("A real stripboard.", "Drag strips, sort by location or time of day, keep named board alternatives, pin shoot days to a calendar, and get a cast and element day out of days from the same board."),
            ("Call sheets you can send.", "Issue a call sheet as a PDF, send it by email or text, and see who confirmed. Daily reports, a take log and a one-click production book come from the same project."),
            ("Send it to your crew.", "Save the whole project as one file and email or AirDrop it. When it comes back, Backlot shows what changed and replaces your copy after backing it up."),
            ("Use your ChatGPT plan.", 'Sign in with ChatGPT and Backlot\'s assists use your ChatGPT plan. Backlot itself is free. <a href="https://help.openai.com/en/articles/20001542">Learn more</a>'),
            ("Works with Claude.", "A built-in MCP server lets Claude and other MCP clients read and edit the same project, with the same validation and undo history as the app."),
        ],
        "extras": ("Script import, scene reading, actor sides, tagged FDX export and PDF printing are included in beta 8. No separate reader, Chrome installation or AI account is needed for them.", [
            "Gorilla workbook and Movie Magic budget/schedule XML export need a separately configured integration. These formats are disabled when unavailable. PDF and CSV output are included.",
            "Email goes through your own Resend account or Google Workspace.",
            "AI assists run on a local Ollama model, your own API key, or your ChatGPT plan.",
        ]),
        "install_note": "Open the disk image and drag Backlot to Applications. Needs an Apple Silicon Mac with macOS 13 Ventura or later.",
        "brew": "backlot",
        "brew_note": "Homebrew asks you to trust a third-party tap once, which is the second line. Update later with <code>brew upgrade --cask backlot</code>.",
        "guide": ("guides/backlot/index.html", "downloads/Backlot-user-guide.zip"),
        "faq": [
            ("Is Backlot free?", "Yes. It is free and open source under GPL-3.0."),
            ("Where is my project stored?", "In one project file on your own disk. Nothing needs an account, and you can email or AirDrop the file to your crew."),
            ("Can it read my script?", "Yes. It imports Final Draft and Fountain drafts, and shows what changed when a revised draft comes in."),
            ("Does it run on Intel Macs or Windows?", "No. Backlot needs an Apple Silicon Mac with macOS 13 Ventura or later."),
        ],
    },
    "dumptruck": {
        "name": "Dumptruck",
        "color": "yellow", "tape": "var(--yellow)",
        "icon": "assets/dumptruck-512.png",
        "macos": "macOS 14 Sonoma or later", "license": "Apache-2.0",
        "category": "MultimediaApplication",
        "title": "Dumptruck: free camera card offload for Mac with verification",
        "description": "Dumptruck is a free, open-source Mac app that copies camera cards to backup drives, verifies every copy with checksums, and writes ASC MHL reports.",
        "what": "Free camera card offload for Mac that checks every copy",
        "tagline": "Camera card offload that checks every copy.",
        "summary": "Dumptruck copies a camera card to your backup drives, reads each copy back off the drive to check it against the card, and writes a report with ASC MHL manifests. A card shows SAFE TO CLEAR only when two separate drives hold verified copies.",
        "points": [
            "A card that kept shooting: only the new clips copy",
            "HTML and PDF reports with clip thumbnails",
            "Reads R3D, BRAW and ARRIRAW metadata",
        ],
        "shot_alt": "Dumptruck after two offloads: both cards marked VERIFIED, SAFE TO CLEAR, with a green lane for each of two backup drives.",
        "lede": "Dumptruck copies a camera card to your backup drives, reads each copy back off the drive to check it against the card, and writes an HTML and PDF report with ASC MHL manifests. A card shows SAFE TO CLEAR only when two separate drives hold verified copies. There is no erase button. Wiping the card is still your call.",
        "note": "This is a beta. SAFE TO CLEAR means the job passed Dumptruck's verification when it ran. It can't protect you from a drive that fails later. Keep your usual backup routine alongside it, and read the report before you erase a card.",
        "features": [
            ("Verification that reads the drive.", "Copies are written past the macOS file cache, so the verify pass reads the data back from the drive itself instead of from memory."),
            ("Cards that keep shooting.", "Bring back a card that wasn't formatted and Dumptruck copies only the new clips into the same folder, adding a new manifest generation. Changed or reused clip names get a loud warning, never a silent skip."),
            ("A pile of cards at once.", "Drag several cards over and Start Offload copies every one that is ready, all at once or one at a time. A card that can't start stays in the list with the reason."),
            ("Pause and carry on.", "Pause holds a transfer where it is, and Resume carries on from the same place with nothing copied twice. Pull the wrong card or kill the power and the next run picks up what is already verified."),
            ("Single clips off a drive.", "Pick the clips you want with Choose Source Files…, or drag them in from Finder, and Dumptruck copies just those, straight from the drive. They finish as VERIFIED, not SAFE TO CLEAR, since the rest of the drive wasn't copied."),
            ("Reports for the client.", "Every offload gets an HTML and PDF report with clip thumbnails and metadata, a JSON receipt, ASC MHL v2.0 and legacy MHL v1.1."),
            ("Camera formats.", "Dumptruck reads R3D, BRAW and ARRIRAW files for metadata and thumbnails through bundled helpers, which ask you to accept their terms the first time. Copying and verification work either way."),
        ],
        "install_note": "Open the disk image and drag Dumptruck to Applications. Needs an Apple Silicon Mac with macOS 14 Sonoma or later.",
        "brew": "dumptruck",
        "brew_note": "Same notarized build as the download. Update later with <code>brew upgrade --cask dumptruck</code>.",
        "clone": "https://github.com/MIM18-code/dumptruck.git",
        "repo": "https://github.com/MIM18-code/dumptruck",
        "faq": [
            ("How does it check a copy?", "It hashes each file as it reads the card, then reads every copy back from the destination drive and compares. The copies are written past the macOS file cache, so that read comes from the drive and not from memory."),
            ("When does a card show SAFE TO CLEAR?", "Only when two separate physical drives hold verified copies and the card itself read the same twice. Two partitions on one disk count as one drive. One verified drive shows VERIFIED and tells you to keep the card."),
            ("What does it write besides the copies?", "An HTML and PDF report with clip thumbnails, a JSON receipt, and ASC MHL v2.0 and legacy MHL v1.1 manifests."),
            ("Does it run on Intel Macs or Windows?", "No. Dumptruck needs an Apple Silicon Mac with macOS 14 Sonoma or later."),
        ],
    },
    "lacquer": {
        "name": "Lacquer",
        "color": "red", "tape": "var(--red)",
        "icon": "assets/lacquer-512.png",
        "macos": "macOS 13 Ventura or later", "license": "GPL-3.0",
        "category": "MultimediaApplication",
        "title": "Lacquer: free Blu-ray authoring app for Mac, with menus",
        "description": "Lacquer is a free, open-source Blu-ray authoring app for Mac. Turn a ProRes or H.264 master into a Blu-ray disc, ISO or BDMV folder with menus.",
        "what": "Free Blu-ray authoring for Mac, with menus",
        "tagline": "Blu-ray discs from your finished master.",
        "summary": "Lacquer takes the ProRes, DNxHR, H.264 or HEVC master you exported and makes a Blu-ray from it, with an on-screen menu if you want one. It writes a BDMV folder, a disc image for a duplicator, or an M2TS for Toast.",
        "points": [
            "Menus built from a frame of your film or your poster",
            "Sets the bitrate to fill a BD-25 or BD-50",
            "Subtitles from an .srt, chapters where you list them",
        ],
        "shot_alt": "Lacquer's window: disc size, video format, audio and chapter settings on the left, and a queued master on the right.",
        "lede": "Lacquer takes the ProRes, DNxHR, H.264 or HEVC master you exported and makes a Blu-ray from it, with an on-screen menu if you want one. It writes a BDMV folder, a disc image you can upload to a duplicator, or an M2TS for Toast. It works out the bitrate to fill the disc and warns you before it starts if anything is off.",
        "note": "This is a beta. Menus are checked with libbluray, the library VLC uses to play Blu-ray menus, but players differ. Burn one disc and try it on your own player before sending a run to a duplicator.",
        "features": [
            ("Menus that look like your film.", "Pick a frame from the film or your poster, choose one of three styles, and name your scenes. The preview shows the menu as a TV will draw it, and you can drive it with the arrow keys. On the disc, Play, scene buttons, subtitles on and off, and Top Menu all work from the remote."),
            ("The right format for your frame rate.", "Blu-ray has no 1080p at 25 or 29.97, so Lacquer carries those masters as 1080i without dropping a frame, and tells you when a format you picked would."),
            ("Audio the way editors export it.", "A 5.1 track is used as is. Six separate mono tracks from Resolve or Premiere are combined into 5.1, in either common channel order. Audio is AC-3, which every Blu-ray player decodes."),
            ("Fits the disc.", "Pick BD-25 or BD-50 and Lacquer sets the video bitrate from the running time. A film that can't fit is caught before encoding, not after."),
            ("Subtitles and chapters.", "Add an .srt and viewers can turn the subtitles on and off. Chapter stops go every 5 or 10 minutes or wherever you list them, and each one lands on its exact frame."),
            ("HDR and older footage.", "HDR masters are tonemapped to standard Rec.709, SD footage gets its color converted, and interlaced sources are deinterlaced before scaling."),
            ("A log for every disc.", "Each job writes a log next to its output with every command it ran, so a problem disc can be traced."),
        ],
        "install_note": "Open the disk image and drag Lacquer to Applications. Needs an Apple Silicon Mac with macOS 13 Ventura or later. FFmpeg and tsMuxeR are built in, so there's nothing else to install.",
        "faq": [
            ("What can I give it?", "A ProRes, DNxHR, H.264 or HEVC master. A 5.1 track is used as is, and six mono tracks are combined into 5.1."),
            ("What does it make?", "A BDMV folder you can burn, a disc image you can upload to a duplicator, or an M2TS for Toast."),
            ("Do I need to install FFmpeg?", "No. FFmpeg and tsMuxeR are built in."),
            ("Does it run on Intel Macs or Windows?", "No. Lacquer needs an Apple Silicon Mac with macOS 13 Ventura or later."),
        ],
    },
}

ORDER = [slug for _, _, slugs in STAGES for slug in slugs]


def esc(text):
    return html.escape(text, quote=True)


def head(*, title, description, path, root, image, extra_ld=None):
    url = SITE + path
    ld = [{
        "@context": "https://schema.org", "@type": "Organization",
        "name": "MindInMotion", "url": SITE + "/",
        "logo": SITE + "/assets/dumptruck-512.png",
    }]
    if extra_ld:
        ld.append(extra_ld)
    blocks = "\n".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>"
                       for x in ld)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MindInMotion Software">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='2' y='3' width='28' height='6' fill='%234CC97A'/%3E%3Crect x='2' y='10' width='28' height='6' fill='%236FA0FF'/%3E%3Crect x='2' y='17' width='28' height='6' fill='%23F7BF34'/%3E%3Crect x='2' y='24' width='28' height='6' fill='%23F4705C'/%3E%3C/svg%3E">
{FONTS}
<link rel="stylesheet" href="{root}assets/site.css">
{blocks}
</head>
"""


def masthead(root, current=None):
    links = "".join(
        f'<a href="{root}{slug}/"{" aria-current=\"page\"" if slug == current else ""}>{esc(APPS[slug]["name"])}</a>'
        for slug in ORDER)
    home = "./" if root == "" else root
    return f"""<header class="masthead">
  <a class="wordmark" href="{home}">MindInMotion Software</a>
  <nav aria-label="Apps">{links}</nav>
</header>"""


def shot(slug, root, *, lazy):
    app = APPS[slug]
    from PIL import Image  # only for the real pixel sizes
    w, h = Image.open(ROOT / f"assets/shots/{slug}-1600.webp").size
    loading = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return (f'<figure class="shot"><img src="{root}assets/shots/{slug}-1600.webp" '
            f'srcset="{root}assets/shots/{slug}-800.webp 800w, {root}assets/shots/{slug}-1600.webp {w}w" '
            f'sizes="(max-width: 900px) 94vw, 640px" width="{w}" height="{h}" alt="{esc(app["shot_alt"])}"{loading}></figure>')


def footer(root):
    links = "".join(f'<a href="{root}{slug}/">{esc(APPS[slug]["name"])}</a>' for slug in ORDER)
    return f"""<footer>
  <div class="wrap">
    <div>
      <p>All five apps are free betas for Apple Silicon Macs. There are no Intel or Windows builds. Every download is signed and notarized by Apple.</p>
      <p>Cold Open, Backlot and Lacquer are licensed under GPL-3.0, Dumptruck under Apache-2.0 and Writers Block under MIT, all copyright MindInMotion LLC. All five come without warranty. Third-party components keep their own licenses, listed in each release.</p>
    </div>
    <nav aria-label="All apps">{links}<a href="https://github.com/MIM18-code">GitHub</a></nav>
  </div>
</footer>
<script src="{root}assets/site.js" defer></script>
</body>
</html>
"""


def download_button(slug, cls="button"):
    rel = RELEASES[slug]
    return (f'<a class="{cls}" data-app="{slug}" data-href="dmg" href="{rel["dmg"]}">Download '
            f'<small>(<span data-app="{slug}" data-field="size">{rel["size"]}</span>)</small></a>')


def build_index():
    parts = [head(
        title="Free Mac apps for filmmakers | MindInMotion Software",
        description="Free Mac apps for filmmakers from MindInMotion: screenwriting, budgeting and scheduling, camera card offload with verification, and Blu-ray authoring.",
        path="/", root="", image="assets/og/index.png",
        extra_ld={"@context": "https://schema.org", "@type": "WebSite",
                  "name": "MindInMotion Software", "url": SITE + "/"})]
    parts.append('<body>\n<div class="wrap">\n' + masthead("") + """
<section class="intro">
  <h1>Free Mac apps for making a film</h1>
  <p><strong>Write the script, budget and schedule the shoot, back up the camera cards, and put the finished film on a Blu-ray.</strong> Five apps from MindInMotion, an independent film company. All of them are free, and four are open source.</p>
</section>
</div>
<main>
""")
    first = True
    for stage, blurb, slugs in STAGES:
        parts.append(f'<div class="daybreak"><div class="wrap"><h2>{stage}</h2><p>{esc(blurb)}</p></div></div>\n')
        for slug in slugs:
            app, rel = APPS[slug], RELEASES[slug]
            points = "".join(f"<li>{esc(p)}</li>" for p in app["points"])
            parts.append(f"""<section class="strip {app["color"]}" id="{slug}" aria-labelledby="{slug}-title">
  <div class="wrap">
    <div>
      <div class="strip-head">
        <img src="{app["icon"]}" alt="" width="64" height="64">
        <h3 id="{slug}-title"><a href="{slug}/">{esc(app["name"])}</a></h3>
      </div>
      <p class="tagline">{esc(app["tagline"])}</p>
      <p class="summary">{esc(app["summary"])}</p>
      <ul class="points">{points}</ul>
      <div class="actions">
        {download_button(slug)}
        <a class="more" href="{slug}/">More about {esc(app["name"])}</a>
      </div>
      <p class="fineprint">Version <span data-app="{slug}" data-field="version">{rel["version"]}</span>. {esc(app["macos"])}, Apple Silicon. {app["license"]}.</p>
    </div>
    {shot(slug, "", lazy=not first)}
  </div>
</section>
""")
            first = False
    parts.append("</main>\n" + footer(""))
    (ROOT / "index.html").write_text("".join(parts))


def install_panel(slug, root):
    app, rel = APPS[slug], RELEASES[slug]
    out = [f"""<aside class="install" aria-label="Get {esc(app["name"])}">
  <div class="install-body">
    <a class="dl" data-app="{slug}" data-href="dmg" href="{rel["dmg"]}">
      Download {esc(app["name"])}
      <small><span data-app="{slug}" data-field="version">{rel["version"]}</span>, <span data-app="{slug}" data-field="size">{rel["size"]}</span> disk image</small>
    </a>
    <p class="after-dl">{esc(app["install_note"])}</p>
"""]
    if "brew" in app:
        tap = app["brew"]
        out.append(f"""
    <h3>Or install with Homebrew</h3>
    <div class="code">
      <pre id="brew-{slug}">brew tap MIM18-code/{tap}
brew trust MIM18-code/{tap}
brew install --cask {tap}</pre>
      <button class="copy" type="button" data-copy="brew-{slug}">Copy</button>
    </div>
    <p class="after-dl">{app["brew_note"]}</p>
""")
    if "clone" in app:
        out.append(f"""
    <h3>Build from source</h3>
    <div class="code">
      <pre id="src-{slug}">git clone {app["clone"]}</pre>
      <button class="copy" type="button" data-copy="src-{slug}">Copy</button>
    </div>
    <p class="after-dl">The README walks through the Python engine, FFmpeg and the SwiftUI app build.</p>
""")
    if "guide" in app:
        page, bundle = app["guide"]
        out.append(f"""
    <h3>User guide</h3>
    <ul class="links">
      <li><a href="{root}{page}">Read the {esc(app["name"])} guide</a><span class="aside">Screenshots and captioned walkthroughs</span></li>
      <li><a href="{root}{bundle}" download>Download the complete guide</a><span class="aside">Read offline, with videos and sample scripts</span></li>
      <li><a href="{root}downloads/GUIDE-SHA256SUMS">Guide checksums</a><span class="aside">SHA-256 for the guide ZIPs</span></li>
    </ul>
""")
    rows = []
    if "repo" in app:
        rows.append(f'<li><a href="{app["repo"]}">Source code</a><span class="aside">{app["license"]}, on GitHub</span></li>')
    if "source" in rel:
        label = "Source archive" if "repo" in app else "Source code"
        note = rel["source_note"] if "repo" in app else f'{app["license"]}, {rel["source_note"]}'
        rows.append(f'<li><a data-app="{slug}" data-href="source" href="{rel["source"]}">{label}</a><span class="aside">{note}</span></li>')
    if "sums" in rel:
        rows.append(f'<li><a data-app="{slug}" data-href="sums" href="{rel["sums"]}">SHA-256 checksums</a><span class="aside">App release files</span></li>')
    rows.append(f'<li><a data-app="{slug}" data-href="release" href="{rel["release"]}">Release notes</a><span class="aside">On GitHub</span></li>')
    heading = "Source and checksums" if ("repo" in app or "source" in rel) else "Checksums"
    out.append(f"""
    <h3>{heading}</h3>
    <ul class="links">
      {chr(10).join("      " + r for r in rows).strip()}
    </ul>
    <p class="hash" data-app="{slug}" data-field="sha" data-file="{rel["dmg_file"]}">DMG SHA-256: {rel["sha256"]}</p>
  </div>
</aside>""")
    return "".join(out)


def build_app(slug):
    app, rel = APPS[slug], RELEASES[slug]
    root = "../"
    ld = {
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": app["name"], "description": app["description"],
        "url": f"{SITE}/{slug}/",
        "applicationCategory": app["category"],
        "operatingSystem": app["macos"].replace("macOS", "macOS").split(" or later")[0] + " or later (Apple Silicon)",
        "softwareVersion": rel["version"],
        "downloadUrl": rel["dmg"],
        "license": "https://spdx.org/licenses/" + {"GPL-3.0": "GPL-3.0-only"}.get(app["license"], app["license"]) + ".html",
        "image": f"{SITE}/{app['icon']}",
        "screenshot": f"{SITE}/assets/shots/{slug}-1600.webp",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Organization", "name": "MindInMotion", "url": SITE + "/"},
    }
    features = "".join(f"<li><b>{esc(lead)}</b> {body}</li>\n" for lead, body in app["features"])
    note = f'<p class="note">{esc(app["note"])}</p>\n' if "note" in app else ""
    extras = ""
    if "extras" in app:
        intro, items = app["extras"]
        extras = ('<h2 class="section-title">Optional extras</h2>\n<div class="small">\n'
                  f"<p>{esc(intro)}</p>\n<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>\n</div>\n")
    faq = "".join(f"<h3>{esc(q)}</h3>\n<p>{esc(a)}</p>\n" for q, a in app["faq"])
    others = "".join(
        f'<li class="{APPS[o]["color"]}"><a href="{root}{o}/"><b>{esc(APPS[o]["name"])}</b><span>{esc(APPS[o]["tagline"])}</span></a></li>'
        for o in ORDER if o != slug)
    page = head(title=app["title"], description=app["description"], path=f"/{slug}/", root=root,
                image=f"assets/og/{slug}.png", extra_ld=ld)
    page += f"""<body style="--tape: {app["tape"]}">
<div class="app-hero {app["color"]}">
  <div class="wrap">
    {masthead(root, slug)}
    <div class="app-hero-body">
      <div class="app-id">
        <img src="{root}{app["icon"]}" alt="" width="84" height="84">
      </div>
      <h1><span class="name">{esc(app["name"])}</span> <span class="what">{esc(app["what"])}</span></h1>
      <p class="lede">{esc(app["lede"])}</p>
      <div class="actions">
        {download_button(slug)}
        <span>Version <span data-app="{slug}" data-field="version">{rel["version"]}</span>. {esc(app["macos"])}, Apple Silicon. Free, {app["license"]}.</span>
      </div>
      {shot(slug, root, lazy=False).replace('sizes="(max-width: 900px) 94vw, 640px"', 'sizes="(max-width: 1180px) 94vw, 1124px"')}
    </div>
  </div>
</div>
<main class="wrap after-hero">
  <div class="columns">
    <div>
      {note}<h2 class="section-title">What it does</h2>
      <ul class="features">
{features}      </ul>
      {extras}<section class="faq" aria-label="Questions">
        <h2 class="section-title">Questions</h2>
{faq}      </section>
    </div>
    {install_panel(slug, root)}
  </div>
</main>
<nav class="others" aria-label="The other apps">
  <ul>{others}</ul>
</nav>
"""
    page += footer(root)
    out = ROOT / slug
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page)


def build_meta():
    urls = ["/"] + [f"/{slug}/" for slug in ORDER] + ["/guides/cold-open/", "/guides/backlot/"]
    body = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + body + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    page = head(title="Page not found | MindInMotion Software",
                description="That page isn't here. The five MindInMotion apps are listed on the home page.",
                path="/404.html", root="/", image="assets/og/index.png")
    page = page.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1)
    page += ('<body>\n<div class="wrap">\n' + masthead("/") + """
<section class="intro">
  <h1>That page isn't here</h1>
  <p>It may have moved when each app got a page of its own. <a href="/">The five apps are listed on the home page.</a></p>
</section>
</div>
<div class="page-end"></div>
""" + footer("/"))
    (ROOT / "404.html").write_text(page)


def build_og():
    """Share images: the app's strip color, its name, and its screenshot."""
    from PIL import Image, ImageDraw, ImageFont
    colors = {"green": "#4CC97A", "teal": "#2CC0B2", "blue": "#6FA0FF", "yellow": "#F7BF34", "red": "#F4705C"}
    bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    regular = "/System/Library/Fonts/Supplemental/Arial.ttf"
    out = ROOT / "assets/og"
    out.mkdir(exist_ok=True)
    for slug in ORDER:
        app = APPS[slug]
        im = Image.new("RGB", (1200, 630), colors[app["color"]])
        d = ImageDraw.Draw(im)
        d.text((60, 54), app["name"], font=ImageFont.truetype(bold, 86), fill="black")
        d.text((62, 160), app["what"], font=ImageFont.truetype(regular, 32), fill="black")
        s = Image.open(ROOT / f"assets/shots/{slug}-1600.webp").convert("RGB")
        s = s.resize((1080, round(s.height * 1080 / s.width)), Image.LANCZOS)
        frame = Image.new("RGB", (s.width + 6, s.height + 6), "black")
        frame.paste(s, (3, 3))
        im.paste(frame, (60, 236))
        im.save(out / f"{slug}.png", optimize=True)
    im = Image.new("RGB", (1200, 630), "black")
    d = ImageDraw.Draw(im)
    band = 630 // 6
    d.text((60, 22), "Free Mac apps for making a film", font=ImageFont.truetype(bold, 62), fill="white")
    for i, slug in enumerate(ORDER):
        app = APPS[slug]
        top = band * (i + 1)
        d.rectangle([0, top, 1200, top + band], fill=colors[app["color"]])
        d.text((60, top + 22), app["name"], font=ImageFont.truetype(bold, 54), fill="black")
        d.text((560, top + 36), app["tagline"], font=ImageFont.truetype(regular, 26), fill="black")
    im.save(out / "index.png", optimize=True)


if __name__ == "__main__":
    build_index()
    for slug in ORDER:
        build_app(slug)
    build_meta()
    build_og()
    print("built index.html,", ", ".join(f"{s}/index.html" for s in ORDER), "sitemap.xml, robots.txt, 404.html and share images")
