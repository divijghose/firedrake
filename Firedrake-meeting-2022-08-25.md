Date and time 2022-08-25 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (JB to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (ongoing)
1. JB: SIAM CSE23 Minisymposium/minisymposterium
1. ~~DH: Produce an MFE for "adjoint of Interp" issue~~ - RESOLVED

# Agenda

Present: CW (minuter), DH, RNH, SV, KS, JB, RK

Apologies: 

## JB: Rescheduling of this meeting

- JB: In on Tuesdays and Thursdays
- DH: In on Wednesday next week
- No meeting for next week
- DH: Aim for 4pm so US can attend
- RK: Monday, Wednesday, Friday all work

## JB: CSE23 minisymposium

- JB: 5 confirmed. Still waiting on Jack Hale. 2 slots for Firedrakers left. These can be given to JB and CW.

## DH: EGU

- DH: Plans are afoot

## DH: Firedrake 22

- DH: Guest speaker from Dedalus ('spectral element Firedrake')

## KS: I/O

- PETSc MR merged
- Firedrake fork updated
- https://github.com/firedrakeproject/firedrake/pull/2461 now ready

- Approved and ready to go.

## DH: Firedrake UFL fork Serendipity elements

- DH: Some elements got merged into the Firedrake UFL fork and not into FEniCS UFL creating an unnecessary conflict.
- RK: Keep ENF in UFL, make them go to cubes, yank div and curl, get merged to FEniCS then propagate through Firedrake. **Action point DH**

## KS: Archer2

- OFI (implementation of MPI) network seems working (can achieve ~4.5 [GiB/s])
- UCX (which is supposed to be better) is still not working

- JB: This is the fabric layer. Archer 2 supports two (which is unusual for clusters). UCX is supposed to be substantially better.
- KS: PETSc works fine with UCX, but Firedrake breaks.
- DH: Try to create a MFE (maybe with mpi4py) **Action point KS**

## Merge PRs

## Date of next meeting

Next meeting: Not next week

1600 UTC [2022-09-08](./Firedrake-meeting-2022-09-08)
