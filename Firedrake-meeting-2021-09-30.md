Date and time 2021-09-30 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: 

Apologies: 

## DH - Office Tuesday

Contact your officemates.

## KS - Orientations (https://github.com/firedrakeproject/firedrake/pull/2101) update

Performance improved by preprocessing the nested dictionary.

50x50x50 P4 example:

In `dmcommon.get_cell_nodes`:

off + j : 0.143 min

off + perm[j] (without preprocessing): 1.47 min

off + perm[j] (with preprocessing) : 0.177 min

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-10-07](./Firedrake-meeting-2021-10-07/)
