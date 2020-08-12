Date and time 2020-08-11 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. ~DH: Provide RWH with abstract and title for SIAM-CSE minisymposterium to make into qualtrics survey~
1. ~DH: Provide JB with contacts for SIAM-CSE Exascale simulation themed minisymposium - Jack is in discussion with Timo.~


# Minutes

Present: Jack Betteridge, David Ham, Rob Kirby, Paul Kelly, Will Saunders, Reuben Hill, Stephan Kramer, Colin Cotter, Nacime Bouziani, Tom Gregory, Dan Shapero, Lawrence Mitchell

Apologies: 

# Agenda

## DH: complex merging

Mostly works? Proposal to switch to only testing PRs to reduce test load.

Action DH: Do that, can do so on master.

Action RH: back merge master to fix conflicts.

DH: Punt pyadjoint for later.

## DH: install/build on CentOS

Build master on centos to catch errors (new docker container)

## JB: Update on numpy/BLAS/gfortran bug

Jack to approach numpy/scipy folks to see what can be done.

