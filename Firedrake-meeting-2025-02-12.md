Date and time 2025-02-12 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: Fix artefactsv3 issue
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present:

Apologies:

## CW: Finally remove `.split()`

[#4204](https://github.com/firedrakeproject/firedrake/pull/4024)

The main controversy is renaming `.subfunctions` to `.subspaces` for function spaces. I think this was just a silly mistake we made when deprecating `.split()`.

## JHC: `EnsembleFunction`
New set of classes for representing finite element spaces/functions distributed over an `Ensemble`. Provides some collective semantics and operations that are either useful (e.g. dealing with one `EnsembleFunction` rather than lists of `Function` on each ensemble member), or downright necessary (e.g. `_ad_dot` to be able to create `ReducedFunctionals` over an `Ensemble` that actually passes the Taylor tests).

Still in draft form, I'm just looking for any feedback at this stage. See the description in the PR for more detail.


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

DD: [#4023](https://github.com/firedrakeproject/firedrake/pull/4023) Move `firedrake_adjoint` tests from pyadjoint to `firedrake/tests/firedrake/adjoint`.

DD: [#192](https://github.com/dolfin-adjoint/pyadjoint/pull/192) Remove `firedrake_adjoint` tests from pyadjoint.

# Date of next meeting
1600 UTC [2025-02-19](./Firedrake-meeting-2025-02-19)