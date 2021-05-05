Date and time 2021-05-05 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: ~Crap out the geometric boundary stuff~ done: please review https://github.com/firedrakeproject/firedrake/pull/2007
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present: Daniel, Koki, Jack, David, Nacime, Connor, Lawrence, Paul, Reuben, Sophia, Colin

Apologies:

## Build servers

David bought a large computer and soon we can move from Jenkins to github actions.

## Loopy sprint

It's almost done.
Do we maintain our own fork of loopy or do we just follow upstream master?
Github actions can be configured to run on a regular schedule and not just on commits or pull requests, so we can regularly test against loopy master.

## Failing tests on master

Lawrence turned some tests that needed MUMPS into ones that don't, so this should be fixed.
Barry Smith says there's a fix in PETSc.

## Merge PRs:

Interior BCs!

## AOB

## Date of next meeting

[2021-05-12](./Firedrake-meeting-2021-05-12) 15:00UTC (16:00BST)