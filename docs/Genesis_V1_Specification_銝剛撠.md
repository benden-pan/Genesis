<!-- Author: Benden Pan · CC BY 4.0 · first published 2026-06 -->
# Genesis — 造世方法論框架
# Genesis — A Methodology for World-Generation

> **版本 / Version**：V1 世代總綱（涵蓋 V1.0–V1.5）· V1 Generation Specification (covering V1.0–V1.5)
> **性質 / Status**：開源初版草案 · Open-source initial draft
> **用途 / Purpose**：作為 Genesis V2 的行為準則，亦作為公開發布的奠基文本 · Serves as the behavioral charter for Genesis V2, and as the founding text for public release.

---

## 前言 · Preface

**中文**
Genesis 是一套「造世」的方法論。它不問「世界由哪些東西組成」，而問一個更底層的問題：**世界憑什麼能一層一層長出來，又憑什麼會崩回去？**

它的核心主張只有一句：世界不是由「東西」堆疊而成的，而是由一連串**壓縮動作**層層折疊而成。每一層不是一類物體，而是一種「把下層折疊起來」的新能力。把無數分子的振動折疊成「溫度」、把一束關聯折疊成「信任」、把一群人的共識折疊成「幣值」——這就是世界生長的方式。

這份文件用 **21 條準則 + 1 條公理 + 2 條脊椎準則**，描述這台折疊引擎如何運轉。它同時誠實地標出引擎碰不到的兩端：最底的「為何存在」與最頂的「何為應然」。Genesis 不是解釋一切的萬物論，而是一台**在兩道牆之間完整運轉**的造世引擎。

**English**
Genesis is a methodology for *world-generation*. It does not ask "what things is the world made of," but a more fundamental question: **by what means can a world grow up, layer by layer, and by what means does it collapse back down?**

Its core claim is a single sentence: the world is not stacked out of "things"; it is folded, layer upon layer, out of a sequence of **compression actions**. Each layer is not a class of objects but a new capability for "folding the layer below." Folding the vibration of countless molecules into "temperature," folding a bundle of relations into "trust," folding the consensus of a crowd into "currency value" — this is how the world grows.

This document uses **21 principles + 1 axiom + 2 spine principles** to describe how this folding engine runs. It also honestly marks the two ends the engine cannot reach: the bottommost "why is there anything," and the topmost "what is truly good." Genesis is not a theory of everything; it is a world-generation engine that runs fully **between two walls**.

---

## 如何閱讀 · How to Read

**中文**
- 先讀「框架總覽」掌握整體形狀，再按需查閱個別準則。
- 每條準則包含：一句話定義、中文詳解、English explanation、與一個具體例子。
- 準則分九類：層級、壓縮、不確定性、意義、崩解、善惡、能動性、邊界，外加貫穿全局的脊椎準則。
- 結尾附詞彙表，供初次接觸者查閱核心術語。

**English**
- Read "Architecture at a Glance" first for the overall shape, then consult individual principles as needed.
- Each principle contains: a one-line statement, a Chinese explanation, an English explanation, and a concrete example.
- Principles fall into nine groups: Layer, Compression, Uncertainty, Meaning, Decompression, Good-and-Evil, Agency, Boundary, plus the cross-cutting Spine principles.
- A glossary of core terms is appended for newcomers.

---

## 框架總覽 · Architecture at a Glance

### 六層因子 · The Six Layers

每一層是一種**壓縮動作**，不是一類物體。往上一層，變數變少，但每個變數背負的資訊更重。
Each layer is a *compression action*, not a class of objects. Going up, variables become fewer, but each carries heavier information.

| 層 Layer | 名稱 Name | 做的事 What it does |
|---|---|---|
| **L0** | 區分 Distinction | 標記差異 · marks difference |
| **L1** | 關係 Relation | 讓差異穩定耦合 · couples differences |
| **L2** | 邊界 Boundary | 第一次壓縮：什麼算「一個單元」· first compression: what counts as "one unit" |
| **L3** | 記憶 Memory | 留住過去、影響未來 · stores the past, shapes the future |
| **L4** | 模型 Model | 在內部模擬外部 · models the outside internally |
| **L5** | 意義 Meaning | 壓縮出「為什麼」· compresses out a "why" |

