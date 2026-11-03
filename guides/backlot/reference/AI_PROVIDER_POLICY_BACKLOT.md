# How Backlot applies AI_SUBSCRIPTION_AUTH_POLICY.md

The policy in docs/AI_SUBSCRIPTION_AUTH_POLICY.md (Joshua, 2026-09-06, researched against the providers' own documentation) is mandatory for every provider change in this repository. This note records where Backlot stands against it so agents and reviewers do not re-derive it.

## Provider modes that ship

| Mode | Policy row | Backlot |
| --- | --- | --- |
| Local model through Ollama | not a subscription; no provider account | Default. qwen3.5:4b. |
| Gemini, Anthropic, OpenAI with the user's own API key | ALLOW (API auth, API billing) | Keys stay in ~/.backlot/assist.json with mode 0600, shown masked, never in the project file, logs or MCP output. The settings panel says the key is billed by the provider. |
| The user's ChatGPT plan | ALLOW as OpenAI's Sign in with ChatGPT plan usage for open-source and locally hosted apps (policy section 2) | Built on 2026-11-01, ported from Cold Open so both apps behave the same. The service registers Backlot with the user's ChatGPT account in the system browser, keeps the tokens OpenAI issues to Backlot in `~/.backlot/chatgpt.enc` (0600, AES-256-GCM, key in the login Keychain), and calls `POST https://api.openai.com/v1/responses` with `store: false` and `stream: true`. It replaced the `codex app-server` route, which let Codex own the login and is now retired. |
| Claude through a Claude Pro or Max subscription (`claude -p`) | DENY | Removed on 2026-09-06. A settings file that still names it falls back to "none" and `/assist/status` explains why. |

## Rules already enforced in code

- Backlot uses the account connection issued to it through the provider's own sign-in flow. It does not reuse credentials from another application. API requests authenticate with the selected provider; saved credentials are not included in project files or MCP output.
- No silent fallback between billing modes: the provider is one explicit setting.
- MCP tools never return provider credentials; the app's own per-run bearer token is separate from provider auth and is now confined by round 16b.
- Assist requests through the app say which provider answered (`provider` and `model` in every `/assist/run` response and in the toast).

## The ChatGPT plan integration, in full

The code is `packages/service/src/assist/chatgpt/` (ported from Cold Open's `apps/desktop/src/main/ai/chatgpt-*.ts` at 2af3e70) and `packages/service/src/assist/providers/chatgpt.ts`. Every network call it makes:

| Call | Purpose |
| --- | --- |
| `GET https://auth.openai.com/.well-known/openid-configuration` | discovery; every endpoint must be on the issuer's origin |
| system browser to the discovered `authorization_endpoint` | registration (`dynamic_agent_client`, `agent_name_hint=Backlot`) or reauthorization with the saved client, plus consent |
| `POST` the discovered `token_endpoint` | code exchange and refresh, with the issued `client_id`, PKCE and `resource=https://api.openai.com/v1` |
| `GET` the discovered `jwks_uri` | ID-token signature check |
| `POST` the discovered `revocation_endpoint` | sign-out, refresh token first |
| `GET https://api.openai.com/v1/models` | the signed-in account's model picker |
| `POST https://api.openai.com/v1/responses` | one assist, `store: false`, `stream: true`, success only on `response.completed` |

The app reaches it through these service routes, which return account metadata only:

| kind | path |
| --- | --- |
| route | `/assist/chatgpt/status` |
| route | `/assist/chatgpt/models` |
| route | `/assist/chatgpt/sign-in` |
| route | `/assist/chatgpt/cancel` |
| route | `/assist/chatgpt/sign-out` |
| route | `/assist/chatgpt/select` |
| route | `/assist/chatgpt/resume` |
| route | `/assist/chatgpt/welcomed` |

Never used: Codex's login or credential file, the `chatgptAuthTokens` variant, ChatGPT's `backend-api`, and any token another program stored. The guardrail is `packages/service/test/policy.test.ts`; it fails the build on any of those appearing in shipped code, and on OpenAI's sign-in host appearing outside the sign-in module.

## Open items

Re-read OpenAI's Sign in with ChatGPT pages (policy section 19) before changing the flow, and whenever Cold Open's copy changes, so the two apps stay the same. If Backlot ever charges money or runs any part of this on a server, ChatGPT plan usage stops until OpenAI approves it through its interest form.

Contributors using Claude Code or Codex to work on this repository are covered by policy section 9's last paragraph: developing Backlot with a subscription client is fine; shipping that subscription as the app's provider is not.
