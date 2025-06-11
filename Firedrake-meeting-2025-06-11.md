Date and time 2025-06-11 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/)) **CW: PROGRESS!**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (interpolate, abstract reduced functionals, etc.)
1. CW: Preliminary prep for PETSc User Meeting 2026 ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-05-28))

# Agenda

Present:

Apologies:

## CW: PETSc user meeting

PETSc are happy with the suggested dates (1-5 June 2026).

DH: Can not announce date yet, but put up webpage with minimum amount of information.

CW: PETSc the begining of the week, Firedrake the end of the week?

## CW: Add Firedrake 25 to website

GW is asking for something official to point to so he can start his travel clearance procedure.

CW: Ask Onno about the website.

## CW: should we stop using our UFL fork?

https://github.com/firedrakeproject/firedrake/pull/4344

Yes.

## CW: petsctools

* petsctools: https://github.com/firedrakeproject/petsctools
* Firedrake PR: https://github.com/firedrakeproject/firedrake/pull/4194

JM wants to use it in pyadjoint but thinks the license might need to change.

DH: GPL does not propagate when distributing.

DH: Would put MIT on everything where possible.

DH: Expecting something like "Copyright (c) 2012. Imperial College London and others."

## Discussion-worthy issues/PR

### LC: ([#4341](https://github.com/firedrakeproject/firedrake/pull/4341)) Vom to vom permutation matrix

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [ASM extruded periodic](https://github.com/firedrakeproject/firedrake/pull/4352) already approved

PB: [Fix typo in test](https://github.com/firedrakeproject/firedrake/pull/4359) already approved

PB: [Matfree SLATE dual fix](https://github.com/firedrakeproject/firedrake/pull/4360) already approved

PB: ~[Demo](https://github.com/firedrakeproject/firedrake/pull/4309) was previously failing doc build for legit reason, now it is the usual broken link~ Merged

PB + KK: [EquationBC + multigrid](https://github.com/firedrakeproject/firedrake/pull/4338) needs review, Name change requested, changed, approved.

KS: UFL CoefficientSplitter https://github.com/FEniCS/ufl/pull/341 Ask if it is ok to merge this on FEniCS channel.

KS: Firedrake counterpart https://github.com/firedrakeproject/firedrake/pull/4349 Changes requested.

PB: ~[DirichletBC bugfix](https://github.com/firedrakeproject/firedrake/pull/4370) needs review but very simple~ Merged

## PETSC link 403 error?

Ask Satish about it?

## Next week

DH: Will not join the meeting next week.

## Date of next meeting

1600 UTC [2025-06-18](./Firedrake-meeting-2025-06-18)
