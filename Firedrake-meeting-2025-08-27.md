Date and time 2025-08-27 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (anyone to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Go through issues and mark with "good first issue" for new MSc/PhD contributor projects.
1. LC: Deprecate `.at()` ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-08-13))

# Agenda

Present: DH, KS, LC, RK, JHC, IM, PB, CC

Apologies: CW

NB - Failing tests on CI
- Links - awaiting info from Leeds, links may need to be reactivated
- UFL - FormArgument not resolving. Probably related to recent upstream changes in UFL
- PETSc Line Search failure - upstream API change. Patch Firedrake main now - KS to fix.

## LC: Change missing_points_behaviour API https://github.com/firedrakeproject/firedrake/pull/4524

PR approved. Merged despite tests due to above failures. to be announced to the community as it is an API change.

## LC: Cell location on bendy meshes: https://github.com/firedrakeproject/firedrake/pull/4517

Approved, merged as above

## LC: Fix permutation matrix for Vector/Tensor valued function spaces: https://github.com/firedrakeproject/firedrake/pull/4510

Approved, merged as above

## LC: PointEvaluator: https://github.com/firedrakeproject/firedrake/pull/4516

Changes requested.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

Also reviewed https://github.com/firedrakeproject/firedrake/pull/4515 - API change breaks downstream packages so these will need to be updated
## Date of next meeting

1600 UTC [2025-09-03](./Firedrake-meeting-2025-09-03)