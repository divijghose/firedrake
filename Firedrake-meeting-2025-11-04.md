Date and time 2025-11-04 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. ~LC: Add self to authors list~

# Minutes

Present: CW AC LC DH JHC PB IM

Apologies:

## CW/JHC: Code review process

[FIAT #183](https://github.com/firedrakeproject/fiat/pull/183) (+46,-19), [Firedrake #4684](https://github.com/firedrakeproject/firedrake/pull/4684) (+96,-17), [Firedrake #4658](https://github.com/firedrakeproject/firedrake/pull/4658) (+15), [Firedrake #4430](https://github.com/firedrakeproject/firedrake/pull/4430) (+1102,-129), and [Firedrake #3478](https://github.com/firedrakeproject/firedrake/pull/3478) (+2241,-516) have all been merged in the past couple of weeks without an approving review. Further, some introduced breaking changes that were not announced.

- DH: This should not be happening. PRs need to be approved before being merged. Reviews can be requested when necessary.

## CW: Point evaluation API fixes

What needs to happen with https://github.com/firedrakeproject/firedrake/pull/4675? Shall we merge this ASAP and make a new patch release?

- There are two (related) points: 1) whether to revert to the previous API behaviour as a bugfix for release and 2) questions on how `Function.__call__` should handle numpy arrays.
- Discussion on what shape is/should be returned - e.g. for vector valued functions the return array is flattened for single point evaluations.
- Given that the previous behaviour was inconsistent between evaluating at one or multiple points, we probably want to move to consistent return values.
- What about evaluating an expression not a Function? e.g. `sin(f)(points)`? Do we still want to support this? It's python all the way down so will be pretty inefficient, and it certainly isn't taped.
- TODO: release - revert to previous behaviour, main - do the sensible thing of allowing a user to pass a single position as a rank-1 vector rather than a rank-2 vector with a length 1 dimension.

## JHC: `mesh_unique` breaking API change

(Firedrake #3478)[https://github.com/firedrakeproject/firedrake/pull/3478] changed the return value of `MixedFunctionSpace.mesh()` from a `Mesh` to a `MeshSequence`. There wasn't an approval for this PR so this API change didn't get much (any?) discussion.
It's a fairly major API change that will require changes in a lot of downstream code. Are we happy with this API change?

Can we ease downstream code changes, e.g. a `FunctionSpace.unique_mesh` property that errors if there are multiple meshes?

- This is the right direction to go, but it needs announcing to users.
- `FunctionSpace.mesh().unique()` is the new standard way of getting the single mesh for any `FunctionSpace` (assuming all components are on a single mesh.
- Need to check that `VectorFunctionSpace` returns a `Mesh` not a `MeshSequence` (it inherits from `MixedFunctionSpace`).

## CW: Remove mailing list from website?

https://github.com/firedrakeproject/firedrake/pull/4691

- Yes remove.

## CW: Should we avoid star imports inside Firedrake (specifically in `firedrake.__init__`)?

See [thread](https://firedrakeproject.slack.com/archives/C1Q0Y6H8A/p1762170237704029). To be clear I am not suggesting we change everything now, just that we record it in our [coding guide](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-Coding-Guide) and try to enforce it for new code.

- Yes this is the right thing to do. Add it to the policy and enforce for new code. When someone touches * imports in old code they should update to being specific.

## LC: simplify `interpolate` function

https://github.com/firedrakeproject/firedrake/pull/4582

Looks good, just needs a more descriptive PR title and description for the release notes.

## Merge PRs

LC: UFL interpolate argument numbering logic https://github.com/FEniCS/ufl/pull/425 - added to merge queue.

## Date of next meeting

1600 UTC [2025-11-11](./Firedrake-meeting-2025-11-11)