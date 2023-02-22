Date and time 2023-02-22 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ALL: Review the Firedrake manual
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements

# Minutes

Present: DH, JB, CW, KS, RK, RNH

Apologies: NB

## DH: Update
Meeting with KS and IM, definitively answer "how to deal with orientations?" Open questions, Zany + Pullbacks.

SysGenX meeting in Oxford will discuss this further.

## JB: Master Failing

Action JB: give Connor access to CI runners

JB: Can't reproduce locally or on runners.

Action CW: try to reproduce hanging test

## Merge PRs

RNH: [#2780](https://github.com/firedrakeproject/firedrake/pull/2780) -> Merged

KS: [#2582](https://github.com/firedrakeproject/firedrake/pull/2582) (periodic extrusion) -> Changes requested, mainly documentation fixes, see PR

KS: [#2778](https://github.com/firedrakeproject/firedrake/pull/2778) -> Needs tests, see next PR

KS: [#2682](https://github.com/firedrakeproject/firedrake/pull/2682) -> Do not refer to `MeshGeometry` as it isn't in the public API

DH Added MeshGeometry and MeshTopology to public API.

## Date of next meeting

CSE23 is next week!

1600 UTC [2023-03-08](./Firedrake-meeting-2023-03-08)