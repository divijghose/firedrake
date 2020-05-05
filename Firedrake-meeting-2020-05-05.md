Date and time 2020-05-05 15:00UTC (16:00BST)

# Action Items
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. ~DRS: Open PR for stream plot~ See PR #1670. Review required
1. ~DH: Tackle the remaining complex sprint items~
1. ~FW: Add the hack to have shape derivatives tests working in complex~
1. ~SV: Expunge references to COFFEE before tsslac merge~
1. ~LM: Go through the tsslac PRs~
1. JB: Add mechanism for python3.8 
1. DH: Find time to fix to get final complex sprint test passing.
1. ALL: Someone to look at TSFC merge needed as part of complex sprint. 
1. DH: Find time to sort out Jenkins to run in real and complex mode.

# Minutes
Present: 

Apologies:

## DRS - Stream Plot PR
Correct metric for various cell geometric quantities discussed. "cell size" vs "cell diameter" where the latter is needed to work on quads. **DECISION**: "cell size" will return "cell diameter" on quads.

## DH Complex Sprint
Now passing in almost all cases - 1 bug (where a test function and trial function get mixed up) needs to be fixed. Noted that real mode could be improved with better implementation of PETSc real matrices.

Merging plan discussed.

PSA: Merging complex will double testing load. Jenkins will stop testing all commits. Only merge commits will be tested and only branches with active pull requests will be tested.


## SV: tsslac merge
Work ongoing.


## LM: COFFEE in codebase
Reasons to keep coffee in: 
 - TSFC used as backend for dolfin; 
 - hard work to remove from certain places where need to glue kernels together; 
 - loopy doesn't work for everything that users want to do and eats memory for breakfast.
Note: In future, prefer to use TSFC kernel interface to decide which code generation to use.


## LM: Improving Loopy
Needs someone from firedrake with time to fix things when bugs arrive.


## JB: Status of issue #1451
~Agenda: In light of dropping COFFEE in the (near?) future, what is the current status of:
https://github.com/firedrakeproject/firedrake/issues/1451~ 

Minutes: See *LM: COFFEE in codebase*


## RWH: further discussion needed on #1667
Agenda: Proposed solution from last meeting introduces new problems without obvious solutions. See https://github.com/firedrakeproject/firedrake/pull/1667

Minutes: Will modify `make_scalar_element` to use mesh topology's `ufl_cell`. Will make sure that all `ufl_cell`s anywhere else which ultimately are created on a mesh topology will use the mesh topology's ufl cell.

## Date of next meeting
2020-05-12 15:00UTC (16:00BST)
