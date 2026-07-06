---
name: refresh-breakouts
description: Refresh the "current-events" prep-reads blocks in course breakout discussion files under `docs/breakouts/*.md`. Discovers target files by lecture number, section name, or refresh status; pulls recent news via WebSearch; rewrites only the content between `<!-- current-events:start -->` markers, preserving evergreen motions and prompts. TRIGGER when the user says any of: "refresh breakouts", "refresh the breakout topics", "refresh breakouts for lecture N", "refresh <section> breakouts" (e.g. technical, platform, legal, measurement, circumvention), "update this week's breakout current events", or "check whether any breakouts need refreshing before class". SKIP for anything outside `docs/breakouts/` — this skill only refreshes breakout discussion files, not slides (use `refresh-course-slides`) or activities.
---

# refresh-breakouts

Refresh the time-sensitive current-events links in a course's breakout discussion files. Each file lives in `docs/breakouts/` and is structured so a bounded, machine-detectable slice of its content is safe to rewrite.

## When to invoke

Trigger phrases:
- "refresh breakouts" / "refresh the breakout topics"
- "refresh breakouts for lecture N"
- "refresh <topic> breakouts" (technical / platform / legal / measurement / circumvention)
- "update this week's breakout current events"
- "check whether any breakouts are stale before class"

Do not invoke for:
- Slide refreshes — use `refresh-course-slides`.
- Book chapter refreshes.
- Rewriting the debate motions, discussion prompts, or instructor notes — those are evergreen and off-limits for this skill.

## The file format (contract you must respect)

Each file under `docs/breakouts/` (except `README.md`) looks like:

```markdown
# Breakout Discussions — Lecture 4: ...

**Format.** ...

---

## Breakout A: <title>
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"..."*

<!-- current-events:start topic="rpki-mandates" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate...]*
<!-- current-events:end -->

**Discussion prompts.**
- ...

**Bring back.** ...

---

## Breakout B: ...

<!--
breakout-metadata:
  lecture: 4
  class: "BGP and Web Manipulation"
  book_chapter: "2.2.3-2.2.4"
  last_refreshed: 2026-07-06
-->
```

Metadata lives in a **bottom-of-file HTML comment** (not YAML frontmatter), because GitHub renders frontmatter as an ugly table at the top of the page. The comment block is invisible on both GitHub and the rendered Jekyll site.

Every refresh does **two passes** per file:

- **Pass 1 — Current events (inside the markers).** Rewrite the prep-reads inside each `<!-- current-events:start ... -->` / `<!-- current-events:end -->` block using fresh WebSearches. This is the same behavior as before.
- **Pass 2 — Reference links (outside the markers).** Scan the evergreen sections (intro paragraph, motions, discussion prompts, bring-back, instructor notes) for named concepts, incidents, court cases, tools, organizations, and technical terms. Ensure each first-mention has an inline markdown link (Wikipedia preferred; primary sources for cases/RFCs; project pages for tools). Add missing links; refresh any that are broken or point somewhere weaker than a stable Wikipedia/primary source. Use the corresponding book chapter as the authority on which entities matter enough to link.

Rules the skill MUST follow:

