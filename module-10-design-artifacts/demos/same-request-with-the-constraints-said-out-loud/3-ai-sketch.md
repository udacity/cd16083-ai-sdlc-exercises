# Architecture sketch: share an episode at a moment

## Component diagram

```
 Larkspur apps (iPhone, Android, web)
              |
              v
        [ API Gateway ]
              |
              v
       [ Share Service ] -----------------> [ Episode Catalog ]
              |                                (existing)
              v
       [ Message Queue ]
         |          |          |
         v          v          v
 [ Short Link ] [ Notification ] [ Friends ]
 [  Service   ] [   Service    ] [ Service ]
         |
         v
   [ Link Store ]
   link_id, episode_id, timestamp_seconds,
   sharer_user_id, sharer_display_name, created_at
```

## How it works

When a listener taps **Share at this moment**, the app sends the episode and the current position to the **Share Service** through the **API Gateway**. The Share Service looks up the episode in the existing **Episode Catalog** and publishes a "share created" event to the **Message Queue**.

Three services consume that event independently, which keeps the design loosely coupled and lets each one scale on its own:

- The **Short Link Service** creates a short link and saves it in the **Link Store**, with the sharer's ID and display name so the recipient can see who shared it. Links are permanent, so a shared moment never breaks.
- The **Notification Service** sends the recipient a push notification or email: "Maya shared a moment from *Episode 42* with you."
- The **Friends Service** records the connection between sharer and recipient, so the app can suggest people to share with next time.

When someone taps the link, the Short Link Service resolves it to the episode and timestamp, and the app opens the episode at that exact second. Any episode in the catalog can be shared, so the feature works for all content from day one.

This event-driven design is scalable, fault-tolerant, and ready for future social features such as comments and reactions.
