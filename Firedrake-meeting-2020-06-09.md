Date and time 2020-06-09 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute** (Position of chair is also negotiable!)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ Start reviewing
1. \*\*: Add `--remove-build-files` to make install smaller; convert this to an issue

# Minutes
Present: DRS, LM, DH, SV, JB, TG, RH, NB, KS, CC

Apologies:

## DH: SIAM CSE

Everyone should go. Minisymposium deadline is July 20. There is a soft limit on the number of people from the same institution in one minisymposium so we need to corral people from outside Imperial.

Alternatively, we can make it a poster session, which has no limits and arguably better visibility for presenters. Work with the FEniCS, freefem++, etc. folks on this.

## DRS: installation debugging flowchart

Will add to Firedrake docs and make a PR.

## KS: ufl.Transformed
One page write-up on a new interpretation of `ufl.Transformed`.  Please find `transformed.pdf` at : 
https://github.com/firedrakeproject/firedrake/issues/1648

Updated write-up of the math and code available on this issue:
https://github.com/firedrakeproject/firedrake/issues/1648
specifically the June 9 update. UFL has no concept of a specific basis and elucidating how this new API does not inject this concept is an ongoing discussion.

## Date of next meeting
2020-06-16 15:00UTC (16:00BST)
