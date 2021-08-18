Date and time 2021-08-11 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present:

Apologies:

## RNH/JB: mesh DM/Coordinates field disconnect
Discussed on slack. See https://github.com/firedrakeproject/firedrake/issues/2185

## RNH: `VertexOnlyMesh` issues
See https://github.com/firedrakeproject/firedrake/issues/2178.
Am I correct to say that on-cell-edge points are just inherently hard to deal with?
How about the parallel distribution question?
Was I wrong to expunge `VertexOnlyMesh` points from parent mesh halos?

Also up for discussion if we want https://github.com/firedrakeproject/firedrake/issues/2186

## DRS: adjoint + quadrature issue

## Merge PRs:
JW: https://github.com/firedrakeproject/firedrake/pull/2174 (Sebastian approved the pyadjoint PR)

RNH: FInAT dual evaluation [Firedrake](https://github.com/firedrakeproject/firedrake/pull/2115), [TSFC](https://github.com/firedrakeproject/tsfc/pull/250), [FInAT](https://github.com/FInAT/FInAT/pull/89)

## AOB

## Date of next meeting

[2021-08-25](./Firedrake-meeting-2021-08-25) 15:00UTC (16:00BST)