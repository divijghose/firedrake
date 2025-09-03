Date and time 2025-09-03 1600 UTC

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

Present: AA, LC (minuter), DH, KS, CW, JHC

Apologies: IM, PB

## CW: Remove `firedrake-jupyter` Docker image

https://github.com/firedrakeproject/firedrake/pull/4512/

nobody using it, remove it
Merged.

## LC: `PointEvaluator`

https://github.com/firedrakeproject/firedrake/pull/4516

Add comment to `.evaluate` method stating that this returns a numpy array and is not compatible with firedrake-adjoint.

Open issue pointing out issue with moving the parent mesh of a VOM. The fix in `Pointevaluator` is fine for now but ideally needs to be one level lower.

## LC: Remove `Interpolator.interpolate`

https://github.com/firedrakeproject/firedrake/pull/4531

Keep `._interpolate` for now. After next release we can rename it back to `.interpolate`.

Keep `.interpolate` and make it return an error telling users to use symbolic `interpolate` function.

## JHC: `petsctools.AppContext` review

The Firedrake PR isn't ready to go yet, so at this stage I'm mainly looking for feedback on the `AppContext` class.

https://github.com/firedrakeproject/petsctools/pull/16

`AppContext` class - like petsc options for arbitrary data

Split docstring code-block into two. 

petsctools needs actual documentation. 

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

## Date of next meeting

1600 UTC [2025-09-10](./Firedrake-meeting-2025-09-10)