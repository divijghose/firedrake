Date and time 2024-09-25 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))

# Agenda

Present: JB, JHC, IM, RK

Apologies: CW

## JB: ARCHER2 Capability day is a painful experience
JHC: Agreed!

## JB: mpi4py update
PR [#3777](https://github.com/firedrakeproject/firedrake/pull/3777) will unpin `mpi4py==3.1.6`, this will be an issue for anyone still running MPI-3 (cough ARCHER2). However, it is believed this is only advanced use cases. `mpi4py>4.0` brings us one step closer to wheel. We should transition over to using wheels (for dependencies) bit by bit, rather than all at once.

## RK: Demos update
New student will add Irksome to the existing demos.

JB: Possible demos hackathon in the future, watch this space.

RK: Where should ideas for new demos go?

JB: Open an issue

Some ideas discussed:
- Exotic elements
- FML
- PatchPC/ASM
- External operator

Possible documentation sprint for Firedrake?

RK will be in the UK in Spring 2025.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*
- [#3778](https://github.com/firedrakeproject/firedrake/pull/3778) Remove ML frameworks from vanilla container. Merged
- [#3725](https://github.com/firedrakeproject/firedrake/pull/3725) Fix ensemble tests. Changes applied.

# Date of next meeting
1600 BST (1500 UTC) [2024-10-02](./Firedrake-meeting-2024-10-02)