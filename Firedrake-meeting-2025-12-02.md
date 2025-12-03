Date and time 2025-12-02 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: LC, JHC, CW, DH, IM, PB, UZ, AC

Apologies:

## JHC: `EnsembleBlockDiagonalMat` and `EnsembleBJacobiPC`

https://github.com/firedrakeproject/firedrake/pull/4711

- Matrix between ensemble function spaces.
- DH: Raise informative error if user passes firedrake Matrix.
- CW: rename Python context `EnsembleBlockDiagonalMat` to make it clearer what it is


## UZ: Discuss what to move from ngsPETSc to Firedrake :)

- DH: Ideally ngsPETSc doesn't have a firedrake dependency
- UZ: Firedrake code only used in one module, utils/firedrake/*
- CW: I made a PR moving this stuff over already
- DH: we'll then need to make sure we don't make ngspetsc a hard dependency
- UZ: I'll merge the stuff asap, then CW can merge his PR
- CW: changes into release branch

## LC: interpolation matrix mat_type

https://github.com/firedrakeproject/firedrake/pull/4749

- approved pending docstring fix


## Merge PRs

* 

## Date of next meeting

1600 UTC [2025-12-09](./Firedrake-meeting-2025-12-09)
