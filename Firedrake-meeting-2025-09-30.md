Date and time 2025-09-30 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Go through issues and mark with "good first issue" for new MSc/PhD contributor projects.
1. LC: Deprecate `.at()` ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-08-13))

# Minutes

Present: CW (minuter), DH, PB, JHC, KS, LC, AG, IM, CC

Apologies:

## DH/LC `.at()` deprecation

* DH: Will be inconvenient for Thetis folk. VoM not currently fast enough for particle tracking (which is also the issue with `streamplot`).
* DH: Thetis will have to use `._at()` until this is fixed.

## CW: Should we release 2025.4.3?

Hear me out. When we make new releases of UFL, pyadjoint, FIAT etc then 2025.4.2 will break because we do not constrain their versions ([eg](https://github.com/firedrakeproject/firedrake/blob/release/pyproject.toml#L22)). Users know that we will stop maintaining 2025.4.x when we release 2025.10.0, but this will soften the transition.

* DH: Yep. Do this.
* JHC: PETSc have released, green light.
* DH: And for the next release do the merge in a PR and check that `main` branches of downstream packages pass.
* CW: I want to make the release from a branch that is not actually `release`. That means that we can test upstream `release` branches in our own `release` CI.
* DH: And tell people in announcement that we won't patch 2025.4.x any more.

## PB: Code-generation for matfree adjoint Interpolation

[Part 1: 0-form, 1-form adjoint](https://github.com/firedrakeproject/firedrake/pull/4552)

[Part 2: 2-form adjoint](https://github.com/firedrakeproject/firedrake/pull/4576)

[Part 3: Mixed, MatNest](https://github.com/firedrakeproject/firedrake/pull/4596)

* Mostly approved.

## Merge PRs

Merged #4585 and #4598

## Date of next meeting

**IMPORTANT: now on Tuesdays!**

**NOTE: 07/10/25 is a UCU strike day**

1600 UTC [2025-10-07](./Firedrake-meeting-2025-10-07)
