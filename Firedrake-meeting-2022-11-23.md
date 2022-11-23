Date and time 2022-11-23 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (KS to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Organise Firedrake 2022 (Registration deadline approaching, events apart from talks?, see discussion below)
1. ALL: Rename split (`.split` -> `.subfunctions`) (ongoing - issue created)
1. JB: A Firedrake manual (ongoing)
1. JB: Python 3.11 (ongoing)
1. All: Go through TSFC PRs
1. RNH: check if [issue #2516](https://github.com/firedrakeproject/firedrake/issues/2516) is still a problem, if yes, see if [#2509 Try installing pre-release of VTK from PyPI (supporting Python 3.10)](https://github.com/firedrakeproject/firedrake/pull/2509) fixes (done)
1. JB: Move PyOP2 and FInAT to firedrakeproject (ongoing)
1. ALL: do things with SV's branches

# Agenda

Present: DH, JB, KS, JHC, RNH, DRS, PK, CW (minuter), NB

Apologies:

## DH: Firedrake 2022

- DH: There are train strikes over this week. DH will look into chartering a coach from Imperial to Totnes via Reading, M4 (for Oxford) and possibly Exeter.
- DH: We might have time for extra events that aren't talks. Maybe general discussion, maybe clinic. DH could also do a longer-form presentation on, for example, how the adjoint works.

## DRS: Checkpointing element bug

- DRS: Pickling of UFL elements broken somewhere.
- KS: Could possibly use `__repr__`.
- DH: Simplest case is variant, degree, cell. `__repr__` might not be sufficient.
- Action point: KS to fix serialisation of elements.

## DRS: pyadjoint + ROL

- Action point: DRS to talk to Angus Gibson about interface changes between ROL v1 and ROL v2. Also consider switching to v2.

## JB: PyOP2 `PYOP2_NO_FORK_AVAILABLE` status
The code associated with `PYOP2_NO_FORK_AVAILABLE` is not tested and is broken
(okay **I** broke it, but it's broken beyond this!! ie: loopy forks, maybe other dependencies too).
I think I know why this exists, but is anyone using it, is it still worth maintaining and testing?

- DH: Realistically all clusters are Linux and no users have hit this. Dropping it is probably safe.
- Action point: JB go ahead and expunge.

## Merge PRs

1. JHC: Additional MPI methods for Ensemble [#2639](https://github.com/firedrakeproject/firedrake/pull/2639) - reviewed
1. CW: Halo freezing: [Firedrake](https://github.com/firedrakeproject/firedrake/pull/2635) and [PyOP2](https://github.com/OP2/PyOP2/pull/680) - merged
1. JB: [GC Fix #2599](https://github.com/firedrakeproject/firedrake/pull/2599) been round once before, DEFCON now has a fix, are we ready? - to resolve in separate meeting with DH
1. JB: [Python 3.11 #2358](https://github.com/firedrakeproject/firedrake/pull/2358), is this ready? Mac users? - not yet, homebrew ML bugs etc

## Date of next meeting

1600 UTC [2022-12-07](./Firedrake-meeting-2022-12-07)
