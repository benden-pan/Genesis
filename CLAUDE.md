<!-- Author: Benden · CC BY 4.0 · first published 2026-06 -->
# CLAUDE.md — Genesis project context

This file orients any Claude (Claude Code / Cowork) picking up the Genesis
project. Read it fully before working. **Also read `conversation/genesis_journey_full_record.md`** (the full record of how this was built — every correction and decision) and **`SETUP_for_Claude_Code.md`** (how to push to GitHub + first tasks). It is the brain-transplant: all the
conventions and decisions the author and I established over a long collaboration.

---

## 0. Who & what

- **Author / owner of the ideas: Benden.** Attribute the framework to Benden.
- **License: CC BY 4.0** (bilingual LICENSE in repo root). Public repo.
- The project has two halves:
  - **Conceptual** (the framework itself — laws, derivations). Primary language
    for dev docs: **Traditional Chinese (Taiwan usage)**. Public-facing artifacts
    are **bilingual (中英對照)** — keep that for anything meant for the repo front.
  - **Code** (three simulators + Python engines). All simulators must stay
    **zero-API, pure-frontend** (see §4).

## 1. The framework in one breath

The world is not stacked from "things"; it is **folded** layer-by-layer by
**compression actions**. Six layers, each an action (not a kind of stuff):

`L0 區分 Distinction → L1 關係 Relation → L2 邊界 Boundary → L3 記憶 Memory → L4 模型 Model → L5 意義 Meaning`

Engine loop: **distinguish → associate → accumulate degree → approach critical
point → randomly snap → compress → fall back to the horizontal plane and
re-associate.** Association (horizontal) and compression (vertical) **alternate**;
randomness fires **only at critical points**. The same engine runs at **every
layer** (self-similar): differences self-replicate by **budding** (L0); units
self-replicate by **fission/division** (L1+). Agency (⊘) is **generated, not
installed** — it ignites when a model-of-other turns back on the self; it
**cannot be leapfrogged**.

