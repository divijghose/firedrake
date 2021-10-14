Date and time 2021-10-14 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present:

Apologies:

## Proposal: Determining whether `offset` is required from the measure - CW

We are trying to generate PyOP2 packing code using just UFL. For the case of an extruded mesh it should be possible to determine what `offset` should be. However, UFL doesn't know that it is operating on an extruded mesh so we don't know whether `offset` is needed or not. Our proposal is to attach this information as metadata to the UFL measure. Is this the right thing to do?

- offset is not only one number, it's an arity tuple
- for time stepping e.g. we want to cache independent of data
- extrusion is mesh property, maybe just add property to ufl.mesh
- be careful that it is hashable

## Merge PRs:

CW: https://github.com/OP2/PyOP2/pull/642

DS: https://github.com/firedrakeproject/firedrake/pull/2244

PB: https://github.com/firedrakeproject/firedrake/pull/2024

LM: https://github.com/FEniCS/ufl/pull/69

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-10-21](./Firedrake-meeting-2021-10-21/)