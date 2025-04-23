Date and time 2025-04-23 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: JHC, IM, CW, DH, RK, PB, KS, AO, CC

Apologies:

## Discussion-worthy issues/PR

### CW: Firedrake release

[#4193](https://github.com/firedrakeproject/firedrake/pull/4193) is ready for review.
* Predominantly updates to workflow files.
* Roll docs build into standard workflow to allow different "main" and "release" website pages with appropriate content/warnings.
* Don't allow any merges into release with `TODO` comments.
* Dev install is now slightly more involved, but makes sure we use the `petsc4py` from the local PETSc repo, not pypi.
* `firedrake-zenodo` has been updated but is mostly untested. We might have to debug this the first time someone wants a record after release.
* FAQ and policies for release procedure reviewed and approved.
* Last dependencies to be released: FIAT and UFL.

### PB: Mixed dual interpolation

[UFL #370](https://github.com/FEniCS/ufl/pull/370)
[Firedrake #4197](https://github.com/firedrakeproject/firedrake/pull/4197)


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* CW: [petsctools](https://github.com/firedrakeproject/firedrake/pull/4194) - wait until after release.
* JHC: [apt packages](https://github.com/firedrakeproject/firedrake/pull/4122) - approved pending removal of bugged VOM test.
* PB: [FacetSplitPC](https://github.com/firedrakeproject/firedrake/pull/4238) - wait until after release.

1600 UTC [2025-04-23](./Firedrake-meeting-2025-04-23)