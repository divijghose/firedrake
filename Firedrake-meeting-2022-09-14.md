Date and time 2022-09-14 15:00UTC (16:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (KS pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (ongoing)
1. JB: SIAM CSE23 Minisymposium/minisymposterium

# Agenda

Present: 

Apologies: 

## ~~JB: Status of PETSc/petsc4py GC MR~~
Since rebasing this now has more memory leaks and needs fixing before it will pass tests. Perhaps revisit this next week.

## CW: `assign` performance issues worth fixing?

I recall that DH described `assign` as equivalent to `interpolate` in many cases and that potentially `assign` would be pared back to only work for the cases where it actually makes sense. TK recently found a performance issue in `assign` that would require a relatively invasive change to fix. Is it worth me spending time on a fix if we're about to change things anyway?

## Merge PRs

## Date of next meeting

Next meeting: Not next week

1600 UTC [2022-09-21](./Firedrake-meeting-2022-09-21)
