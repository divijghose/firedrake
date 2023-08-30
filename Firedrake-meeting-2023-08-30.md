Date and time 2023-08-30 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: discuss preparation for Firedrake User meeting
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. NB: PP24 minisymposium update

# Minutes

Present: JB, DD, CW, DH, RK, RNH

Apologies: Where is Nacime?

## Firedrake23 Update:
Programme is available, participants have been emailed, website will be updated soon (see next item).

## SysGenX Meeting Update:
- Connor and Pablo will work on local sparse tensors.
- Jack and Igor will discuss GPUs.
- Also UFL things.

## RNH: Doc building is broken again
See for example https://github.com/firedrakeproject/firedrake/actions/runs/6009640862/job/16299473406?pr=3067

This is "fixed" in https://github.com/firedrakeproject/firedrake/pull/3083 (but please never write code like this).

## Merge PRs

- #3082 Website update for Firedrake23 (Rebase)
- #3073 Block sparsity fix - Remove package branch and approved
- RNH [Parallel Compatible Cross-Mesh Interpolation #3067](https://github.com/firedrakeproject/firedrake/pull/3067) - Changes requested

# Date of next meeting

1600 BST (1500 UTC) [2023-09-06](./Firedrake-meeting-2023-09-06)