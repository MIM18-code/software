# The phone remote

An iPhone can read the live script and send back lines, dictated takes and notes for you to accept or ignore on the Mac.

Tools > Phone Companion… opens the Phone panel.

## Connect at home (Wi-Fi)

1. Connect the Mac and iPhone to the same Wi-Fi.
2. Open Tools > Phone Companion… and choose the Wi-Fi interface under Connect through.
3. Choose Start phone pairing….
4. In Cold Open on the iPhone, tap **Scan code** and point at the QR code on the Mac. Or choose **Copy app pairing code** on the Mac and **Paste a pairing code** on the phone.

A pairing made this way works only while the iPhone is on the same network as the Mac, which usually means your home Wi-Fi. To keep working after you leave the house, pair through Tailscale instead (next section). That pairing works at home too.

The link is encrypted automatically. The QR code carries a secret that never crosses the network, and both devices encrypt everything they send with keys made from it. There is no certificate to install and nothing to choose. Keep the QR code and the copied pairing code private: whoever has one can read the script while the pairing lasts.

A one-off pairing expires after two hours; tick Remember this iPhone to survive restarts. A remembered iPhone uses a fixed port, shown under Advanced; keep it unchanged while the phone is remembered.

If the iPhone answers a fresh code with "Scan the code in the Mac’s Phone panel", update Cold Open on the iPhone. An iPhone that an earlier Cold Open remembered over Wi-Fi no longer connects, because that pairing was not encrypted. The Mac lists it with "Pair this iPhone again": pair it again, then revoke the old entry. Takes still waiting on that iPhone can be sent to the Mac by AirDrop first.

### The table-read page in Safari

The Phone panel can also make a link to a page in Safari that reads the table read aloud and controls the Mac's. A web page cannot use the encrypted link. Over Tailscale the page is served over HTTPS: choose Copy Safari link. On home Wi-Fi the page is off unless you open Advanced and tick Also make a Safari link (not encrypted) before a one-off pairing. Anyone on that Wi-Fi could then read what the page shows and sends. The iPhone app's link stays encrypted either way.

## Connect from anywhere (Tailscale)

Tailscale is a separate app, made by another company, that privately links your own devices over the internet. With it on the Mac and the iPhone, the phone reaches the Mac from a café, a set or another city. You need a Tailscale account; its Personal plan is free (checked November 2026).

Set this up once, while the iPhone is at the Mac. The Phone panel's Use from anywhere list ticks off each step as you finish it, and Check again looks afresh.

1. **Install Tailscale on the Mac.** Choose Install Tailscale in the panel.
2. **Sign in.** Open Tailscale on the Mac and sign in, or make an account. Its icon sits in the menu bar.
3. **Turn on MagicDNS.** Choose Open Tailscale's DNS page in the panel. On that page, turn on MagicDNS if it is off. It gives the Mac a name the iPhone can find.
4. **Turn on HTTPS.** On the same page, find HTTPS Certificates and choose Enable HTTPS. Cold Open uses it to encrypt the link. When you pair, Cold Open gets a certificate for the Mac, and certificates are listed in a public record along with the Mac's Tailscale name. If the name says more than you'd like, such as your full name, rename the Mac on Tailscale's Machines page before you pair.
5. **Install Tailscale on the iPhone.** Get it from the App Store and sign in with the same account as the Mac. The iPhone asks to add a VPN configuration; allow it.
6. **Pair through Tailscale.** In the Phone panel, choose Tailscale under Connect through, tick Remember this iPhone, choose Start phone pairing…, and confirm with Start private-network link. Scan the QR code in Cold Open on the iPhone. If the panel is showing a pairing code and no Connect through, choose Pair another iPhone (or Stop sharing / revoke link, for a one-off pairing) to bring it back. The list ticks this step once the iPhone has connected.

An iPhone you already paired at home has to be paired again this way, because a home pairing only ever reaches the Mac on its own network. Do it at home, after everything you wrote has reached the Mac: what is still waiting belongs to the old pairing and is not sent through the new one. On the iPhone, tap the tray icon at the top right of the script to open Status and check that nothing says Pending. Then choose Disconnect and pair again, confirm Disconnect, and scan the new code.

When you leave:

- In the Phone panel, tick Keep this Mac awake while it shares with an iPhone. Leave Cold Open and the paired script open, and Tailscale connected.
- On a MacBook, leave the lid open and the charger in. A closed lid still puts it to sleep, unless the MacBook is connected to a display. The screen can still turn off and lock.
- Keep Tailscale on in the iPhone.
- If the iPhone can't reach the Mac, what you write waits on the phone and sends when it reaches the Mac again.

The last, optional item on the list is an iCloud Drive folder. Choose it in the Mac's Phone panel, then choose the same folder on the iPhone: open Status (the tray icon) and tap Choose iCloud Drive fallback folder. When the iPhone can't reach the Mac, it saves what you write to that folder. Once iCloud has synced the file to the Mac, it lands in the review inbox.

## Review inbox

1. On the iPhone, pick a script line and add a note, or dictate a take.
2. On the Mac, the Review inbox lists them with source text.
3. Choose Accept or Ignore per item. Accepted and ignored items return to the phone when the live link reconnects.

Items wait in a bounded local inbox until you handle them, even after sharing stops. Source text that no longer matches is accepted as an unanchored note rather than attached to guessed text.

The native iPhone app saves unfinished writing on the phone. If the app closes before you send, it reopens your text. If pairing ends while you write, copy your text before pairing again.

Tools > Stop One-Off Phone Link ends a one-off pairing. Remembered iPhones stay connected; to remove one, choose Revoke beside it. The Connect through drop-down at the top of the panel chooses the path: Tailscale, or a named Wi-Fi interface with its address.

## Limits worth knowing

- Opening another document ends a one-off link; a remembered iPhone resumes when its script is open again.
- The Safari page on home Wi-Fi is not encrypted. Use the iPhone app, or Tailscale, for anything private.
- Home Wi-Fi pairing needs a current Cold Open on both the Mac and the iPhone.
