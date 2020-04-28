Date and time 2020-04-28 15:00UTC (16:00BST)

# Action Items
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. DRS: See the [related Firedrake issue](https://github.com/firedrakeproject/firedrake/issues/1649), and start having a good at load/store plex objects. To make smart checkpoints

# Minutes
Present: David Ham, Lawrence Mitchell, Jack Betteridge, Koki Sagiyama, Nacime Bouziani, Sophia Vorderwuelbecke, Florian Wechsung, Reuben Hill, Thomas Gregory, Dan Shapero, Colin Cotter, Robert Kirby, Luke Olson

Apologies:

## RWH: Correct way to modify PETSc in firedrake
Rebuilding PETSc via `firedrake-update --rebuild` when small changes have been made is time consuming while not required. Wiki page tackling this question : [wiki page](./Modifying-and-Rebuilding-PETSc-in-Firedrake)

## RWH: CoordinatelessFunction's UFL mesh
Not discussed.

## State of complex sprint
Briefing following the complex sprint that happened last week (cf. https://github.com/firedrakeproject/firedrake/wiki/MergeComplexSprint).

All the tests are now passing except two shape derivatives based tests in pyadjoint (`firedrake_adjoint/test_dynamic_meshes.py` and `firedrake_adjoint/test_shape_derivatives.py`).

Here is a write-up explaining the core issue: https://github.com/FEniCS/ufl/issues/21, the solution proposed is to add a hack in UFL to add `conj` at the end of the process where needed. Long-term solutions would require deeper and more invasive changes in UFL.

There are still some deeper infrastructure questions that need to be addressed to land complex as soon as possible --> David's job

Complex mode doubles the load of test, potential solutions addressed : 
   - Stop testing every commits
   - Only test when PRs are open
   - Instead of testing the commit and the merge commit, just test the merge commits (should half the test load)

Florian: Add the hack to have shape derivatives tests working in complex

David: Tackle the remaining complex sprint items

## DRS: streamplot

Ready to be merged!

Dan: Open the PR

## SV: Tsslac

Tsfc side (adds code generation for shaped things in tsfc) is almost there.

For the firedrake side, a lot of things are inherent to the structure of the compiler initially written (cf. Thomas Gibson's work), these things are not necessary anymore -> Getting rid of them should alleviate the code.

There a 2 new shape operations: 
   - An inverse operation (for rank 2 tensors)
   - A solve operation

Question: how are these operations represented in GEM?

Sophia: Expunge references to COFFEE

Lawrence: Go through the PRs

## JB: Building Firedrake on Isambard
For anyone interested: https://github.com/firedrakeproject/isambard/tree/alternative_install
The mechanism is working with firedrake master. Check changes in firedrake-install.

## JB: Python 3.8
It is possible to land a fix using the Isambard branch.
We can automatically detect when firedrake is installed if it is with Python 3.8 and pull the relevant wheel. It should make Python 3.8 land.

Jack: Add this mechanism


## JB: Test organisation - short_test for quick verification
Use Isambard to run tests in parallel.
 - Few problem noticed when parallelizing tests in Isambard, a workaround was found
 - Fix pytests on supercomputer would require additional works

Jack: Use the workaround

## CC: Linesmoother+GTMG, an update
Adds a line smoother that couples vertically aligned degrees of freedom in extruded meshes.

PR ready to be merged: https://github.com/firedrakeproject/firedrake/pull/1664)

Example of applications: gravity waves test problem

## Firedrake installation problem
Manually add lines to pip install `cached_property` and `pkgconfig` should work.

## Additional notes

Lecture about Mutligrid (Luke Olson) happening soon:
 - Github link: https://github.com/lukeolson/imperial-multigrid
 - Spreadsheet: https://docs.google.com/spreadsheets/d/13Z5VSijFgn3SGng9YJMfR8nRF8ATs4wpy7sgPFQEAk4/edit#gid=0

## Date of next meeting
2020-05-05 15:00UTC (16:00BST)