V1 charter = 21 principles + 1 axiom + 2 spine principles (frozen). Two walls:
**P16 normative ceiling** (can't adjudicate ultimate good) and **P20 grounding
floor** (can't explain the first difference). Genesis floats between them.

## 2. V1 vs V2 — keep these distinct

- **V1 = the operating laws.** Descriptive, universal. DONE (frozen charter +
  bilingual spec in `docs/`).
- **V2 = the exact method to make *this* world (Earth-now).** Constructive, not a
  parameter-space scan (scanning would just be more V1). V2 closes a loop:
  - **start spec** (what to invest + how much) — see §5
  - **forward path** (the 100 steps, `docs/Genesis_V2.1_...Steps1-100...`)
  - **time axis** (the τ log-time staircase) — see §6
  - **driver** (N² × retention) — see §6
  - **PENDING: four-dimensional closure alignment** — see §7

## 3. THE central-metaphor correction (most important — don't regress)

The engine was first built **wrong**, as a **pyramid** with the drama at the
**top** (folding/collapse), bottom static. The author corrected this over many
turns. The correct metaphor is **STRATA**:

> Every layer continually **accumulates and is retained**, and layers
> **mutually lift each other**. Collapse is a **rare, local exception**, not the
> main story. The low level is **alive** (continually born / churns / proliferates),
> and high structure persists **through** the turnover (that is what indelibility,
> P14, actually means).

Two design decisions the author made (honor them):
- **Decision 1b — retention-dominant, but erodible:** thickness mostly only
  grows; collapse erodes it only **微 (a tiny ratio)**. ("Culture *can* be lost,
  rarely.")
- **Decision 2b — mutual lifting is BIDIRECTIONAL:** lower thickness lifts the
  layer above (standing on accumulation) AND upper lifts lower (e.g. medicine →
  faster/longer lives → faster population growth at the base; P6 reaction).

`genesis_strata.py/.html` implement this and were validated headless: every
layer thickens monotonically; lower strata cross thresholds before upper (the
wave propagates up = mutual lifting); mid-layers (L1/L2) are thickest (a barrel,
not a spire); collapse erosion ≈ 7% of accumulation (a footnote).

## 4. Hard constraints on the simulators

- **Zero-API, pure-frontend.** Each HTML computes everything client-side. No
  server, no API call, no token cost when *running*. (Developing them via Claude
  does cost tokens — that's separate.) Only external load is Google Fonts; can be
  removed for full offline.
- **No browser storage** (localStorage/sessionStorage) inside artifacts.
- **Validate before shipping:** bracket balance, `node --check`, and a headless
  run of the ported JS engine to confirm it matches the Python reference.
- **Aesthetic:** dark "cosmological instrument" — deep-indigo void, IBM Plex Mono
  + Space Grotesk, left instrument panel + canvas, cold→warm layer spectrum
  (L0 blue → L6 white). Keep the three consistent.
- **Mobile matters** (author often on iPhone): keep node counts / per-frame cost
  reasonable.

## 5. V2 start spec — the real "what to invest" (closed system: matter closed, energy open)

Rules the author set: Earth is closed for **matter** (outside = free-floating,
not counted; non-artificial elements are the given t=0 seed, source not
questioned — P20 floor), but **open for energy** (sunlight etc. counted). Ceiling
= Earth itself.

Findings (the "Earth recipe"):
- **Initial investment is NOT 10^50 atoms.** With **fission/proliferation**, the
  seed self-replicates, so necessary investment ≈ a **~10^6-atom self-replicating
  autocatalytic seed** (≈10^-44 of the planet). The vastness is **grown**, not
  invested. "The world is expensive, but expensive in **mechanism**, not material."
- **Material roster (real elements), by role** — now in `genesis_world`:
  - **LIFE (CHONPS):** C,H,O,N,**P,S**. Carbon = quality, **phosphorus = rate**
    (scarcest, the bottleneck). With P added, the sim now assembles a
    nucleotide-class molecule (C/H/N/O/P).
  - **CATALYST metals:** Fe,Mg,Zn,Mo (enzyme active centres → boost local bonding).
  - **FILLER:** Si (inert structural rock).
  - **BATTERY (radioactive):** K,U,Th — Earth's internal heat; heaviest, sink to
    the core. (Don't treat all heavy elements as mere filler — U/Th are the battery.)
- **Energy:** ~1.7×10^17 W solar (main fire) + geothermal (second fire) + tidal;
  cold sink = space. One-source–one-sink heat engine.
- **Seven enabling mechanisms** (pre-embed in the seed; only the first four need a
  real initial carrier): liquid water (L1 medium) → lipids/membrane (L2 ignitor)
  → autocatalytic network → **replicable nucleic-acid template (L3 — THE
  bottleneck)** → peptides/enzymes. L4/L5/⊘ are **grown, not invested**.
- **Boundary conditions:** planet mass/gravity, habitable-zone orbit, magnetic
  field, time stability.
- **Time** (~40 Gyr): increment needs only ~116 doubling generations; the rest is
  **turnover / sculpting the configuration**, not adding quantity.

## 6. τ log-time axis + the two acceleration engines

- **τ = log₁₀(years-before-present).** Left = ancient (compressed), right = modern
  (expanded), right end **dynamically self-adaptive** (drop the unit year→month→
  week to re-expand any dense segment). Self-similar log staircase.
- Three burst-points with **geometrically shrinking** log-intervals
  (Cambrian τ≈8.7 → language τ≈4.7 → industrial τ≈2.4 → AI τ≈1.0; gaps 4.0→2.3→1.4)
  ⇒ **super-exponential** (even log-time can't flatten it).
- **Why** (the two engines, which connect directly to the strata correction):
  **progress rate ∝ (agent count N)² × (accumulated retention thickness)**, both
  growing and mutually feeding ⇒ super-exponential. Engine 1: population ↑ →
  collision ∝ N². Engine 2: retention thickens (P14 stickiness + P8 off-loaded
  carriers like writing) → each trigger stands higher. Dilution at the base
  (low seed/area ratio, trigger ∝ concentration²) is the slow early tail.

## 7. PENDING / next steps  →  see `TASKS.md` for the live list

- **Four-dimensional closure alignment (the V2 core): DONE.** Filled across five
  epochs (dilution / proliferation / retention / AI / projection), closed with no
  missing or redundant investment, ending in the **multi-axis** fork (at the ⊘
  critical point the τ-axis opens from single→multiple; A/B side-by-side, decided
  by selection pressure / human choice). V2 derivation is complete & self-consistent.
- **NEXT = writing phase** (the conversation's value is the *process of
  correction*). Three deliverables, tracked in `TASKS.md`:
  1. **導正史長文** (narrative of the corrections) — do first, Chinese-primary, deep.
  2. **V2 formal spec** (bilingual, → `docs/`), companion to the 100-step run.
  3. **literary short** (story form), builds on `Genesis_Description`.
  Author said **不急 (not urgent)** — recorded as todo, confirm scope before writing.
- **Optional later:** deep chemistry (ionic/metallic/Si networks); repo housekeeping.

## 8. Working style (the author's preferences)

- Explores concepts before coding ("先別急著動手"); gives sharp conceptual
  critiques that must be **grounded in measurement/validation**, not asserted.
- Picks options by letter (A/B/1b/2b). Confirm plans before large rewrites.
- "Validate the simulation first, then produce the document" (成功之後再產文件).
- Traditional Chinese primary in conversation; bilingual for public artifacts.
- Cares a lot about **zero running cost** of the simulators.

## 9. File map

```
README.md · LICENSE (CC BY 4.0) · CLAUDE.md (this file) · TASKS.md · PROTECTION.md
SETUP_for_Claude_Code.md · MANIFEST.md · .gitignore
simulators/   genesis_engine.html · genesis_world.html · genesis_strata.html   (zero-API)
engines/      genesis_engine.py · genesis_world.py · genesis_strata.py · genesis_chem.py
docs/         V1 spec (中英對照) · Description 敘述版 · V2.0 · V2.1 (100 steps) · consolidations
docs/development/   V1.0–V1.5 iteration history
conversation/ genesis_journey_full_record.md (full structured record / 導正史 raw material)
              TRANSCRIPT_PASTE_HERE.md (placeholder for Benden's verbatim export)
```
