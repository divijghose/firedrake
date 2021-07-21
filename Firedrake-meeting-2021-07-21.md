Date and time 2021-07-21 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Agenda

Present: DH, MG, JB, NB, RNH, RK, KS, CW

Apologies: SV, LM

## Firedrake Archer training

There are already quite a few people registered so attendance is likely to be high. How many people can we actually give assistance to?

- (RNH) Since it's free lots of people might not actually show up.
- (DH) Maybe ~100 people. Zoom limit is 300 so won't be an issue.
- (DH) JW has checked and fixed the tutorials. DH to check that notebooks work.
- (KS) Has managed to get install to Archer working. Observed that Firedrake hangs for more complex problems.
- (CW) Keith Roberts has been having hanging issues for a while. Might be related.
- (DH) Poisson in a `for` loop keeps overwriting variables. This could trigger unsafe PETSc destructors. Could try disabling generational garbage collector to avoid this bug. Possible solutions to this include:
  - Remove all cyclical references from Firedrake (esp. PyOP2) (see #1617)
  - Have petsc4py objects register to be destructed
  - Establish a global registry of Python objects so none of them ever die (massive memory leak)

## Firedrake '21 progress

- (DH) Webpage ready but registration stalled by payment issues. Gather town also set up.
- (NB) File size upload limit for posters. Need to check if it is a problem.
- (RNH) We still need prizes and a tech support system.
- (DH) Prizes can be mailed directly to winners. Tech support can be deferred for now.

## Merge PRs:

## AOB

## Date of next meeting
[2021-07-28](./Firedrake-meeting-2021-07-28) 15:00UTC (16:00BST)
