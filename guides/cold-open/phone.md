# The phone remote

An iPhone can read the live script and send back lines, dictated takes and notes for you to accept or ignore on the Mac.

Tools > Phone Companion… opens the Phone panel.

## Connect at home (Wi-Fi)

1. Connect the Mac and iPhone to the same private Wi-Fi.
2. Open Tools > Phone Companion… and choose the Wi-Fi interface under Connect through.
3. Choose connection protection. HTTPS is the default: choose Choose HTTPS certificate and key… and supply a matching certificate and key for the selected Mac IP address. The iPhone must trust the certificate issuer. Alternatively, explicitly choose HTTP · unencrypted, trusted Wi-Fi only for a trusted private network.
4. Choose Start phone pairing…. HTTPS pairing stays disabled until its certificate is supplied.
5. In the native Cold Open iPhone app, tap **Scan code** and point at the QR code on the Mac. Or choose **Copy app pairing code** on the Mac and **Paste a pairing code** on the phone. For the Safari reader, open the separate **Copy pairing link** URL instead.

The panel reports whether encryption is active. A one-off pairing expires after two hours; tick Remember this iPhone to survive restarts. Cold Open remembers the phone's port; keep it unchanged while the phone is remembered.

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
- Real iPhone testing beyond Safari pairing, native microphone capture and trusted-CA setups on arbitrary networks are areas still in development; the safest path is the Tailscale one above.
