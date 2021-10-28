Date and time 2021-10-28 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Minutes

Present: KS, JB, DH, NB, CW, CC, LM, SV

Apologies:

## KS: Subspace preparation PRs (cont.)

Firedrake https://github.com/firedrakeproject/firedrake/pull/2200

tsfc: https://github.com/firedrakeproject/tsfc/pull/261

Viewed commits one by one, starting where we left off last week. Suggested changes added to the PR.

Action KS: Make suggested changes (esp. Documentation).

This commit refactors and covers part of the work in #234, next PR will add functionality.

## CW: PCPATCH discussion

CW: Want to move from PETSc handling looping to something in PyOP2.

LM: Decomp mesh into little pieces and solve problems on pieces. Looping over list of pieces happens in PETSc, PETSc calls back to user provided functions to do assembly on the patch. Local dat and local mat are used to handle local indexing on patches.

LM: Magic C code for SNES patch is even more disgusting (but 40x speed up).

DH: We want to make PyOP2 more PETSc aware.

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-11-04](./Firedrake-meeting-2021-11-04/)