Date and time 2020-06-30 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ \*\*: Review this.
1. \*\*: Add `--remove-build-files` to make install smaller; convert this to an issue

# Minutes

Present: David Ham, Lawrence Mitchell, Paul Kelly, Reuben Hill, Sofia, Dan Shapero, Jack Betteridge, Koki Sagiyama, Matthew Kan, Nacime Bouziani, Rob Kirby, Sophia Vorderwuelbecke, Tom Gregory, Tuomas Karna

Apologies:

## Tuomas Karna - Equispaced Coordinate Fields (added by RWH)
Should coordinates be in equispaced function space by default?
* vtk only supports equispaced FS
* Equispaced FS is okay if multilinear, but not if higher order

Should `FunctionSpace` constructor have the variant as an argument?
* FEniCS allows for passing strings to constructor (which is a design error)
* FEniCSx (probably) fixes this by allowing for pasing "element"

Options:
* Use FunctionSpace(mesh, ..., **kwargs) and mimic how pyadjoint duplicates/removes contents of kwargs? (Can be messy for extruded cases as we have horizonal variant + vertical variant)
* Use FiniteElement as argument (ufl.FiniteElement constructor does not take meshes -> Drop mesh shell in "firedrake.FiniteElement".)

Immediate fix:
Use "FunctionSpace(..., variant=...)"

See issue [1763](https://github.com/firedrakeproject/firedrake/issues/1763), PR [1732](https://github.com/firedrakeproject/firedrake/pull/1732)

## LM : PETSc 4.0

PETSc are [scoping ideas for 4.0](https://gitlab.com/petsc/petsc/-/issues/643), no idea is a priori off the table, are there things we wish they had?

See https://gitlab.com/petsc/petsc/-/issues?label_name%5B%5D=petsc-future for discussion so far.

This is a major number change.

Different implementation language? 
* C++, ...

What we might want PETSc to have:
* Composable plexes 
* FunctionSpaces -> might drop half of Firedrake to PETSc
* Runtime JIT

ALL: Jump into the discussion (using the link above) if you want some features to be added.

## SVDW : Vectorisation
Loopy branch here https://github.com/firedrakeproject/loopy/pull/6/files
PyOP2 branch here https://github.com/OP2/PyOP2/pull/581
Firedrake test run here https://github.com/firedrakeproject/firedrake/tree/trigger-tests-for-vec, 2 tests are still failing

Getting TJ's vectorisation done.

Two versions of vectorisation by TJ:
* vec datatype & pragma  <- SV is using this, which is good.
* pragma only

Two tests are failing with --tree-vectrise off:
* diverge when solving.
* getting wrong answer :(

SV:
* Switch off --tree-vectrise
* Use docker and take a very small kernel (e.g., mass matrix) 
* Look at the assembler to understand why we are getting wrong answer.

also:
* Check if we can reproduce this locally
* Can we reproduce it with PYOP2_DEBUG=1 ? (If No, maybe a gcc bug)


## Pull Requests
* complex
* vectorisation (mostly loopy)

Proposed workflow for vectorisation branches:
* merge loopy -> PyOP2 -> Firedrake

SV: check if loopy branch is fine -> we can merge loopy


## Date of next meeting
2020-07-07 15:00UTC (16:00BST)
