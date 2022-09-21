Date and time 2022-09-14 15:00UTC (16:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (SV pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (done? maybe we can take this out for now)
1. JB: SIAM CSE23 Minisymposium/minisymposterium

# Minutes

Present: David, Scott, Rob, Reuben, Connor, Daiane, Colin, Jack, Koki, Nacime, Me

Apologies: 

## Firedrake"22"
- 4th-6th of January, down of Exeter, co-organised with Jemma and Nele
- invited speakers are not finalised yet
- 48 hour meeting

## ~~JB: Status of PETSc/petsc4py GC MR~~
Since rebasing this now has more memory leaks and needs fixing before it will pass tests. Perhaps revisit this next week.

## CW: `assign` performance issues worth fixing?

I recall that DH described `assign` as equivalent to `interpolate` in many cases and that potentially `assign` would be pared back to only work for the cases where it actually makes sense. TK recently found a performance issue in `assign` that would require a relatively invasive change to fix. Is it worth me spending time on a fix if we're about to change things anyway?
- problem is that rhs can be anything
- assign should only weights sum of things in the same space (unless maybe different components in the same vector space)
- @Connor don't bother fix the performance bug

## RK: Irksome's docs builds are failing

## Merge PRs

## Date of next meeting

1600 UTC [2022-09-21](./Firedrake-meeting-2022-09-21)
