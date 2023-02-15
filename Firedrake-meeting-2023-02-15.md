Date and time 2023-02-15 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: A Firedrake manual
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements

# Agenda

Present: DS, JB, DH, CW, RNH, FA, RK, NB

Apologies:

## JB: Firedrake manual

Branch got merged to master. Need to pick a release date.

-> JB: Add instructions explaining how to build manual

## KS: Fix checkpointing error with pickling elements

-> KS: Use Firedrake's UFL fork and not Fenics' one because of the PR that accidentally got merged in Firedrake UFL instead of upstream

## DRS: PasTiX / Fortran

Check for existing open issues

-> DS: Check if Fortran can be built with PasTix, if not that might be an issue on PETSc land.

## Merge PRs

RNH: [Firedrake: VertexOnlyMesh on ExtrudedMesh #2750](https://github.com/firedrakeproject/firedrake/pull/2750): Approved

RNH: [FIAT: Add methods for getting L1 distance of a point from reference cells #33](https://github.com/firedrakeproject/fiat/pull/33): Merged

RNH: [Firedrake: Guarantee finding cell for point on boundary #2662](https://github.com/firedrakeproject/firedrake/pull/2662): Minor changes requested

CW: [Firedrake: Respect MACOSX_DEPLOYMENT_TARGET environment variable if set #2770](https://github.com/firedrakeproject/firedrake/pull/2770): Merged

CW: [Firedrake:  Add zero utility method to Function #2769 ](https://github.com/firedrakeproject/firedrake/pull/2769): Minor changes requested

CW: [Refactor parallel test markers #2763](https://github.com/firedrakeproject/firedrake/pull/2763): Approved


## Date of next meeting

1600 UTC [2023-02-22](./Firedrake-meeting-2023-02-22)