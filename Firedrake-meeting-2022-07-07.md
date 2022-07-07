Date and time 2022-07-07 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (KS to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022
1. JB: SIAM CSE23 Minisymposium/minisymposterium

# Agenda

Present: DH, CW (minuter), JB, RNH, KS, PB, SV, RK

Apologies:

## DH: Adjoint checkpointing is landed

- DH: We now have lazy taping of values. It is only copied if it is used as an input later on.

## DH: Assemble expression and assign

- DH: `assign` can do a number of 'dodgy' pointwise evaluations (e.g. `y.assign(y*y)`). Ultimately only weighted sums are valid, otherwise you are doing backdoor interpolation.
- DH: Adjoint to assign is a problem, and causes problems with external operators.
- DH: Advocates removing this functionality and forcing users to switch to interpolation when needed.
- DH: Main use case of `assign` is in timestepping loops, and this will be unaffected as these really are weighted sums.

## CSE23

- DH: We could possibly do a minisymposterium on "Software for PDEs" so that we can have additional speakers.
- RK: The next next CSE (2025) will be held in Fort Worth (Texas).

## Merge PRs

None

## Date of next meetings
Next meeting: 1200 UTC [2022-07-21](./Firedrake-meeting-2022-07-21)

