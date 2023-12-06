Date and time 2023-11-29 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))? JB: Waiting for https://github.com/Toblerity/rtree/pull/292
1. DD: Investigate adjoint test fails in teardown ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-11-22#jb-pyadjoint-firedrake-tests-erroring))

# Agenda

Present:

Apologies:

## CW: Fix for fun finalize bug

Is [#3282](https://github.com/firedrakeproject/firedrake/pull/3282) an acceptable fix for [#3247](https://github.com/firedrakeproject/firedrake/issues/3247)? In particular my fix will not catch this failure mode again, but I have no idea how to do that.

## CW/JB: `Constant` implementation discussion

The way `Constant`s are currently implemented is hacky and weird (e.g. see [#3261](https://github.com/firedrakeproject/firedrake/pull/3261) for how we differentiate them and implement `ufl2unicode`). What is the way forward? Do they need adding to UFL (I think no, providing that UFL fix their type system)? Do we need to have vector-valued real `Function`s (not `Argument`s)?

## PB: `Constant(domain=mesh)` warnings in tests

More than half of the ~1250 warnings raised during CI are coming from 3 files (regression/test_zero_forms.py, regression/test_scaled_mass.py, test_interpolation_from_parent.py). The most common warning has to do with `Constant(domain=mesh)`. Some of these Constants are vector valued, and cannot be replaced with Function(Rspace), as there's a silent bug that allows the creation of a vector-valued R-space but with Function.dat of the wrong shape, see [#3046](https://github.com/firedrakeproject/firedrake/issues/3046).

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- PB: [fix demo #3281](https://github.com/firedrakeproject/firedrake/pull/3281)

# Date of next meeting

1600 GMT (1600 UTC) [2023-12-13](./Firedrake-meeting-2023-12-13)