Date and time 2024-08-21 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Agenda

Present: DH, CW, JB, IM, DD, RK, PB, JHC, KS

Apologies:

##

GregVernon's PR [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116):

real-mode test failed for some reason.

Sophia's PR:

DH: This is not the part of the code that we often touch.

# Firedrake US 2025

Friday and Saturday before CSE.

## JHC: Docs

JHC: [PR#3742](https://github.com/firedrakeproject/firedrake/pull/3742).
By default, Sphinx doesn't build the docs for "special" methods i.e. dunder methods. This PR adds a line to the documentation configuration so that `__call__` methods are documented in the API listing.

DH: Uncontroversial.

## DD: MUMPS + Mac updates:
* The PETSc `make test` runs successfully with MUMPS. However, Firedrake tests are still failing when run in parallel.
* petsc4py also fails in parallel when using MUMPS. So, I believe this is not a problem with Firedrake itself but rather with petsc4py. I will continue to investigate this further.

DD: Wrap up MFE and open new issue in upstream.

## JB: Caching update
WIP is in [PyOP2](https://github.com/OP2/PyOP2/pull/724) and [Firedrake](https://github.com/firedrakeproject/firedrake/pull/3730) PRs, discussion needed?

JB: Centralise all caching in one place (disk or memory cache). Removed CachedObject.

DH: In principle this looks right.

## Irksome

DH: Is it nice to have progress bar?

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS: [part1](https://github.com/firedrakeproject/firedrake/pull/3727): Minor changes required.

DD: [FWI demo](https://github.com/firedrakeproject/firedrake/pull/3562): 

# Date of next meeting
No meeting next week!
1600 BST (1500 UTC) [2024-09-04](./Firedrake-meeting-2024-09-04)
