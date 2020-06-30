Date and time 2020-06-30 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ Continue reviewing
1. \*\*: Add `--remove-build-files` to make install smaller; convert this to an issue

# Minutes

Present:

Apologies:

## Tuomas Karna - Equispaced Coordinate Fields (added by RWH)
- Should coordinates be in equispaced function space by default?
- Should `FunctionSpace` constructor have the variant as an argument?

See issue [1763](https://github.com/firedrakeproject/firedrake/issues/1763), PR [1732](https://github.com/firedrakeproject/firedrake/pull/1732)

## LM : PETSc 4.0

PETSc are [scoping ideas for 4.0](https://gitlab.com/petsc/petsc/-/issues/643), no idea is a priori off the table, are there things we wish they had?

See https://gitlab.com/petsc/petsc/-/issues?label_name%5B%5D=petsc-future for discussion so far.

## SVDW : Vectorisation
Loopy branch here https://github.com/firedrakeproject/loopy/pull/6/files
PyOP2 branch here https://github.com/OP2/PyOP2/pull/581
Firedrake test run here https://github.com/firedrakeproject/firedrake/tree/trigger-tests-for-vec, 2 tests are still failing

## Date of next meeting
2020-07-07 15:00UTC (16:00BST)
