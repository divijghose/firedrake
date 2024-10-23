Date and time 2024-10-23 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PRs: [Voting algorithm](https://github.com/firedrakeproject/firedrake/pull/3293), [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. DH: Finish UFL element.value_shape() update
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. JB/UZ: ngsPETSc releases ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-16))

# Agenda

Present:

Apologies: PB

## DD: [PR #3723](https://github.com/firedrakeproject/firedrake/pull/3723)

Adjoint Variational Solver and fix recomputing tape when Jacobian is constant.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [#3814](https://github.com/firedrakeproject/firedrake/pull/3814) MG for R space

DD: [#3816](https://github.com/firedrakeproject/firedrake/pull/3816) Fix gradient computation where the boundary condition is a control parameter.

# Date of next meeting
1600 BST (1500 UTC) [2024-10-30](./Firedrake-meeting-2024-10-30)