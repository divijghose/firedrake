Date and time 2024-10-16 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PRs: [Voting algorithm](https://github.com/firedrakeproject/firedrake/pull/3293), [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ~JB: Rebase and test [Transpose](https://github.com/firedrakeproject/firedrake/pull/3167)~ Done
1. DH: Finish UFL element.value_shape() update

# Agenda

Present:

Apologies:

## JB: ngsPETSc
If Umberto is attending we should talk about this again in light of Patrick's comments. If not `goto next`.

## JB: An ancient branch rebased
Is anyone interested in further developing this work? https://github.com/firedrakeproject/firedrake/pull/3799

## JB: Allow the test suite to run with MPI "on the outside"
And other test suite fixes: https://github.com/firedrakeproject/firedrake/pull/3385

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: Merge in any order

PB: [FInAT #141](https://github.com/FInAT/FInAT/pull/141) Fixes docs, but points to legacy fenics FIAT (same as in FD).

PB: [FIAT #89](https://github.com/firedrakeproject/fiat/pull/89) High-degree tabulated quadratures. Already tested firedrake

PB: [TransferManager #3796](https://github.com/firedrakeproject/firedrake/pull/3796)

PB: Merge in this order. Already reviewed.

PB: [FIAT #86](https://github.com/firedrakeproject/fiat/pull/86)

PB: [FInAT #140](https://github.com/FInAT/FInAT/pull/140)

PB: [TSFC #320](https://github.com/firedrakeproject/tsfc/pull/320)

PB: [Firedrake #3795](https://github.com/firedrakeproject/firedrake/pull/3795)

# Date of next meeting
1600 BST (1500 UTC) [2024-10-23](./Firedrake-meeting-2024-10-23)