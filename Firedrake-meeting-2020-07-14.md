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

Present:  David Ham (DH), Dan Shapiero (DRS), Sophia Vdw (SV), Koki Sagiyama (KS), Stephan Kramer (SK), Tom Gregory, MKan, mohamadusman, Nick T, and Colin Cotter

Apologies: Reuben Hill, Jack Betteridge, Nacime Bouziani, Lawrence Mitchell

# SV: Tsslac
Can we merge?
Getting there. Everything is functional, but Lawrence has requested some improvements in the interfacing with TSFC.

Vectorisation merge is also close to landing...

# Moved to next week: (JB: Cholesky factor)
Can we assemble F*x, where F contains a local Cholesky factorisation?
There is a factorisation node in Slate, which takes the type of factorisation as argument, can we use that?

# DRS: American Geophysical Union Fall Meeting

Addressing Challenges for the Next Generation of Earth System Models](https://agu.confex.com/agu/fm20/prelim.cgi/Session/103241
DRS: Anyone interested in teaming up for this? Many people asked me about firedrake and its advantages for geoscientific models (layers, tensors meshes, etc.). Meeting is virtual. Submission deadline 29 July 2020 (2 weeks!).

DRS to set up a wiki page as a focal point for firedrake submissions. SK to advertise in AMCG/Earth Science dept.

# KS: Correct UFL interface?

KS discussed better interface for Filtered/Masked functionality at UFL level (see https://github.com/FEniCS/ufl/pull/22)

V = ufl.FunctionSpace(...)
v = ufl.TestFunction(V)
V0 = ufl.Subspace(V)  # terminal
v0 = ufl.Maked(v, V0)  # terminal_modifier: v0 = v if v in V0 else 0
v1 = v - v0
a = inner(u, v0) * ds + inner(u, v1) * ds

Two basic cases: pointwise scalar multiplication of coefficients, and pointwise tensor transformation. DH argues that we need to specify at UFL level which one we are dealing with. Discussed performance implications of multiplying with identity matrix everywhere, potential optimisation at firedrake level to restrict transformation to boundary subdomain only.

## Date of next meeting
2020-07-21 15:00UTC (16:00BST)
