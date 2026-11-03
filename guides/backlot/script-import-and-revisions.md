# Script import, revisions, and live script

Scripts get into Backlot three ways, and revised drafts re-import with a review step.

## Import

Script import is included in Backlot beta 8. FDX and Fountain work without Python, another reader or AI. You can also use [manual scene entry](getting-started.md#add-one-scene-without-importing-a-script).


1. In the Breakdown view, choose Import FDX.
2. Pick an `.fdx` (tagged or not) or a `.fountain` file.
3. Review the proposed changes and choose Confirm import. Backlot reads the scenes, the cast from dialogue cues, and from a tagged FDX the breakdown elements in their categories.

The screenplay reader is included. If a valid script cannot be read, keep the original and see [Troubleshooting](troubleshooting.md).

Review the cast and page changes before confirming. Cue extensions such as V.O. and CONT'D share the speaker's identity; different cue names such as NELL and YOUNG NELL remain separate. Known speakers mentioned silently in action can also appear in the scene cast.

Backlot preserves reliable page lengths stored in an FDX. When those lengths are missing or are converter placeholders, it estimates them with the included screenplay engine and marks them as estimated. These estimates can differ from older Backlot versions. Re-import previews the proposed page changes before applying them.

## Re-import a revised draft

1. Import the new draft.
2. Backlot previews the change: matched, added and missing scenes, with scenes whose text changed listed.
3. Confirm the import only after reviewing the proposal.

Backlot proposes marking missing scenes as omitted rather than deleting them; omitted scenes show greyed at zero pages until you restore one. Changed scenes get a colored tab in standard revision order: white, blue, pink, yellow, then later colors. The confirm step exists so nothing lands on the board unread.

The Cold Open handoff ("Review Draft in Backlot…") keeps matched scene identities from the last reviewed import, so renaming a scene heading keeps it the same scene.

## Live script

To follow a script while it is still being written:

1. In Cold Open, choose File > Copy Read-only Invite (from the Co-writing panel).
2. In Backlot, choose Breakdown > Live script… and paste the invite.
3. Backlot lists what changed since your last reconcile: added, removed, renumbered or retitled scenes, and any scene whose length moved by 2/8 page or more.
4. Choose Reconcile. The review opens on a frozen copy of the live script.

Backlot cannot edit the script and refuses a read-write invite for exactly that reason. If the host stops sharing, Backlot keeps the last script it saw.

## Video walkthrough

[Import and reconcile a tagged script](videos/import-tagged-script.mp4) · [Captions](videos/import-tagged-script.srt). See [video notes and draft narration](videos/index.md).
