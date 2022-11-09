Date and time 2022-11-09 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Organise Firedrake 2022 (Abstracts open)
1. ALL: Rename split (`.split` -> `.subfunctions`) (ongoing)
1. JB: A Firedrake manual (ongoing)
1. JB: Python 3.11 (ongoing)

# Agenda

Present:

Apologies:

## JB: Black
(Low priority) We have had the conversation before in the past: Should we use black to autoformat code?
Some formatting is inconsistent/bad. I have used black in a recent PR to cleanup `utility_meshes.py`.

## JB: PyOP2
(Low priority) This PR changes testing from Python 3.6 to Python 3.7-3.11, is the matrix worth it? Should PyOP2 use our Firedrake runners? Should we move PyOP2 to Firedrake organisation? 

## Merge PRs

JB: Versioneer finally removed `distutils` dependency, so these are ready to go:

- https://github.com/firedrakeproject/firedrake/pull/2368,
- https://github.com/OP2/PyOP2/pull/678

JB: We can ignore this failing test (I think) https://github.com/firedrakeproject/firedrake/pull/2613

## Date of next meeting

1600 UTC [2022-11-16](./Firedrake-meeting-2022-11-16)