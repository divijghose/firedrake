Date and time 2024-12-11 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ~CW (formerly JB): Move TSFC to firedrake and move FInAT to FIAT~ (Done)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ~ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)~ (Done)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. RK: sort out Firedrake USA details and website before Christmas time
1. CW: fix PyOP2+TSFC failing tests
1. CW: Fix artefactsv3 issue

# Minutes

Present: CW (minuter), SM, RK, PB, IM, KS, DD, DH

Apologies: JHC

## RCK: Firedrake USA'25
* I have a  PR with the Web page that's approved, but it's failing CI tests for seemingly unrelated things like PyOP2 and TSFC.
* Update: we have a travel support request form, are waiting on a business office person to give us a registration link.

* Merged.

## CW: Testing strategy

Someone just reported that Firedrake fails with an int64 build. Since we don't test it we didn't notice. My proposal:

* We should have a set of smoke tests that target a large surface where we encounter issues (e.g. libsupermesh, VoM, parallel, ...). This should take ~5 minutes to run (and we can even call it `make check`).
* We can run a larger number of possible Firedrake configurations whenever we merge to master (e.g. int64, OpenMPI?, etc). We can also run them if we apply a sensible label like we do for MacOS (`ci:macOS`, `ci:int64`, etc). Using pip it only takes about [30 minutes for a workflow to run](https://github.com/firedrakeproject/firedrake/actions/runs/12199795603).

* DH: Tentative approval.
* **Action point CW** make this happen.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

RCK: [Firedrake conference](https://github.com/firedrakeproject/firedrake/pull/3910)

* Merged.

KS:[restricted function space with extrusion](https://github.com/firedrakeproject/firedrake/pull/3905)

* Merged

DD: [Enable measure options for Riesz representation](https://github.com/firedrakeproject/firedrake/pull/3911/)

* This would be better exposed via `form_compiler_parameters`. PR is not required.

DD: [Ensemble reduced functional arguments](https://github.com/firedrakeproject/firedrake/pull/3908)

* Merged.

DD: [Document the Reduced functional args (pyadjoint)](https://github.com/dolfin-adjoint/pyadjoint/pull/186)

* Merged.

DD: [Options for Riesz represention solver (pyadjoint)](https://github.com/dolfin-adjoint/pyadjoint/pull/184)

* DD to revisit in light of #3911 feedback.

# Date of next meeting
1600 UTC [2025-01-08](./Firedrake-meeting-2025-01-08)

