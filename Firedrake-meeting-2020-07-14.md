Date and time 2020-07-14 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Provide RWH with abstract and title for SIAM-CSE minisymposterium to make into qualtrics survey
1. DH: Provide JB with contacts for SIAM-CSE Exascale simulation themed minisymposium


# Minutes

Present: 

Apologies: Reuben Hill, Jack Betteridge, Nacime Bouziani, Lawrence Mitchell

# SV: Tsslac
Can we merge?

# Move to next week: (JB: Cholesky factor)
Can we assemble F*x, where F contains a local Cholesky factorisation?
There is a factorisation node in Slate, which takes the type of factorisation as argument, can we use that?

# DRS: American Geophysical Union Fall Meeting
Anyone interested in teaming up for this?

# KS: Correct UFL interface?
V = ufl.FunctionSpace(...)
v = ufl.TestFunction(V)
V0 = ufl.Subspace(V)  # terminal
v0 = ufl.Maked(v, V0)  # terminal_modifier: v0 = v if v in V0 else 0
v1 = v - v0
a = inner(u, v0) * ds + inner(u, v1) * ds

## Date of next meeting
2020-07-21 15:00UTC (16:00BST)
