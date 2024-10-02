Date and time 2024-10-02 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))

# Minutes

Present: JB, DH, PB, IM, LC, CC, RK

Apologies:

## DH: Introductions for Leo Collins
You all know who you are!

## RK: Is anyone missing from the Irksome author list?
See: https://github.com/firedrakeproject/Irksome/pull/75

## JB: mpi4py version 4.0
This release is only compatible with MPI 4 or later.

DH: We need a way for users to specify this in the install/update script. Otherwise we can't install on ancient HPC clusters.

## JB: Do something with Lilly's branch
DH: Open PR

JB: Done: https://github.com/firedrakeproject/firedrake/pull/3784/files

## DH: Spec up new runners
Action item for JB: spec up some new CI runners

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*
- PB [#3771](https://github.com/firedrakeproject/firedrake/pull/3771) Some discussion about different finite element flavours and variational crimes. (changes TESTS! requested) Associated PRs in FI(n)AT/TSFC may need docs too.
- PB [#3736](https://github.com/firedrakeproject/firedrake/pull/3736) Lots of small changes requested, o/w good.


# Date of next meeting
1600 BST (1500 UTC) [2024-10-09](./Firedrake-meeting-2024-10-09)