### 造世引擎 · The World-Generation Engine

```
區分 → 關聯 → 程度累積 → 逼近臨界 → 隨機咬合 → 壓縮 → 落回水平再關聯
Distinction → Association → Magnitude builds → Nears critical → Randomness engages → Compression → back to the horizontal plane, associate again
```

加上第四驅動 **能動性**（夠強的高層能刻意驅動壓縮或崩解、並移動臨界點）。
Plus a fourth driver, **Agency** (a strong enough high layer can deliberately drive compression or collapse, and move the critical point).

### 兩道牆 · The Two Walls

| | 牆 Wall | 碰不到 Cannot reach | 標記 Marked by |
|---|---|---|---|
| **上界 Ceiling** | 規範邊界 Normative boundary | 何種價值「真的」對 · which value is *truly* right | 準則 16 / Principle 16 |
| **下界 Floor** | 奠基邊界 Grounding boundary | 為何「真的」有差異 · why difference *truly* exists | 準則 20、地標準則 1 / Principle 20, floor-marker Principle 1 |

---

# 準則詳解 · The Principles in Detail

## 公理 · Axiom

### 層是分類，不是序列 | Layers Are a Classification, Not a Sequence

> **中** ｜ L0–L5 標示「世界獲得了哪一種折疊能力」，不是先後發生的階段。
> **EN** ｜ L0–L5 label *which kind* of folding capability the world has gained, not chronological stages.

**詳解**｜六層是結構分類，不是時間表。一個事件可以靠關聯與壓縮的交錯**幾乎同時安裝好幾層**，也可以在某些層缺席時越級湧現。把六層讀成「先有 L0、再有 L1……」是對框架的誤用。

**Explanation**｜The six layers are a structural taxonomy, not a timeline. A single event can install several layers almost simultaneously through the interleaving of association and compression, and can also emerge across skipped levels. Reading them as "first L0, then L1…" misuses the framework.

**例 · Example**｜生命起源時，細胞膜（L2 邊界）與遺傳（L3 記憶）並非依序出現，而是互相拉拔、共同湧現。· In the origin of life, the cell membrane (L2) and heredity (L3) do not appear in order; they bootstrap and emerge together.

---

## 層級準則 · Layer Principles

### 準則 1 · 可區分性是入場券 | Distinguishability Is the Price of Entry

> **中** ｜ 任何東西要存在，必先有一個差異能被標記。
> **EN** ｜ For anything to exist, there must first be a difference that can be marked.

**詳解**｜完全均質的宇宙裡沒有任何變數、無物可命名。差異是一切的前提。這條同時是整個框架的**地板**——其下 Genesis 無法再探（見準則 20）。

**Explanation**｜In a perfectly uniform universe there are no variables and nothing can be named. Difference is the precondition of everything. This is also the framework's **floor** — Genesis cannot reach below it (see Principle 20).

**例 · Example**｜「溫度」只在分子運動有快慢差異時才存在；完全靜止均勻處，溫度無從談起。· "Temperature" exists only where molecular motion differs in speed; in perfect uniform stillness, temperature has no meaning.

### 準則 2 · 共現才算關係 | Co-occurrence Is What Makes a Relation

> **中** ｜ 單一差異不構成結構；唯有多個差異穩定地一起變動，才形成耦合。
> **EN** ｜ A single difference is not structure; only differences that vary together reliably form a coupling.

**詳解**｜關係是世界的第一張網。它還不是「物體」，只是「哪些差異綁在一起」。上層的一切，都建立在這張耦合網上。

**Explanation**｜Relations are the world's first web. They are not yet "objects," only "which differences are bound together." Everything above is built on this web of couplings.

**例 · Example**｜深水、避風、有淡水——這幾個地理差異穩定共現，才構成「適合靠岸」這個關係。· Deep water, shelter from wind, fresh water — these geographic differences co-occurring reliably constitute the relation "good for landing a ship."

### 準則 3 · 命名權來自穩定（含對偶）| Naming Rights Come from Stability (with Its Dual)

> **中** ｜ 下層模式穩定到「可被命名」時，才有資格被折疊成上層的一個單元。對偶：變動多元者不獲命名權，歸入觀察標的。
> **EN** ｜ A lower pattern earns folding into a higher unit only once stable enough to be named. Dual: the variable-and-multiple earns no naming rights and becomes an observational target.

