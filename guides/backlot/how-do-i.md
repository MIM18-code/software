# How do I…?

Short recipes for common jobs in Backlot.

## Import a tagged script and start scheduling

Check [the import prerequisite](setup-and-ai.md#what-each-task-needs) first. For a fresh install without those tools, use [manual scene entry](getting-started.md#add-one-scene-without-importing-a-script).

1. Create a project with its title, folder and union status. The optional Script path attaches the source without importing scenes.
2. Breakdown `⌘1`: choose Import FDX and select the tagged `.fdx` from Cold Open. Review the proposed changes, choose Confirm import, then check the elements.
3. Stripboard `⌘2`: arrange the order, insert day breaks, run Sort board once as a draft.
4. Calendar `⌘3`: set Production start to place shoot days. Drag a day within the calendar, or choose Change date, to pin a different date.

## Export a breakdown to Movie Magic

1. Tag the script in Cold Open and export the `.fdx` (or use Review Draft in Backlot…), or import it here.
2. Reports view: pick the stripboard or one-line schedule export.
3. Choose the Movie Magic XML export for the budget or the schedule, and save it for Movie Magic.

## Get a call sheet out today

1. Calendar `⌘3`: confirm tomorrow's date is on the board.
2. People `⌘7`: check cast contacts are linked to characters (that is what fills the cast block).
3. Call sheets `⌘8`: draft, set call times and department calls, Issue.
4. With delivery configured, distribute by email, text or the published page; watch confirmations and remind the quiet ones. Without confirmation pages, save the issued PDF and attach it manually in your mail app.
5. After wrap, file the day report and enter costs.

## Follow a script that is being written

1. Ask the writer for the read-only invite (File > Copy Read-only Invite in Cold Open).
2. Breakdown `⌘1` > Live script… and paste it.
3. Watch the change list; Reconcile to open the review. Backlot stays read-only by design.

## Send the whole production to a producer

1. Home > Send a copy.
2. Send the `.backlot` file. It carries the project, history, attachments, issued sheets and reports.
3. Tell the recipient to open it with Backlot and to change nothing while you still have your copy.

## Recover yesterday's board

1. History view: find the change and undo from there; or
2. Home view: restore one of the thirty backups. Restores are journaled and undoable.

## Add a fringes line that follows shoot days

1. Budget `⌘4`: make the line use a global value such as Shoot days.
2. If the board's day count later differs, open the Mismatches row rather than hunting by hand.
