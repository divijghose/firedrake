Date and time 2024-11-06 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
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
1. PB+DD: Speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30))

# Minutes

Present: JB, DD, CW, KS, DH, IM, FA, PB, UZ, JHC, JK

Apologies:

## JB/UZ: ngsPETSc releases

JB/UZ are getting issues associated with petsc4py, specifically with numpy version.
Hopefully, petsc4py developers can help to fix it. Perhaps a manual release can be done for now.

## CW: Python 3.10 for loopy

Andreas [has indicated](https://github.com/firedrakeproject/loopy/issues/27) that loopy will be moving to Python 3.10 soon. Do we follow? If we don't then we might need to pin to a pymbolic git hash instead of a version.

DH is fine to drop python 3.9.

## CW: Slack channel for developers?

I don't want to bother 650 people when our docs fail to build etc...

DH thinks is good to make the community aware of the firedrake developers' questions/discussions.

## About USA Firedrake'25

JK is asking for a budget.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* CW: https://github.com/dolfin-adjoint/pyadjoint/pull/174

Merged.

* DD: tape `_recompute_count`: https://github.com/dolfin-adjoint/pyadjoint/pull/172

Merged.

* DD: [Adjoint variational solver](https://github.com/firedrakeproject/firedrake/pull/3723)

Merged.

* DD: [Test mode for FWI CI execution](https://github.com/firedrakeproject/firedrake/pull/3836)

Require changes.

* KS: [EquationBC + PC](https://github.com/firedrakeproject/firedrake/pull/3842)

Merged.

# Date of next meeting
1600 UTC [2024-11-13](./Firedrake-meeting-2024-11-13)