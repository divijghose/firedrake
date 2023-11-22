Date and time 2023-11-22 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  - see below
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
  - Last week, RK said Andreas thinks the ball is in someone else's court
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?
1. NB: Look for changes needed to manual to account for dual spaces

# Agenda

Present: 

Apologies:

## Pyadjoint Firedrake tests erroring
[#3247](https://github.com/firedrakeproject/firedrake/issues/3247)

## Merge PRs

- PB: [FIAT #54](https://github.com/firedrakeproject/fiat/pull/54)
- PB: [FInAT #115](https://github.com/FInAT/FInAT/pull/115)
- PB: [MG easy fix](https://github.com/firedrakeproject/firedrake/pull/3246)
- PB: [reconstruct FunctionSpace](https://github.com/firedrakeproject/firedrake/pull/3241)
- JHC: [sort FormSum.coefficients](https://github.com/FEniCS/ufl/pull/243)
- JB: [#3117](https://github.com/firedrakeproject/firedrake/pull/3117) Separate out Matplotlib
- JB: [#3152](https://github.com/firedrakeproject/firedrake/pull/3152) A public interface to the garbage collector (for those who _really_ want one, not that I am encouraging anyone to actually use it!):
  + Look at in this order: [#3152](https://github.com/firedrakeproject/firedrake/pull/3152), [#3229](https://github.com/firedrakeproject/firedrake/pull/3229), [PyOP2 #711](https://github.com/OP2/PyOP2/pull/711), [PyOP2 #712](https://github.com/OP2/PyOP2/pull/712)
  + Needs merging in this order: [#3229](https://github.com/firedrakeproject/firedrake/pull/3229), [PyOP2 #712](https://github.com/OP2/PyOP2/pull/712), [PyOP2 #711](https://github.com/OP2/PyOP2/pull/711), [#3152](https://github.com/firedrakeproject/firedrake/pull/3152)
- PB: [HypreAMS easy fix](https://github.com/firedrakeproject/firedrake/pull/3252)
- KS: [#3174](https://github.com/firedrakeproject/firedrake/pull/3174)

# Date of next meeting

1600 GMT (1600 UTC) [2023-11-29](./Firedrake-meeting-2023-11-29)
