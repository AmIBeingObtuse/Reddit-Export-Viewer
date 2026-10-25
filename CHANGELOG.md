# Changelog

## 0.2

### Added
- A disclaimer in the README, the code and the landing page: made with Claude Code, shared as-is, use at your own risk.
- **Insights page:** account stats, activity by year, weekday-by-hour heat map, top communities, voting habits per community, writing stats, most-used words and emoji, post types and linked sites, conversations, saved items, awards and money, privacy footprint, and an overview of your data files.
- Vote arrows on comments, showing how you voted.
- A "Your votes on other people's comments here" section on post pages.
- Version number on the landing page and sidebar.

### Changed
- Post vote arrows now show only your own vote; the misleading "+1" is gone, because Reddit's export has no scores.
- Search tab counts now reflect the current search.

### Security
- The security policy now runs only the page's own script (pinned by hash), so injected inline code or `javascript:` links are blocked.
- External links no longer send the page's address to the sites they open.
- Data rows can't interfere with the page's internals, even if a file has a column named `__proto__`.
- Damaged, oversized or encrypted zips show a clear message.
- The table filter ignores masked columns, so it can't be used to guess hidden values.

### Fixed
- Top-level comments were wrongly tagged "reply".
- Messages from your own username in different capitalisation weren't shown as yours.
- "← Back" could leave the page.
- Hover tooltips could stay stuck on screen.

## 0.1

- First release: open the export as a folder, files or `.zip`, Reddit-style views for all activity, messages, communities and account data, search, remote media toggle (off by default), private info toggle, light and dark mode, and phone layout.
