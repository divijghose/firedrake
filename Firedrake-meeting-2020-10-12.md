Date and time 2020-10-05 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. RK: Report back on quadrature estimation
1. KS: Complex merge


# Minutes

Present: David Ham, Connor Ward, Koki Sagiyama, Paul Kelly, Sophia Vorderwuelbecke, Colin Cotter, Lawrence Mitchell, Jack Betteridge, Tom Gregory, Rob Kirby

Apologies: Reuben Nixon-Hill (note new surname!)

## DH: Complex has landed

## RK: Report back on quadrature moved to "the future"

## DH: Move meeting to Weds from next week (still at 1600 GMT+1)
Also note that there is an hour's disparity the following week due to Daylight savings differences between different countries.

## JB: Numpy bug
Finally successfully installed on MacOS, we have working install script now.

Can also import Firedrake, but we need a hack:
```
export DYLD_INSERT_LIBRARIES=/usr/local/opt/openblas/lib/libblas.dylib:/usr/local/opt/openblas/lib/liblapack.dylib
```
We should discuss whether we are happy with such a hack.

Conclusion, this is a bodge. Can be fixed by adding correct rpath to offending modules that are loading the incorrect shared libraries.
Action JB fix this.


## KS: Subspace
Refactor tsfc/driver.py 
- gem construction
- impero_c construction
- kernel construction

etc.

`firedrake/tsfc_interface.py`

Ex: Jacobian assembly:
```
all_gem_expr = []
split form according to indices (i, j) -> subform
    split subform according to test/trial subspaces (test_sub, trial_sub) -> subsubform
       gem_expr = compile_ufl(subsubform, ...)
  ->   gem_expr = transform(gem_expr, test_sub, trial_sub) (test_sub and trial_sub know right transformation rule, such as rotation)
       all_gem_expr.append(gem_expr)
    kernel = construct_kernel(all_gem_expr)
```
Question:

`Masked` is still a `ufl` class (now defined in Firedrake), but disappear before calling `compile_ufl`.
This is convenient when we take `action` and `derivative`, but not sure if this is a good practice.

KS: Masked is "UFL", but defined in Firedrake.

DH: This is an issue if transforms are called on UFL expressions.

LM: Can we just merge TSFC driver refactroring standalone?

DH: This will allow us to have a hiatus on this work.

## Merge PRs:
Various fixes in FunctionMergeBlock :ballot_box_with_check: 

KVM elements :ballot_box_with_check: 

Fix index relabelling in assignments :ballot_box_with_check: 

# DH: Possible topic for future discussion: Online Firedrake 2021?
# DS: Another possible future discussion point is Extrusion lift operator

## Date of next meeting

Discuss changing meeting to Wednesday early at Gebina Ham's request.

**[2020-10-21](./Firedrake-meeting-2020-10-21) 15:00UTC (16:00BST)**