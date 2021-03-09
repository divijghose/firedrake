Date and time 2021-03-10 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR

# Agenda

Present:

Apologies:

## IGG: (Via JB)
Ivan Graham would like to promote the use of Firedrake through a training event, probably hosted "in" Bath for wider GW4 community. Main questions are:
* would the Firedrake team be happy to run such an event, and if so in which form?
* which resources (in terms of tutors and their financial compensation) would be required?
* which technical infrastructure is required (probably just laptops)?
* and when is the best time to run this (maybe in the summer)? JB suggests either avoiding having it at the same time as Firedrake21 or coinciding
* Does anyone have / want to develop some bad cop Helmholtz demo material for such an event?

## LM: "geometric" BCs

This issue (https://github.com/firedrakeproject/firedrake/issues/1661) arose again. This requests applying BCs to interior facets. The only thing that is fiddly is determining the dofs on those facets, and pushing through a few other minor bits and pieces.

The wrinkle is that this is all much easier if one uses topological BCs: you can just pull everything out of the section straightforwardly. For geometric bcs we have to go via facet indirections and the code is uglier.

Given that geometric bcs don't make any sense really, we could just remove that option.

## Merge PRs:

## AOB

## Date of next meeting

[2021-03-17](./Firedrake-meeting-2021-03-17) 16:00UTC (16:00GMT)