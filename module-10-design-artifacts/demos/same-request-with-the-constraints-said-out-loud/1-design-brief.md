# Design brief: share an episode at a moment

**Larkspur** is a podcast app for iPhone, Android and the web. Listeners follow shows, and the app plays episodes from each show's feed.

## The request

> Let listeners share an episode at a specific moment, so a friend who taps the link lands at exactly the right second.

## What we already have

- **Accounts.** Every listener signs in. Our listeners include family accounts, where a parent sets up profiles for their children.
- **The episode catalog.** Every episode we can play, read from the shows' feeds. It is the record of what exists and what each episode is rated (clean or explicit).
- **Notifications.** The app already sends push notifications and email through our notifications service.
- **The phone's share sheet.** Listeners already send links through messages, WhatsApp and email. We don't have a friends list, and we don't plan to build one.

## What we expect

- A few thousand shares a day.
- Sharing should work for all our content: free shows, and shows from paid and private feeds.
- Shows sometimes remove episodes from their feeds.
