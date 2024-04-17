Date and time 2024-04-17 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto
1. JB: build numpy release candidate (CW: I [did this](https://github.com/firedrakeproject/firedrake/pull/3290), but we should maybe wait to use actual releases instead of release candidates before merging?)

# Notices
1. Submit abstract for PDESoft 1-3 July 2024, Cambridge, UK [PDESoft](https://pdesoft.org) (Registration early 28th March/late 31st May, Abstracts 17th May)
1. PETSc User Meeting 23-24 May 2024 Cologne, Germany [PETSc User Meeting](https://cds.uni-koeln.de/en/workshops/petsc-2024/registration) (Registration and Abstracts 11th April)
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration/Abstracts TBD)
1. pyop3 sprint is next week (Monday to Friday) at Imperial. More information can be found [here](https://hackmd.io/@G8tNQvhuS3yL2uv94U1YNQ/BJjzJmBeR/edit).

# Agenda

Present: JB, DH, DD, KS, CW, DV

Apologies: NB

## CW: Built with numpy 2.0
Things seem to work!

## pyop3 sprint
Is happening! Meeting at 10am each day, preferably in person, but online will be available. DH may not be on site on Friday.

## DD: Fixing Cofunction.sub with adjoint
Generalising merge blocks (DD: [#3470](https://github.com/firedrakeproject/firedrake/pull/3470)).

## DH: We're behind UFL issue
UFL finite element: Reference space or physical space? Firedrake and TSFC need updating to use new code.

## CW: optimize.py
:rofl: 

## JB: Another manual release
DH: Maybe not needed (yet). At this point David got distracted and started reading a paper.

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- DH: [#3505](https://github.com/firedrakeproject/firedrake/pull/3505) Fix docs for interpolate (merged)
- JB: [#3348](https://github.com/firedrakeproject/firedrake/pull/3348) PETSc Needs another look

# Date of next meeting

1600 BST (1500 UTC) [2024-04-24](./Firedrake-meeting-2024-04-24)
