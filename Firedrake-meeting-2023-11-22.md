Date and time 2023-11-22 1600 GMT (1600 UTC)

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
1. NB: Look for changes needed to manual to account for dual spaces

# Minutes

Present: CW (minuter), DD, JB, KS, DH, RNH, PB, NB, JHC, IM, FA

Apologies:

## JB: Pyadjoint Firedrake tests erroring
[#3247](https://github.com/firedrakeproject/firedrake/issues/3247)

* JB: PETSc errors are getting raised in `PetscFinalize` in the Firedrake pyadjoint tests.
* JB: Solution should be able to catch this in future.
* DD: Issue is somehow related to pytest-xdist (i.e. `pytest -n ???`).
* Action point DD: Investigate further.

## TB: What guarantees does Firedrake provide that checkpoints will survive `firedrake-update`?

* DH: No guarantees are made for the ordering between checkpoint files and meshes. To make comparisons one needs to load the mesh from the checkpoint.
* DH: Could possibly use interpolation to get this to work. One can take a spanning DG space and interpolate into it.
* DH: If FE definitions changes (e.g. PB changing Lagrange) then these guarantees do not hold. One could add a check here where we do an interpolation and make sure that the interpolation matrix is the identity.

## JB: Separate Matplotlib
This is PR 3117 below. CW suggests this is worth wider discussion.

* CW: This is currently an API change since plotting functions would no longer be in the `from firedrake import *`.
* DH: We should replace the moved functions in the global namespace with functions that raise a hard error and point users to the right function to call.
* DH: We could follow the same approach for making VTK optional.
* DH: Could have a policy that external dependencies should be truly optional.

## JB: Public interface to GC
This is PR 3152 below. CW suggests this is worth wider discussion. JB thinks this should really only be a semi-public interface, excessive calls to this functionality will be disastrous for performance!

* DH: Fine for GC routines to be out of the public namespace.
* DH: `garbage_cleanup` should crash if a communicator is not found.
* DH: Let's keep the `atexit` comm cleanup stuff. No real reason to get rid of it.

## CW: Docs currently failing, what's the status of the fix?

See below.

## DD: Users are having errors on installing Firedrake with Xcode15
and apparently, Xcode15 has sorted this issue.

See the PR 3249

## DD: Documentation building is now working with the PR 3239.

JB and I were trying to move the documentation for numpydoc format. 

Merged, build is fixed. The transition to numpydoc remains outstanding.


## Merge PRs

- PB: [FIAT #54](https://github.com/firedrakeproject/fiat/pull/54) - merged
- PB: [FInAT #115](https://github.com/FInAT/FInAT/pull/115) - merged
- PB: [MG easy fix](https://github.com/firedrakeproject/firedrake/pull/3246) - merged
- PB: [reconstruct FunctionSpace](https://github.com/firedrakeproject/firedrake/pull/3241) - feedback given, `MixedFunctionSpace`s can contain primal and dual spaces
- JHC: [sort FormSum.coefficients](https://github.com/FEniCS/ufl/pull/243) - merged
- JB: [#3117](https://github.com/firedrakeproject/firedrake/pull/3117) Separate out Matplotlib - see discussion above
- JB: [#3152](https://github.com/firedrakeproject/firedrake/pull/3152) A public interface to the garbage collector (for those who _really_ want one, not that I am encouraging anyone to actually use it!): - see discussion above
  + Look at in this order: [#3152](https://github.com/firedrakeproject/firedrake/pull/3152), [#3229](https://github.com/firedrakeproject/firedrake/pull/3229), [PyOP2 #711](https://github.com/OP2/PyOP2/pull/711), [PyOP2 #712](https://github.com/OP2/PyOP2/pull/712)
  + Needs merging in this order: [#3229](https://github.com/firedrakeproject/firedrake/pull/3229), [PyOP2 #712](https://github.com/OP2/PyOP2/pull/712), [PyOP2 #711](https://github.com/OP2/PyOP2/pull/711), [#3152](https://github.com/firedrakeproject/firedrake/pull/3152)
- PB: [HypreAMS easy fix](https://github.com/firedrakeproject/firedrake/pull/3252)
- KS: [#3174](https://github.com/firedrakeproject/firedrake/pull/3174)
- DD: [#3239](https://github.com/firedrakeproject/firedrake/pull/3239) - merged
- DD: [#3250](https://github.com/firedrakeproject/firedrake/pull/3250)
- JHC: [3235](https://github.com/firedrakeproject/firedrake/pull/3235) - more discussion/thought required

# Date of next meeting

1600 GMT (1600 UTC) [2023-11-29](./Firedrake-meeting-2023-11-29)
