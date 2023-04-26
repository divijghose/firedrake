Date and time 2023-04-19 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ALL: Review the [Firedrake manual](https://github.com/firedrakeproject/firedrake/files/10537013/Firedrake_draft1.pdf)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: Pick a date for Firedrake User meeting

# Minutes

Present: DH, JB, DD, KS, PB, FA

Apologies:

## Firedrake Manual
We should enable napolean to allow us to use numpy and google style docstrings.

## FDM
Fast diagonalisation method. There is a code performance issue that needs addressing in the future.

## Updates to Github actions coming soon
- PETSc will be built in the firedrake-env image
- Docker images will be built separately
- Firedrake website will be built and uploaded to github pages

## Merge PRs
JB: Firedrake Manual (errata) [#2784](https://github.com/firedrakeproject/firedrake/pull/2784) ready to go (changes requested)

PB: FDM for de Rham elements [#2801](https://github.com/firedrakeproject/firedrake/pull/2801) (changes requested)

PB: together with [tsfc#287](https://github.com/firedrakeproject/tsfc/pull/287) (ready to go but needs to be merged with Firedrake #2801)

JB: If [#2893](https://github.com/firedrakeproject/firedrake/pull/2893) passes it should go in. This is a rebase of Alberto's work (#2754), but he didn't respond for a month + (automerge enabled)

# Date of next meeting

1600 BST (1500 UTC) [2023-05-03](./Firedrake-meeting-2023-05-03)