#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genesis — a world on real chemistry  (now with the REAL element roster)
=======================================================================

L0 now runs on the actual element shortlist derived in the V2 investment
analysis, sorted by the four roles we established:

  LIFE (CHONPS)  -- do real covalent chemistry, build molecules:
        C,H,O,N,P,S   (carbon=quality, phosphorus=rate; now complete)
  CATALYST (metals) -- present, heavy, and they LOWER the local bonding
        barrier (enzymes' active centres):  Fe, Mg, Zn, Mo
  FILLER (structure) -- present, inert, heavy, the "rock":  Si, (Fe doubles)
  BATTERY (radioactive) -- present, very heavy, sink to the core; Earth's
        internal heat source:  K, U, Th

Only LIFE atoms bond (valence>0). Catalysts boost nearby bonding. Filler and
battery atoms are inert markers that still feel gravity (stratification).

L0 atoms -> L1 molecules -> L2 compartments, on a thermal field.
Run:  python3 genesis_world.py
"""
from __future__ import annotations
import math, random
from collections import Counter

# element -> (valence, electronegativity, mass, role)
ELEMENTS = {
    # LIFE -- real covalent chemistry
    'H': (1, 2.20,   1, 'life'),
    'C': (4, 2.55,  12, 'life'),
    'N': (3, 3.04,  14, 'life'),
    'O': (2, 3.44,  16, 'life'),
    'P': (5, 2.19,  31, 'life'),   # phosphate backbone -- the rate-limiter
    'S': (2, 2.58,  32, 'life'),   # thiols / disulfides -- proteins
    # CATALYST -- inert to covalent bonding here, but boost nearby bonding
    'Fe': (0, 1.83, 56, 'catalyst'),
    'Mg': (0, 1.31, 24, 'catalyst'),
    'Zn': (0, 1.65, 65, 'catalyst'),
    'Mo': (0, 2.16, 96, 'catalyst'),
    # FILLER -- inert structural rock
    'Si': (0, 1.90, 28, 'filler'),
    # BATTERY -- inert, very heavy, radioactive heat
    'K':  (0, 0.82, 39, 'battery'),
    'U':  (0, 1.38, 238, 'battery'),
    'Th': (0, 1.30, 232, 'battery'),
}


class Atom:
    __slots__ = ('el', 'val', 'chi', 'mass', 'role', 'x', 'y', 'vx', 'vy', 'bonds')
    def __init__(self, el, x, y):
        v, chi, m, role = ELEMENTS[el]
        self.el = el; self.val = v; self.chi = chi; self.mass = m; self.role = role
        self.x, self.y = x, y
        self.vx = self.vy = 0.0
        self.bonds = {}
    @property
    def used(self): return sum(self.bonds.values())
    @property
    def free(self): return self.val - self.used


class GenesisWorld:
    def __init__(self, composition, box=1.0, seed=7, gravity=0.011):
        self.rng = random.Random(seed)
        self.box = box; self.g = gravity; self.atoms = []; self.T = 1.0
        self.r_bond = 0.045; self.r_agg = 0.085; self.tick = 0
        for el, n in composition.items():
            for _ in range(n):
                self.atoms.append(Atom(el, self.rng.random()*box, self.rng.random()*box))

    def _d(self, a, b): return math.hypot(a.x-b.x, a.y-b.y)
    def _form_prob(self): return 0.55 * max(0.0, 1 - self.T)
    def _promote_prob(self): return 0.30 * max(0.0, 1 - self.T)
    def _break_prob(self, order): return 0.45 * self.T * self.T / (order * order)

    def step(self):
        self.tick += 1
        cell = self.r_bond
        amp = 0.02 * math.sqrt(max(self.T, 0.02))
        for a in self.atoms:
            a.vx += self.rng.uniform(-amp, amp); a.vy += self.rng.uniform(-amp, amp)
            a.vy += self.g * math.log(a.mass + 1) * 0.12
        for a in self.atoms:
            for bid, order in a.bonds.items():
                b = self.atoms[bid]
                dx, dy = b.x-a.x, b.y-a.y; d = math.hypot(dx, dy) or 1e-9
                f = (d - self.r_bond*(0.62-0.05*order)) * 0.28
                a.vx += dx/d*f; a.vy += dy/d*f
        for a in self.atoms:
            a.vx *= 0.6; a.vy *= 0.6; a.x += a.vx; a.y += a.vy
            if a.x < 0 or a.x > 1: a.vx *= -1; a.x = min(max(a.x, 0), 1)
            if a.y < 0 or a.y > 1: a.vy *= -1; a.y = min(max(a.y, 0), 1)
        for i, a in enumerate(self.atoms):
            for bid in list(a.bonds):
                if bid > i:
                    o = a.bonds[bid]
                    if self.rng.random() < self._break_prob(o):
                        o -= 1
                        if o <= 0: del a.bonds[bid]; del self.atoms[bid].bonds[i]
                        else: a.bonds[bid] = o; self.atoms[bid].bonds[i] = o
        cat = self._catalysis(cell)
        fp = self._form_prob()
        grid = {}
        for i, a in enumerate(self.atoms):
            grid.setdefault((int(a.x/cell), int(a.y/cell)), []).append(i)
        for i, a in enumerate(self.atoms):
            if a.free <= 0: continue
            gx, gy = int(a.x/cell), int(a.y/cell)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for j in grid.get((gx+dx, gy+dy), ()):
                        if j <= i: continue
                        b = self.atoms[j]
                        if b.free <= 0 or j in a.bonds: continue
                        if self._d(a, b) <= self.r_bond:
                            p = fp * (1 + cat.get((gx, gy), 0.0))
                            if self.rng.random() < min(0.95, p):
                                a.bonds[j] = 1; b.bonds[i] = 1
                                if a.free <= 0: break
        pp = self._promote_prob()
        for i, a in enumerate(self.atoms):
            for bid in list(a.bonds):
                if bid > i and a.free > 0 and self.atoms[bid].free > 0:
                    if a.bonds[bid] < 3 and self.rng.random() < pp:
                        a.bonds[bid] += 1; self.atoms[bid].bonds[i] += 1

    def _catalysis(self, cell):
        field = {}
        # complete molecules self-template (Step 15)
        for comp in self.molecules():
            if len(comp) > 1 and all(self.atoms[i].free == 0 for i in comp):
                cx = sum(self.atoms[i].x for i in comp)/len(comp)
                cy = sum(self.atoms[i].y for i in comp)/len(comp)
                k = (int(cx/cell), int(cy/cell)); field[k] = field.get(k, 0.0) + 0.6
        # CATALYST metals lower the local bonding barrier (enzymes' active centres)
        for a in self.atoms:
            if a.role == 'catalyst':
                k = (int(a.x/cell), int(a.y/cell)); field[k] = field.get(k, 0.0) + 0.9
        return field

    def molecules(self):
        n = len(self.atoms); seen = [False]*n; mols = []
        for i in range(n):
            if seen[i]: continue
            stack, comp = [i], []
            while stack:
                x = stack.pop()
                if seen[x]: continue
                seen[x] = True; comp.append(x)
                for b in self.atoms[x].bonds:
                    if not seen[b]: stack.append(b)
            mols.append(comp)
        return mols

    def _formula(self, comp):
        c = Counter(self.atoms[i].el for i in comp); s = ''
        for el in ('C', 'H', 'N', 'O', 'P', 'S'):
            if c[el]: s += el + (str(c[el]) if c[el] > 1 else '')
        return s

    def compartments(self):
        mols = [m for m in self.molecules() if len(m) > 1]
        cents = [(sum(self.atoms[i].x for i in m)/len(m), sum(self.atoms[i].y for i in m)/len(m)) for m in mols]
        n = len(cents); seen = [False]*n; out = []
        for i in range(n):
            if seen[i]: continue
            stack, grp = [i], []
            while stack:
                x = stack.pop()
                if seen[x]: continue
                seen[x] = True; grp.append(x)
                for j in range(n):
                    if not seen[j] and math.hypot(cents[x][0]-cents[j][0], cents[x][1]-cents[j][1]) <= self.r_agg:
                        stack.append(j)
            if len(grp) >= 3: out.append(grp)
        return out

    def census(self):
        cc = Counter(); free = 0; complete = 0
        for comp in self.molecules():
            if len(comp) == 1:
                if self.atoms[comp[0]].role == 'life': free += 1
                continue
            if all(self.atoms[i].free == 0 for i in comp): complete += 1
            cc[self._formula(comp)] += 1
        return cc, free, complete

    def role_strat(self):
        out = {}
        for role in ('life', 'catalyst', 'filler', 'battery'):
            ys = [a.y for a in self.atoms if a.role == role]
            out[role] = sum(ys)/len(ys) if ys else 0
        return out


def main():
    comp = {
        'H': 90, 'O': 28, 'C': 18, 'N': 14, 'P': 4, 'S': 4,      # life: CHONPS
        'Fe': 4, 'Mg': 3, 'Zn': 2, 'Mo': 1,                      # catalysts
        'Si': 6,                                                 # filler
        'K': 3, 'U': 1, 'Th': 1,                                 # battery
    }
    w = GenesisWorld(comp, box=1.0, seed=7, gravity=0.011)
    n = len(w.atoms)
    print("=" * 80)
    print("Genesis world on the REAL element roster | LIFE=CHONPS, +catalyst/filler/battery")
    print(f"L0 atoms: {n}  |  life chemistry + metal catalysis + gravity stratification")
    print("=" * 80)

    def temp_at(t):
        if t < 45: return 1.0 - 0.95*(t/45)
        if t < 120: return 0.05
        return min(1.0, 0.05 + 0.95*((t-120)/40))

    for t in range(170):
        w.T = temp_at(t); w.step()
        if t in (0, 44, 80, 119, 169):
            cc, free, complete = w.census(); comps = w.compartments()
            top = ", ".join(f"{f}x{n}" for f, n in cc.most_common(7))
            rs = w.role_strat()
            print(f"t{t:>3} T={w.T:.2f} | L1 mol={sum(cc.values()):>3} complete={complete:>3} "
                  f"L2 comp={len(comps):>2}")
            print(f"           census: {top}")
            print(f"           strat y (low=top): life={rs['life']:.2f} catalyst={rs['catalyst']:.2f} "
                  f"filler={rs['filler']:.2f} battery={rs['battery']:.2f}")
    print("-" * 80)
    print("Reading: CHONPS now complete (P=phosphate rate-limiter, S=thiols); metals")
    print("catalyse nearby bonds; heavy battery (U/Th) sinks deepest -- a layered world.")


if __name__ == "__main__":
    main()
