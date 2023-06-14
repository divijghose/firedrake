Date and time 2023-06-14 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: discuss preparation for Firedrake User meeting
1. DH: Email to Andreas to have 2 loopy PRs merged
1. DH: Get firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))

# Agenda

Present: RK, DH, CW (minuter), KS, DD, JB, NB

Apologies:

## CW: Lazy petsc4py import update ([prior minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-05-31#cw-lazy-petsc4pypetsc-import))

Sadly this is just not possible without significant petsc4py changes/Cython magic. I can avoid lazy imports in Python but `cimport petsc4py.PETSc` is everywhere in our Cython code and this also initialises PETSc (and hence MPI).

- DH: This would require potentially involved changes in petsc4py equivalent to mpi4py (`import mpi4py; mpi4py.rc.initialize = False; from mpi4py import MPI`).

## CW: Adjoint caching strategies

See https://github.com/firedrakeproject/firedrake/issues/2979.

- DH: Creating solvers is inherently expensive because of work done factorising the matrices.
- DH: The need for a linear solver in the adjoint will go away with dual spaces because we can have cofunctions as RHS. Therefore optimising the linear solve at present may not be a current priority.
- DH: We could possibly replace `NonlinearVariationalSolver` and `LinearVariationalSolver` with `VariationalSolver` in future.

## Merge PRs

UZ: [2986](https://github.com/firedrakeproject/firedrake/pull/2986) Fix Netgen demo

JB: [2987](https://github.com/firedrakeproject/firedrake/pull/2987) Firedrake Manual DOI

JB: [2927](https://github.com/firedrakeproject/firedrake/pull/2927) Constants - MERGED!

DD: [2982](https://github.com/firedrakeproject/firedrake/pull/2982) Delegate checkpoint in recompute. - changes requested

# Date of next meeting

1600 BST (1500 UTC) [2023-06-21](./Firedrake-meeting-2023-06-21)