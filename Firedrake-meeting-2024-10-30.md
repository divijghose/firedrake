Date and time 2024-10-30 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. DH: Finish UFL element.value_shape() update
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. JB/UZ: ngsPETSc releases ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-16))

# Minutes

Present: DH, JB, IM, JHC, CW, LC, KS

Apologies: DD

## CW: Voting algorithm

https://github.com/firedrakeproject/firedrake/pull/3293

mesh.py line 4171 explains.

merged.

## (from last week) JB: Long running tests
```
427.50s call     tests/demos/test_demos_run.py::test_demo_runs[full_waveform_inversion.py.rst]
363.02s call     tests/macro/test_macro_interp_project.py::test_piola_convergence[h1_proj-3-Johnson-Mercier-1-1]
345.51s call     tests/regression/test_fdm.py::test_p_independence_hcurl[Box]
```
CI time has shot up as a result.

JB: Why are fdm tests slow?

PB: Can make it use lower-degrees.

PB: Code generations are slow with Johnson-Mercier.

DH: Are they supposed to be that slow?

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS: [io high-order mesh H(div)/H(curl)](https://github.com/firedrakeproject/firedrake/pull/3838)

DH: We do not want additional arguments in `save_function`.

KS: Best solution is to fix our definition of elements so that DG projection would not be necessary.

# Date of next meeting
1600 UTC [2024-11-06](./Firedrake-meeting-2024-11-06)