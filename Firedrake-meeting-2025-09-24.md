Date and time 2025-09-24 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Go through issues and mark with "good first issue" for new MSc/PhD contributor projects.
1. LC: Deprecate `.at()` ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-08-13))

# Agenda

Present: DH, AG, LC, CW, IM, JHC, PB, KS

Apologies:

## CW+DH: Move Firedrake meetings to Tuesdays?

It will allow CW and JHC to attend in person.

Action CW: Ask RK.

To be clarified.

## CW: Style guide

Following https://github.com/firedrakeproject/firedrake/pull/4489#discussion_r2282267243 I have [drafted a style guide](https://github.com/firedrakeproject/firedrake/wiki/Style-guide) for discussion.

## CW: FYI

Just passing this on so everyone knows: https://github.com/FEniCS/ufl/pull/385

DH: requested so that this would happen after October release.

## LC: deprecate .at 

~https://github.com/firedrakeproject/firedrake/pull/4543~ Merged.

## LC: interpolate renumbering warning

~https://github.com/firedrakeproject/firedrake/pull/4572~ Merged.

## LC: annotation inside PointEvaluator

https://github.com/firedrakeproject/firedrake/pull/4567

CW: Shall we error or warn?

DH: Users tend to ignore warnings, but once adjoint breaks they may see warnings.

DH: Accessing dat is semi explicit.

DH: If we are doing something definitely wrong, we should error.

Merged.

## LC: delete `_from_cell_list`

https://github.com/firedrakeproject/firedrake/pull/4557

Merged.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* CW: https://github.com/dolfin-adjoint/pyadjoint/pull/226
* CW: https://github.com/firedrakeproject/petsctools/pull/14 then https://github.com/firedrakeproject/fiat/pull/180 then https://github.com/firedrakeproject/firedrake/pull/4560

CW: Firedrake citation to petsctools.

All approved.

* CW: https://github.com/firedrakeproject/firedrake/pull/4539

CW: Move docs build to separate job.

Approved.

* CW: https://github.com/firedrakeproject/firedrake/pull/4565

CW: Make VTK a hard dependency again.

Merged.

* CW: https://github.com/firedrakeproject/firedrake/pull/4545

CW: Use appropriate user in CI to avoid permissions errors on later runs

Approved.

## Date of next meeting

**IMPORTANT: now on Tuesdays!**

1600 UTC [2025-09-30](./Firedrake-meeting-2025-09-30)