**詳解**｜穩定者升格為「結構」（可被當成固定積木操作）；本質為變動、多元、流動的東西，則歸入**觀察標的**——只被觀察，不被固化成層或準則。框架因此知道什麼該固定、什麼該放它流動。

**Explanation**｜The stable is promoted to "structure" (operable as a fixed building block); what is essentially variable, plural, and fluid becomes an **observational target** — watched, never frozen into a layer or principle. Thus the framework knows what to fix and what to let flow.

**例 · Example**｜「一座城市」穩定到可被當成單一變數操作；但「自我意識」因本質流動多變，拒絕被釘成一層。· "A city" is stable enough to operate as one variable; but "self-consciousness," fluid by nature, refuses to be pinned into a layer.

### 準則 4 · 邊界是約定但即真 | Boundaries Are Conventions, Yet Real

> **中** ｜ 把一群緊密關係劃成「一個東西」的邊界是人為約定，但一旦劃定就極其真實。
> **EN** ｜ The boundary packaging tight relations into "one thing" is a convention, yet once drawn it is utterly real.

**詳解**｜邊界決定「什麼算一個單元」。它不是天生的，但換一條邊界，就是換一個世界——稅收、認同、命運都跟著改變。

**Explanation**｜A boundary decides "what counts as one unit." It is not innate, but to redraw it is to change the world — taxation, identity, and fate all shift with it.

**例 · Example**｜市界是劃出來的，但併入鄰市或獨立設市，會真的改變一地的命運。· A city limit is drawn by people, yet merging into a neighbor or becoming independent genuinely changes a place's fate.

### 準則 5 · 記憶製造路徑依賴 | Memory Creates Path Dependence

> **中** ｜ 一旦單元能存住過去、影響未來，因果鏈變長，可預測性同時增強又減弱。
> **EN** ｜ Once a unit stores the past and shapes the future, causal chains lengthen; predictability both rises and falls.

**詳解**｜記憶讓系統有了「歷史」。可預測性增強，因為有規律可循；又減弱，因為被歷史綁架、無法重來。基因、習慣、制度都是記憶。

**Explanation**｜Memory gives a system a "history." Predictability rises (there are regularities) and falls (the system is hostage to its history and cannot be re-run). Genes, habits, and institutions are all memory.

**例 · Example**｜開國皇帝的安排，綁住了後世幾百年的制度走向。· A founding emperor's arrangements bind the institutional trajectory of centuries that follow.

### 準則 6 · 表徵會反作用 | Representations Act Back

> **中** ｜ 高層模型不只被動描述世界，它會反過來改寫下層。
> **EN** ｜ A high-level model does not merely describe the world; it reaches back and rewrites the layers below.

**詳解**｜這是 L4 的詭異之處：模型越強，向下重組現實的力量越大。它也是後面「創造／毀滅」與「能動性」的引擎源頭。

**Explanation**｜This is the uncanny power of L4: the stronger the model, the greater its power to reshape reality downward. It is also the engine-source of "creation/destruction" and "agency" later on.

**例 · Example**｜一張「這裡要建新港」的規劃圖，會真的讓地貌被推平重塑。· A blueprint that says "a new harbor goes here" really does get the landscape leveled and rebuilt.

### 準則 7 · 意義憑空湧現卻最有權力（僅表徵式）| Meaning Emerges from Nothing Yet Rules Most (Represented Meaning Only)

> **中** ｜ 最高層的價值在底層找不到對應物，卻對下層支配力最強。
> **EN** ｜ Top-layer values have no counterpart below, yet command the lower layers most powerfully.

**詳解**｜人會為了一個「認同」去改寫地貌。注意：本條只描述**表徵式意義**（被意識、被言說的價值）；另有一種「湧現式意義」不經表徵（見準則 12）。

**Explanation**｜People will reshape the earth for an "identity." Note: this principle describes only *represented* meaning (values that are conscious and spoken); there is also "emergent meaning" that bypasses representation (see Principle 12).

**例 · Example**｜「守護我們的港」在任何一塊石頭裡都找不到，卻能讓人為它犧牲。· "Defend our harbor" is found in no single stone, yet people will die for it.

