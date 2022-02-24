Date and time 2022-02-24 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (KS to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: LM DH JB RK KS DS PK CW SV

Apologies: 

## JB: libspatialindex
Do we need to maintain a fork of libspatialindex, or can we fix the version and use upstream?

Either way we need to update, we can't currently compile the fork (with the Intel compiler).

Jack's doing this for spack purposes. Deeper question bc we should speak same coordinate language as PETSc. Grid hashing doesn't work for high order coordinates (but probs libspatialindex neither).

Massive conversation about if we could replace TSFC and use CEED efforts instead.

## LM: test suite warnings

These pollute stuff, someone needs to fix it.

Variant warning is one of them. Solution a) remove the warning b) actually make the change
There are more...

## Merge PRs
#2349
#2357

## AOB

## Date of next meeting

1600 UTC (1600 GMT) [2022-03-03](./Firedrake-meeting-2022-03-03/)
