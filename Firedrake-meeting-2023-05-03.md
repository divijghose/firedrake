Date and time 2023-05-03 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ALL: Review the [Firedrake manual](https://github.com/firedrakeproject/firedrake/files/11374708/Firedrake.pdf) DONE, see PRs
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: Pick a date for Firedrake User meeting

# Minutes

Present: DD, KS, JB, CW, DH, FA, SK, RK, RNH, PB

Apologies:


## SysGenX + Firedrake meeting
Need to find a date, but these will be the same week and colocated.

## RNH: Slow point evaluation
Discussed here, https://github.com/firedrakeproject/firedrake/discussions/2902
Fixed by my PR https://github.com/firedrakeproject/firedrake/pull/2909

Approved PR 2909.
Approved PR 2784.

## CW: Removing COFFEE
### PRs
- https://github.com/firedrakeproject/firedrake/pull/2899 
(Long no longer issue: https://github.com/firedrakeproject/firedrake/issues/1451)
- https://github.com/OP2/PyOP2/pull/697
- https://github.com/firedrakeproject/tsfc/pull/291
(Update test)

### Discussion points
- Rounding and tolerances for vertex-only meshes (https://github.com/firedrakeproject/firedrake/pull/2899#issuecomment-1531262106)
(It is done.)
- String parloops (https://github.com/firedrakeproject/firedrake/issues/2898)
(Discussion about parloops. Resolved)
## CW: CI Issues/Python version support
Resolved.
- Python 3.7 has been dropped by [loopy](https://github.com/inducer/loopy/blob/main/setup.py#L85) and [UFL](https://github.com/FEniCS/ufl/blob/main/setup.cfg#L40), this is breaking (at least) TSFC and PyOP2 CI.

## Check links
Action item: Only check links on master.

## Merge PRs
JB: Please merge [#2784](https://github.com/firedrakeproject/firedrake/pull/2784)
Merged!

PB: Please merge [#2801](https://github.com/firedrakeproject/firedrake/pull/2801)
Missing comments about safe parallelization and addition of tests.

RNH: Please merge [#2910](https://github.com/firedrakeproject/firedrake/pull/2910) unless the new firedrake manual will cause issues (JB: It won't)
Merged!

# Date of next meeting

1600 BST (1500 UTC) [2023-05-10](./Firedrake-meeting-2023-05-10)