Date and time 2022-04-07 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** .
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: JB DH RK PK SM CW 

Apologies: SV

## Firedrake on M1

What is the safe way to get the required linker flag to the compiler called by PyOP2?

DH: Need to pass a bunch of flags to the M1 compiler
SM: Hit this bug importing PyOP2 before Firedrake
JB: Can we just add LDFLAGS to the PyOP2 compiler class?
DH: Yes, what if GCC updates?
JB: We can just have multiple paths (this spews warnings if the path doesn't exist, but this is fine)

Action DH: Add these flags to LDFLAGs in PYOP2 compiler class

## SM: Push PETSc fork forward
Action CW: Test PETSc main against current Firedrake


## JB: Can we change the @parallel text marker?
JB: Currently the @parallel test marker causes a subprocess call which fails with later versions of pytest. Pytest is wrapping mpiexec, can we change this so that mpiexec wraps pytest? (See mpi4py test suite)
DH: What about xdist? We still want to run MPI parallel tests in parallel to avoid slowing down the test suite
Action JB: Look into this


## Merge PRs

#2350 CW: Add caching for pointwise expression kernels - Merged

#2037 SM: Generalizing interface for PlaneSmoother - Rebase on top of master


## Date of next meetings

* 2022-04-28 clashes with Firedrake Australia

Next meeting: [2022-05-05](./Firedrake-meeting-2022-05-05)
