Date and time 2024-05-15 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto
1. JB: Fix runners (Docker permissions issues)

# Notices
1. Submit abstract for PDESoft 1-3 July 2024, Cambridge, UK [PDESoft](https://pdesoft.org) (Registration early 28th March/late 31st May, Abstracts 17th May)
1. PETSc User Meeting 23-24 May 2024 Cologne, Germany [PETSc User Meeting](https://cds.uni-koeln.de/en/workshops/petsc-2024/registration) (Registration and Abstracts 11th April)
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Agenda

Present:

Apologies:

## JB: What to do about TinyASM

## JB: Python 3.12 and New Unbuntu container

## JB: New PETSc changes
I think most are in favour of dropping Chaco from the default build (and we already dropped ML).
The following PRs demonstrate that we can run Firedrake with the following PETSc configurations:
- [No chaco](https://github.com/firedrakeproject/firedrake/pull/3566)
- [No superlu_dist](https://github.com/firedrakeproject/firedrake/pull/3567)
- [No MUMPS/scalapack???](https://github.com/firedrakeproject/firedrake/pull/3564) Okay, I think we might require MUMPS for the test suite, this is not great...
- [No hypre](https://github.com/firedrakeproject/firedrake/pull/3563)
- Just MPI+HDF5+MUMPS+scalapack

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*
- JB: [2248](https://github.com/firedrakeproject/firedrake/pull/3348) PETSc changes.



# Date of next meeting

1600 BST (1500 UTC) [2024-05-22](./Firedrake-meeting-2024-05-22)