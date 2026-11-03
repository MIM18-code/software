# Troubleshooting Backlot

## Unexpected totals

1. Check which board is active: the Board menu at the top of the Stripboard.
2. Check which budget alternative is active: Budget view > Budget administration and alternatives. The active one is marked.
3. Budget lines do not read the board's day count; they use the Shoot days global. The Mismatches row in the Budget view says when that global or a day-priced line disagrees with the board.
4. For dated fringes, the board's dates decide how much of the fringe is charged, so fixing the Calendar can fix the fringe math.
5. Actuals and estimated final cost overrides are the same in every alternative: switching alternatives changes budget figures, never what was spent.

## An older version reports missing tools

Beta 8 includes FDX/Fountain reading, tagged FDX export, actor sides and desktop PDF output. Update an older Backlot if script import asks for a Python reader or desktop PDF output asks for Chrome. Gorilla/Movie Magic budget interchange remains separate and is disabled when unavailable.

## A project will not create

If Create is disabled, fill Title and check the required fields highlighted by the form. Keep the generated Project file location for your first project, and leave the optional script and JSON fields blank.

If Backlot says the project file already exists, choose Open file… to reopen that project. For a separate practice project, start New project again and choose a different empty parent folder. The title alone does not change the generated file location in this version.

## Reports will not save as PDF

The desktop app includes its PDF renderer. Keep the project open, retry Save PDF or Issue, and report the exact message if it fails. An issue that fails to produce its PDF remains a draft. A separately launched headless service still needs Chrome; this does not apply to the packaged desktop workflow.

## Script import fails

Import first previews the changes; it does not change the project until you confirm. If a file cannot be parsed, dismiss the error and keep the original. Check that it is a real FDX or Fountain screenplay and report a valid file that fails. No separate reader or AI connection is required in beta 8.

If an older app reports a missing screenwriting bridge or Python interpreter, update Backlot. Do not install development repositories to make the basic import workflow work.

## Gorilla or Movie Magic export is disabled

These budget/schedule interchange formats use a separate integration that this installer does not supply. PDF reports and CSV exports still work. Signing into AI does not enable those formats.

## Call sheet delivery looks stuck

1. Open the issue's delivery history: every attempt and its outcome is listed.
2. Retry failed deliveries; resend to late additions; remind unconfirmed recipients.
3. A delivery with unknown outcome must be resolved first, by design, so retrying cannot send twice.

## Email is refused

In-app call-sheet email needs a configured email service and confirmation site. If they have not been set up for this installation, save the issued PDF and attach it manually in your own mail app. The [delivery setup notes](setup-and-ai.md#email-and-confirmation-links) explain the difference.

## An AI assist answers with the wrong provider

The provider is one explicit setting with no silent fallback. Open the AI settings from the AI pill in the top bar and check the active provider; every response names the provider that answered.

## Union status changed after project start

Recalculate. The union status set at creation drives hold calculations, the SAG agreement and DOOD assumptions; changing it later does not silently re-price what is on the board.

## A change went the wrong way

Undo it in the History view (or `⌘Z` outside a text field), or restore a backup from the Home view. Both actions are journaled, so undoing the undo is possible.

## Ask for help

Report a problem on the [public Backlot issue tracker](https://github.com/MIM18-code/homebrew-backlot/issues). Include the exact message, Backlot version, macOS version and the action you tried. Describe whether you started with an empty project or opened an existing one. You can report the error without attaching your screenplay, account keys or a production project.
