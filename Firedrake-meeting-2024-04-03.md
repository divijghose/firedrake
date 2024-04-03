Date and time 2024-04-03 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (NB to pick)
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

# Agenda

Present:

Apologies:

## PB + RK Macroelements

We've implemented macroelements in [FIAT #64](https://github.com/firedrakeproject/fiat/pull/64) (without tiling a reference subelement for a good reason).

We want feedback on our proposed interface: Alfeld and P1-P2-Iso as Lagrange variants (this requires no UFL or firedrake PRs).

We don't get the sparsity right so far, good candidates for this are pyop(2/3) kernels on subcells (similar to what we have for `dS`) or even sparse GEM.


## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


# Date of next meeting

1600 BST (1500 UTC) [2024-04-10](./Firedrake-meeting-2024-04-10)