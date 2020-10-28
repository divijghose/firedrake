Date and time 2020-10-28 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. ~RK: Report back on quadrature estimation~
1. ~KS: Complex merge~
1. ~DH: Online Firedrake 2021~ Will return to in 2021.
1. DS: Anaconda on Mac

# Agenda

Present: David Ham, Lawrence Mitchell, Reuben Nixon-Hill, Rob Kirby, Jack Betteridge, Connor Ward, Stephan Kremar, Tom Gregory, Sophia Vorderwuelbecke, Paul Kelly

Apologies: 

## DS: Anaconda on Mac
`pyenv`, tool for managing python versions and `venv`s, lets you run anaconda alongside firedrake.
Pollution successfully avoided on first check.
Unclear if `pyenv` is able to avoid pollution when anaconda installs packages with compiler toolchains (or e.g using anaconda to install openMPI) - DS will check.
DS will also check `firedrake-update`.

## DH: MSc projects for this year (MSc applied maths, MSc computing, MISCADA?...)

RK suggestions: 
 - Optimal quadrature estimation (e.g. for tensor product elements)
 - Irksome: 
    - getting data layout and function spaces right for vectorisation
    - enabling IMEX methods

LM suggestions:
 - Second half of MKan's project (exploiting structure information in dual evaluation in FInAT/sum factorisation when doing interpolation). Needs symbolics to be in place before student starts? Lots of TSFC work.
 - Symmetry groups in FIAT for unstructured hex cells. LM has industrial application. PETSc has necessary information, we don't know how to use
 - Catamorphisms for finite elements - could be boring though
 - Automated performance models
 - FInAT Bernstein (triangular loop nests in TSFC)
 - Mixed data layout

PK suggestions:
 - Assembly with structured sparsity? (TSFC kernel giving you back block sparse matrix). Potential interesting language problem there to solve.

RNH / RK suggestions:
 - Element oracle? Hard to come up with research angle.

CONCLUSION: Everyone please write up descriptions to gauge scope.

## DH: Announcement: Faculty position at IC Maths coming up imminently.

## RNH: Strange test failures (from last week)

Last week:
`tests/regression/test_aw.py::test_aw[conforming]` is failing on https://github.com/firedrakeproject/firedrake/pull/1867 and https://github.com/firedrakeproject/firedrake/pull/1884 which don't touch the relevant code

This week:
`tests/regression/test_aw.py::test_aw[conforming]` fails intermittently when testing in firedrake complex mode.
DH wonders if problem is poorly conditioned.
RK suggests changing solver options to get it working in complex mode.
LM hypothesises that problem might be to do with tests running in nondeterministic order(issue to do with which builder the jenkins build ran on).
Questions:
 - Does it always fail on the same build hardware but not other build hardware?
 - Is SNES deterministic?
 - Could the FPU on one of the builders be bad?
DH notes that failure is very soft - could just be squashed by doing more iterations.

## JB: To what extent are we willing to change solver options to get tests passing in complex?
Fine when not expected to get convergence at same rate in complex mode to real mode.

## RNH: what else does MKan's work need to merge? A masters level set of changes?
No. RNH and DH to think about how to kill the bug.

## Merge PRs:

## AOB
## Date of next meeting

[2020-11-04](./Firedrake-meeting-2020-11-04) 16:00UTC (16:00GMT)