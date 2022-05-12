Date and time 2022-05-12 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (CW to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. CW/KS: Test PETSc main against current Firedrake (passed on to Koki)
1. JB: Look into updating the `@parallel` test marker (ongoing)


# Minutes

Present: DH, JB, CC, RK, JHC, SV, CW, KS

Apologies:

## CC: Multigrid on Emmersed manifold

CC: Has `ManifoldTransfer` class to move coordinates. Can we merge this into Firedrake?

DH: Rather than writing those details, instantiate `TransfreManager`(TM) and stash things; this way it is more self-contained in the TM at least.

CC: Make a PR.

JB: Relevant?
https://github.com/firedrakeproject/firedrake/issues/2185

https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2021-08-18#rnhjb-mesh-dmcoordinates-field-disconnect

## CC: Time parallel checkpoininting

DH:

- 1st option. Just open HDF5 file with "COMM_WORLD" and write from subcommunicator.
- 2nd option. Schedule who has got file open and one subcomm writes at a time using "-a".

## Merge PRs

## Date of next meetings

Next meeting: [2022-05-19](./Firedrake-meeting-2022-05-19)

