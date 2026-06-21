<!-- Author: Benden · CC BY 4.0 · first published 2026-06 -->
# SETUP — pushing Genesis to GitHub via Claude Code

You now have a computer. This is the one-time setup to get this folder onto your
(empty, public) GitHub repo using Claude Code, plus the first tasks to hand it.

---

## A. One-time: install Claude Code

1. Install Node.js (LTS) if you don't have it — https://nodejs.org
2. Install Claude Code (current method may differ — check
   https://docs.claude.com for the exact command). Typically a single install,
   then run `claude` inside a project folder.
3. Open a terminal **inside this `genesis/` folder** (the one containing
   `README.md`, `CLAUDE.md`, etc.).

## B. One-time: push to your empty GitHub repo

Easiest — let Claude Code do it. In the `genesis/` folder, start `claude` and say:

> "Initialise git here and push everything to my GitHub repo:
> `https://github.com/<you>/<repo>.git`. It's a public repo. Use the commit
> message 'Genesis: V1 + V2 + simulators + full record (Benden, CC BY 4.0)'."

It will run `git init`, add the remote, commit, and push. First time it may ask
you to authenticate with GitHub — follow its prompts once.

**Manual equivalent** (if you prefer typing it yourself):
```bash
git init
git add .
git commit -m "Genesis: V1 + V2 + simulators + full record (Benden, CC BY 4.0)"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

## C. First thing to tell the new Claude

Point it at the context so it loads everything:

> "Read CLAUDE.md, TASKS.md, PROTECTION.md, and
> conversation/genesis_journey_full_record.md before doing anything. That's the
> full project context."

`CLAUDE.md` is the brain-transplant; it will pick up every convention and decision.

---

## D. Suggested first tasks (from TASKS.md)

In priority order — confirm scope with Claude before it writes:

1. **Paste the verbatim transcript** into
   `conversation/TRANSCRIPT_PASTE_HERE.md` and commit (see that file for how).
2. **導正史長文** (corrections-history long-form) — the #1 writing deliverable;
   `conversation/genesis_journey_full_record.md` is its raw material. Chinese-primary,
   deep. (This is also your strongest originality evidence — see PROTECTION.md.)
3. **Embed attribution headers** in core files:
   `Author: Benden · CC BY 4.0 · first published 2026-06` (PROTECTION.md todo).
4. **Privacy:** turn off the training toggle in Claude Settings → Privacy (5y→30d).
5. Later: V2 formal spec → `docs/`; literary short; optional deep chemistry.

---

## E. Sanity check after pushing

- The three simulators are zero-API pure-frontend: open any
  `simulators/*.html` directly in a browser — they just run, no server needed.
- The Python engines: `python3 engines/genesis_strata.py` (etc.) run headless.
- Nothing here needs an API key or network to run (only Google Fonts loads in the
  HTML for typography; removable for full offline).
