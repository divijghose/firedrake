Date and time 2020-09-21 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Only test PRs on master
1. RH: On complex back merge master to fix conflicts
1. ??: Build master on centos to catch errors


# Minutes

Present: Reuben Hill, Lawrence Mitchell, David Ham, Sophia Vorderwuelbecke, Stephan Kramer, Jack Betteridge, Koki Sagiyama, Nacime Bouziani, Colin Cotter, Paul Kelly

Apologies: 

## DH: Minisymposterium
15 Posters have been submitted!

## DH: Improved IO
Koki's material needs to be in a state to be put on pause in next 6 weeks as grant for improving IO should start soon. (There is a letter to prove this)

## DH: Masters Students and PhD students
- MLMC with Firedrake: Nick Twyman finishing masters project, soon there will be some MLMC code that will compose with Firedrake.
- Need to check status of other masters students' code in preparation for merging.
- DH has new PhD student (Connor) looking at reworking PyOP2. *

## DH: Master is broken?
This is due to changes in Finat, LM: check https://github.com/FEniCS/ufl/pull/41.
There is potential for issues due to Norwegian numbering of finite elements.

## DH: Issues with quadrature estimator
There are multiple issues with the quadrature estimator, these need to be fixed for newly introduced elements.
Could take a look at what Fenics is doing here.
Action item on RK to report back on quadrature estimation.

## LM: *PyOP2
LM: Should "PyOP3" actually be written in Python?
DH: Will we have to re-engineer Firedrake?
LM: I have done experiments to find which parts of PyOP2 are expensive (which parts are runtime Python)
DH: Connor should investigate the strong scaling of PyOP2 as a first step


## RH: Status of complex
DH: 25 (corrected 14) days ago PR merge passed
RH: Checked and fixed failing tests, need to know what dependencies have merged feature branches (Ie: UFL fix_cell_diam)
DH: Someone should turn off testing on branch, just merge test. Also need to double compute resources used for testing complex (Ie: test real and complex on separate workers)
RH: Will continue to chase issues (action item RH)

## RK: Non-local operators
RK is close to writing code using external operators.

## DH: Admin
When should we hold meeting from this week on?
LM: Need to change from 9th Nov
DH: Stick with Monday 1500 UTC until then

## Date of next meeting
[2020-09-28](./Firedrake-meeting-2020-09-28) 15:00UTC (16:00BST)