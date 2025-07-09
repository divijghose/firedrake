Date and time 2025-07-09 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (interpolate, abstract reduced functionals, etc.)
1. CW: Preliminary prep for PETSc User Meeting 2026 ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-05-28))

# Agenda

Present: DH, LC, KS, RK, PB, CW, IM

Apologies: JHC

## CW: Is it time for a new major release?

A lot of new features have been added. I don't believe that we have to follow PETSc (though a patch release may be necessary).

Minutes:
- PB/RK having Irksome issues, they don't work with the release, combined with UFL main due to API changes relating to differentiation.
- DH points out that a major release now means we would need to continue supporting the old release, at least until October.
- Irksome master works with current release of firedrake and ufl - suggestion to make Irksome release now. Then merge things that are broken and allow Irksome master to track Firedrake master.
- CW to help RK to set up releases in Irksome. DH suggests a release branch should exist to enable quick bug fixes.
- No Firedrake release until October as planned. Note that we should publicise this well in September.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

https://github.com/firedrakeproject/firedrake/pull/4425
  - More payments links to be added
  - Merge this now, add the others later

KS: remove mesh.init() https://github.com/firedrakeproject/firedrake/pull/4201
  - Significant changes to mesh constructor
  - Lots of removals of mesh.init() calls
  - CW suggests lowering the new parameter `ignore_label_halo` to a different level of the API.

LC: VOM permutation matrix https://github.com/firedrakeproject/firedrake/pull/4341
  - Adds correct structure to match PETSc MatContext
  - Some conversation about how to handle errors raised from PETSc in tests - resolved that what is there is fine.
  - Merged

Blitz of other PRs took us from 100 open PRs to less than 90!
## Date of next meeting

1600 UTC [2025-07-16](./Firedrake-meeting-2025-07-16)