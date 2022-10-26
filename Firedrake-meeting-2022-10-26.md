Date and time 2022-10-26 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** Jack chairing (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open)
1. ALL: Rename split (`.split` -> `.subfunctions`)
1. JB: A Firedrake manual

# Agenda

Present: JB, KS, CW (minuter)

Apologies: RNH

## JB: Clocks change

UK on 30th October

## CW: `assign` for weighted sums

https://github.com/firedrakeproject/firedrake/pull/2562 is very nearly done. Currently the only failures are in pyadjoint (https://github.com/dolfin-adjoint/pyadjoint/pull/93) where `assign` in Firedrake now fails but switching to `interpolate` breaks FEnICs. What should I do?

Defer to next week.

## Merge PRs

#2592 merged.

## Date of next meeting

1600 UTC [2022-11-02](./Firedrake-meeting-2022-11-02)
