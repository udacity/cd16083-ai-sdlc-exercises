# Module 10 demo prompts

Evaluate AI-Generated Design Artifacts

Every prompt used in this module's demo videos, in the order it was pasted into Claude Code in the Udacity workspace. Where a prompt refers to a file, the file sits in the demo's workspace folder.

# Demo 1: The sketch that looks finished

No live prompt. The engineer's prompt below is shown on screen as the prompt that produced the prepared sketch (3-ai-sketch.md). Workspace folder: share-design.

> Here's our design brief for Larkspur. Propose an architecture for the share-at-a-moment feature: a component diagram, and a short explanation of how it works. (The design brief was pasted below the prompt.)

# Demo 2: Same request, with the constraints said out loud

Workspace folder: share-design (1-design-brief.md, 3-ai-sketch.md, 4-design-questions.md). Claude Code creates 5-directed-sketch.md and 6-alternative-sketch.md.

**Prompt 1: the five constraints.**

> Read share-design/1-design-brief.md. Propose an architecture for the share-at-a-moment feature and write it to share-design/5-directed-sketch.md: a component diagram as text, and a short explanation. Constraints:
> 1. This is a link that opens the app at the right second, not a social feature. No friends list and no new notifications; sharing goes through the phone's share sheet.
> 2. Episodes from paid and private feeds cannot be shared. Check this before a link is created.
> 3. A link carries no personal data, so no sharer ID or name. Links expire after 30 days.
> 4. Before playback, check the episode's content rating against the profile opening the link. Child profiles cannot open explicit episodes.
> 5. Expect a few thousand shares a day. Use as few parts as the problem needs, and reuse the existing episode catalog and accounts.

**Prompt 2: the alternative.**

> Now give me a simpler alternative to that design and write it to share-design/6-alternative-sketch.md. For both designs, list what each one assumes. Don't recommend one; tell me which assumptions differ.

**Prompt 3: the human decision.**

> Decision: a link to an episode that has been removed from its feed should open the show's page with a short message that the episode is no longer available, not an error. Add this to share-design/5-directed-sketch.md.

