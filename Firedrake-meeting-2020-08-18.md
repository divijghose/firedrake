Date and time 2020-08-11 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Only test PRs on master
1. RH: On complex back merge master to fix conflicts
1. ??: Build master on centos to catch errors


# Agenda

Present: 

Apologies: 

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

