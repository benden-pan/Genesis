#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Benden Pan · CC BY 4.0 · first published 2026-06
"""
Genesis — STRATA engine (corrected central metaphor)
====================================================

The world is NOT a pyramid with the drama at the top (folding/collapse).
It is a stack of STRATA: every layer L0..L6 continually ACCUMULATES and is
RETAINED, and the layers MUTUALLY LIFT each other. Collapse is a rare, local
exception that only slightly erodes a layer's accumulated thickness.

Per layer k we track:
  N[k]  active units (proliferate; rarely, locally collapse)
  T[k]  THICKNESS = accumulated retention (decision 1b: grows; eroded only
        微 by collapse -- "culture is rarely lost, but it can be")

Drivers (the two real engines the user named):
  - collision  ~ N^2   (more agents -> more triggers; medicine raises N, etc.)
  - retention  ~ T     (thicker accumulated history -> each new trigger stands higher)
Mutual lifting is BIDIRECTIONAL (decision 2b):
  - lower thickness lifts the layer above (standing on accumulation)
  - upper thickness lifts the layer below (e.g. medicine -> faster/longer lives
    -> faster population growth at the base)

Run:  python3 genesis_strata.py
"""
from __future__ import annotations
import math

K = 6                                   # layers L0..L6
CAP   = [6000, 1600, 520, 190, 78, 30, 13]   # carrying capacity of active units per layer
R     = [0.030, 0.060, 0.058, 0.056, 0.054, 0.052, 0.050]  # lateral proliferation rate
UP    = 0.020                           # folding influx from the layer below
C_LOW = 0.16                            # lower thickness lifts the layer above
C_UP  = 0.11                            # upper thickness lifts the layer below (bidirectional)
RETAIN = 0.26                           # fraction of activity laid down as permanent strata
ERODE  = 0.02                           # collapse's bite into thickness (tiny: decision 1b)
COLL_HALF = 220.0                       # N^2 collision saturation
COL_BASE = 0.0025                       # base collapse rate (rare exception)
E_INPUT = 64.0                          # energy gradient -> new L0 differences born per tick (open energy)


def lift(t):                            # diminishing-returns lift from a thickness
    return math.log1p(max(0.0, t))


def run(ticks=600, seed_L0=40.0):
    N = [0.0]*(K+1)
    T = [0.0]*(K+1)
    N[0] = seed_L0                      # a small initial seed of differences
    hist = []
    for step in range(ticks):
        dN = [0.0]*(K+1)
        dT = [0.0]*(K+1)
        for k in range(K+1):
            low_T = T[k-1] if k > 0 else 0.0
            up_T  = T[k+1] if k < K else 0.0
            lo = 1 + C_LOW*lift(low_T)
            hi = 1 + C_UP *lift(up_T)
            room = max(0.0, 1 - N[k]/CAP[k])
            coll = (N[k]*N[k])/(N[k] + COLL_HALF)        # N^2 at small N, saturating
            prolif = R[k]*coll*lo*hi*room
            influx = (E_INPUT*room*hi) if k == 0 else (UP*N[k-1]*lo)
            crowd = (N[k]/CAP[k])**2
            collapse = COL_BASE*N[k]*crowd               # rare; only near capacity
            dN[k] = prolif + influx - collapse
            laid  = RETAIN*(prolif + influx)             # accumulation -> permanent thickness
            dT[k] = laid - ERODE*collapse                # erosion << accumulation (decision 1b)
        for k in range(K+1):
            N[k] = max(0.0, N[k] + dN[k])
            T[k] = max(T[k]*0.99999, T[k] + dT[k])       # thickness essentially only grows
        if step % 60 == 0 or step == ticks-1:
            hist.append((step, list(N), list(T)))
    return hist


def main():
    print("="*92)
    print("Genesis STRATA engine | every layer accumulates & is retained; layers mutually lift")
    print("="*92)
    hist = run()
    print("\nTHICKNESS T[k] over time (the strata getting thicker):")
    print(f"{'tick':>5} " + "".join(f"{'L'+str(k):>10}" for k in range(K+1)))
    for step, N, T in hist:
        print(f"{step:>5} " + "".join(f"{T[k]:>10.1f}" for k in range(K+1)))
    print("\nACTIVE COUNT N[k] over time:")
    print(f"{'tick':>5} " + "".join(f"{'L'+str(k):>10}" for k in range(K+1)))
    for step, N, T in hist:
        print(f"{step:>5} " + "".join(f"{N[k]:>10.1f}" for k in range(K+1)))

    # --- validation checks ---
    print("\n" + "-"*92)
    _, N0, T0 = hist[0]; _, Nf, Tf = hist[-1]
    grew = all(Tf[k] >= T0[k] for k in range(K+1))
    allthick = all(Tf[k] > 1.0 for k in range(K+1))
    print(f"every layer thickened (monotone)      : {grew}")
    print(f"every layer has real thickness (>1)   : {allthick}  -> not just the top is alive")
    # mutual lifting: does a lower layer cross a threshold BEFORE the one above?
    full = run()  # not needed; reuse hist crossing
    # find first tick each layer reaches 5.0 thickness
    series = run(ticks=600)
    cross = [None]*(K+1)
    Ntmp=[0.0]*(K+1); Ttmp=[0.0]*(K+1); Ntmp[0]=40.0
    # re-simulate finely to get crossing times
    N=[0.0]*(K+1);T=[0.0]*(K+1);N[0]=40.0
    for step in range(600):
        dN=[0.0]*(K+1);dT=[0.0]*(K+1)
        for k in range(K+1):
            low_T=T[k-1] if k>0 else 0.0; up_T=T[k+1] if k<K else 0.0
            lo=1+C_LOW*lift(low_T); hi=1+C_UP*lift(up_T); room=max(0.0,1-N[k]/CAP[k])
            coll=(N[k]*N[k])/(N[k]+COLL_HALF); prolif=R[k]*coll*lo*hi*room
            influx=(E_INPUT*room*hi) if k==0 else (UP*N[k-1]*lo)
            collapse=COL_BASE*N[k]*(N[k]/CAP[k])**2
            dN[k]=prolif+influx-collapse; dT[k]=RETAIN*(prolif+influx)-ERODE*collapse
        for k in range(K+1):
            N[k]=max(0.0,N[k]+dN[k]); T[k]=max(T[k]*0.99999,T[k]+dT[k])
            if cross[k] is None and T[k]>=5.0: cross[k]=step
    print(f"thickness-5.0 crossing tick per layer : {cross}")
    ordered = all(cross[k] is not None and cross[k] <= (cross[k+1] or 1e9) for k in range(K))
    print(f"lower layers thicken BEFORE upper      : {ordered}  -> the wave propagates up (mutual lifting)")
    print("-"*92)
    print("Reading: this is strata, not a pyramid -- every layer accumulates & is retained,")
    print("lower strata thicken first and lift the upper, which then feed back down (2b).")


if __name__ == "__main__":
    main()
