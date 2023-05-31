Date and time 2023-05-31 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: discuss preparation for Firedrake User meeting
1. DH: Email to Andreas to have 2 loopy PRs merged

# Agenda

Present:

Apologies:

## RNH Broken Ubuntu Install

## CW: Lazy `petsc4py.PETSc` import?

I think that it is possible to delay the import of `petsc4py.PETSc` such that `from firedrake import *` can run without calling PETSc Initialize. This will make importing Firedrake do less "magic". In particular MPI Init would not be called so we could use OpenMPI for running our parallel tests.

Is this idea worth spending any time on?

## Merge PRs

JB: [#2892](https://github.com/firedrakeproject/firedrake/pull/2892) Add Firedrake manual to website + Github (still missing DOI).

JB: [#2871](https://github.com/firedrakeproject/firedrake/pull/2871) Change GH actions + Firedrake docker images. Also build website on GH pages automatically.

# Date of next meeting

1600 BST (1500 UTC) [2023-06-07](./Firedrake-meeting-2023-06-07)
