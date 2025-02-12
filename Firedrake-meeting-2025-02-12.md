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
1. ~CW: Fix artefactsv3 issue~ (done by DD for pyadjoint, no other instances found)
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: PB, DH, KS, DD, CC, JHC, RK, CW, IM, LC

Apologies:

## CW: Finally remove `.split()` merged

[#4204](https://github.com/firedrakeproject/firedrake/pull/4024)

The main controversy is renaming `.subfunctions` to `.subspaces` for function spaces. I think this was just a silly mistake we made when deprecating `.split()`.

We don't want to merge it now as we want to announce it on Slack first and then merge later this week.

## JHC: [`EnsembleFunction`](https://github.com/firedrakeproject/firedrake/pull/4025)
New set of classes for representing finite element spaces/functions distributed over an `Ensemble`. Provides some collective semantics and operations that are either useful (e.g. dealing with one `EnsembleFunction` rather than lists of `Function` on each ensemble member), or downright necessary (e.g. `_ad_dot` to be able to create `ReducedFunctionals` over an `Ensemble` that actually passes the Taylor tests).

Still in draft form, I'm just looking for any feedback at this stage. See the description in the PR for more detail.

## DH/CW PETSc updates

[#3997](https://github.com/firedrakeproject/firedrake/pull/3997) before [#3999](https://github.com/firedrakeproject/firedrake/pull/3999). Note that we expect the other workflows to fail because they are using the wrong PETSc (from the container).

`DMSwarm` API changed, we need to adopt the new API
`DMSwarm_cellid` is now a variable that has to be accessed

We put our options and then pull them out, this incorrectly raised "unused options" warnings.
Options which have not been used from our solvers are only those for which we raise warnings.
Failing tests with large number of solver options. Needs more work.

## CW: Gusto smoke tests

[#4017](https://github.com/firedrakeproject/firedrake/pull/4017)

We should let other downstream packages know that we have done this so they can also submit a small set of tests to run.

CW: Time limit is 5 min. Takes 2 min.

CW: We want to do this for thetis, Irksome, ...

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

DD: [#4023](https://github.com/firedrakeproject/firedrake/pull/4023) Move `firedrake_adjoint` tests from pyadjoint to `firedrake/tests/firedrake/adjoint`. merged

DD: [#192](https://github.com/dolfin-adjoint/pyadjoint/pull/192) Remove `firedrake_adjoint` tests from pyadjoint. merged

PB: [FEniCS-style bcs](https://github.com/firedrakeproject/firedrake/pull/3995) merged

PB: [Subclass LinearSolver](https://github.com/firedrakeproject/firedrake/pull/4012) review half of it, DH concluded that this is adjoint-safe 

# Date of next meeting
1600 UTC [2025-02-19](./Firedrake-meeting-2025-02-19)