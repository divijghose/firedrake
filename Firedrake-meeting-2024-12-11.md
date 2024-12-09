Date and time 2024-12-01 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. CW (formerly JB): Move TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. RK: sort out Firedrake USA details and website before Christmas time

# Agenda

Present: 

Apologies: JHC

## CW: Testing strategy

Someone just reported that Firedrake fails with an int64 build. Since we don't test it we didn't notice. My proposal:

* We should have a set of smoke tests that target a large surface where we encounter issues (e.g. libsupermesh, VoM, parallel, ...). This should take ~5 minutes to run (and we can even call it `make check`).
* We can run a larger number of possible Firedrake configurations whenever we merge to master (e.g. int64, OpenMPI?, etc). We can also run them if we apply a sensible label like we do for MacOS (`ci:macOS`, `ci:int64`, etc). Using pip it only takes about [30 minutes for a workflow to run](https://github.com/firedrakeproject/firedrake/actions/runs/12199795603).

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

# Date of next meeting
1600 UTC [2024-12-18](./Firedrake-meeting-2024-12-18)
