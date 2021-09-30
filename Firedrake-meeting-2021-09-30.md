Date and time 2021-09-30 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: Lawrence, Koki, David, Sophia, Nacime, Jack, Connor, Colin, Paul, Thomas

Apologies:

## DH - Office Tuesday

Contact your officemates.

## KS - Orientations (https://github.com/firedrakeproject/firedrake/pull/2101) update

Problem:

> When handling orientations for CG/DG (see PR https://github.com/firedrakeproject/firedrake/pull/2101), we need to get a DoF permutation for each dimension for each entity for each possible orientation, but this is slow.

Update: Performance improved by preprocessing the nested dictionary.


> 50x50x50 P4 example:

> Performance (in `dmcommon.get_cell_nodes`):

> off + j (without orientation): 0.143 min 

> off + perm[j] (orientation without preprocessing): 1.47 min

> off + perm[j] (orientation with preprocessing) : 0.177 min

Associated PRs:

- [Firedrake](https://github.com/firedrakeproject/firedrake/pull/2101/files)
- [FInAT](https://github.com/FInAT/FInAT/pull/87)
- [FIAT](https://github.com/firedrakeproject/fiat/pull/25)

All merged!

## Merge PRs:

- [Fix parameter handling in Slate compiler (#2227)](https://github.com/firedrakeproject/firedrake/pull/2227): Merged
- [New Slate optimisation pass (#2233)](https://github.com/firedrakeproject/firedrake/pull/2233): Looks great, it needs to be updated before being merged (1 failing test + minor corrections).

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-10-07](./Firedrake-meeting-2021-10-07/)
