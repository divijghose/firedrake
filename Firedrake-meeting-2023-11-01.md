Date and time 2023-11-01 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?
1. PB: Spectral on triangles and tetrahedra?


# Agenda

Present: PB, IM, FA, RNH, DH, JB, KS, CW, DD, NB

Apologies:


## PB: Spectral on triangles and tetrahedra?

Check docs: https://www.firedrakeproject.org/variational-problems.html#element-variants

The default is spectral.

PB: Add support for P and DP and update the docs accordingly

## PB: GLL/GL on simplices with recursive points

fiat PR: https://github.com/firedrakeproject/fiat/pull/46

-> PB: Use Tobin Isaac' code (can be piped installed) and replace `fiat/setup.py` by a `pyproject.toml` (see [here](https://github.com/firedrakeproject/fiat/issues/48))

## Merge PRs

PB: [#3159](https://github.com/firedrakeproject/firedrake/pull/3159): Changes requested

JB: [#3192](https://github.com/firedrakeproject/firedrake/pull/3192): Merged

PB: [#3178](https://github.com/firedrakeproject/firedrake/pull/3178): Closed -> lifted to UFL: https://github.com/FEniCS/ufl/pull/232

# Date of next meeting

1600 GMT (1600 UTC) [2023-11-08](./Firedrake-meeting-2023-11-08)
