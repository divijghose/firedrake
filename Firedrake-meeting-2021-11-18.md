Date and time 2021-11-18 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Minutes

Present: NB, CW, DH, LM, KS, JB, RK, SV, PK

Apologies:

## ECCOMAS
Jack Hale advised us (Firedrake) of this conference in Oslo: http://www.eccomas2022.org/frontal/default.asp

Abstracts by 10th December.

Action: JB, SV, do this (CW, KS NB also think about this!)

## NB: Refactor UFL type (Add UFLType):

Draft: https://github.com/firedrakeproject/ufl/commit/9dac91e17e5ee5e618477c6d906cbd07ca317b56

LM: We should rip the type stuff out of UFL

NB: We need this for multifunctions (for matrix derivatives)

DH: The change looks okay, need to get it passing tests though

Action: NB, fix it

## CW: `ComponentFunctionSpace` and `DatView.index` vs UFL

This indexing information is not represented in UFL. What should I do? Can we consider this to be premature optimisation?

LM: Consider introducing coefficient views in UFL. Think about consequences of this to appease FEniCS.

DH: Indexing a coeff is not sufficient for what we're doing. ~Perhaps sub should be a write only feature?~ 

DH: Perhaps we need another layer between Firedrake and UFL to handle indexing information. This layer could also handle boundary condition information.

LM: In terms of design, TSFC doesn't need to look at this info. How does this information make it out the other end of form compilation?

DH: Could be handled in a similar manner to external operator. This seems like the right way to do things, in the past we were clearly doing dodgy things.

## Merge PRs:

No

## AOB

DH: Need fix for R-space (possibly cast to float), in somebody's free time

## Date of next meeting

1600 UTC (1600 BST) [2021-11-25](./Firedrake-meeting-2021-11-25/)
