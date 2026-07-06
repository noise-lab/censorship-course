# Breakout Discussion Topics

Each lecture in the course has a corresponding file in this directory with **two breakout debate topics**. In class, students split into small groups, spend ~15 minutes on one (or both) of the topics, then report back to the full group.

Topics are designed to be:

- **Debatable** — framed as a motion or contested claim, not a closed-book question.
- **Grounded in current events** — each includes a short "prep reads" list of recent news, reports, or primary sources students can skim before/during the breakout.
- **Refreshable** — flagged so a future skill can identify and update stale links.

## File format

Each file has YAML frontmatter followed by two breakout sections:

```markdown
---
lecture: <int>                    # lecture number, matches schedule
class: "<topic title>"            # class topic from schedule
book_chapter: "<ref>"             # book chapter or section (e.g. "1", "2.2.1")
last_refreshed: YYYY-MM-DD        # date the current-events links were last verified
---

# Breakout Discussions — Lecture N: <Topic>

**Format.** ...instructor framing...

---

## Breakout A: <Sub-topic>
<!-- breakout id="A" status="current" refreshed="YYYY-MM-DD" -->

**Motion.** *"<contested claim>"*

<!-- current-events:start topic="<slug>" -->
**Prep reads (5–10 min).**
- [Title](https://url) — Publisher, Month YYYY
- [Title](https://url) — Publisher, Month YYYY
<!-- current-events:end -->

**Discussion prompts.**
- ...

**Bring back.** <one-line report-back ask>

---

## Breakout B: <Sub-topic>
...
```

## Markers a refresh skill should recognize

- **`last_refreshed:` in frontmatter** — the last time any current-events block in the file was verified. If older than N weeks, the file is a candidate for refresh.
- **`<!-- current-events:start topic="..." -->` / `<!-- current-events:end -->`** — wraps the block of time-sensitive links. Everything between these markers is fair game to rewrite. The `topic` slug hints at what to search for.
- **`<!-- breakout id="A" status="stub|current" refreshed="YYYY-MM-DD" -->`** — per-breakout status. `status="stub"` means the breakout was seeded from the book chapter without live current-event lookup and should be refreshed before the lecture is taught. `status="current"` means links were verified on `refreshed`.

Content **outside** these markers (motion, discussion prompts, bring-back) is treated as evergreen — the refresh skill should not rewrite it unless the whole breakout is marked `status="stub"`.

## Adding or refreshing topics

The intended workflow (once the `refresh-breakouts` skill exists):

1. Instructor runs `/refresh-breakouts <lecture-number>` a few days before class.
2. Skill reads the corresponding book chapter (in the sibling `censorship-book/` repo) to find current-event references and identify the topic focus.
3. Skill runs web searches for recent news on those topics.
4. Skill rewrites the `current-events:start`/`end` block with fresh links, updates `last_refreshed`, and flips `status="stub"` to `status="current"` where applicable.
5. Instructor reviews the diff.
