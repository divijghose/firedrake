Date and time 2023-03-29 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ALL: Review the [Firedrake manual](https://github.com/firedrakeproject/firedrake/files/10537013/Firedrake_draft1.pdf)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements
1. CW: Attempt to fix gc + CheckpointFile [JB: DONE?]

# Agenda

Present: JB, DD, CW, KS, DH, RNH, PK, RK, FA, IM, UZ, NB

Apologies:

## JB: Please review the manual
[Link](https://github.com/firedrakeproject/firedrake/pull/2784)
 - All: treat this as a publication and read it!
 - DH: Everyone who has their name on this needs to be told

## JB: Merge or rebase forks
What goes [here](https://github.com/firedrakeproject/firedrake/wiki/Updating-forked-dependencies#git-merge-vs-git-rebase). Thanks to Connor for these wiki contributions!
 - Always merge. Everything will break if not.

## DH: Should PyOP2 be in the Firedrake repo? And FInAT in the FIAT repo?
 - Would make dealing with merges easier
 - Also FInAT/FIAT combination would help with element definitions being pulled out of UFL
 - FInAT/FIAT needs careful work due to FInAT depending on GEM which is in TSFC

## JB: We should add some minor namespacing to plotting to avoid hard matplotlib dependency
 - Yes.
 - Might also speed up import

## UZ: NetGen firedrake interface is now very delayed for reasons beyond our control
 - Thanks NetGen!

## Merge PRs

UZ: [https://github.com/firedrakeproject/firedrake/pull/2703](https://github.com/firedrakeproject/firedrake/pull/2703)
 - DH has concerns that introducing a weight property to `DirichletBC` might not be the correct way to do this.
 - We should make the weight be an option for assemble and, for example, make it an argument to `ExplicitMatrixAssembler._apply_bc`. See PR review.

RNH: [VOM voting algorithm](https://github.com/firedrakeproject/firedrake/pull/2773)
 - Merged

JB: [2825](https://github.com/firedrakeproject/firedrake/pull/2825) [2732](https://github.com/firedrakeproject/firedrake/pull/2732) [2842](https://github.com/firedrakeproject/firedrake/pull/2842) [692](https://github.com/OP2/PyOP2/pull/692)
 - 2732 merged
 - 2842 (issue and PR templates) auto-merged
 - pyop2/692 merged

NB: [PyTorch coupling](https://github.com/firedrakeproject/firedrake/pull/2804)
 - See review comments

PB: [FIAT #36](https://github.com/firedrakeproject/fiat/pull/36)
 - Already merged

## Date of next meeting

1600 BST (1500 UTC) [2023-04-05](./Firedrake-meeting-2023-04-05)