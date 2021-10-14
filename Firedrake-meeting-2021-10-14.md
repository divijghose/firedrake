Date and time 2021-10-14 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present:

Apologies:

## Proposal: Determining whether `offset` is required from the measure - CW

We are trying to generate PyOP2 packing code using just UFL. For the case of an extruded mesh it should be possible to determine what `offset` should be. However, UFL doesn't know that it is operating on an extruded mesh so we don't know whether `offset` is needed or not. Our proposal is to attach this information as metadata to the UFL measure. Is this the right thing to do?

## Merge PRs:

CW: https://github.com/OP2/PyOP2/pull/642

DS: https://github.com/firedrakeproject/firedrake/pull/2244

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-10-21](./Firedrake-meeting-2021-10-21/)