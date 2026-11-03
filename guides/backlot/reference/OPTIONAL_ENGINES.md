# Optional external programs

The desktop app includes Backlot's Python bridge scripts. It does not bundle
Python, the screenwriting-mcp or film-budget-mcp repositories, Codex, Ollama,
or Chrome. Missing tools appear in the capability checks; ordinary project
editing does not require these optional engines.

PDF rendering uses a locally installed Chrome. Some script reading and
budget/schedule export operations use separately installed Python engines.
The bridge starts Python and imports modules from the user's configured local
engine checkout. BACKLOT_SCRIPT_PY and BACKLOT_BUDGET_PY select interpreters;
the current engine checkout locations are ~/screenwriting-mcp and
~/film-budget-mcp. These are private development integrations, not components
licensed or supplied by this release. Do not download or bundle them on the
assumption that Backlot's GPL covers them.

Before distributing either engine, establish its ownership and license,
pin its source revision and audit its dependencies. The reviewed local
requirements name mcp 1.27.0 and openpyxl 3.1.5, but that is not a complete
license inventory of either engine. No external engine was relicensed as
part of Backlot's release preparation.

Users provide their own AI account or separately billed API access. Backlot's
software license does not grant access to hosted services or imply provider
approval.
