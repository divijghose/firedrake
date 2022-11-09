Date and time 2022-11-09 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Organise Firedrake 2022 (Abstracts open)
1. ALL: Rename split (`.split` -> `.subfunctions`) (ongoing)
1. JB: A Firedrake manual (ongoing)
1. JB: Python 3.11 (ongoing)

# Agenda

Present: RK RNH KS CW JB DH

Apologies:

## DH: Firedrake 22
Please submit abstracts and register.

## Actionables:
 - Firedrake 22: Please submit abstracts and register.
 - `.split` -> `.subfunctions` to become an issue.
 - Python 3.11: Still need macos VTK wheels, Koki to (hopefully) make intel macos wheel
   - Mac mini test machines will be up and running soon, just need appropriate admin rights

## JB: Black
(Low priority) We have had the conversation before in the past: Should we use black to autoformat code?
Some formatting is inconsistent/bad. I have used black in a recent PR to cleanup `utility_meshes.py`.
 - We will see if we can make it work, including adding "has this been run through black" to the linter

## JB: PyOP2
(Low priority) This PR changes testing from Python 3.6 to Python 3.7-3.11, is the matrix worth it? Should PyOP2 use our Firedrake runners? Should we move PyOP2 to Firedrake organisation? 
 - Python change could cause issues with ubuntu's default python: we should choose not to care! We will instead follow python's support (which is 5 years, i.e. back to 3.7)
   - We will keep f-strings out of the install script to make sure users of old python get appropriate warnings
 - Yes PyOP2 should use our runners
 - Fork PyOP2 and FInAT into firedrake organisation and tombstone the old ones (will need to update the documentation)

## DH: Hiring
Person who was offered mesh refinement role turned it down. If anyone knows someone looking for a postdoc in firedrake land please let us know!

## DH: UFL changes
Join the #newfl slack channel on fenics slack where changes to the language are being discussed

## Merge PRs

JB: Versioneer finally removed `distutils` dependency, so these are ready to go:

- https://github.com/firedrakeproject/firedrake/pull/2368,
- https://github.com/OP2/PyOP2/pull/678

JB: We can ignore this failing test (I think) https://github.com/firedrakeproject/firedrake/pull/2613

## Date of next meeting

1600 UTC [2022-11-16](./Firedrake-meeting-2022-11-16)