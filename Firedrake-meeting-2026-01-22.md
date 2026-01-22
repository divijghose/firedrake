Date and time 2026-01-22 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (PB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: DH AS LC PB IM CW JHC

Apologies:

## Agenda items

### LC: https://github.com/firedrakeproject/firedrake/pull/4792
Looks correct, just needs manual section describing how the matrix structure is obtained from the interpolation expression.

### g-adopt failing due to pandas 3.0.0
Raise issue on g-adopt repo

### Sum factorisation index limit
Changing the limit is difficult because
- Just increasing it blows up the compile time.
- Letting it be variable means that the limit should be in the cache key, but it isn't straightforward to add in this case.
- CW: make TSFC control the index contraction limit rather than finat, then it can add it to the cache key?
- DH: looking at the debugger traces, sum factorisation is called far more than would be expected.

## Merge PRs

Reviewing some recent smaller PRs

## Date of next meeting

1600 UTC [2026-01-22](./Firedrake-meeting-2026-01-29)
