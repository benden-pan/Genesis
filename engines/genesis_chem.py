#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Benden Pan · CC BY 4.0 · first published 2026-06
"""
Genesis — formal science at L0/L1 : valence chemistry on a thermal field
========================================================================

This grounds the Genesis L0->L1 operations in REAL chemistry + thermodynamics,
replacing the abstract feature-vector substrate:

  L0 = atoms           : each has an element, a valence (free bonds it wants),
                         a position, and thermal motion.
  A  = chemical bonding : two atoms bond if close, both have free valence, and
                          it is cold enough (a bond is a relation, P2).
  C^ = molecule        : a bonded cluster with ALL valences satisfied folds into
                          an L1 unit -- a molecule (naming-rights from stability, P3).
  Cv = thermal break   : a bond dissociates when hot (decompression, P13).
  Energy gradient/T    : the source + the critical points (P10/P11; narrative Step 2).

Cooling a hot soup of H/O/C/N should self-assemble a recognizable *reducing
atmosphere*: H2O, CH4, NH3, H2 ... (the chemistry of the early Earth).

Run:  python3 genesis_chem.py
"""
from __future__ import annotations
import math, random
from collections import Counter

# a tiny periodic table: element -> (valence = single bonds, electronegativity)
ELEMENTS = {'H': (1, 2.20), 'O': (2, 3.44), 'N': (3, 3.04), 'C': (4, 2.55)}

class Atom:
    __slots__ = ('el', 'val', 'chi', 'x', 'y', 'vx', 'vy', 'bonds')
    def __init__(self, el, x, y):
        self.el = el
        self.val, self.chi = ELEMENTS[el]
        self.x, self.y = x, y
        self.vx = self.vy = 0.0
        self.bonds = set()          # ids of bonded atoms
    @property
    def free(self):
        return self.val - len(self.bonds)


class ChemWorld:
    def __init__(self, composition, box=1.0, seed=7):
        self.rng = random.Random(seed)
        self.box = box
        self.atoms = []
        self.T = 1.0                # normalized temperature (1 = hot, 0 = cold)
        for el, n in composition.items():
            for _ in range(n):
                self.atoms.append(Atom(el, self.rng.random()*box, self.rng.random()*box))
        self.r_bond = 0.045
        self.tick = 0

    def _d(self, a, b):
        dx, dy = a.x-b.x, a.y-b.y
        return math.hypot(dx, dy)

    def _form_prob(self):   # cold -> bonds form (P2 association favoured when calm)
        return 0.55 * max(0.0, 1 - self.T)
    def _break_prob(self):  # hot -> bonds dissociate (P13 thermal decompression)
        return 0.45 * self.T * self.T

    def step(self):
        self.tick += 1
        n = len(self.atoms)
        idx = {id(a): i for i, a in enumerate(self.atoms)}
        # --- thermal motion; bonded atoms stay close (spring) ---
        amp = 0.02 * math.sqrt(max(self.T, 0.02))
        for a in self.atoms:
            a.vx += self.rng.uniform(-amp, amp); a.vy += self.rng.uniform(-amp, amp)
        for a in self.atoms:
            for bid in a.bonds:
                b = self.atoms[bid]
                dx, dy = b.x-a.x, b.y-a.y
                d = math.hypot(dx, dy) or 1e-9
                f = (d - self.r_bond*0.7) * 0.25
                a.vx += dx/d*f; a.vy += dy/d*f
        for a in self.atoms:
            a.vx *= 0.6; a.vy *= 0.6
            a.x += a.vx; a.y += a.vy
            if a.x < 0 or a.x > self.box: a.vx *= -1; a.x = min(max(a.x, 0), self.box)
            if a.y < 0 or a.y > self.box: a.vy *= -1; a.y = min(max(a.y, 0), self.box)
        # --- C-down: thermal bond breaking ---
        bp = self._break_prob()
        for i, a in enumerate(self.atoms):
            for bid in list(a.bonds):
                if bid > i:  # each bond once
                    if self.rng.random() < bp:
                        a.bonds.discard(bid); self.atoms[bid].bonds.discard(i)
        # --- A: bonding (valence + proximity + cold) ---
        fp = self._form_prob()
        # spatial bucketing for speed
        cell = self.r_bond
        grid = {}
        for i, a in enumerate(self.atoms):
            key = (int(a.x/cell), int(a.y/cell))
            grid.setdefault(key, []).append(i)
        for i, a in enumerate(self.atoms):
            if a.free <= 0: continue
            gx, gy = int(a.x/cell), int(a.y/cell)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for j in grid.get((gx+dx, gy+dy), ()):
                        if j <= i: continue
                        b = self.atoms[j]
                        if b.free <= 0 or j in a.bonds: continue
                        if self._d(a, b) <= self.r_bond and self.rng.random() < fp:
                            a.bonds.add(j); b.bonds.add(i)
                            if a.free <= 0: break

    # --- C-up: identify molecules (L1 units) = bonded clusters -------------
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

    def census(self):
        comp_count = Counter()
        free_atoms = 0
        complete = 0
        for comp in self.molecules():
            if len(comp) == 1:
                free_atoms += 1
                continue
            satisfied = all(self.atoms[i].free == 0 for i in comp)
            if satisfied:
                complete += 1
            formula = self._formula(comp)
            comp_count[formula] += 1
        return comp_count, free_atoms, complete

    def _formula(self, comp):
        c = Counter(self.atoms[i].el for i in comp)
        order = ['C', 'H', 'N', 'O']  # Hill-ish ordering
        s = ''
        for el in order:
            if c[el]:
                s += el + (str(c[el]) if c[el] > 1 else '')
        for el in c:
            if el not in order:
                s += el + (str(c[el]) if c[el] > 1 else '')
        return s


def main():
    # a reducing mix (lots of hydrogen), like a primordial atmosphere
    world = ChemWorld({'H': 110, 'O': 34, 'C': 28, 'N': 30}, box=1.0, seed=7)
    print("=" * 72)
    print("Genesis — formal chemistry at L0/L1  (H/O/C/N, cooling then reheating)")
    print(f"L0 atoms: {len(world.atoms)}   |  A=bonding  C^=molecule  Cv=thermal break")
    print("=" * 72)

    # temperature schedule: hot -> cool -> hold cold -> reheat
    def temp_at(t):
        if t < 40:   return 1.0 - 0.95 * (t/40)      # cool from hot to cold
        if t < 90:   return 0.05                       # hold cold (chemistry settles)
        return min(1.0, 0.05 + 0.95 * ((t-90)/40))    # reheat

    for t in range(150):
        world.T = temp_at(t)
        world.step()
        if t in (0, 20, 39, 65, 89, 115, 149):
            cc, free, complete = world.census()
            top = ", ".join(f"{f}x{n}" for f, n in cc.most_common(6))
            print(f"t{t:>3} T={world.T:.2f} | molecules(L1)={sum(cc.values()):>3} "
                  f"complete={complete:>3} freeAtoms(L0)={free:>3}")
            print(f"            census: {top}")
    print("-" * 72)
    print("Reading: cold -> atoms (L0) bond into molecules (L1); heat -> they break")
    print("back to atoms. C^ and Cv here are REAL chemistry, not abstract clustering.")


if __name__ == "__main__":
    main()
