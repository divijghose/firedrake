Date and time 2021-01-13 16:00UTC (16:00GMT)

# Action Items
~1. Pick Chair and Minuter.~
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: LM, JB, SV, SK, PHJK, KS, RNH, CW, TG, DAH, RCK

Apologies: NB

## JB

Can someone test 3.9 fixes on MacOS: yes TG will do so.

## Status updates

LM: Teaching, teaching, teaching...

JB: scaling runs on Isambard (alfi solver). Reasonable looking strong scaling. Coarse grid synchronisation is the major bottleneck right now.

KS: firedrake-IO. Working on petsc side right now, for serialisation of sections (petsc's idea of a functionspace).

RNH: interpolation onto a point cloud. Long dependency list (partly finat stuff). At the moment, trying to get the adjoint stuff for hessians for interpolate. This book (Imperial has access) is probably useful for the theory: https://doi.org/10.1137/1.9781611972078

SK: Ocean-flow under iceshelves (with variable-layer meshes); Stokes for geodynamics (with Rhodri [ANU]), needs near nullspaces through FS (petsc support not complete?)

PHJK: Busy teaching

CW: Profiling solves in the small problem limit and squashing annoying bugs where we're doing stupid things.

TG: Mostly writing, more analysis of the Gopalakrishnan & Tan non-nested MG for the SW case.

SV: local matrix-free slate. has been getting local solver ready (algorithm side). then slate rewrites for expressions for minimum complexity application. Refactoring order in which slate assembly calls are interleaved with the expressions in the compiler.

DAH: Teaching, admin, ...

DRS: Icepack paper submitted to GMD. Proposal to NASA went in (mostly applications, some code improvements) with RCK.

RCK: Paper revisions (irksome, nonlocal BCs for helmholtz). NASA proposal includes "element oracle" stuff, first stab at macro elements. Patch smoothers for serendipity (with Jorge Menendez) -> Copper Mountain.

## Hessian stuff

RNH: notes that Function.assign(...) has the wrong Hessian in adjoint mode.

## Merge PRs:

Did a bunch of this.

## AOB


## Date of next meeting

[2021-01-20](./Firedrake-meeting-2021-01-20) 16:00UTC (16:00GMT)
