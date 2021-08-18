Date and time 2021-08-11 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present: CW, SV, LM, DS, MG, KS, JB, RNH, JW, RK, NB, SK

Apologies:

## RNH/JB: mesh DM/Coordinates field disconnect
Discussed on slack. See https://github.com/firedrakeproject/firedrake/issues/2185

- LM: The coordinate field of a DM is not in the same order as the one we use in Firedrake. To fix this we do our own ordering. Users are allowed to modify this. This works fine unless we directly interact/query the DM which is out-of-date. This is an issue with periodic meshes for example as well as RNH's vertex mesh stuff. The solution is to have these coordinate fields be the same. In theory possible now for piecewise-linear coordinates if we use a PETSc Section. Not sure about high-order and discontinuous. KS's IO/orientation work should hopefully help 'line things up'.
- LM: We can't check to see if the field has been modified, but we could. NB has done some work on this in PyOP2 to monitor state. There is no quick fix.
- RNH: Will update documentation to reflect this.
- LM: NB needs to check that all areas where state is modified are covered.

## RNH: `VertexOnlyMesh` issues
See https://github.com/firedrakeproject/firedrake/issues/2178.
Am I correct to say that on-cell-edge points are just inherently hard to deal with?
How about the parallel distribution question?
Was I wrong to expunge `VertexOnlyMesh` points from parent mesh halos?

Also up for discussion if we want https://github.com/firedrakeproject/firedrake/issues/2186

- RNH: Issue with points getting discarded when they lie on the mesh boundary. PETSc doesn't have way to deal with this.
- LM: A point on the boundary of two cells can sometimes be considered in neither due to floating point trickery.
- RNH: There is no way in DMSWARM/DMPLEX to query 'nearest cell'.
- LM: If you end up in the wrong cell you can get a different value. In some cases this can be 'not that wrong'. Thinks just picking a cell is good enough.
- RNH: Will email PETSc users for advice.
- LM: Specify an absolute distance in reference space.

## DRS: adjoint + quadrature issue

See this issue: https://github.com/firedrakeproject/firedrake/issues/2179

- DRS: Cannot figure out how to set quadrature degree for adjoint solve.
- RK: May be an easy UFL fix. Adjoint of form may not be propagating metadata.
- DRS: Quadrature degree can be specified in two places.
- LM: This appears similar to previous issue of passing solver parameters through adjoint.
- SK: Thinks specifying quadrature degree via `dx` works.
- SK: By default solver options match the forward problem.

## Merge PRs:
JW: https://github.com/firedrakeproject/firedrake/pull/2174 (Sebastian approved the pyadjoint PR)

RNH: FInAT dual evaluation [Firedrake](https://github.com/firedrakeproject/firedrake/pull/2115), [TSFC](https://github.com/firedrakeproject/tsfc/pull/250), [FInAT](https://github.com/FInAT/FInAT/pull/89)

## AOB

## Date of next meeting

TBC. Next Thursday?