---

## 壓縮準則 · Compression Principles

### 準則 8 · 壓縮可轉移主體 | Compression Can Transfer Its Subject

> **中** ｜ 折疊後承載新變數的「主體」不必是原本那堆東西。
> **EN** ｜ The "subject" carrying a newly folded variable need not be the original stuff.

**詳解**｜三種壓縮：**就地**（仍寄生原物質，如溫度←分子）；**轉移**（主體跳到新載體，如幣值住在集體信念裡）；**分布式**（折疊的是「一束關聯」，如信任散布於制度、記憶、習慣）。

**Explanation**｜Three kinds: **in-place** (still parasitic on the same matter, e.g., temperature ← molecules); **off-loaded** (the subject jumps to a new carrier, e.g., a currency's value lives in collective belief); **distributed** (what is folded is "a bundle of relations," e.g., trust spread across institutions, memory, and habit).

**例 · Example**｜燒掉一張鈔票，紙沒了，但「幣值」不滅——主體早已轉移到所有人的共識裡。· Burn a banknote and the paper is gone, but "currency value" survives — its subject long since transferred into everyone's shared belief.

### 準則 9 · 壓縮與關聯交錯驅動 | Compression and Association Drive in Alternation

> **中** ｜ 關聯產生組合，組合穩定後被壓縮成新變數，新變數回到水平面再關聯。
> **EN** ｜ Association produces combinations; a stable combination is compressed into a new variable; it returns to associate again.

**詳解**｜垂直（壓縮）與水平（關聯）是同一引擎的兩個衝程。純爆炸→混沌，純收攏→死板；正是這個**交錯**，讓世界既豐富又可計算。

**Explanation**｜Vertical (compression) and horizontal (association) are two strokes of one engine. Pure explosion → chaos; pure folding → rigidity. It is the **alternation** that makes the world both rich and computable.

**例 · Example**｜制度、記憶、習慣三者反覆共現（關聯），穩定後被折疊（壓縮）成一個新變數，我們叫它「信任」。· Institutions, memory, and habit co-occur repeatedly (association); once stable they are folded (compression) into a new variable we call "trust."

---

## 不確定性準則 · Uncertainty Principles

### 準則 10 · 隨機性是臨界點的扳機 | Randomness Is the Trigger at Critical Points

> **中** ｜ 唯有「程度」逼近臨界閾值時，隨機性才咬合進來，決定系統倒向哪個分支。
> **EN** ｜ Only as a magnitude nears the critical threshold does randomness engage, deciding which branch the system falls toward.

**詳解**｜遠離臨界時，系統確定、可還原、平滑演化——這正是世界大部分時間可預測的原因。隨機性是**間歇性**的，只在臨界點短暫掌權，做完分支選擇後退場。

**Explanation**｜Far from criticality, the system is deterministic, reducible, smooth — which is why the world is predictable most of the time. Randomness is **intermittent**, holding power only briefly at the critical point, then leaving once the branch is chosen.

**例 · Example**｜水到 100°C 前，加熱平滑確定；到了臨界點，哪個分子先汽化由隨機決定。· Below 100°C, heating is smooth and determined; at the critical point, which molecule vaporizes first is decided by chance.

### 準則 11 · 臨界點的自由維繫未來的開放 | The Freedom of the Critical Point Keeps the Future Open

> **中** ｜ 臨界閾值不是客觀常數，它隨視角與情境自由浮動。
> **EN** ｜ The critical threshold is not an objective constant; it floats freely with viewpoint and situation.

**詳解**｜正因岔路口的**位置**無法被預先釘死，未來才不塌縮成一組預定的岔路。隨機性管「在路口選哪條路」，臨界點的自由管「路口本身長在哪」。高層能動性還能主動移動這個臨界點。

**Explanation**｜Precisely because the *location* of the fork cannot be fixed in advance, the future does not collapse into a set of predetermined branches. Randomness governs "which road at the fork"; the freedom of the critical point governs "where the fork grows." High-layer agency can even move it on purpose.

**例 · Example**｜一個行為何時從善翻成惡，閾值隨時代移動（奴隸制曾「可接受」，今為惡）——道德進步因此可能。· When an act flips from good to evil, the threshold moves with the era (slavery once "acceptable," now evil) — which is why moral progress is possible.

---

## 意義準則 · Meaning Principle

### 準則 12 · 意義有兩條路徑 | Meaning Has Two Routes

> **中** ｜ 意義（L5）不必然從模型（L4）長出。湧現式由選擇安裝、無需表徵；表徵式活在模型裡。
> **EN** ｜ Meaning (L5) need not grow from modeling (L4). Emergent meaning is installed by selection without representation; represented meaning lives inside a model.

**詳解**｜湧現式：細菌「求生」卻什麼都沒建模——目的由天擇安裝。表徵式：人有意識地珍視某物。兩者非互斥，可共同生產同一意義變數（如天命、善惡）。

**Explanation**｜Emergent: a bacterium "wants" to survive yet models nothing — its purpose installed by natural selection. Represented: a human consciously values something. The two are not exclusive and can co-produce a single meaning-variable (e.g., the Mandate of Heaven, good/evil).

**例 · Example**｜嬰兒偏好「幫忙者」勝過「阻礙者」是湧現式道德；成文倫理學是表徵式道德。· An infant preferring a "helper" over a "hinderer" is emergent morality; written ethics is represented morality.

---

## 崩解準則 · Decompression Principles

### 準則 13 · 壓縮可逆：崩解 | Compression Is Reversible: Decompression

> **中** ｜ 支撐上層變數的下層耦合衰敗過臨界，該變數失去資格，碎回下層。
> **EN** ｜ When the lower couplings supporting a high-level variable decay past critical, that variable loses its standing and shatters back down.

**詳解**｜上層的「一個東西」碎回下層的「一堆關係」。長與崩共用同一台引擎、同一套臨界邏輯，差別只在方向：壓縮是「組合穩定到可命名」，崩解是「組合鬆動到不可名」。

**Explanation**｜The upper "one thing" shatters back into lower "many relations." Building and collapse share one engine and one critical logic, differing only in direction: compression is "a combination stabilizing into nameability"; decompression is "a combination loosening into namelessness."

**例 · Example**｜朝代崩潰時，「朝廷」不再是一個可用的單變數，碎回地域割據。· When a dynasty falls, "the court" is no longer a usable single variable; it shatters back into regional warlordism.

### 準則 14 · 崩解是差別的（黏性）| Collapse Is Differential (Stickiness)

> **中** ｜ 各層死法不同。黏性 = 主體被卸載到「耐久、與單元無關之載體」的程度。
> **EN** ｜ Layers die differently. Stickiness = the degree to which a subject is off-loaded onto durable, unit-independent carriers.

**詳解**｜轉移壓縮比就地壓縮抗崩。黏性梯度：基因（湧現式）> 深層文化 > 淺層慣例（表徵式）。卸載得越深、載體越與當下單元無關，越能在崩潰中存活。

**Explanation**｜Off-loaded compression resists collapse better than in-place. Stickiness gradient: genome (emergent) > deep culture > shallow convention (represented). The more deeply off-loaded, and the more carrier-independent of the present unit, the better it survives a collapse.

**例 · Example**｜王朝亡了，天命一夕蒸發，但制度典籍（記憶）被下一朝代整套繼承——因為它的載體與某一朝代無關。· A dynasty falls and its Mandate evaporates overnight, but its institutions and texts (memory) are inherited wholesale by the next dynasty — because their carriers are independent of any one dynasty.

---

## 善惡準則 · Good-and-Evil Principles

### 準則 15 · 惡常是崩解，不總是建構 | Evil Is Often Decompression, Not Always Construction

> **中** ｜ 善幾乎總是整合（壓縮）；惡卻有兩條路徑，其一是崩解。
> **EN** ｜ Good is almost always integration (compression); evil has two routes, one of which is decompression.

**詳解**｜善＝把他者納入更大的「我們」。惡的兩條路徑：**崩解型**（把他者表徵為主體的模型失效，鄂蘭的「平庸之惡」）與**建構型**（連貫的價值體系明確標記某類為「應消除」）。善惡因此不對稱。

**Explanation**｜Good = folding the other into a larger "us." Evil's two routes: the **decompression kind** (the model representing the other as a subject fails — Arendt's "banality of evil") and the **constructed kind** (a coherent value system explicitly marking a group as "to be eliminated"). Good and evil are therefore asymmetric.

