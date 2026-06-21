#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genesis Engine — MVP v3 (LIVING substrate)
==========================================

v2 fixed two things (substrate persists; diversity + indelibility) but left a
real logical flaw the user caught: the low level was DEAD. It was posited once
and then only coarse-grained upward -- it never grew or changed.

v3 makes the low level alive, faithful to the framework's own Steps 1-3
("D = potential-for-difference"; "distinction self-replicates"):

  - DISTINCTION (ongoing): each tick new L0 differences are born beside existing
    ones (same lineage). The substrate keeps being CREATED.
  - DISSIPATION (entropy): old, weakly-coupled free L0 differences fade. The
    substrate keeps CHANGING (turnover), and growth stays bounded.
  - RECRUITMENT: new differences are absorbed into nearby existing units, which
    also lose members to turnover. Units PERSIST THROUGH turnover -- which is
    what indelibility (P14) actually means: structure surviving while its
    substrate is replaced (a cell swaps molecules; an institution swaps people).

So: low level churns; high level is indelible THROUGH the churn; lineages stay
plural. Run:  python3 genesis_engine.py
"""
from __future__ import annotations
import math, random
from dataclasses import dataclass, field
from collections import Counter


@dataclass
class WorldSeed:
    feature_dim: int = 6
    n_mega: int = 3
    branch: int = 3
    mega_sep: float = 1.0
    spreads: tuple = (0.13, 0.037, 0.0106)
    point_noise: float = 0.003

    sim_sigma: float = 0.12
    relax: float = 1.6
    assoc_floor: float = 0.10
    association_gain: float = 0.34

    edge_min: float = 0.42
    compress_density: float = 0.36
    min_cluster_size: int = 3
    threshold_jitter: float = 0.05

    base_decay: float = 0.03
    layer_stick: float = 0.7
    dissolve_cohesion: float = 0.15
    support_boost: float = 0.04
    grace_ticks: int = 14

    # --- LIVING substrate (v3) ---
    birth_rate: int = 12           # new L0 differences born per tick (self-limiting below carrying)
    birth_noise: float = 0.006     # how far a newborn sits from its parent difference
    l0_min_age: int = 8            # free L0 can't dissipate before this
    l0_death_prob: float = 0.06    # per-tick chance a weak, aged, free L0 fades
    member_death_prob: float = 0.004  # slow turnover of bound L0 (the contents replace)
    recruit_sim: float = 0.45      # a free L0 this similar to an L1 unit is absorbed
    split_size: int = 8            # a unit this big proliferates by dividing (L1+ self-replication)
    layer_penalty: float = 0.09    # each higher fold is harder -> a NATURAL ceiling (no infinite tower)
    max_layer: int = 6             # hard ceiling: the framework has finitely many layers (L0..L5/6)
    carrying: int = 820            # substrate steady-state target (logistic births)

    ticks: int = 140


@dataclass
class Node:
    nid: int
    layer: int
    feature: list
    members: list = field(default_factory=list)
    parent: int = None
    cohesion: float = 1.0
    bind: float = 1.0
    age: int = 0
    exists: bool = True
    lineage: int = -1


class World:
    def __init__(self, seed: WorldSeed):
        self.s = seed
        self.rng = random.Random(11)
        self.nodes = {}
        self.couplings = {}
        self._id = 0
        self.tick = 0
        self.events = Counter()
        self._build()

    def _nid(self):
        i = self._id; self._id += 1; return i

    def _dist(self, a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def _key(self, a, b):
        return (a, b) if a < b else (b, a)

    def _rand_dir(self):
        v = [self.rng.gauss(0, 1) for _ in range(self.s.feature_dim)]
        n = math.sqrt(sum(x * x for x in v)) or 1e-9
        return [x / n for x in v]

    def _build(self):
        s = self.s
        megas, guard = [], 0
        while len(megas) < s.n_mega and guard < 100000:
            guard += 1
            c = [self.rng.random() for _ in range(s.feature_dim)]
            if all(self._dist(c, m) >= s.mega_sep for m in megas):
                megas.append(c)
        for idx, m in enumerate(megas):
            self._gen(m, 0, idx)

    def _gen(self, center, level, lin):
        s = self.s
        if level == len(s.spreads):
            for _ in range(s.branch):
                feat = [center[d] + self.rng.gauss(0, s.point_noise) for d in range(s.feature_dim)]
                nid = self._nid()
                self.nodes[nid] = Node(nid=nid, layer=0, feature=feat, lineage=lin)
            return
        for _ in range(s.branch):
            d = self._rand_dir()
            child = [center[k] + s.spreads[level] * d[k] for k in range(s.feature_dim)]
            self._gen(child, level + 1, lin)

    def existing(self):
        return [n for n in self.nodes.values() if n.exists]

    def frontier(self):
        return [n for n in self.nodes.values() if n.exists and n.parent is None]

    def _sim(self, a, b):
        d = self._dist(a.feature, b.feature)
        return math.exp(-(d * d) / (2 * self.s.sim_sigma ** 2))

    # --- D: ongoing distinction (the low level keeps being CREATED) --------
    def distinction(self):
        s = self.s
        live = sum(1 for n in self.nodes.values() if n.exists)
        n_new = int(round(s.birth_rate * max(0.0, 1 - live / s.carrying)))
        leaves = [n for n in self.nodes.values() if n.exists and n.layer == 0]
        if not leaves or n_new <= 0:
            return
        for _ in range(n_new):
            base = self.rng.choice(leaves)
            feat = [base.feature[d] + self.rng.gauss(0, s.birth_noise) for d in range(s.feature_dim)]
            nid = self._nid()
            self.nodes[nid] = Node(nid=nid, layer=0, feature=feat, lineage=base.lineage)
            self.events["born"] += 1

    def associate(self):
        s = self.s
        for k in list(self.couplings):
            self.couplings[k] *= (1 - s.base_decay)
            if self.couplings[k] < 0.02:
                del self.couplings[k]
        fr = self.frontier()
        for a in fr:
            cand, dmin = [], float('inf')
            for b in fr:
                if b is a or b.lineage != a.lineage:
                    continue
                sim = self._sim(a, b)
                if sim < s.assoc_floor:
                    continue
                d = self._dist(a.feature, b.feature)
                cand.append((d, sim, b))
                if d < dmin:
                    dmin = d
            cut = dmin * s.relax
            for d, sim, b in cand:
                if d <= cut:
                    k = self._key(a.nid, b.nid)
                    self.couplings[k] = min(1.0, self.couplings.get(k, 0.0) + s.association_gain * sim)

    def _clusters(self):
        s = self.s
        edge = s.edge_min + self.rng.uniform(-s.threshold_jitter, s.threshold_jitter)
        adj = {}
        for (a, b), w in self.couplings.items():
            if w < edge:
                continue
            na, nb = self.nodes[a], self.nodes[b]
            if not na.exists or na.parent is not None or not nb.exists or nb.parent is not None:
                continue
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)
        seen, out = set(), []
        for start in list(adj):
            if start in seen:
                continue
            stack, comp = [start], []
            while stack:
                x = stack.pop()
                if x in seen:
                    continue
                seen.add(x); comp.append(x)
                stack.extend(adj[x] - seen)
            if len(comp) >= s.min_cluster_size:
                out.append(comp)
        return out

    def _density(self, comp):
        n = len(comp)
        if n < 2:
            return 0.0
        cs = set(comp)
        pres = sum(w for (a, b), w in self.couplings.items() if a in cs and b in cs)
        return pres / (n * (n - 1) / 2)

    def compress(self):
        s = self.s
        for comp in self._clusters():
            target = max(self.nodes[i].layer for i in comp) + 1
            if target > s.max_layer:                      # natural ceiling: no infinite tower
                continue
            dens = self._density(comp)
            crit = (s.compress_density + s.layer_penalty * (target - 1)
                    + self.rng.uniform(-s.threshold_jitter, s.threshold_jitter))
            if dens >= crit and self.rng.random() < min(1.0, dens + 0.2):
                self._fold(comp, dens)

    def _fold(self, comp, dens):
        members = [self.nodes[i] for i in comp]
        layer = max(m.layer for m in members) + 1
        dim = len(members[0].feature)
        centroid = [sum(m.feature[d] for m in members) / len(members) for d in range(dim)]
        nid = self._nid()
        unit = Node(nid=nid, layer=layer, feature=centroid, members=comp[:],
                    cohesion=1.0, bind=min(1.0, dens), age=0, lineage=members[0].lineage)
        self.nodes[nid] = unit
        cs, ext = set(comp), {}
        for (a, b), w in list(self.couplings.items()):
            ina, inb = a in cs, b in cs
            if ina and inb:
                del self.couplings[(a, b)]
            elif ina or inb:
                o = b if ina else a
                ext[o] = max(ext.get(o, 0.0), w)
                del self.couplings[(a, b)]
        for o, w in ext.items():
            on = self.nodes[o]
            if on.exists and on.parent is None:
                self.couplings[self._key(nid, o)] = w
        for m in members:
            m.parent = nid
        self.events[f"fold->L{layer}"] += 1

    # --- recruitment: new differences feed into existing units -------------
    def recruit(self):
        s = self.s
        units = [n for n in self.frontier() if n.layer == 1]
        if not units:
            return
        by_lin = {}
        for u in units:
            by_lin.setdefault(u.lineage, []).append(u)
        for n in list(self.nodes.values()):
            if not n.exists or n.parent is not None or n.layer != 0:
                continue
            best, bs = None, 0.0
            for u in by_lin.get(n.lineage, ()):
                sim = self._sim(n, u)
                if sim > bs:
                    bs, best = sim, u
            if best and bs >= s.recruit_sim:
                n.parent = best.nid
                best.members.append(n.nid)
                self._refresh(best)
                best.cohesion = min(1.0, best.cohesion + 0.04)   # renewal strengthens (P14)
                self.events["recruit"] += 1

    def _refresh(self, unit):
        ms = [self.nodes[m] for m in unit.members if self.nodes[m].exists]
        if not ms:
            return
        for d in range(self.s.feature_dim):
            unit.feature[d] = sum(x.feature[d] for x in ms) / len(ms)

    # --- proliferation: units self-replicate by FISSION (the L1+ analog of
    #     L0's "distinction self-replicates"). Same generative function, one
    #     scale up: a unit that has grown enough divides into two (P9, P10/11
    #     on a size critical-point). Members are conserved (substrate persists).
    def proliferate(self):
        s = self.s
        for u in list(self.frontier()):
            if u.layer < 1:
                continue
            alive = [m for m in u.members if self.nodes[m].exists]
            if len(alive) >= s.split_size:
                self._split(u, alive)

    def _split(self, u, alive):
        s = self.s
        ms = [self.nodes[m] for m in alive]
        # divide along the axis of greatest internal spread (a natural cleavage plane)
        dim = max(range(s.feature_dim),
                  key=lambda d: max(m.feature[d] for m in ms) - min(m.feature[d] for m in ms))
        ms.sort(key=lambda m: m.feature[dim])
        half = len(ms) // 2
        g1, g2 = ms[:half], ms[half:]
        if len(g1) < s.min_cluster_size or len(g2) < s.min_cluster_size:
            return
        for g in (g1, g2):
            cent = [sum(m.feature[d] for m in g) / len(g) for d in range(s.feature_dim)]
            child = Node(nid=self._nid(), layer=u.layer, feature=cent,
                         members=[m.nid for m in g], cohesion=1.0, bind=u.bind,
                         age=0, lineage=u.lineage)
            self.nodes[child.nid] = child
            for m in g:
                m.parent = child.nid
        for k in [k for k in self.couplings if u.nid in k]:
            del self.couplings[k]
        u.exists = False
        self.events["split"] += 1

    # --- C-down + turnover -------------------------------------------------
    def decompress(self):
        s = self.s
        for n in self.frontier():
            n.age += 1
            if n.layer == 0 or not n.members:
                continue
            alive_m = [m for m in n.members if self.nodes[m].exists]
            n.members = alive_m
            if len(alive_m) < s.min_cluster_size:        # starved of substrate -> dissolve
                self._dissolve(n); continue
            support = sum(w for (a, b), w in self.couplings.items() if a == n.nid or b == n.nid)
            stick = (1 + s.layer_stick * n.layer) * (0.4 + 1.2 * n.bind)
            n.cohesion *= (1 - s.base_decay / stick)
            n.cohesion = min(1.0, n.cohesion + s.support_boost * support)
            if n.age > s.grace_ticks and n.cohesion < s.dissolve_cohesion:
                self._dissolve(n)

    def _dissolve(self, unit):
        for mid in unit.members:
            m = self.nodes[mid]
            if m.exists:
                m.parent = None; m.cohesion = 1.0; m.age = 0
        for k in [k for k in self.couplings if unit.nid in k]:
            del self.couplings[k]
        unit.exists = False
        self.events[f"collapse<-L{unit.layer}"] += 1

    # --- entropy at the bottom: free L0 turnover; bound L0 slow turnover ----
    def dissipate(self):
        s = self.s
        for n in list(self.nodes.values()):
            if not n.exists or n.layer != 0:
                continue
            if n.parent is None:                          # free differences age + may fade
                n.age += 1
                if n.age > s.l0_min_age and self.rng.random() < s.l0_death_prob:
                    sup = sum(w for (a, b), w in self.couplings.items() if a == n.nid or b == n.nid)
                    if sup < 0.3:
                        self._erase(n)
            else:                                         # bound differences slowly turn over
                if self.rng.random() < s.member_death_prob:
                    self._erase(n)

    def _erase(self, n):
        if n.parent is not None and n.parent in self.nodes:
            par = self.nodes[n.parent]
            if n.nid in par.members:
                par.members.remove(n.nid)
        for k in [k for k in self.couplings if n.nid in k]:
            del self.couplings[k]
        n.exists = False
        self.events["dissipate"] += 1

    def agency(self):
        for n in self.frontier():
            if n.layer >= 1 and n.nid in self._trans(n.nid):
                return True
        return False

    def _trans(self, nid, seen=None):
        seen = seen if seen is not None else set()
        for m in self.nodes[nid].members:
            if m in self.nodes and m not in seen:
                seen.add(m); self._trans(m, seen)
        return seen

    def layer_hist(self):
        return Counter(n.layer for n in self.existing())

    def lineage_count(self):
        return len(set(n.lineage for n in self.frontier() if n.layer >= 1))

    def step(self):
        self.tick += 1
        self.distinction()   # D: low level keeps being created
        self.associate()
        self.compress()
        self.recruit()       # new differences feed existing structure
        self.proliferate()   # units self-replicate by fission (L1+ proliferation)
        self.decompress()    # turnover + indelibility check
        self.dissipate()     # entropy at the bottom

    def run(self):
        for t in range(self.s.ticks):
            self.step()
            if t % 14 == 0 or t == self.s.ticks - 1:
                h = self.layer_hist()
                tot = sum(h.values())
                desc = " ".join(f"L{L}:{h[L]}" for L in sorted(h))
                print(f"t{t:>3} | {desc:<30} | tallest L{max(h) if h else 0} "
                      f"| lineages {self.lineage_count()} | live {tot} | created {self._id}")


def main():
    s = WorldSeed()
    w = World(s)
    print("=" * 76)
    print("Genesis Engine MVP v3  |  LIVING substrate: born / churns / persists through turnover")
    print("=" * 76)
    w.run()
    h = w.layer_hist()
    print("-" * 76)
    print(f"tallest layer         : L{max(h) if h else 0}")
    print(f"lineages (diversity)  : {w.lineage_count()}")
    print(f"live nodes (end)      : {sum(h.values())}   |  total ever created: {w._id}")
    print(f"L0 born / dissipated  : {w.events.get('born',0)} / {w.events.get('dissipate',0)}  "
          f"(low level is alive: created AND turned over)")
    print(f"folds / collapses     : {sum(v for k,v in w.events.items() if k.startswith('fold'))}"
          f" / {sum(v for k,v in w.events.items() if k.startswith('collapse'))}")
    print(f"recruited into units  : {w.events.get('recruit',0)}  (units refresh their substrate)")
    print(f"agency (P19)          : {w.agency()}")


if __name__ == "__main__":
    main()
