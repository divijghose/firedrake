Date and time 2025-05-07 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (interpolate, abstract reduced functionals, etc.)

# Agenda

Present:

Apologies: LC

## Discussion-worthy issues/PR

## KS: ufl.DAGTraverser

https://github.com/FEniCS/ufl/pull/365

## PB: Fix R space assembly

Recent changes in quadrature degree estimation broke assembly of mixed R-spaces on extruded meshes.

It seems like `kernel.info.coefficients` does not store split coefficients if we have an extruded mesh. Do we want to instead make sure that they are properly split?

https://github.com/firedrakeproject/firedrake/pull/4331

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


KS: Extract codim-1 submesh: https://github.com/firedrakeproject/firedrake/pull/4329


1600 UTC [2025-05-28](./Firedrake-meeting-2025-05-28)