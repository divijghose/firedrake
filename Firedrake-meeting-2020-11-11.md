Date and time 2020-11-11 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. ~DS: Anaconda on Mac~
1. CW: PyOP2 sphinx documentation

# Agenda

Present: LM, DAH, RCK, DRS, RNH, JDB, SV, KS, CW, TG

Apologies: 

## DRS: Anaconda

pyenv seems to do a fine job at isolating things.

## Strange test failures

Update, is this why master is failing?

Conjecture, some memory corruption somewhere.

Actions:

RNH: Push build of pre-complex merge firedrake (to check if this all
works fine)

LM: Build trunk with --with-debugging switched on in PETSc.

DRS: Build trunk with -fsanitize=address switched on.

## DAH: cofunctions/dual spaces in UFL

Document WIP. See https://www.overleaf.com/read/tqzqzdybsdsq. Comments/suggestions/improvements to DAH

## Merge PRs:

## AOB
## Date of next meeting

[2020-11-18](./Firedrake-meeting-2020-11-18) 16:00UTC (16:00GMT)
