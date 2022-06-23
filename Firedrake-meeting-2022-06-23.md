Date and time 2022-06-23 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS: Test PETSc main against current Firedrake
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022
1. ?: Decide who will organise SIAM CSE23 Minisymposium/minisymposterium

# Agenda

Present: JB, DH, AM, KS, JW, RNH, CW, SK, SV, RK

Apologies:

## RNH and Joe Walwark: Plex to Plex interpolation
Joe has 2 new parallel plex-to-plex interpolation MRs on PETSc: [#5345](https://gitlab.com/petsc/petsc/-/merge_requests/5345) and [#5354](https://gitlab.com/petsc/petsc/-/merge_requests/5354). How can we best get this working with Firedrake? My (RNH's) thoughts are:
 - DMSwarmSetPointCoordinates (which we called prior to the merging of [#2437](https://github.com/firedrakeproject/firedrake/pull/2437)) calls DMLocatePoints which, were we to revert to using it, would solve the issue of out-of-rank points (see issue [#2178](https://github.com/firedrakeproject/firedrake/issues/2178) and discussion [#2450](https://github.com/firedrakeproject/firedrake/discussions/2450))
 - Because of the missing link between PETSc coordinate fields and Firedrake coordinate fields (issue [#2185](https://github.com/firedrakeproject/firedrake/issues/2185)) meshes created from coordinate fields, fixed in [#2437](https://github.com/firedrakeproject/firedrake/pull/2437), would not work by reverting to calling DMSwarmSetPointCoordinates.

JW: Parallel interp doesn't work in PETSc, details available in MR. Serial is fine.

DH: This comes from the PETSc FE stuff. There's an easy part and a hard part. Easy: in DMPlex there should be a description of nodes and basis functions wrt a reference cell (like in Firedrake). Hard: orientation, PETSc has one concept of this, Firedrake is missing this, but Koki has implemented this for CG/DG. More fundamental problem is there is no common field data format between FEM packages.

(General discussion on how to incorporate these changes into Firedrake.)

RNH: How does this affect VertexOnlyMesh?

DH: DMSwarm is mapped to a parent mesh, so is a special case of interpolation.

AM: What happens with manifolds?

DH: This is a different problem, needs someone to do the work. We have a mathematically correct solution, we just need to ensure the code is implementing this.

AM: What about a horrible circle?

DH: There is a question about how we choose candidate cells so it's not expensive. This is what we use libspatialindex for, in combination with bounding boxes.

AM: Is someone going to do this for us?

DH: No.

DH: Also we need to think about what happens with extruded meshes.

## DH and KS: Firedrake coordinates and plex coordinates

KS: Arising in PR for IO. Need to generate mesh from mesh coordinates directly.

DH: We need to think about the circumstances we actually want to do this. Probably always, although we need to be careful with mesh hierarchies. Does IO support dumping hierarchies? (KS: No) This should be implemented, but not in this PR.

## DH: Disk Checkpointing
DH: Everything is working, but SK is still seeing an issue. I am implementing fancy checkpointing with chunking in revolve. Revolve is 20 years old though, but want to use an updated version from Inria. James Maddison has also made an implementation, but covers fewer cases.

The issue SK is seeing is with determining what things need checkpointing (things that are being input and things getting output).

## RK: Orientations
RK: Orientations are in Fiat now, something goes wrong with serendipity elements. Can this be fixed?

DH: Koki fixed some of this.

DH: Merge stuff from branches if you want things fixed (this is a PSA). There may be an issue with orienting serendipity, needs careful thinking about. Orientation needs fixing properly.

## Merge PRs
None

## Date of next meetings
Next meeting: 1200 UTC [2022-06-30](./Firedrake-meeting-2022-06-30)
