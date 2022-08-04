Date and time 2022-08-04 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (NB to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (ongoing)
1. JB: SIAM CSE23 Minisymposium/minisymposterium

# Minutes

Present: DH, CW (minuter), JB, NB, RNH, KS

Apologies:

## JB: Beware, there might be install issues on the horizon:

1. Pip is changing the way that packages are installed, this affects the libraries mpi4py/petsc4py link against

2. VTK wheels: Urgh! (RH has started investigating)

- JB: Linking issues with system packages. E.g. mpi4py may pick up system MPI instead of our own MPICH.
- RNH: `pip install vtk` seems to fix things but it's a development version, not release version.
- JB: Latest Python (3.10) now has a wheel available because a new VTK version is getting developed.

## JB: Garbage collector in PETSc

- JB: Slow progress getting made.

## KS: PETSc MR progress

- KS: Having some issues on Archer.
- DH: It would be handy to have KS's work and JB's on a single branch.
- **Action point** JB to coordinate with KS to get a shared branch.

## Merge PRs

### #2504

- DH: Maybe at some point we could link Spack package versions with Zenodo.

### #2487

- **Merged**

### https://github.com/firedrakeproject/tsfc/pull/282

- NB to take a look.

### https://github.com/firedrakeproject/tsfc/pull/280

- **Closed**

## Date of next meetings

Next meeting: 1200 UTC [2022-08-11](./Firedrake-meeting-2022-08-11)