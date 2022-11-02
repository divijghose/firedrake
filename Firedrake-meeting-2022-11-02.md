Date and time 2022-11-02 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (Update: Done!)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open)
1. ALL: Rename split (`.split` -> `.subfunctions`) (ongoing)
1. JB: A Firedrake manual (ongoing)

# Agenda

Present: CW (minuter), DH, RNH, JB, DS, KS

Apologies:

## DH: Loopy caching issue [2610](https://github.com/firedrakeproject/firedrake/issues/2610)

- DH: We should have a single `FIREDRAKE_CACHE_DIR` variable that would set all other cache directories.

## RNH: Issue [2595](https://github.com/firedrakeproject/firedrake/issues/2595)
The UFL update to fenics main made certain things not work any more and is currently breaking Gusto

- DH: We possibly overlooked a case since `ReferenceGrad` is just linear so we should know how to take a derivative of it.
- DH: [TODO](https://github.com/FEniCS/ufl/blob/0c934309c0ae5908c75efaf04ae5b6f4e106af5e/ufl/algorithms/apply_derivatives.py#L890) comment suggests that it should be doable for the simple case which would fix the current issue.

## JB: GC fix landing soon
Need to look over "abuse of comms" [PR in PyOP2](https://github.com/OP2/PyOP2/pull/676) and [GC fix in Firedrake](https://github.com/firedrakeproject/firedrake/pull/2599).

- JB: All PyOP2 objects should now always use an internal communicator.
- DH: Reviewed, small changes requested.

## JB: Python 3.11 is here
MacOS users, please create me some [VTK](https://github.com/firedrakeproject/VTKPythonPackage) wheels! We are still waiting for an mpi4py wheel before [this](https://github.com/firedrakeproject/firedrake/pull/2358) can be merged :slightly_frowning_face:.

- JB: Step PyOP2 supported versions too.
- DH: Once MacOS machines are up we will set up a GitHub action to build and publish the wheels we need.

## Merge PRs

CW: https://github.com/firedrakeproject/firedrake/pull/2562 and https://github.com/dolfin-adjoint/pyadjoint/pull/93

- DH: FEniCSx doesn't support adjoint any more so compatibility issues not so important.
- DH: More discussion required.

## Date of next meeting

1600 UTC [2022-11-09](./Firedrake-meeting-2022-11-09)