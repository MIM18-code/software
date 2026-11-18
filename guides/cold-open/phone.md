# The phone remote

An iPhone can read the live script and send back lines, dictated takes and notes for you to accept or ignore on the Mac.

Tools > Phone Companion… opens the Phone panel.

## Connect at home (Wi-Fi)

1. Connect the Mac and iPhone to the same Wi-Fi.
2. Open Tools > Phone Companion… and choose the Wi-Fi interface under Connect through.
3. Choose Start phone pairing….
4. In Cold Open on the iPhone, tap **Scan code** and point at the QR code on the Mac. Or choose **Copy app pairing code** on the Mac and **Paste a pairing code** on the phone.

The link is encrypted automatically. The QR code carries a secret that never crosses the network, and both devices encrypt everything they send with keys made from it. There is no certificate to install and nothing to choose. Keep the QR code and the copied pairing code private: whoever has one can read the script while the pairing lasts.

A one-off pairing expires after two hours; tick Remember this iPhone to survive restarts. A remembered iPhone uses a fixed port, shown under Advanced; keep it unchanged while the phone is remembered.

If the iPhone answers a fresh code with "Scan the code in the Mac’s Phone panel", update Cold Open on the iPhone. An iPhone that an earlier Cold Open remembered over Wi-Fi no longer connects, because that pairing was not encrypted. The Mac lists it with "Pair this iPhone again": pair it again, then revoke the old entry. Takes still waiting on that iPhone can be sent to the Mac by AirDrop first.

### The table-read page in Safari

The Phone panel can also make a link to a page in Safari that reads the table read aloud and controls the Mac's. A web page cannot use the encrypted link. Over Tailscale the page is served over HTTPS: choose Copy Safari link. On home Wi-Fi the page is off unless you open Advanced and tick Also make a Safari link (not encrypted) before a one-off pairing. Anyone on that Wi-Fi could then read what the page shows and sends. The iPhone app's link stays encrypted either way.

## Connect from anywhere (Tailscale)

Away from home Wi-Fi, Turn on the four checks and Cold Open will tell you exactly what is missing:

1. Tailscale installed on this Mac.
2. Tailscale signed in and running.
3. MagicDNS on.
4. HTTPS certificates on. Turn them on in the Tailscale admin console (the panel links there directly).

Sign in to Tailscale on the iPhone with the same account. In the Mac panel, choose Tailscale under Connect through, then Start phone pairing…. In Cold Open on the iPhone, scan the QR code on the Mac. iCloud Drive can serve as a fallback folder: choose the same folder on the Mac and on the iPhone, and what arrives still lands in the review inbox.

## Review inbox

1. On the iPhone, pick a script line and add a note, or dictate a take.
2. On the Mac, the Review inbox lists them with source text.
3. Choose Accept or Ignore per item. Accepted and ignored items return to the phone when the live link reconnects.

Items wait in a bounded local inbox until you handle them, even after sharing stops. Source text that no longer matches is accepted as an unanchored note rather than attached to guessed text.

The native iPhone app saves unfinished writing on the phone. If the app closes before you send, it reopens your text. If pairing ends while you write, copy your text before pairing again.

Tools > Stop Phone Sharing ends the stream. The Connect through drop-down at the top of the panel chooses the path: Tailscale, or a named Wi-Fi interface with its address.

## Limits worth knowing

- Opening another document ends a one-off link; a remembered iPhone resumes when its script is open again.
- The Safari page on home Wi-Fi is not encrypted. Use the iPhone app, or Tailscale, for anything private.
- Home Wi-Fi pairing needs a current Cold Open on both the Mac and the iPhone.
