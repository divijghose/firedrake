Date and time 2022-12-14 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Organise Firedrake 2022 (Chartering a coach, events apart from talks?)
1. JB: A Firedrake manual
1. JB: Python 3.11
1. All: Go through TSFC PRs
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements
1. DRS: Fix ROL/pyadjoint versioning issues with Angus Gibson
1. JB: **Buy a new laptop!**

# Minutes

Present: UZ CW RNH DH JB KS NB PK

Apologies:

## DH: Firedrake22
Coach is organised, DH to send email with timings but leaving 0800 4th Jan from Imperial College.

Name badges are coming, but no glasses :slightly_frowning_face: 

## DH: Python 3.11 on Mac
Now working on ARM Mac, just need to test on Intel Mac.

## KS: Fix checkpointing error with pickling elements
Can't test locally due to broken MPI.

DH: When checkpointing was pickling finite elements, but this doesn't work since upstream changes in UFL.

## Merge PRs

UZ: [#2607](https://github.com/firedrakeproject/firedrake/pull/2607), changes requested (see PR for comments). Needs to be more abstraction and look less like PETSc code.

~~JB: [#2358](https://github.com/firedrakeproject/firedrake/pull/2358)~~

KS: [#2682](https://github.com/firedrakeproject/firedrake/pull/2682), changes requested.

NB: [#2550](https://github.com/firedrakeproject/firedrake/pull/2550), missing performance results? See Melina's Masters Thesis

## Date of next meeting

1600 UTC [2023-01-11](./Firedrake-meeting-2023-01-11)

