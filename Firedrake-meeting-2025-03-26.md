Date and time 2025-03-26 1400 UTC

# Action Items
1. **Pick Chair and Minuter** (LC not here, someone else pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present:

Apologies: LC, CW (maybe)

## CW: What happens to Zenodo when we move to releases?

* git information not available for packages, instead we have version numbers
* if someone is using a version of Firedrake then we already have a GitHub release that they are using
* The simplest case is to gather the various GitHub releases together and put them in a Zenodo release
    * If so might not need our own forks of PETSc etc
* What if someone is working from a branch? Do they have to make their own release?

## CW: Use upstream PETSc: [#4137](https://github.com/firedrakeproject/firedrake/pull/4137)

Proposed roadmap:
1. Merge this (breaks `firedrake-zenodo`)
2. Update to latest release of PETSc (v3.23.0) very close to release
3. Firedrake releases (and fix `firedrake-zenodo`). This will require a little thought about what branches of PETSc we track

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* CW: [#4138](https://github.com/firedrakeproject/firedrake/pull/4138)

# Date of next meeting
1600 UTC [2025-04-02](./Firedrake-meeting-2025-04-02)