**例 · Example**｜不把他者當人看的殘忍是崩解型惡；意識形態驅動的屠殺是建構型惡。· Cruelty from no longer seeing the other as a person is decompression-evil; ideologically driven genocide is constructed-evil.

### 準則 16 · 規範邊界（上界）| The Normative Boundary (Upper Wall)

> **中** ｜ Genesis 能描述任何價值的「架構」，卻不裁決任何價值的「約束力」。
> **EN** ｜ Genesis can describe the *architecture* of any value, but adjudicates the *bindingness* of none.

**詳解**｜「相信 X 是善」還原得了（演化本能＋文化共識）；但「X 本身是善」這個應然的約束力還原不到（休謨：實然推不出應然）。這是框架的**天花板**——它能把抉擇照亮到極致，卻無法替你做出抉擇。

**Explanation**｜"Believing X is good" reduces (to evolved instinct + cultural consensus); but "X itself being good" — the bindingness of the ought — does not (Hume: no ought from an is). This is the framework's **ceiling** — it can illuminate a choice completely, yet cannot make the choice for you.

**例 · Example**｜Genesis 能解釋道德為何存在、如何演變，卻無法告訴你「人類應該選擇存續」這個應然。· Genesis can explain why morality exists and how it evolves, yet cannot tell you the ought "humanity should choose to survive."

