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

# Minutes

Present: CW (minuter), KS, DD, DH, RK, PB, IM

Apologies: NB

## DH: Announcements

* The FEniCS conference is 12th-14th June in Oslo, DH contacted by Marie Rognes. `checkpoint_schedules` (DD) would potentially be a good topic to discuss. DH may also go.

## PB + RK Macroelements

We've implemented macroelements in [FIAT #64](https://github.com/firedrakeproject/fiat/pull/64) (without tiling a reference subelement for a good reason).

We want feedback on our proposed interface: Alfeld and P1-P2-Iso as Lagrange variants (this requires no UFL or firedrake PRs).

We don't get the sparsity right so far, good candidates for this are pyop(2/3) kernels on subcells (similar to what we have for `dS`) or even sparse GEM.

* DH: Interpolation may be difficult for these elements.
* DH: Sparsity is "local", and therefore a concern for TSFC + GEM.
* RK: Aim to create 1D macro-elements to get quads and hexes.
* PB: PETSc have recently improved their matrix infrastructure s.t. preallocation is supposedly no longer required.

## CW: MacOS build issues with latest Xcode

What is the current status of this?

DD: We have a set of issues involving [CHACO](https://gitlab.com/petsc/petsc/-/issues/1557) and [mpich](https://gitlab.com/petsc/petsc/-/issues/1569) for Xcode15.3. In [mpich issue](https://gitlab.com/petsc/petsc/-/issues/1569), downgrading the Xcode version was one of the core petsc suggestions.
DH: Should indicate to users to first try downgrading Xcode and then using [this workaround](https://github.com/firedrakeproject/firedrake/wiki/Install-Frequently-Asked-Questions). Need to wait for PETSc to resolve this.

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


# Date of next meeting

1600 BST (1500 UTC) [2024-04-10](./Firedrake-meeting-2024-04-10)
