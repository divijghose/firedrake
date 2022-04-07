Date and time 2022-04-07 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (KS to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: CW (minuter), KS, DH, SV

Apologies: JB :sneezing_face: 

## Error on DP on quads? (DH)

We've been warning on DP on Quads for ever. Should we actually kill it? Now that we have DPC, DP is ambiguous.

DH: There are two discontinuous spaces on quads: DQ + DP. Currently interpret 'DP' as 'DQ' and spew warning.
DH: Action point: Now throw error on DP.

## Arm bugs (DH)

DH: Need to set additional LDFLAGS in PyOP2 compilation. But it is compiler version dependent so we need to sniff the compiler.
Action point: Give this to JB.

## KS:

PR: Only include components of mixed functions that are actually used

https://github.com/firedrakeproject/firedrake/pull/2364

Just needs a bit of documentation.

## Merge PRs

CW:

- https://github.com/firedrakeproject/firedrake/pull/2348
- https://github.com/firedrakeproject/tsfc/pull/268

These are ready to go but need to drop branch commit.

- https://github.com/firedrakeproject/firedrake/pull/2395

Merged

## Date of next meetings

* 2022-04-14 is not a work day at Imperial
* 2022-04-28 clashes with Firedrake Australia

Next meeting: 2022-04-21
