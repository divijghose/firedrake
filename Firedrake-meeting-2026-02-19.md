Date and time 2026-02-19 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: DH LC RK IM CW PB AC JHC

Apologies:

## CW: Quick policy question

Sia (G-ADOPT) has opened a PR but needs approval to run the workflow. That's definitely silly.

- Yes Sia should have access, they can be added to the Firedrake contributors list (contributors have access without superpowers).

- DH action point: cull inactive members of github project teams?

Similarly, what's our policy towards adding authors?

- CW action point: try and draft something up for when you get added to contributors/authors/maintainers etc lists.

## CW/PB: AI generated code

https://github.com/firedrakeproject/firedrake/pull/4878

And now also: https://github.com/firedrakeproject/firedrake/pull/4903

Draft policy: https://github.com/firedrakeproject/firedrake/wiki/AI-contribution-policy

Contributions that are wholly or majority created by an AI agent?
- Has the person run the code locally? If not then its potentially wasting reviewer time.
- CW: See recent hit piece from matplotlib AI "contributor"???
- If there are large blocks of code generated, how do we know there aren't any licensing issues?
- DH Suggestion: Contributor should be in a position to license us the code?? (i.e. can you guarantee it isn't breaking training data licenses?). e.g. the `cached_property` PR is just search-replace has no ideas or logic in so there's no chance of it having licensing issues.
- What if we want to keep "good first issues" for actual users as small tasks for new contributors to learn the ropes?
- Policy point about author being able to explain (and justify) the changes is very important (in general but especially for non-human generated code).

## JHC/CW: checkpointing performance issue

https://github.com/firedrakeproject/firedrake/pull/4891

What's the right abstraction?

- The new locally-saving-a-function functionality should be abstracted into its own thing rather than being inserted into the CheckpointFunction.
- Making a new class is a good way to do it to make it really clear that it is not interchangeable with `CheckpointFile` (can't checkpoint a mesh, need identical partition at save/load etc).

## LC: Build spatialindex with array operations rather than loops

https://github.com/firedrakeproject/firedrake/pull/4865

Merged.

- For the future: LC has found a faster implementation than libspatialindex that we could move over to. This wouldn't remove libspatialindex as a dependency because of libsupermesh.

## LC: bounding box calculation optimisation

https://github.com/firedrakeproject/firedrake/pull/4900

Merged.

## LC: parent_mesh_embedding optimisation

https://github.com/firedrakeproject/firedrake/pull/4906

Looks fine but make sure CI passes before we merge.

## Merge PRs

## Date of next meeting

1600 UTC [2026-02-26](./Firedrake-meeting-2026-02-26)