---

## 能動性準則 · Agency Principles

### 準則 17 · 創造與毀滅同源 | Creation and Destruction Share One Source

> **中** ｜ 使人類獨步的創造力，正是使人類獨步的自毀力。
> **EN** ｜ The creativity that sets humanity apart is identically the self-destructiveness that sets it apart.

**詳解**｜兩者都是高層模型對下層的強大反作用（準則 6 的極致）指向不同方向。無法只要創造力而剔除毀滅力；兩者振幅同步於「模型之強 × 意義之烈」。

**Explanation**｜Both are the powerful downward reaction of high-level models (Principle 6 at its extreme), pointed in different directions. One cannot keep the creative power and discard the destructive; both amplitudes scale together with "strength of model × intensity of meaning."

**例 · Example**｜核能、基因工程、AI——每一項創造同時就是一項自毀風險，是同一枚硬幣的兩面。· Nuclear power, genetic engineering, AI — each creation is simultaneously a self-destruction risk, two faces of one coin.

### 準則 18 · 崩解有兩個方向 | Decompression Has Two Directions

> **中** ｜ 由下而上是衰敗（緩慢、非刻意）；由上而下是自毀（可瞬間、可刻意）。
> **EN** ｜ Bottom-up is decay (slow, unintended); top-down is self-destruction (possibly instant, possibly deliberate).

**詳解**｜由上而下的崩解遠比由下而上危險，因為高層能用創造力反過來攻擊自身基質，並主動把臨界點往前拉。

**Explanation**｜Top-down collapse is far more dangerous than bottom-up, because a high layer can turn its creative power against its own substrate and deliberately drag the critical point forward.

**例 · Example**｜文明的自我毀滅不是慢慢爛掉，而是高層的一個決定、一個按鈕。· A civilization's self-destruction is not a slow rot but a high-layer decision, a single button.

### 準則 19 · 能動性是高層的新驅動 | Agency Is a New Driver at High Layers

> **中** ｜ 當一個層能模擬並作用於整座塔（含自身），能動性成為引擎的第四驅動。
> **EN** ｜ When a layer can model and act upon the whole stack (including itself), agency becomes the engine's fourth driver.

**詳解**｜能動性的**機制** = L4 自指模型 ＋ L5 價值梯度 ＋ 準則 6 反作用，在臨界點**接管隨機性的選擇槽**，並能移動系統自身的臨界點。機制是結構、可還原；它所生的**自我意識**因變動多元，是觀察標的。「自由」＝隨機性的選擇槽被「自指模型＋價值梯度」接管。

**Explanation**｜Agency's **mechanism** = L4 self-referential model + L5 value gradient + Principle-6 reaction, **taking over randomness's selection slot** at the critical point and able to move the system's own critical point. The mechanism is structure and reducible; the **self-consciousness** it gives rise to, being variable and plural, is an observational target. "Freedom" = randomness's selection slot taken over by "self-model + value gradient."

