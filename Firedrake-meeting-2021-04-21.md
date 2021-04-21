Date and time 2021-04-21 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: ~Crap out the geometric boundary stuff~ done: please review https://github.com/firedrakeproject/firedrake/pull/2007
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present:

Apologies:

* Getting EquationBC to work with pyadjoint: Using the branch `equation_bc_tape_mc` (and some changes to pyadjoint) we are now able to correctly tape EquationBC. However, there are a few issues calculating the derivative mainly because EquationBC was not designed to be used with `_la_solve` which is what pyadjoint uses when calculating the derivative. [MC]

## Merge PRs:


## AOB

## Date of next meeting

[2021-04-28](./Firedrake-meeting-2021-04-28) 15:00UTC (16:00BST)