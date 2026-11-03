# How do I…?

Short recipes for common jobs.

## Tag a script and send it to Backlot

1. Tag the script: Tools > Tag Selected Text… per passage (see [Breakdown tagging](breakdown.md)), or Tools > Suggest Breakdown Tags… for a first pass.
2. Open the project in Backlot.
3. In Cold Open, File > Review Draft in Backlot….
4. Pick the project, set cast reconciliation, choose Preview captured draft.
5. Review the scene matches, cast changes and tags in Cold Open. Resolve any unmatched identities; choose Review revised choices after changing options.
6. Choose Apply reviewed import…. Then check the affected days in Backlot.

## Export a breakdown to Movie Magic

1. Tag the script in Cold Open.
2. File > Export Movie Magic Scheduling (.sex)….
3. Import the `.sex` in Movie Magic Scheduling. Cold Open's `.sex` export carries the scene data and tags the breakdown needs.

## Co-write with someone in another city

1. Install Tailscale on both Macs and sign in with the same account (or accounts that share a tailnet).
2. Cold Open: Settings > Co-writing, set the name your partner sees.
3. File > Share for Co-writing…; choose On a different network. Connect Tailscale and choose Check Tailscale again if prompted.
4. Copy the Editing invite privately to your partner. They choose File > Join Co-writing Session… and paste it.
5. Check the panel's diagnostics if either side cannot reach the other.

No Tailscale and not on one network? Follow the [self-hosted relay setup](co-writing.md#in-another-city-your-own-relay), then put its address in Settings > Co-writing and share as usual.

## Get AI working

Local, free, private:

1. Tools > Set up AI… > Run on this Mac.
2. Choose Set up local AI for me, or Download writing model if Ollama is already running. Earlier beta 8 builds show separate Ollama install/start and model download buttons; see [AI setup](ai.md).
3. If the model is already ready, choose Use AI on this Mac when offered. Wait for AI on this Mac is ready, then choose Done.
4. Open Ask (Tools > Ask About the Script…) or request breakdown suggestions. Format Draft has its own pinned-model controls under Tools > Manage Local Formatting Models….

With your ChatGPT plan:

1. Tools > Set up AI… > Sign in with ChatGPT.
2. Complete the browser sign-in and enable plan usage if requested. If already signed in, choose Use ChatGPT, then Done.
3. Ask About the Script…; ChatGPT usage counts against your own plan.

## Get the table read set up

1. Tools > Table Read… (Listen panel).
2. Manage voice packs…; download a local neural pack (see sizes in [Table read](table-read.md)). Apple silicon and macOS 15+ needed for the neural pack route.
3. Assign a voice per character, Recast until you like them, Lock the ones you want to keep.
4. Press Play. Export a WAV with Export this range as WAV… when it suits a scene.

## Produce sides for tomorrow's rehearsal

1. File > Export Sides…; tick the scenes (add scenes by hand for the silent reads).
2. Choose Final Draft or Fountain if the actors' readers are technical.
3. For PDF sides: File > Delivery PDF, Watermarks and Actor Sides…, document "Actor / scene sides", tick Emphasize the selected character's lines, set the recipient watermark, Export previewed PDF….

## Number scenes and start a revision pass

1. Script > Number Scenes.
2. Production > Revision Mode.
3. Production > New Revision Set…: pick the color of your next draft, set the date and mark, Create revision set.
4. Rewrite. Changed text carries the mark; Settings > Printing decides whether marked pages print in color.

## Keep a dangerous cut

1. Select the passage.
2. Tools > Save Selected Passage to Cuts….
3. Delete from the script with confidence. The copy stays in the Notes panel under Cuts; nothing prints.

## Draft in bed on the phone

1. Mac and iPhone on one Wi-Fi, or Tailscale on both (see [The phone remote](phone.md)).
2. Tools > Phone Companion…: choose the connection and configure its protection as described in [The phone remote](phone.md), then Start phone pairing….
3. On the iPhone, open the companion, pick the line, and leave notes or dictate takes.
4. On the Mac, accept the good ones from the Review inbox.
