Date and time 2020-09-07 15:00UTC (16:00BST)

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

## KS: ufl.Subspace
Summary

View `ufl.Subspace` as a generalisation of `ufl.FunctionSpace`.

UFL:

- `ufl.AbstractSubspace` 
- `ufl.Subspace` (subclass)

TSFC:

`fem.py`

- `ufl.FunctionSpace` -> `\phi`
- `ufl.Subspace` -> `L\phi` (`L.shape = (sh, sh)`)

If `L==I`, we recover the standard `ufl.FunctionSpace`.

`kernel_interface/firedrake_loopy.py`
- `obj` : Firedrake subspace object
- `obj -> gem_expr` `(sh, )`
- `L = obj.transform_matrix(ufl_elem, gem_expr)` `(sh, sh)`



Firedrake:
```
class Subspace(ufl.Subspace):
    ...
    @staticmethod
    def transform_matrix(ufl_elem, gem_expr):
        # Diagonal L
        L = diagonalise(gem_expr)
        return L
```

```
class RotatedSubspace(ufl.Subspace):
    ...
    @staticmethod
    def transform_matrix(ufl_elem, gem_expr):
        # Rotation
        # Roughly, ...
        L = gem_expr^T gem_expr
        return L
```







## Date of next meeting
[2020-09-14](./Firedrake-meeting-2020-09-14) 15:00UTC (16:00BST)