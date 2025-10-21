Date and time 2025-10-21 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (LC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. LC: Add self to authors list

# Agenda

Present: DH, JHC, LC, AC, IM, CJW, PB, CJC, KS

Apologies:

## JHC: Pyadjoint `ReducedFunctionalMat` PETSc Mat for TAO

https://github.com/dolfin-adjoint/pyadjoint/pull/213

pyadjoint assumes that you are on finite dimensional Hilbert space.

ReducedFunctional is not necessarily scalar as Firedrake is not necessarily the last thing in computation.

Use RestrictedFunctionSpace?

Our current BC approach is fine for gradient decent (not very fine for eigensolver).

DH: ReducedFunctionalMatClass -> Should this (and other Mat classes) be a subclass of some abstract class that should be implemented in petsctools?

JHC: PCBase, too?

## CW: Retire the mailing list?

It is now just spam.

DH: We could remove, but DH would need to figure out how to.

## IPOPT

[pyadjoint228](https://github.com/dolfin-adjoint/pyadjoint/issues/228)

DH: It seems IPOPT returns some non-overloaded numpy array.

CW: Why did it start failing in 2025.10?

## CI

We currently have only 2 states: pass and fail.

Do we want a third state for some failure which we care less?

## Meeting next week

Wednesday

## Merge PRs

[SciPy Riesz map fix #230](https://github.com/dolfin-adjoint/pyadjoint/pull/230) -- Changes suggested.

[LinearEigensolver4634](https://github.com/firedrakeproject/firedrake/pull/4634) -- Merged.

## Date of next meeting

1600 UTC [2025-10-28](./Firedrake-meeting-2025-10-28)
