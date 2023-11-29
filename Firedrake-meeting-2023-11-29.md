Date and time 2023-11-29 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))? JB: Waiting for https://github.com/Toblerity/rtree/pull/292
1. DD: Investigate adjoint test fails in teardown ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-11-22#jb-pyadjoint-firedrake-tests-erroring))

# Agenda

Present:

Apologies: JB

## PB: MixedFunctionSpace([primal, dual])

Currently `V * V.dual() == V * V` is wrong, and `is_primal(V * V) == True` goes against the original design. We need a better wrapper class for MixedFunctionSpace (as opposed to `WithGeometry`) or change what a MixedFunctionSpace is in ufl. The PR where we introduce `V.reconstruct()` should not address this.

## DD: about the petsc message errors in `firedrake_adjoint` tests.
Actually, the test message error appears for every case. 
For an unknowing reason (at least for me) the flag `-cov` hides (or fixes?) these message errors. See the PR [#3260](https://github.com/firedrakeproject/firedrake/pull/3260).

## DD: Build a [FAQ](https://github.com/firedrakeproject/firedrake/wiki/Frequently-Asked-Questions-(FAQ)) at firedrake wiki.

## Merge PRs (ideally already reviewed)

- PB: [ufl #246](https://github.com/FEniCS/ufl/pull/246)
- PB: [tsfc #304](https://github.com/firedrakeproject/tsfc/pull/304)
- PB: [Expunge ufl_domain #3259](https://github.com/firedrakeproject/firedrake/pull/3259)
- PB: [HypreAMS easy fix](https://github.com/firedrakeproject/firedrake/pull/3252)
- PB: [reconstruct FunctionSpace](https://github.com/firedrakeproject/firedrake/pull/3241)
- DD: [#3260](https://github.com/firedrakeproject/firedrake/pull/3260)
- KS: [#3174](https://github.com/firedrakeproject/firedrake/pull/3174)
- KS: [#3240](https://github.com/firedrakeproject/firedrake/pull/3240)
- NB: [#3274](https://github.com/firedrakeproject/firedrake/pull/3274) (very easy one)

# Date of next meeting

1600 GMT (1600 UTC) [2023-12-06](./Firedrake-meeting-2023-12-06)