Date and time 2024-03-20 1600 GMT (1600 UTC)

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

# Notices
1. Submit abstract for PDESoft 1-3 July 2024, Cambridge, UK [PDESoft](https://pdesoft.org) (Registration early 28th March/late 31st May, Abstracts 17th May)
1. PETSc User Meeting 23-24 May 2024 Cologne, Germany [PETSc User Meeting](https://cds.uni-koeln.de/en/workshops/petsc-2024/registration) (Registration and Abstracts 11th April)
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration/Abstracts TBD)

# Minutes

Present: DD, KS, KB, JB, CW, NB, DH, IM, FA, PB  

Apologies:


## JB: Firedrake namespacing
PF raises the point that some of our recent namespacing changes have undesirable consequences. However, sometimes this is necessary. There should be a discussion around having a policy on what needs to be added to the global namespace (eg: UFL yes, FML no).

JB: To have a proper plan to change namespacing. 

## About [PR 3455](https://github.com/firedrakeproject/firedrake/pull/3348)

It is building `create_halo_exchange_sf`. Tests for this is that every parallel test is not going to die.

## About [PR 3426](https://github.com/firedrakeproject/firedrake/pull/3426)

`RestrictedFunctionSpace` is not a Function Space. `ufl.FunctionSpace` has now a label as str of a set of boundary values.

## KS mentioned UFL and Pestc meging in firedrake. KS can work in petsc upstream merging. 

## Reuben viva is this coming Monday!

Comments DH: Petsc words local and global are related to the parallel. 


## About [PR 3348](https://github.com/firedrakeproject/firedrake/pull/3348)

This branch uses different petsc configurations. It is nearly to merge it.

## See the time change. The next weak is UTC and after the next weak is UTC+1

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

[PR 3461](https://github.com/firedrakeproject/firedrake/pull/3461) was approved.

# Date of next meeting

1600 GMT (1600 UTC) [2024-03-27](./Firedrake-meeting-2024-03-27)