Date and time 2025-08-06 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (abstract reduced functionals, etc.)
1. All: Go through issues and mark with "good first issue" for new MSc/PhD contributor projects.

# Minutes

Present: KS RK CW IM JHC

Apologies: DH

### UFL error on CI
https://github.com/firedrakeproject/firedrake/actions/runs/16777757965/job/47507893616?pr=3941

Error message appears on CI but not locally.

`2	FAILED firedrake-repo/tests/firedrake/regression/test_periodic_interval_advection.py::test_periodic_1d_advection_parallel[DG0] - AttributeError: 'Sum' object has no attribute 'coefficients'`

* Advised to fix adjoint failures first as global state may be polluted.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


## Date of next meeting

1600 UTC [2025-08-13](./Firedrake-meeting-2025-08-13)