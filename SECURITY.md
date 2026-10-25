# Security & privacy

Reddit Export Viewer handles personal data, so it's built to keep that data on your device.

## How it protects your data

- **Reads locally.** Files are read with the browser's own file APIs and never sent anywhere.
- **Locked-down security policy.**
  - Only the page's own script can run (pinned by its SHA-256 hash), so injected inline code, inline event handlers and `javascript:` links are blocked.
  - The page can't connect to any server: no fetch or XHR, no external scripts, fonts or frames.
  - Images can only load over `https:`, and only when you turn on remote media.
- **Text is escaped before rendering.** Post and comment text is made safe before the small Markdown renderer runs. Only `http(s)` links are ever created.
- **No referrer.** Links don't send the page's address to the sites they open, and they open in a new tab that can't control this page.
- **Private info is masked.** IPs, email, phone, birthdate and account IDs are hidden until you choose to show them, and that choice resets on reload.

## Reporting a problem

If you find a way for exported data to run code, leave the browser, or bypass the masking, please report it privately: go to this repo's **Security** tab and click **Report a vulnerability**. Describe the problem without including any real export data.

## Disclaimer

This project was made with Claude Code for personal use and is shared as-is, with no warranty. I take no responsibility for its use, and you use it at your own risk. Please review the code yourself before trusting it with your data.
