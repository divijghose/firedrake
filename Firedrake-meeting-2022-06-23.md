Date and time 2022-06-23 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS: Test PETSc main against current Firedrake
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022
1. ?: Decide who will organise SIAM CSE23 Minisymposium/minisymposterium

# Agenda

Present: 

Apologies:

## RNH and Joe Walwark: Plex to Plex interpolation
Joe has 2 new parallel plex-to-plex interpolation MRs on PETSc: [#5345](https://gitlab.com/petsc/petsc/-/merge_requests/5345) and [#5354](https://gitlab.com/petsc/petsc/-/merge_requests/5354). How can we best get this working with Firedrake? My (RNH's) thoughts are:
 - DMSwarmSetPointCoordinates (which we called prior to the merging of [#2437](https://github.com/firedrakeproject/firedrake/pull/2437)) calls DMLocatePoints which, were we to revert to using it, would solve the issue of out-of-rank points (see issue [#2178](https://github.com/firedrakeproject/firedrake/issues/2178) and discussion [#2450](https://github.com/firedrakeproject/firedrake/discussions/2450))
 - Because of the missing link between PETSc coordinate fields and Firedrake coordinate fields (issue [#2185](https://github.com/firedrakeproject/firedrake/issues/2185)) meshes created from coordinate fields, fixed in [#2437](https://github.com/firedrakeproject/firedrake/pull/2437), would not work by reverting to calling DMSwarmSetPointCoordinates.

## Merge PRs


## Date of next meetings
Next meeting: 1200 UTC [2022-06-23](./Firedrake-meeting-2022-06-16)
