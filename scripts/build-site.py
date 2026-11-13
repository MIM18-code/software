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

# The stages of a film, in order, and the apps that belong to each.
STAGES = [
    ("Write", ["cold-open", "writers-block"]),
    ("Plan", ["backlot"]),
    ("Shoot", ["dumptruck"]),
    ("Deliver", ["lacquer"]),
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
        "shot_alt": "Cold Open with a script open: the scene list on the left, the screenplay page in the middle, and the table-read panel on the right.",
        "lede": "Cold Open writes screenplays with Final Draft's elements and keys, paginates the way Final Draft does, and opens and saves .fdx files, keeping the Final Draft data it doesn't edit. It also reads and writes Fountain.",
        "features": [
            ("Final Draft keys and pages", "Tab and Return move through scene headings, action, characters and dialogue. Scene numbers lock and take A-numbers, revisions get their page colors, and script notes and breakdown tags survive a trip through FDX."),
            ("Templates", "Features, one-hour drama, half-hour single-camera, multi-camera and stage plays, with act breaks and page breaks where those formats put them."),
            ("Co-writing", "Co-writers on the same network, or through a relay, type in the same script at once and see each other's cursors."),
            ("Dictation", "The speech recognizer is included and works offline. Dictate rough text, then use Format Draft to turn it into screenplay elements. Format Draft needs a one-time local model setup."),
            ("Table read", "Download local voices and Cold Open reads the script aloud, with a cast picked from what the script says about each character."),
            ("AI, if you turn it on", 'Proofreading suggestions, an assistant that reads the whole script before it answers and proposes edits you approve, casting help, and sentence completion that stays off until you switch it on. These run on a local Ollama model, your own API key or your ChatGPT plan, and nothing changes in the script until you accept it. Sign in with ChatGPT and Cold Open\'s AI features use your ChatGPT plan. Cold Open itself is free. <a href="https://help.openai.com/en/articles/20001542">Learn more</a>'),
        ],
        "clips": [
            ("editor", "The editor, scene list and outline"),
            ("dictation", "Formatting a dictated transcript"),
            ("breakdown", "Tagging a prop and sending the draft to Backlot"),
            ("movie-magic", "Exporting for Movie Magic Scheduling"),
        ],
        "gallery": [
            ("templates", "New from Template, with the five formats."),
            ("breakdown", "The Breakdown panel tagging the cast in scene 1."),
            ("revisions", "Starting a blue revision set."),
            ("dictation", "The Dictate panel."),
        ],
        "size_note": "Most of the download is the speech recognition model that lets dictation work offline.",
        "install_note": "Open the disk image and drag Cold Open to Applications. Needs an Apple Silicon Mac with macOS 14 Sonoma or later; local table-read voices need macOS 15.",
        "brew": "cold-open",
        "brew_note": "Homebrew asks you to trust a third-party tap once, which is the second line. Update later with <code>brew upgrade --cask cold-open</code>.",
        "guide": ("guides/cold-open/index.html", "downloads/ColdOpen-user-guide.zip"),
        "repo": "https://github.com/MIM18-code/cold-open",
        "faq": [
            ("Is Cold Open free?", "Yes. It is free and open source under GPL-3.0. The AI features are optional and run on a local model, your own API key or your ChatGPT plan."),
            ("Can it open my Final Draft scripts?", "Yes. It opens and saves .fdx files and keeps the Final Draft data it doesn't edit, so a script can go back to Final Draft afterwards. It reads and writes Fountain as well."),
            ("Why is the download so large?", "Most of it is the speech recognition model that lets dictation work offline. The app is built on Electron, which accounts for most of the rest."),
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
        "shot_alt": "Writers Block: the dictated words on the left and the same scene formatted as a screenplay page on the right.",
        "lede": "Click an empty paragraph in Final Draft, press Command-Option-D and talk through the scene: where you are, what happens, who says what. Press it again and the scene lands at your cursor as real Final Draft paragraphs, with the scene heading, action, character names, parentheticals and dialogue each in its own element. The speech recognition and the formatting both run on your Mac.",
        "note": "The formatting model gets most takes right, not every one. Read what it pasted the way you'd read any dictated draft. Every recording and transcript is saved, so a take that goes wrong can be fixed or run again.",
        "features": [
            ("What the model does", "The model decides which of your sentences is action and which is dialogue. It isn't asked to rewrite them. When a take drops or changes words, Writers Block pastes it anyway and tells you which words to check."),
            ("Corrections", "“Scratch that”, “no wait” and corrections partway through a sentence are handled. So is a heading you say in the middle of a sentence, like “she walks in, interior kitchen, night”."),
            ("Where it runs", "Parakeet transcribes your recording and a writing model running in Ollama formats it, both on your Mac. Nothing is uploaded. On first launch, Writers Block walks you through installing Ollama and downloading the two models, about 6 GB in all."),
            ("Other writing apps", "In the Writers Block workspace you can record or paste a transcript, check the scene, then copy it, send it to any open app, or export Fountain, FDX or plain text."),
            ("Other dictation apps", "If you already dictate with another app, paste its text into the workspace and Writers Block formats it the same way."),
        ],
        "clips": [
            ("format", "Formatting a pasted transcript with the local model"),
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
        "tagline": "Budgets, breakdowns, schedules and call sheets for a film shoot.",
        "summary": "Backlot keeps the budget, script breakdown, stripboard, day out of days, call sheets and daily reports in one project file on your own disk, and prints them the way a production office expects to see them.",
        "shot_alt": "Backlot's stripboard: colored scene strips for interior and exterior scenes, split by black end-of-day bars across three shoot days.",
        "lede": "Backlot keeps the budget, script breakdown, stripboard, day out of days, call sheets and daily reports in one project file on your own disk, and prints them the way a production office expects to see them.",
        "features": [
            ("Budget", "Fringes, globals and budget alternatives, plus purchase orders, invoices and petty cash posted against each line, so every account shows committed, spent and variance."),
            ("Script breakdown", "Import a Final Draft or Fountain draft. When a revised draft comes in, Backlot shows what changed before it touches anything and marks the pages in the standard revision colors."),
            ("Stripboard", "Drag strips, sort by location or time of day, keep named board alternatives, pin shoot days to a calendar, and get a cast and element day out of days from the same board."),
            ("Call sheets and reports", "Issue a call sheet as a PDF, send it by email or text, and see who confirmed. Daily reports, a take log and a one-click production book come from the same project."),
            ("Sharing a project", "Save the whole project as one file and email or AirDrop it. When it comes back, Backlot shows what changed and replaces your copy after backing it up."),
            ("AI, if you turn it on", 'The assists run on a local Ollama model, your own API key or your ChatGPT plan. Sign in with ChatGPT and Backlot\'s assists use your ChatGPT plan. Backlot itself is free. <a href="https://help.openai.com/en/articles/20001542">Learn more</a>'),
            ("Claude and MCP", "A built-in MCP server lets Claude and other MCP clients read and edit the same project, with the same validation and undo history as the app."),
        ],
        "clips": [
            ("import", "Importing a tagged script"),
            ("schedule", "Building a shooting schedule"),
            ("call-sheets", "Drafting a call sheet"),
        ],
        "gallery": [
            ("budget", "The budget, with globals above the accounts."),
            ("breakdown", "One scene's breakdown: cast, props, sound, set and the other element categories."),
            ("call-sheets", "A call sheet draft beside its PDF preview."),
            ("dood", "Day out of days for cast and elements."),
        ],
        "extras": ("Script import, scene reading, actor sides, tagged FDX export and PDF printing are included in beta 8. No separate reader, Chrome installation or AI account is needed for them.", [
            "Gorilla workbook and Movie Magic budget/schedule XML export need a separately configured integration. These formats are disabled when unavailable. PDF and CSV output are included.",
            "Email goes through your own Resend account or Google Workspace.",
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
        "tagline": "Copies camera cards to your backup drives and checks every copy.",
        "summary": "Dumptruck copies a camera card to your backup drives, reads each copy back off the drive to check it against the card, and writes a report with ASC MHL manifests. A card shows SAFE TO CLEAR only when two separate drives hold verified copies.",
        "shot_alt": "Dumptruck after an offload: card A001 marked VERIFIED, with a green lane for each of two backup drives.",
        "lede": "Dumptruck copies a camera card to your backup drives, reads each copy back off the drive to check it against the card, and writes an HTML and PDF report with ASC MHL manifests. A card shows SAFE TO CLEAR only when two separate drives hold verified copies. There is no erase button. Wiping the card is still your call.",
        "note": "SAFE TO CLEAR means the job passed Dumptruck's verification when it ran. It can't protect you from a drive that fails later. Dumptruck is still a beta, so keep your usual backup routine alongside it, and read the report before you erase a card.",
        "features": [
            ("Verification", "Copies are written past the macOS file cache, so the verify pass reads the data back from the drive itself instead of from memory."),
            ("Cards that come back", "Bring back a card that wasn't formatted and Dumptruck copies only the new clips into the same folder, adding a new manifest generation. Changed or reused clip names get a loud warning, never a silent skip."),
            ("Several cards", "Drag several cards over and Start Offload copies every one that is ready, all at once or one at a time. A card that can't start stays in the list with the reason."),
            ("Pause and resume", "Pause holds a transfer where it is, and Resume carries on from the same place with nothing copied twice. Pull the wrong card or kill the power and the next run picks up what is already verified."),
            ("Single clips", "Pick the clips you want with Choose Source Files…, or drag them in from Finder, and Dumptruck copies just those, straight from the drive. They finish as VERIFIED, not SAFE TO CLEAR, since the rest of the drive wasn't copied."),
            ("Reports", "Every offload gets an HTML and PDF report with clip thumbnails and metadata, a JSON receipt, ASC MHL v2.0 and legacy MHL v1.1."),
            ("Camera formats", "Dumptruck reads R3D, BRAW and ARRIRAW files for metadata and thumbnails through bundled helpers, which ask you to accept their terms the first time. Copying and verification work either way."),
        ],
        "clips": [
            ("offload", "Offloading one card to two drives"),
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
        "tagline": "Makes a Blu-ray from your finished master.",
        "summary": "Lacquer takes the ProRes, DNxHR, H.264 or HEVC master you exported and makes a Blu-ray from it, with an on-screen menu if you want one. It writes a BDMV folder, a disc image for a duplicator, or an M2TS for Toast.",
        "shot_alt": "Lacquer's window: disc size, video format, audio and chapter settings on the left, and a queued master on the right.",
        "lede": "Lacquer takes the ProRes, DNxHR, H.264 or HEVC master you exported and makes a Blu-ray from it, with an on-screen menu if you want one. It writes a BDMV folder, a disc image you can upload to a duplicator, or an M2TS for Toast. It works out the bitrate to fill the disc and warns you before it starts if anything is off.",
        "note": "Menus are checked with libbluray, the library VLC uses to play Blu-ray menus, but players differ. Burn one disc and try it on your own player before sending a run to a duplicator.",
        "features": [
            ("Menus", "Pick a frame from the film or your poster, choose one of three styles, and name your scenes. The preview shows the menu as a TV will draw it, and you can drive it with the arrow keys. On the disc, Play, scene buttons, subtitles on and off, and Top Menu all work from the remote."),
            ("Frame rates", "Blu-ray has no 1080p at 25 or 29.97, so Lacquer carries those masters as 1080i without dropping a frame, and tells you when a format you picked would."),
            ("Audio", "A 5.1 track is used as is. Six separate mono tracks from Resolve or Premiere are combined into 5.1, in either common channel order. Audio is AC-3, which every Blu-ray player decodes."),
            ("Disc size", "Pick BD-25 or BD-50 and Lacquer sets the video bitrate from the running time. A film that can't fit is caught before encoding, not after."),
            ("Subtitles and chapters", "Add an .srt and viewers can turn the subtitles on and off. Chapter stops go every 5 or 10 minutes or wherever you list them, and each one lands on its exact frame."),
            ("HDR and older footage", "HDR masters are tonemapped to standard Rec.709, SD footage gets its color converted, and interlaced sources are deinterlaced before scaling."),
            ("Job log", "Each job writes a log next to its output with every command it ran, so a problem disc can be traced."),
        ],
        "clips": [
            ("disc", "Adding a menu and starting the encode"),
        ],
        "gallery": [
            ("menu", "The menu designer with the Title Card style, on a test-pattern master."),
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

ORDER = [slug for _, slugs in STAGES for slug in slugs]


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


def shot(slug, root, *, lazy, wide=False, link=None):
    app = APPS[slug]
    from PIL import Image  # only for the real pixel sizes
    w, h = Image.open(ROOT / f"assets/shots/{slug}-1600.webp").size
    loading = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    sizes = "(max-width: 1100px) 94vw, 1044px" if wide else "(max-width: 900px) 94vw, 620px"
    img = (f'<img src="{root}assets/shots/{slug}-1600.webp" '
           f'srcset="{root}assets/shots/{slug}-800.webp 800w, {root}assets/shots/{slug}-1600.webp {w}w" '
           f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(app["shot_alt"])}"{loading}>')
    if link:
        img = f'<a href="{link}" aria-label="More about {esc(app["name"])}">{img}</a>'
    return f'<figure class="shot">{img}</figure>'


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


def download_button(slug):
    rel = RELEASES[slug]
    return (f'<a class="button" data-app="{slug}" data-href="dmg" href="{rel["dmg"]}">Download '
            f'<small><span data-app="{slug}" data-field="size">{rel["size"]}</span></small></a>')


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
  <p>Write the script, budget and schedule the shoot, back up the camera cards, and put the finished film on a Blu-ray. Five apps from MindInMotion, an independent film company. All of them are free, and four are open source.</p>
</section>
<main>
""")
    first = True
    for stage, slugs in STAGES:
        for slug in slugs:
            app, rel = APPS[slug], RELEASES[slug]
            parts.append(f"""<section class="app" id="{slug}" aria-labelledby="{slug}-title" style="--tape: {app["tape"]}">
  <div class="app-text">
    <p class="stage">{stage}</p>
    <div class="app-head">
      <img src="{app["icon"]}" alt="" width="56" height="56">
      <h2 id="{slug}-title"><a href="{slug}/">{esc(app["name"])}</a></h2>
    </div>
    <p class="tagline">{esc(app["tagline"])}</p>
    <p class="summary">{esc(app["summary"])}</p>
    <div class="actions">
      {download_button(slug)}
      <a class="more" href="{slug}/">More about {esc(app["name"])}</a>
    </div>
    <p class="fineprint">Version <span data-app="{slug}" data-field="version">{rel["version"]}</span>. {esc(app["macos"])}, Apple Silicon. {app["license"]}.</p>
  </div>
  {shot(slug, "", lazy=not first, link=f"{slug}/")}
</section>
""")
            first = False
    parts.append("</main>\n</div>\n" + footer(""))
    (ROOT / "index.html").write_text("".join(parts))


def media_size(path):
    from PIL import Image
    return Image.open(ROOT / path).size


def clips_section(slug, root):
    app = APPS[slug]
    if "clips" not in app:
        return ""
    figures = []
    for name, title in app["clips"]:
        w, h = media_size(f"assets/video/{slug}-{name}.webp")
        figures.append(
            f'<figure><video controls muted playsinline preload="none" width="{w}" height="{h}" '
            f'poster="{root}assets/video/{slug}-{name}.webp" aria-label="{esc(title)}">'
            f'<source src="{root}assets/video/{slug}-{name}.mp4" type="video/mp4"></video>'
            f"<figcaption>{esc(title)}</figcaption></figure>")
    if len(figures) == 1:
        hint = "A screen recording of the app with captions, under a minute long. It has no sound."
    else:
        hint = "Screen recordings of the app with captions, each under a minute long. They have no sound."
    if "guide" in app:
        guide = app["guide"][0].rsplit("/", 1)[0] + "/videos/index.html"
        hint += f' <a href="{root}{guide}">The user guide has the full-length versions.</a>'
    return f"""<section aria-labelledby="clips-title">
      <h2 id="clips-title">See it work</h2>
      <p class="hint">{hint}</p>
      <div class="clips{" one" if len(figures) == 1 else ""}">
        {chr(10).join("        " + f for f in figures).strip()}
      </div>
    </section>
"""


def gallery_section(slug, root):
    app = APPS[slug]
    if "gallery" not in app:
        return ""
    figures = []
    for name, caption in app["gallery"]:
        w, h = media_size(f"assets/shots/{slug}-{name}-720.webp")
        figures.append(
            f'<figure><a href="{root}assets/shots/{slug}-{name}-1440.webp">'
            f'<img src="{root}assets/shots/{slug}-{name}-720.webp" width="{w}" height="{h}" '
            f'alt="{esc(app["name"])} screenshot" loading="lazy" decoding="async"></a>'
            f"<figcaption>{esc(caption)}</figcaption></figure>")
    title = "More screenshots" if len(figures) > 1 else "Another screenshot"
    return f"""<section aria-labelledby="gallery-title">
      <h2 id="gallery-title">{title}</h2>
      <div class="gallery{" one" if len(figures) == 1 else ""}">
        {chr(10).join("        " + f for f in figures).strip()}
      </div>
    </section>
"""


def install_section(slug, root):
    app, rel = APPS[slug], RELEASES[slug]
    out = [f"""<section id="install" aria-labelledby="install-title">
      <h2 id="install-title">Install</h2>
      <p>{esc(app["install_note"])}</p>
      <p class="actions">{download_button(slug)}</p>
"""]
    if "guide" in app:
        page, bundle = app["guide"]
        out.append(f"""      <p>The <a href="{root}{page}">{esc(app["name"])} user guide</a> has screenshots and captioned walkthroughs. You can also <a href="{root}{bundle}" download>download the whole guide</a> to read offline.</p>
""")
    tech = []
    if "brew" in app:
        tap = app["brew"]
        tech.append(f"""        <h3>Homebrew</h3>
        <div class="code">
          <pre id="brew-{slug}">brew tap MIM18-code/{tap}
brew trust MIM18-code/{tap}
brew install --cask {tap}</pre>
          <button class="copy" type="button" data-copy="brew-{slug}">Copy</button>
        </div>
        <p class="small">{app["brew_note"]}</p>
""")
    if "clone" in app:
        tech.append(f"""        <h3>Build from source</h3>
        <div class="code">
          <pre id="src-{slug}">git clone {app["clone"]}</pre>
          <button class="copy" type="button" data-copy="src-{slug}">Copy</button>
        </div>
        <p class="small">The README walks through the Python engine, FFmpeg and the SwiftUI app build.</p>
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
    if "guide" in app:
        rows.append(f'<li><a href="{root}downloads/GUIDE-SHA256SUMS">Guide checksums</a><span class="aside">SHA-256 for the guide ZIPs</span></li>')
    rows.append(f'<li><a data-app="{slug}" data-href="release" href="{rel["release"]}">Release notes</a><span class="aside">On GitHub</span></li>')
    has_source = "repo" in app or "source" in rel
    if "brew" in app:
        summary = "Homebrew, source code and checksums"
    elif has_source:
        summary = "Source code and checksums"
    else:
        summary = "Checksums and release notes"
    out.append(f"""      <details class="tech">
        <summary>{summary}</summary>
{"".join(tech)}        <ul class="links">
          {chr(10).join("          " + r for r in rows).strip()}
        </ul>
        <p class="hash" data-app="{slug}" data-field="sha" data-file="{rel["dmg_file"]}">DMG SHA-256: {rel["sha256"]}</p>
      </details>
    </section>
""")
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
    features = "".join(f"        <div><dt>{esc(label)}</dt><dd>{body}</dd></div>\n" for label, body in app["features"])
    note = f'<p class="note">{esc(app["note"])}</p>\n    ' if "note" in app else ""
    size_note = f' {esc(app["size_note"])}' if "size_note" in app else ""
    guide_link = f'<a class="more" href="{root}{app["guide"][0]}">User guide</a>' if "guide" in app else ""
    extras = ""
    if "extras" in app:
        intro, items = app["extras"]
        extras = ('<section aria-labelledby="extras-title">\n      <h2 id="extras-title">Optional extras</h2>\n'
                  f"      <p>{esc(intro)}</p>\n      <ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>\n    </section>\n    ")
    faq = "".join(f"      <h3>{esc(q)}</h3>\n      <p>{esc(a)}</p>\n" for q, a in app["faq"])
    others = "".join(
        f'<li style="--tape: {APPS[o]["tape"]}"><a href="{root}{o}/"><b>{esc(APPS[o]["name"])}</b><span>{esc(APPS[o]["tagline"])}</span></a></li>'
        for o in ORDER if o != slug)
    page = head(title=app["title"], description=app["description"], path=f"/{slug}/", root=root,
                image=f"assets/og/{slug}.png", extra_ld=ld)
    page += f"""<body style="--tape: {app["tape"]}">
<div class="wrap">
  {masthead(root, slug)}
  <header class="app-top">
    <img class="app-icon" src="{root}{app["icon"]}" alt="" width="72" height="72">
    <h1><span class="name">{esc(app["name"])}</span> <span class="what">{esc(app["what"])}</span></h1>
    <p class="lede">{esc(app["lede"])}</p>
    <div class="actions">
      {download_button(slug)}
      {guide_link}
    </div>
    <p class="fineprint">Version <span data-app="{slug}" data-field="version">{rel["version"]}</span>. {esc(app["macos"])}, Apple Silicon. Free, {app["license"]}.{size_note} <a href="#install">Other ways to install</a></p>
  </header>
  {shot(slug, root, lazy=False, wide=True)}
  <main class="page">
    {note}<section aria-labelledby="features-title">
      <h2 id="features-title">What it does</h2>
      <dl class="features">
{features}      </dl>
    </section>
    {clips_section(slug, root)}{gallery_section(slug, root)}{extras}<section class="faq" aria-labelledby="faq-title">
      <h2 id="faq-title">Questions</h2>
{faq}    </section>
    {install_section(slug, root)}  </main>
  <nav class="others" aria-label="The other apps">
    <h2>The other apps</h2>
    <ul>{others}</ul>
  </nav>
</div>
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
<div class="page-end"></div>
</div>
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
        size = 26  # shrink a long tagline until it fits beside the name
        while d.textlength(app["tagline"], font=ImageFont.truetype(regular, size)) > 650 and size > 16:
            size -= 1
        d.text((490, top + 52), app["tagline"], font=ImageFont.truetype(regular, size), fill="black", anchor="lm")
    im.save(out / "index.png", optimize=True)


if __name__ == "__main__":
    build_index()
    for slug in ORDER:
        build_app(slug)
    build_meta()
    build_og()
    print("built index.html,", ", ".join(f"{s}/index.html" for s in ORDER), "sitemap.xml, robots.txt, 404.html and share images")
