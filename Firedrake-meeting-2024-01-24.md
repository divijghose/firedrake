Date and time 2024-01-24 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to minute)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))? JB: Waiting for https://github.com/Toblerity/rtree/pull/292
1. NB: Update on what is needed for Interp/ExternalOperator to be merged
1. ALL: Submit abstract for PDESoft [PDESoft](https://pdesoft.org))

# Agenda

Present:

Apologies:

## JB: Spatialindex include headers are in Rtree 1.2.0
On PyPI https://pypi.org/project/Rtree/ merging https://github.com/firedrakeproject/firedrake/pull/3138 and associated supermesh PR should be fairly uncontroversial, as well as archiving our fork of `libspatialindex`.

## UZ: Mesh Hierarchy support when working with Netgen mesh 2D
The PR [3314](https://github.com/firedrakeproject/firedrake/pull/3314) only covers 2D for serial and parallel implementation.
The 3D case requires a bit of work on the Netgen side, which needs to land in Netgen main, so is far in the timeline.
I think the 3D implementation deserves a separate PR.

## UZ: Netgen meshing documentation (following up on Connor comment in PR 3314)
Since Patrick has been preparing a course on how to solve PDE using Firedrake with a specific class on Netgen, we have a lot of new or improved material for documentation and demos.
What is the appropriate way to include the new material in the Firedrake manual, more demos? Or a specific section on Netgen as mesher ?
If the section is the best way to go, what should be the content? Some ideas:
Constructive Solid Geometry via OCC, 
Linear Netgen mesh and parameters for splits (we can now do Powell-Sabin and Alfeld), 
Anisotropic mesh refinement, 
Adaptive mesh refinement (many improvements thanks to Patrick), 
High-order mesh in Netgen (curved Alfeld and Powell-Sabin splits), 
Netgen multi-grid hierarchies.

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- ~JB: [3324](https://github.com/firedrakeproject/firedrake/pull/3324) Requested changes have been made~ There are more changes from the minutes not logged on the PR that haven't been made...

- PB: [pyop2 #708](https://github.com/OP2/PyOP2/pull/708)

- DD: [Fix constant dimension #3344](https://github.com/firedrakeproject/firedrake/pull/3344)

- DD: [Update inactive and active team.](https://github.com/firedrakeproject/firedrake/pull/3350)

# Date of next meeting

1600 GMT (1600 UTC) [2024-01-31](./Firedrake-meeting-2024-01-31)