**例 · Example**｜人類能主動把自毀臨界點往後推（條約、規範）或往前拉（軍備競賽）；MAD 是最純粹的例子。· Humans can push the self-destruction critical point back (treaties, norms) or forward (arms races); Mutually Assured Destruction is the purest example.

---

## 邊界準則 · Boundary Principles

### 準則 20 · 奠基邊界（下界）| The Grounding Boundary (Lower Wall)

> **中** ｜ Genesis 解釋世界在「至少有一個區分」之後如何展開，但解釋不了「為何有第一個差異而非全無」。
> **EN** ｜ Genesis explains how the world unfolds *given* at least one distinction, but cannot explain "why there is a first difference rather than nothing at all."

**詳解**｜引擎寄生於「差異之潛能」的存在，無法生出潛能本身。這是框架的**地板**。它正是各傳統插入答案之處（第一因、必然存在者、偶然事實、多重宇宙）；Genesis 在它們之間保持沉默。

**Explanation**｜The engine is parasitic on the existence of a "potential-for-difference"; it cannot produce that potential itself. This is the framework's **floor**. It is exactly where various traditions insert their answers (a first cause, a necessary being, brute contingency, the multiverse); Genesis stays silent among them.

**例 · Example**｜物理能解釋「物從量子真空來」，但量子真空已是「某種結構化的潛能」，不是徹底的無。· Physics explains "things come from the quantum vacuum," but the quantum vacuum is already "a structured potential," not sheer nothingness.

### 準則 21 · 起源是引擎的極限情形 | The Origin Is the Engine's Limit Case

> **中** ｜「無」＝絕對均質＝終極臨界點；第一個區分＝該臨界點上的一次隨機破缺。
> **EN** ｜ "Nothing" = perfect homogeneity = the supreme critical point; the first distinction = a random symmetry-break at that critical point.

**詳解**｜完美均質之所以是「終極臨界點」，是因為它無限平衡、無限敏感——任何方向都一樣，沒有東西把它釘住。由準則 10，第一個區分就是這個臨界點上的隨機破缺。引擎能把起源上溯到「差異之潛能」為止，不能再下（接準則 20）。

**Explanation**｜Perfect homogeneity is the "supreme critical point" because it is infinitely balanced and infinitely sensitive — every direction is alike, nothing pins it down. By Principle 10, the first distinction is a random break at that critical point. The engine can trace the origin back as far as the "potential-for-difference," and no further (continues into Principle 20).

**例 · Example**｜量子真空漲落、早期宇宙的自發對稱破缺，都是「終極臨界點上的隨機破缺」。· Quantum vacuum fluctuations and spontaneous symmetry-breaking in the early universe are both "random breaks at the supreme critical point."

---

## 脊椎準則 · Spine Principles

### 脊椎 A · 向下可還原 | Reducibility Downward

> **中** ｜ 上層任何變數須能拆回下層，或拆回「承接它的新載體」；指得出新主體即非迷信。
> **EN** ｜ Any upper variable must reduce to lower layers, or to "the new carrier that took it on"; if you can point to the new subject, it is not superstition.

**詳解**｜這是防止「憑空造世」的安全鎖。拆不回任何主體的，是幻覺或迷信。但這條鎖有上下兩道邊界：它還原「相信—價值」卻不還原「價值—本身」（準則 16），也還原不到「第一個差異」之下（準則 20）。

**Explanation**｜This is the safety lock against "world-building from thin air." Whatever reduces to no subject at all is illusion or superstition. But the lock has two boundaries: it reduces "belief-in-value" but not "value-itself" (Principle 16), and cannot reduce below "the first difference" (Principle 20).

**例 · Example**｜鈔票的「幣值」拆不回紙張，但拆得回「集體信念狀態」——指得出，故非迷信。· A banknote's "value" does not reduce to paper, but it does reduce to "a collective state of belief" — pointable, hence not superstition.

### 脊椎 B · 隨機性只換身份、不消失 | Randomness Only Changes Identity, Never Vanishes

