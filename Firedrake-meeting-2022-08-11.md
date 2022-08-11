Date and time 2022-08-11 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (CW to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (ongoing)
1. JB: SIAM CSE23 Minisymposium/minisymposterium
1. JB: PETSc branch with GC fix (JB) + IO (KS)

# Agenda

Present: 

Apologies:

## JB: CSE Minisymposium
3-4 currently responded to requests for talks.
Have response from Tom Bendall, George Bisbas, deferred response from Jack Hale, Kaushik yes, others still waiting.
Will have 2 from our group so only 3 still to fill.

## DH: Checkpoint reloading now approximately works
Still have issues with adjoint, e.g. when writing and reading forcing data in parallel. Koki confirms this is a known limitation on his branch.

## DH: PETSc MRs
JB has resolved all review comments, will push for another review once he has documented the relevant parts of petsc4py and to perform benchmarks.
KS still waiting on review from Matt Knepley.
KS needs to ask Vaslav about parallel topology.

## JB: Strange Docker failure
No error code, no backtrace. Same docker image builds locally just fine. Seems odd:
https://github.com/firedrakeproject/firedrake/runs/7768477380?check_suite_focus=true
Anyone else had a similar experience? This is holding up #2504
 - JB to log on to the machines and rebuild petsc in debug mode
 - JB can also get container to play with by not running the tests

## DH: Needs to sort out licenses for docker on mac and windows

## JB: Status of intel and AMD compilers - Legally allowed to use for CI with spack?
DH says should only work with valid licence key but JB finds it works without intervention locally for him.
 - Intel's docs suggest it should be fine - you only have to license/pay if you want intel support.
 - AMD EULA says it can be used as long as it's only on AMD hardware. Given we run CI on AMD it should be fine.

Nvidia arm compiler is still WIP for JB.

## Merge PRs

## Date of next meetings

Next meeting: 1200 UTC [2022-08-18](./Firedrake-meeting-2022-08-18)