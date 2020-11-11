Date and time 2020-11-04 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. DS: Anaconda on Mac

# Agenda

Present: David Ham, Lawrence Mitchell, Rob Kirby, Colin Cotter, Jack Betteridge, Connor Ward, Sophia Vorderwuelbecke, Paul Kelly, Stephan Kremar, Koki Sagiyama

Apologies: Reuben Nixon-Hill

## JB: Numpy Nightmare

Issues:
- linking to old libgfortran -> link agaist the right openblas from homebrew
- numpy import time error (RK and CJC have observed on IPython).
- A lot of wheels are missing in Python3.9 -> Suggest that users use 3.8
- JB has observed some stochastic Xcode errors...

Good thing about firedrake:
- Platform independent install mechanism (except on super-computer)
- Incremental rebuild.

Build conda package?
- will need completely different system on supercomputer (bad).

Short term solution suggested by JB:
 - Worked for RK
 - JB: Have CJC check if this solution works.
 - JB: Put the recipe of this solution on this minute:

Run
```
export DYLD_INSERT_LIBRARIES=/usr/local/opt/openblas/lib/libblas.dylib:/usr/local/opt/openblas/lib/liblapack.dylib
```
in a terminal before importing Firedrake, or add to Firedrake activate script.

## Strange test failures (from last week)
Update

Questions:
 - Does it always fail on the same build hardware but not other build hardware?
 - Is SNES deterministic?
 - Could the FPU on one of the builders be bad?

Summary:
 - PYOP2_DEBUG=1 -> pass
 - vector registers in Intel chips have a lower precision than the scalar ones?

CW submitted PR:
 - increased `snes_max_it`
 - see https://github.com/firedrakeproject/firedrake/pull/1898

## CW/LM: PyOP2 documentation

It's very out of date. Should we remove it?

PyOP2 documentation, some are wrong, others are not.

Action:

CW: Push sphinx documentation when test (LM: auto-build with github action is better?)

## CW/LM: Random test failures

See, e.g., https://github.com/firedrakeproject/firedrake/pull/1898

First observed around when:
- complex landed,
- default solver changed (mumps global variable clean up issue?).

Action:

LM: make superlu default and see if it magically fixes the issue.

??: set `omp_num_threads`

## Merge PRs:

## AOB
## Date of next meeting

[2020-11-11](./Firedrake-meeting-2020-11-11) 16:00UTC (16:00GMT)