> **中** ｜ 同一份不確定性，在 L0 是真隨機，在 L2–L3 是混沌，在 L4–L5 是自由。
> **EN** ｜ One and the same uncertainty is true-randomness at L0, chaos at L2–L3, and freedom at L4–L5.

**詳解**｜每跨一層，不確定性被重新詮釋，從不被消除。「自由」不是「沒有被決定」，而是「被自己的模型與價值決定，而非被盲目隨機決定」——這讓 Genesis 天然落在相容論一側。

**Explanation**｜At each layer crossing, uncertainty is reinterpreted, never eliminated. "Freedom" is not "being undetermined" but "being determined by one's own model and values rather than by blind randomness" — placing Genesis naturally on the compatibilist side.

**例 · Example**｜你無法完整模擬自己（自指系統算不過自己），所以總有一塊「我還沒決定」的殘餘——自由感繼承了隨機性的開放性。· You cannot fully simulate yourself (a self-referential system cannot out-compute itself), so there is always a residue of "I haven't decided yet" — the sense of freedom inherits randomness's openness.

---

# 詞彙表 · Glossary

| 中文 | English | 釋義 · Definition |
|---|---|---|
| 區分 | Distinction | 標記差異的最底層動作 · the bottommost act of marking difference |
| 關聯 / 耦合 | Association / Coupling | 差異之間穩定的共同變動 · stable co-variation among differences |
| 壓縮 | Compression | 把穩定的下層組合折疊成一個上層變數 · folding a stable lower combination into one upper variable |
| 崩解 | Decompression / Collapse | 壓縮的逆運算；上層變數碎回下層 · the inverse of compression; an upper variable shatters back down |
| 臨界點 | Critical point | 系統對微擾極度敏感、分支發生之處 · where the system is hypersensitive and branching occurs |
| 程度 | Magnitude | 變數在量上的累積，逼近臨界 · a variable's quantitative buildup toward criticality |
| 能動性 | Agency | 高層反過來操作整座塔（含自身）的能力 · a high layer's capacity to operate the whole stack, itself included |
| 觀察標的 | Observational target | 因變動多元而不被固化成結構的現象 · a phenomenon too variable to be frozen into structure |
| 結構 | Structure | 穩定、可命名、構成引擎的零件 · the stable, nameable parts that make up the engine |
| 黏性 | Stickiness | 變數抵抗崩解的程度 · a variable's resistance to collapse |
| 就地 / 轉移 / 分布式壓縮 | In-place / Off-loaded / Distributed compression | 三種主體承載方式 · three ways the subject is carried |
| 湧現式 / 表徵式意義 | Emergent / Represented meaning | 意義的兩條生產路徑 · the two production routes of meaning |
| 規範邊界 | Normative boundary | 框架上界：不裁決價值對錯 · the upper wall: no adjudication of value |
| 奠基邊界 | Grounding boundary | 框架下界：不解釋為何存在 · the lower wall: no explanation of why anything exists |

---

# 作為 V2 行為準則的用法 · Using This as the V2 Charter

**中文**
這 21 條準則 + 公理 + 脊椎，是 Genesis V2「造世」時的行為準則。任何被造出的世界、任何被加入的機制，都必須通過三道檢查：(1) **脊椎 A**——它的每個上層變數都指得出可還原的主體嗎？(2) **公理**——它沒有把結構分類誤當成時間序列吧？(3) **兩道牆**——它有沒有僭越規範邊界（偷渡「應然」）或奠基邊界（假裝解釋了「為何存在」）？凡通過三道檢查者，方為合法的造世動作。

**English**
These 21 principles + axiom + spine are the behavioral charter for Genesis V2's act of world-generation. Any world built, any mechanism added, must pass three checks: (1) **Spine A** — does every upper variable point to a reducible subject? (2) **The Axiom** — has it avoided mistaking a structural taxonomy for a timeline? (3) **The Two Walls** — has it refrained from overstepping the normative boundary (smuggling in an "ought") or the grounding boundary (pretending to explain "why anything exists")? Whatever passes all three is a legitimate act of world-generation.

---

*Genesis — 造世方法論框架 · A Methodology for World-Generation*
*V1 世代總綱（V1.0–V1.5）· V1 Generation Specification (V1.0–V1.5)*
*開源初版草案 · Open-source initial draft*
