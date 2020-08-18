Date and time 2020-08-11 15:00UTC (16:00BST)

# Action Items
1. ~Pick Chair and Minuter.~
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Only test PRs on master
1. RH: On complex back merge master to fix conflicts
1. ??: Build master on centos to catch errors


# Agenda

Present: RK, LM, JB, KS, CJC, DRS, IY, MK, NB, PHJK, SK, SV, WS

Apologies: 

## Ongoing numpy/blas issues

Batched blas stuff current candidate is MKL

RK: are there any licensing issues here.

JB: Would it work on ARM?

Action: All with MacOS systems, see if you can reproduce problem.

## CC: Parallel multigrid for sphere meshes

Creating a MeshHierarchy for IcosahedralMesh fails with
  File "mg_test.py", line 9, in <module>
    mh = fd.MeshHierarchy(basemesh, ref_level)
  File "/Users/colincotter/firedrake/src/firedrake/firedrake/mg/mesh.py", line 99, in MeshHierarchy
    raise RuntimeError("Cannot refine parallel overlapped meshes "
RuntimeError: Cannot refine parallel overlapped meshes (make sure the MeshHierarchy is built immediately after the Mesh)

See: https://gist.github.com/colinjcotter/2c3154c14c1532e3686eb2d32666a245
This is because IcosahedralMesh works by recursively refining an icosahedron and pushing out to the sphere. I'm not completely sure 
if it is due to the editing of the coordinate mesh, or the fact that we used Plex to refine the mesh twice when we create the Hierarchy 
(once for the base, once for the Hierarchy).
Similar things arise with PeriodicMesh where Patrick has something on a branch. Patrick was wondering if there might be a general solution that solves both, but I need to understand the sphere case on its own first.


LM: Workaround is to make a "flat" sphere mesh then the hierarchy, and then push out every level in the hierarchy to make the higher-order sphere meshes.

A proper fix requires removing the "two-stage" mesh construction and just always growing halos straight away. The multigrid hierarchy creation should refine such a mesh and then remove the (now too big) halo and regrow it to the correct size. This requires some fiddling with dmplex submeshes and then keeping track of the relationship between coarse and fine cells.

## KS: ufl.Subspace
UFL/Firedrake interfaces are converging (I think).

UFL:
- Vsub = ufl.Subspace(V)  -> represents (shape, ) x (shape, ) matrix multiplied to the basis vector in TSFC
- vsub = ufl.Masked(v, Vsub)

LM: I think the (shape, ) * (shape, ) part is somewhat misleading, since it presupposes a particular type of subspace extraction. I guess this is saying `Vsub` is obtained from `V` by some projection, and we also get `V \ Vsub` via `Vsub.complement` ?

Firedrake:

Low-level interfaces for ufl.Subspace:
- firedrake.ScalarSubspace  -> diagonal thing
- firedrake.RotatedSubspace  -> rotation thing

High-level interface specifically for boundary subspaces:
- firedrake.BoundarySubspace  -> returns Subspaces used to apply u = g on boundary

New example: Dirichlet BC for Hermite element:

https://github.com/firedrakeproject/firedrake/blob/fs_filter/tests/filter/test_filter_rotated_subspace.py


Some discussion of whether or not this solves the maths problem of strong bcs for Hermite elements. RCK to think about it.


## DONM

Proposal to move to Mondays at 4pm agreed for the foreseeable.