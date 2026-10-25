# Reddit Export Viewer

A tiny, single-file, offline viewer for your [Reddit data export](https://www.reddit.com/settings/data-request).
Reddit gives you your data as a pile of `.csv` files. This turns them into a familiar Reddit-style site you can browse, search and explore.

One HTML file · no dependencies · no build step · nothing is uploaded

<img width="2502" height="1706" alt="Screenshot From 2026-10-25 22-18-36" src="https://github.com/user-attachments/assets/ccc4e979-a828-4ccd-a803-5e87f380cf8b" />


> **Disclaimer**
> For 100% transparency: I made this with [Claude Code](https://claude.com/claude-code). It is for personal use, but I have uploaded it here to share with the world (and off world) and anyone who wants to use it. I take no responsibility for its use, and you use it at your own risk.

## Features

- **Opens anything:** drop in the export `.zip`, the unzipped folder, or loose `.csv` files. It works out which you gave it.
- **Reddit-style layout:** posts, comments, threads, community pages, light and dark mode, and a layout that works on phones.
- **Your votes:** upvoted and downvoted posts and comments, with your vote shown on every post and comment.
- **Saved, hidden, drafts and scheduled posts.**
- **Inbox:** private messages grouped into conversations, chat history and announcements.
- **Communities:** joined, moderated and approved-submitter communities, plus custom feeds.
- **Awards:** awards given and received.
- **Insights:** activity by year, a weekday-by-hour heat map, top communities, voting habits, writing stats, most-used words and emoji, top correspondents, and a privacy footprint showing what Reddit recorded and inferred about you.
- **Account data:** every file can be opened as a sortable, filterable table, including files the viewer doesn't specifically know about.
- **Checksum verification** against the export's `checkfile.csv`.
- **Search** across everything, plus a filter on every list.

## How to use

1. Request your data at <https://www.reddit.com/settings/data-request> and download the `.zip` when Reddit emails you.
2. Download `reddit-viewer.html` from this repo and open it in a modern browser (Chrome, Edge, Firefox or Safari).
3. Drop the `.zip` or the unzipped folder onto the page, or use **Open folder** / **Open .zip or files**.

No install and no server. It works from your downloads folder, offline.

## Privacy

- **Everything stays in your browser.** The files are read locally and never uploaded.
- **No network requests by default.** The page's security policy blocks it from contacting any server. The only exception is images, and only when you turn on **Media**.
- **Remote media is off by default.** Images from Reddit or Imgur load only when you turn the **Media** toggle on, or click a single image.
- **Private info is hidden by default.** IP addresses, email, phone number, birthdate and account IDs are masked until you turn on **Private info**, which resets on every reload.
- **Nothing is remembered** between visits except your theme and media settings.

See [SECURITY.md](SECURITY.md) for details.

## Limitations

- **No scores or karma.** Reddit's export doesn't include vote counts for posts or comments, only *your own* votes, so the viewer can't show them. Live scores can't be fetched either, because Reddit blocks requests from web pages.
- **Only your side of conversations.** Other people's replies to you aren't in the export.
- **Videos show as links.** Reddit-hosted videos can't play without extra libraries, and Imgur albums are also links only.
- **No ZIP64.** Very large zips in this format aren't supported; unzip and open the folder instead.

## Editing the code

The page only runs a script whose SHA-256 hash matches the one in its security policy. **After editing the `<script>` block, run:**

```bash
python3 csp-hash.py reddit-viewer.html
```

Otherwise the browser blocks the script and the page stops working.

## License

Public domain, via [The Unlicense](LICENSE). Use it, change it, share it or sell it, for any reason, without asking or crediting anyone.
