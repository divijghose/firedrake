Date and time 2025-11-04 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. LC: Add self to authors list

# Agenda

Present:

Apologies:

## CW/JHC: Code review process

[FIAT #183](https://github.com/firedrakeproject/fiat/pull/183) (+46,-19), [Firedrake #4684](https://github.com/firedrakeproject/firedrake/pull/4684) (+96,-17), [Firedrake #4658](https://github.com/firedrakeproject/firedrake/pull/4658) (+15), [Firedrake #4430](https://github.com/firedrakeproject/firedrake/pull/4430) (+1102,-129), and [Firedrake #3478](https://github.com/firedrakeproject/firedrake/pull/3478) (+2241,-516) have all been merged in the past couple of weeks without an approving review. Further, some introduced breaking changes that were not announced.

## CW: Point evaluation API fixes

What needs to happen with https://github.com/firedrakeproject/firedrake/pull/4675? Shall we merge this ASAP and make a new patch release?

## JHC: `mesh_unique` breaking API change

(Firedrake #3478)[https://github.com/firedrakeproject/firedrake/pull/3478] changed the return value of `MixedFunctionSpace.mesh()` from a `Mesh` to a `MeshSequence`. There wasn't an approval for this PR so this API change didn't get much (any?) discussion.
Its a fairly major API change that will require changes in a lot of downstream code. Are we happy with this API change?

Can we ease downstream code changes, e.g. a `FunctionSpace.unique_mesh` property that errors if there are multiple meshes?

## CW: Remove mailing list from website?

https://github.com/firedrakeproject/firedrake/pull/4691

## CW: Should we avoid star imports inside Firedrake?

See [thread](https://firedrakeproject.slack.com/archives/C1Q0Y6H8A/p1762170237704029). To be clear I am not suggesting we change everything now, just that we record it in our [coding guide](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-Coding-Guide) and try to enforce it for new code.

## Merge PRs

## Date of next meeting

1600 UTC [2025-11-11](./Firedrake-meeting-2025-11-11)