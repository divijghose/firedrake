Date and time 2022-10-26 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (Update: Done!)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open)
1. ALL: Rename split (`.split` -> `.subfunctions`)
1. JB: A Firedrake manual

# Agenda

Present:

Apologies:

## CW: `assign` for weighted sums

https://github.com/firedrakeproject/firedrake/pull/2562 is very nearly done. Currently the only failures are in pyadjoint (https://github.com/dolfin-adjoint/pyadjoint/pull/93) where `assign` in Firedrake now fails but switching to `interpolate` breaks FEnICs. What should I do?

## RNH: Issue [2595](https://github.com/firedrakeproject/firedrake/issues/2595)
The UFL update to fenics main made certain things not work any more and is currently breaking Gusto

## JB: GC fix landing soon
Need to look over "abuse of comms" [PR in PyOP2](https://github.com/OP2/PyOP2/pull/676) and [GC fix in Firedrake](https://github.com/firedrakeproject/firedrake/pull/2599).

## JB: Python 3.11 is here
MacOS users, please create me some [VTK](https://github.com/firedrakeproject/VTKPythonPackage) wheels! We are still waiting for an mpi4py wheel before [this](https://github.com/firedrakeproject/firedrake/pull/2358) can be merged :slightly_frowning_face:.

## Merge PRs

## Date of next meeting

1600 UTC [2022-11-09](./Firedrake-meeting-2022-11-09)
