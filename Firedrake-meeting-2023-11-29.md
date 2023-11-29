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

# Minutes

Present: CW, DH, DD (minuter), KS, NB, PB, RK, IM, RNH, FA

Apologies: JB

## PB: MixedFunctionSpace([primal, dual])

Currently `V * V.dual() == V * V` is wrong, and `is_primal(V * V) == True` goes against the original design. We need a better wrapper class for MixedFunctionSpace (as opposed to `WithGeometry`) or change what a MixedFunctionSpace is in ufl. The PR where we introduce `V.reconstruct()` should not address this.

The PR [reconstruct FunctionSpace](https://github.com/firedrakeproject/firedrake/pull/3241) is involved with this issue.

## DD: about the petsc message errors in `firedrake_adjoint` tests.
Actually, the test message error appears for every single firedrake tests. 
For an unknowing reason (at least for me) the flag `python3 -m pytest --cov` hides (or fixes?) these message errors in firedrake tests. The original problem is in `petsc4py.init(sys.args)`. See the [PR #3260](https://github.com/firedrakeproject/firedrake/pull/3260)

DH suggestion: Try to give the arguments from petsc.

## DD: Build a [install FAQ](https://github.com/firedrakeproject/firedrake/wiki/Install-Frequently-Asked-Questions) at firedrake wiki.

DH suggestion: Keep the text at the wiki and Pin the install FAQ in the discussions.

## Merge PRs (ideally already reviewed)

- PB: [ufl #246](https://github.com/FEniCS/ufl/pull/246)

This PR stops many of ufl warnings. PR approved.

- PB: [tsfc #304](https://github.com/firedrakeproject/tsfc/pull/304)

PR approved.

- PB: [Expunge ufl_domain #3259](https://github.com/firedrakeproject/firedrake/pull/3259)

PR approved.

- PB: [HypreAMS easy fix](https://github.com/firedrakeproject/firedrake/pull/3252)

PR approved.

- PB: [reconstruct FunctionSpace](https://github.com/firedrakeproject/firedrake/pull/3241)

PR approved.

- KS: [#3174](https://github.com/firedrakeproject/firedrake/pull/3174)

This PR requires changes. RNH will review this.

- KS: [#3240](https://github.com/firedrakeproject/firedrake/pull/3240)

PR approved. Related to periodic mesh in firedrake.

- NB: [#3274](https://github.com/firedrakeproject/firedrake/pull/3274) (very easy one)

PR Approved. Fix bug cofunction equality.

# Date of next meeting

1600 GMT (1600 UTC) [2023-12-06](./Firedrake-meeting-2023-12-06)