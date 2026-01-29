Date and time 2026-01-29 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: DH, LC, CW, PB, AC, JHC

Apologies:

## Agenda items

### PB: Multigrid for non-Lagrange [PR #4839](https://github.com/firedrakeproject/firedrake/pull/4839)

Enabling `prolong`/`restrict`/`inject` for non-Lagrange elements in a very similar spirit to LC's [PR #4804](https://github.com/firedrakeproject/firedrake/pull/4804).

Accidentally opens the door to extending supermesh projections to non-Lagrange elements.

Minutes:
Conversation about general version - conclusion that it is likely to be slower without the structure currently included (we should find out at some point)
Important to ensure documentation is updated with this capability.
Tests timing out - seems to be to do with IO
Approved pending merge

### PB: Adaptive Multigrid [PR #4726](https://github.com/firedrakeproject/firedrake/pull/4726)

Includes demo.

Needs to wait for #4804 to be merged so it can be simplified. 
### LC: Mixed interpolation matrix cross-mesh https://github.com/firedrakeproject/firedrake/pull/4792

### LC: Cross-mesh interpolate into Hdiv / Hcurl etc. https://github.com/firedrakeproject/firedrake/pull/4804

Queue: Merge #4839, Fix later ones to use this, then merge 

## Merge PRs

## Date of next meeting

1600 UTC [2026-02-05](./Firedrake-meeting-2026-02-05)
