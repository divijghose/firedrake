Date and time 2021-02-03 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: DAH, LM, RK, JDB, RNH, NB, KS, SK, CW, PK, SV, KK, TG

Apologies: 

## RNH: TSFC master is failing on python 3.8
See [travis](https://travis-ci.org/github/firedrakeproject/tsfc/builds/755156591)

Failing because the name of the ufl package was changed (from `ufl` to `fenics-ufl`)

Fix: in requirement.txt set `#egg=fenics-ufl`


## CW: Merge Flame Graph to PETSc master

Certain operations can be timed in PETSc via timer flags present in the code.

This merge enables to generate a svg file containing the flame graph with the time elapsed for the different timed operations.

Same principle can be applied to time the different firedrake operations (e.g. assemble,solve, etc.).

## RK: Nonlocal operator (using ExternalOperator)

The nonlocal operator for Helmholtz (complex) is working.

Next step: the adjoint

## Merge PRs: 

"Fix passing of nearnullspace in mixed problem to subproblem" [#1952](https://github.com/firedrakeproject/firedrake/pull/1952):  **Merged **


## ALL: SIAM CSE:

Don't forget to register !

## AOB


## Date of next meeting

[2021-02-10](./Firedrake-meeting-2021-02-10) 16:00UTC (16:00GMT)