1. **Wording is evergreen.** In Pass 2 you may ADD `[...](url)` link syntax around existing phrases, but you may NOT change wording, punctuation, emphasis, or the order of prompts. If the surrounding text doesn't already contain a natural anchor, wrap the shortest phrase that does. If nothing natural exists, skip that concept — do not invent phrasing.
2. **Only edit inside `<!-- current-events:start ... -->` / `<!-- current-events:end -->` markers for prep-reads.** Everything outside those markers is evergreen and only accepts link-syntax additions per Pass 2.
3. **Preserve the `topic="..."` slug** on the `current-events:start` marker. Use it as a search hint. Do not rename it — that's an editorial decision.
4. **After refreshing a breakout, update its `<!-- breakout id="X" status="..." refreshed="YYYY-MM-DD" -->` marker** to `status="current"` and today's date.
5. **After refreshing any block in a file, update the `last_refreshed:` line inside the bottom `<!-- breakout-metadata: ... -->` comment** to today's date. Do not touch the other metadata fields.
6. **Never invent URLs.** If a Pass 1 search doesn't turn up usable results, leave the block's placeholder in place and flag as `needs manual review`. For Pass 2, if you cannot verify a link target (article doesn't exist, redirect looks wrong), do not add it — leave the phrase unlinked and note it in the summary.
7. **Do not remove existing links** unless they are demonstrably broken (404) or point to a clearly stale/inferior source than the one the book now cites.
8. **Delete any leftover `<!-- refresh-hint: ... -->` comments** you encounter. Those were one-shot hints and should not persist.

The canonical example of what a refreshed file should look like is `docs/breakouts/full-stack.md` — that's the reference for prose style, link formatting, and per-link context.

## Arguments

The skill is invoked with an argument string. Parse it as follows:

| Argument | Meaning |
|---|---|
| *(empty)* | Do NOT start work. Enter plan mode and ask the user what they want. Present the menu of options below (all, stubs, stale, a lecture number, a section name). Wait for a decision. Never assume — the blast radius of a wrong choice (dozens of WebSearches, a bunch of files touched) is too high. |
| `all` | Refresh every lecture file. Confirm the file count before starting — this is a lot of WebSearch calls. |
| `stubs` | Explicit form of the default: refresh only `status="stub"` breakouts. |
| `stale` | Refresh files whose frontmatter `last_refreshed` is more than 21 days before today. |
| `<N>` or `lecture <N>` | Refresh only lecture N (a single file). |
| `intro` | Lecture 1 (`full-stack.md`). |
| `technical` | Lectures 2–6 (dns, transport, bgp, throttling, ddos). |
| `platform` | Lectures 7–10 (propaganda, disinformation, moderation, personalization). |
| `legal` | Lectures 11–13 (copyright, net-neutrality, zero-rating). |
| `measurement` | Lectures 14–16 (measurement, transparency, legal-economic). |
| `circumvention` | Lectures 17–18 (vpn, tor). |
| `today` / `this week` / `next class` | Ask the user which lecture(s) they're teaching in that window. Do not guess. |
| Comma-separated (e.g. `4,7,legal`) | Union of the above. |

The lecture ↔ section mapping is authoritative from the frontmatter `lecture:` field in each file. Do not hardcode filenames — discover them by reading frontmatter.

## Workflow

### 1. Discover files

```
Glob("docs/breakouts/*.md")
```

Exclude `README.md`. For each remaining file, read the bottom `<!-- breakout-metadata: ... -->` HTML comment to extract `lecture`, `class`, `book_chapter`, and `last_refreshed`. Build a lecture-number → filepath map from this.

### 2. Resolve the argument to a target list

Apply the argument rules above.

**If the argument is empty**, do not proceed. Enter plan mode and ask the user which set they want, showing current file counts so they can choose intelligently. For example:

> No argument given. What do you want to refresh?
>
> - **all** — every lecture (18 files)
> - **stubs** — files with `status="stub"` breakouts (currently: 17)
> - **stale** — files with `last_refreshed` >21 days old (currently: 0)
> - **`<N>`** — a single lecture number
> - **`<section>`** — technical (5), platform (4), legal (3), measurement (3), circumvention (2), intro (1)
>
> Which one?

Wait for the user's answer. Do not guess.

**If the argument is non-empty**, state the plan concisely before starting:

> Refreshing 5 files: lecture 2 (dns.md), 3 (transport.md), 4 (bgp.md), 5 (throttling.md), 6 (ddos.md).

Wait for user confirmation on `all` or on target lists larger than 6 files (unless auto mode is active AND the argument was explicit — auto mode does not override an ambiguous empty argument).

### 3. Parallelize when the list is large

- **1–3 files:** do them serially, in-conversation. Faster than agent overhead.
- **4+ files:** spawn general-purpose subagents (one per section, or one per 3–4 files) so WebSearch calls run in parallel.

Each subagent gets:
- The target file path(s)
- The path to the corresponding book chapter under `../censorship-book/` (for context; readable if the sibling repo exists — do not fail if it doesn't)
- The rules in this SKILL.md (paste the relevant sections into the agent prompt)
- Instructions to return a compact per-file summary and nothing else

### 4. For each file, do this

a. Read the file.
b. Extract, per breakout:
   - Lecture number, class topic, book chapter (from the bottom `<!-- breakout-metadata: ... -->` comment)
   - Motion text (context for the search — do NOT edit it)
   - Topic slug from `current-events:start topic="..."`
   - Current breakout status marker
   - Existing inline links in the evergreen sections (so Pass 2 doesn't duplicate them)

c. Read the corresponding book chapter (path pattern below) for extra grounding on (1) what current events the book itself references (for Pass 1) and (2) which concepts, incidents, tools, and cases the book expects students to know (for Pass 2). Skip this step gracefully if the book repo isn't present.

   Book path patterns (sibling repo `../censorship-book/`):
   | Book chapter ref | Path glob |
   |---|---|
   | `1` | `intro/intro.tex` |
   | `2.*` | `technical/*.tex` |
   | `3.*` | `platform/*.tex` |
   | `4.*` | `legal/*.tex` |
   | `5.*` | `measurement/*.tex` |
   | `6.*` | `circumvention/*.tex` |

d. **Pass 1 — current events.** For each current-events block that needs refresh:
   - Run `WebSearch` using the topic slug plus 1–2 supporting keywords drawn from the motion.
   - Restrict mentally to the last ~12 months. Prefer:
     - Primary sources: regulator press releases (Ofcom, ICO, EU Commission, FCC, ACMA, eSafety), court filings, official government announcements
     - Reputable news: Reuters, AP, FT, WSJ, NYT, BBC, NPR, Al Jazeera, MIT Tech Review, Ars Technica, The Verge
     - NGOs/research: Access Now (KeepItOn), EFF, Citizen Lab, OONI, Freedom House, Article 19
   - Deprioritize: vendor blog posts without data, opinion columns, aggregator sites, listicles.
   - Pick 2–4 links per block. Each link one line: `- [Title](url) — Publisher, Month YYYY. One-sentence context.`
   - Replace the content between the markers. Leave the markers themselves intact.

e. **Pass 2 — reference links (evergreen content).** Walk the intro paragraph, both motions, both sets of discussion prompts, both bring-back questions, and the instructor notes. For each specific concept, incident, court case, tool, organization, or historical event mentioned:
   - Check if it already has a link. Skip if yes.
   - Use the book chapter as an authority — if the book links or footnotes something, that's a strong signal it deserves a link in the breakout too.
   - Preferred targets: Wikipedia (concepts, people, incidents, historical events); primary sources (Justia / CourtListener / Cornell LII for cases; RFC editor for protocols; regulator sites for orders); project pages (torproject.org, ietf.org, ooni.org, eff.org, etc.).
   - Aim for 3–6 links per breakout, first-mention only. Overlinking is worse than underlinking.
   - Wrap the shortest natural phrase already in the text — do NOT change any wording. If no natural anchor exists, skip.
   - Delete any leftover `<!-- refresh-hint: ... -->` comments encountered.

f. Flip the breakout status marker: `status="stub"` → `status="current"`, `refreshed="<today>"`.

g. Update the bottom `<!-- breakout-metadata -->` `last_refreshed:` to today's ISO date (YYYY-MM-DD).

### 5. Verify each edit

After writing, re-read the file. Confirm:
- Both `current-events:start` and `current-events:end` markers still present, one per breakout.
- Every breakout marker still present with a valid `status=` value.
- Bottom `<!-- breakout-metadata -->` block still present and syntactically clean.
- No wording outside the markers was changed — only link syntax was added. A `git diff` should show only additions like `[text` and `](url)` around existing phrases, plus deletions of any `<!-- refresh-hint -->` comments.
- Pass 1 rewrote prep-reads inside markers; Pass 2 only added link syntax.

If any check fails, revert and flag for manual review.

### 6. Summarize

Print a summary table:

```
| Lecture | File | Breakouts refreshed | Notes |
| 4 | bgp.md | A, B | 4 links each; RPKI mandate debate updated with EU mandate news |
| 7 | propaganda.md | A | B left as stub — no strong recent hit for state-media-labels |
```

End with any files that need manual review.

## Safety rules

- **Never touch anything outside `current-events:start`/`end` blocks** other than the breakout status marker and frontmatter `last_refreshed`. If you find yourself wanting to "fix" a motion or prompt, stop — that's out of scope for this skill.
- **Never fabricate citations.** If WebSearch is thin, leave the placeholder and report. An empty stub is far better than an invented URL.
- **Never rename topic slugs.** They are a stable interface between the file and this skill.
- **Never delete a breakout section.** If a topic feels obsolete, flag it in the summary so the instructor can decide.
- **Never batch-write dozens of files without user confirmation.** `all` requires an explicit ok even in auto mode, because a bad WebSearch pass could pollute many files at once.
- **Show a diff or summary before committing** any changes to git. This skill does not commit — leave that to the user.

## Example sessions

**Refresh just lecture 4:**
> User: `/refresh-breakouts 4`
> Skill: Reads `bgp.md`. Two current-events blocks (`rpki-mandates`, `internet-shutdown-orders`). Runs 2 WebSearches. Rewrites both blocks with 3–4 links each. Bumps frontmatter date, flips both breakout statuses to `current`. Reports 1 file, 2 blocks refreshed.

**Refresh a whole section:**
> User: `/refresh-breakouts technical`
> Skill: Enumerates lectures 2–6 → 5 files. Spawns 2 subagents (each handles 2–3 files in parallel). Each subagent does WebSearches and writes files. Reports back.

**Check without touching:**
> User: `check whether any breakouts are stale before class`
> Skill: Lists files by `last_refreshed` date and by `status="stub"` count. Does NOT edit. Recommends which ones to refresh.

**No argument — ask first:**
> User: `/refresh-breakouts`
> Skill: Enters plan mode. Lists options (all / stubs / stale / <N> / <section>) with current file counts. Waits for the user to pick before doing any work.

**Refresh only stubs explicitly:**
> User: `/refresh-breakouts stubs`
> Skill: Filters to files with any `status="stub"` breakout. Confirms plan. Refreshes.
