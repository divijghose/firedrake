Date and time 2020-07-07 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ \*\*: Review this.
1. ~\*\*: Add `--remove-build-files` to make install smaller; convert this to an issue~ [#1771](https://github.com/firedrakeproject/firedrake/issues/1771)


# Minutes

Present:

Apologies:

## RCK: discuss FIAT progress for dual spaces, what to do in FInAT dual evaluation?

## LM: reworking MG interpolation

## LM: Vectorisation status

## JB: SIAM-CSE
Thoughts on running minisyposia as well as minisymposterium? Chased up Chris Richardson and he's very keen to contribute for possible Exascale simulation themed mini. (Also happy to contribute a poster).

## JB: Randomgen
Is Firedrake currently using any features of randomgen that aren't now in numpy?

## KS: ufl.Filtered/ufl.Transformed -> ufl.Masked
Status:
https://github.com/firedrakeproject/firedrake/issues/1648

Summary:

0. Viewing `ufl.Transformed` as a map is awkward.

1. Introduce `V0 = ufl.Subspace(V, some_constraint)`

2. Introduce `v0 = ufl.Masked(v, V0)` (v0 = v if v in V0 else 0) 


## Date of next meeting
2020-07-07 15:00UTC (16:00BST)
