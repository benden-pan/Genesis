# Genesis · 造世方法論框架

**A methodology for world-generation — and the engines that run it.**
**一套從第一原理出發的造世方法論——以及讓它運轉的引擎。**

Author / 作者: **Benden**  ·  License / 授權: **CC BY 4.0**

---

## What this is / 這是什麼

Genesis is a framework for how *any* world is generated — not by stacking
"things", but by **folding** difference layer-by-layer through acts of
compression. It is described by a small set of laws (V1), and then used
constructively to ask how *this* world — Earth — could be produced (V2).

Genesis 主張：世界不是把「東西」堆起來的，而是透過一連串**壓縮動作**，
把差異**一層層折疊**出來的。V1 找出這套運作的**法則**；V2 則反過來，
用這些法則去推演「造出地球這一個世界」的確切方法。

### The six layers / 六層

Each layer is a *compression action*, not a kind of stuff:

| Layer | 名稱 | The act / 動作 |
|------|------|----------------|
| **L0** | 區分 Distinction | a first difference is drawn |
| **L1** | 關係 Relation | differences are coupled |
| **L2** | 邊界 Boundary | a coupling is closed into an inside/outside |
| **L3** | 記憶 Memory | a boundary's state is retained |
| **L4** | 模型 Model | retained states simulate the world |
| **L5** | 意義 Meaning | a model values its own states |

The engine that drives all six: **distinguish → associate → accumulate degree →
approach a critical point → randomly snap → compress → fall back to the
horizontal plane and re-associate.** Association (horizontal) and compression
(vertical) alternate; randomness only fires at critical points.

---

## The simulators / 三台儀器 (`simulators/`)

Three standalone, **zero-API, pure-frontend** HTML instruments. Open any of them
in a browser — they compute everything on your own device, no server, no API,
no token cost, forever. (Only Google Fonts loads externally, for typography.)

開啟即跑、純前端、**零 API、零成本**。三台各對應框架的一個視角：

- **`genesis_engine.html`** — the abstract folding mechanism. How any difference
  folds into layers, proliferates (L0 buds, L1+ divides), and persists through
  turnover. Plural lineages that never merge (diversity); structure that resists
  erasure (indelibility).
  抽象折疊機制：折疊、增生、汰換中存續、世系並存。

- **`genesis_world.html`** — a concrete world on **real chemistry**. The real
  element roster (CHONPS for life + catalyst metals + filler + radioactive
  battery) on a thermal field: atoms bond into molecules, gravity stratifies a
  differentiated planet (heavy battery sinks to the core, organics float), and
  molecules fold into L2 compartments. Cool it to condense a world; heat it to
  undo one.
  具體化學世界：真元素 → 真分子 → 真區室，重力分化行星。

- **`genesis_strata.html`** — the **strata accumulation law**. The corrected
  central metaphor: the world is *not* a pyramid with the drama at the top, but
  a stack of strata where **every layer keeps accumulating and is retained, and
  the layers mutually lift each other**. Collapse is a rare footnote.
  地層累積律：全層堆積、留存、互相墊高；崩解是例外。

## The engines / Python 參考實作 (`engines/`)

Headless reference implementations (the HTML mirrors these):

- `genesis_engine.py` — abstract folding engine (living substrate + fission)
- `genesis_world.py` — real-chemistry world (L0 atoms → L1 molecules → L2 compartments)
- `genesis_strata.py` — strata accumulation (per-layer thickness + mutual lifting)
- `genesis_chem.py` — early chemistry prototype (valence chemistry on a thermal field)

```bash
python3 engines/genesis_strata.py   # watch every layer thicken & mutually lift
```

## The documents / 框架文件 (`docs/`)

- `Genesis_V1_Specification_中英對照.md` — the authoritative V1 spec (bilingual)
- `Genesis_Description_敘述版.md` — a narrative, story-form introduction
- `Genesis_V2.0_造世_奠基.md` — V2 founding (the descriptive→generative turn)
- `Genesis_V2.1_WorldRun1_Steps1-100_bilingual.md` — "An Earth from Nothing", 100 steps
- consolidations + `development/` (V1.0–V1.5 iteration history)

---

## V1 vs V2

- **V1 — the operating laws.** Descriptive, universal: whatever world is running,
  it obeys this one engine (21 principles + 1 axiom + 2 spine principles, frozen).
  運作法則。描述性、普適。

- **V2 — the exact method to make *this* world.** Constructive: given V1's laws
  and a target (Earth-now), find the exact initial investment and the step-path
  that reach it — reverse-derivation must equal the start of forward-derivation.
  造出此世界的確切方法。構造性、特定。

---

## License / 授權

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
You may share and adapt it, including commercially, with attribution to **Benden**.
本作品採 CC BY 4.0 授權；可自由分享與改作（含商業用途），惟須標示原作者 **Benden**。
