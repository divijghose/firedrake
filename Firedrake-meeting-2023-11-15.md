Date and time 2023-11-15 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick minuter - RNH picked)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  - see below
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
  - RK says Andreas thinks the ball is in someone else's court
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?
1. UZ: Review, check and merge upstream NGSolve changes required for UFL update. DONE!
1. NB: Look for changes needed to manual to account for dual spaces

# Agenda

Present: JB, KS, CW, RK, NB, UZ, PB, FA, RNH

Apologies:

## PB: Sympy FIAT changes
Now this has been merged, Firedrake test suite now runs faster!
Some cool new things coming soon (the minuter missed exactly what these were)

## UFL big update
Done https://github.com/firedrakeproject/firedrake/pull/3166

**Master is failing!** UZ needs to fix his NGSPetsc merge, which wasn't testing against the correct branches. Seems to be an easy fix, using a method which is no a property. Connor fix it!

## JB: Meeting format review
**Not** an underhanded power grab whilst David is away! I just want some input on what everyone thinks of the current meeting format and PR merging process.
- Code review is technical and doesn't always involve everybody
  - Suggestion: Ask someone (Jack, Koki, Connor, Nacime) to review before meeting (this is what Jack and Connor did before this meeting)
- Like the idea of adding more space for discussion

## RK: Manual for Irksome
JB says can just add an Irksome page to the Firedrake manual.
CW suggests this can be under a 'firedrake and friends' section which would link to the actual Irksome documentation in the Irksome repo (could also icepack etc).
Could also be a demo or notebook!

## Merge PRs

- PB: [TSFC #301](https://github.com/firedrakeproject/tsfc/pull/301). Changes requested
 - Failing tests after merge of Matt Scroggs UFL stuff 
- PB: [FD docs #3221](https://github.com/firedrakeproject/firedrake/pull/3221). Dependent on TSFC #301
- PB: [MG bugfix #3231](https://github.com/firedrakeproject/firedrake/pull/3231). Changes Requested

# Date of next meeting

1600 GMT (1600 UTC) [2023-11-22](./Firedrake-meeting-2023-11-22)
