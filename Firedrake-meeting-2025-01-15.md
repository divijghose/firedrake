Date and time 2025-01-15 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: Fix artefactsv3 issue
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: DH, DD, IM, AO, PB, RK, CW, LC, KS

Apologies:

## Firedrake 25

DH, KS, CW, PB, FA are (at least) going.

## Meeting with Matt in Buffalo before Firedrake 25: 

DH, KS: Unify PETSc/Firedrake coordinates,

CW: Deal with a single PETSc commit that Firedrake is carrying.

## PB: [FIAT CR](https://github.com/firedrakeproject/fiat/pull/118)

RK: Only works with odd order

DH: What happens if we pass order=2?

PB: Value error.

Merged

## CCP

Host use-case-based Hackathon in Exeter after Easter (hosted by Jemma).

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: ~[Firedrake ASM stats](https://github.com/firedrakeproject/firedrake/pull/3875)~ Merged

PB: ~[FIAT HDivTrace](https://github.com/firedrakeproject/fiat/pull/117)~ Merged

PB: ~[Firedrake CR](https://github.com/firedrakeproject/firedrake/pull/3969)~ Merged

PB: [FIAT cell caching](https://github.com/firedrakeproject/fiat/pull/128) Changes requested

JM: [Adjoint](https://github.com/firedrakeproject/firedrake/pull/3965) Need to fix test report -> Run adjoint tests

Action All:

Come back to:

[JM](https://github.com/firedrakeproject/firedrake/pull/3965)

[JM](https://github.com/firedrakeproject/firedrake/pull/3939)

Action KS:

Rebase [hex](https://github.com/firedrakeproject/firedrake/pull/3878)

# Date of next meeting
1600 UTC [2025-01-22](./Firedrake-meeting-2025-01-22)