Date and time 2026-03-26 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (IM to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. DH: Trim github organisation teams member.

# Agenda

Present: 

Apologies: JHC

## PB/CW: ngsPETSc breaking change?

The breaking change has already been merged in https://github.com/NGSolve/ngsPETSc/pull/93. 
We stopped supporing MeshHierarchy + Netgen CSG in favour of Netgen OCC to support creating netgen meshes from a refined DMPlex.
Netgen CSG meshes cannot snap the plex points to the boundary. This means that linear refined meshes do not snap and trying to curve this mesh results in a segfault. 

## CW: https://github.com/firedrakeproject/firedrake/pull/4993

## CW: https://github.com/firedrakeproject/firedrake/pull/4836

Needs a full review from someone please.

## Merge PRs

## Date of next meeting
Meeting times going forward: Tuesday 4pm unless David has a monthly meeting, in which case Tuesday 3pm. First Tuesday meeting 31st March.

1600 UTC [2026-03-19](./Firedrake-meeting-2026-03-19)