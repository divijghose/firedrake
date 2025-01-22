Date and time 2025-01-22 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: Fix artefactsv3 issue
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do JM's PRs [transpose -> adjoint](https://github.com/firedrakeproject/firedrake/pull/3965) and [Cofunction self-assignment via interpolate](https://github.com/firedrakeproject/firedrake/pull/3939)

# Agenda

Present: DD, DH, LC, CW, PB, JHC

Apologies:

## CW: Firedrake versioning?

Versioning would prevent us from accidentally breaking downstream packages with no warning.

* Should we version Firedrake and FIAT? How often would releases be? Semantic or date-based versioning?
* What about our forks of loopy and UFL?
* What about `firedrake-zenodo`?


Discussion:
* Yes we want to, previous aim has been to do it after pip install lands
* Biggest organisational barrier is how do you manage bugfixes - do you only add to main, and versions are static, do we bugfix in minor versions? How many versions do we maintain? Bugfixes then need to be applied multiple time. This will be a big change for firedrake contributors, but is potentially just necessary.
* Loopy is a problem - doesn't have versioning, and even if we make releases for our fork, we would also need to pin a release for all of loopy's upstream dependencies.
* PETSc seem to do calendar releases for minor release but rolling patches.
* Semantic versioning is hard to do properly. Calender releases are easier to organise (still having minor versioning for bugfixes).
* Calendar releases would be simple (e.g. 2025.1, 2025.2), but we then need to decide how to do bugfix patches (2025.1.1, 2025.1.2 etc) - do we only patch for bugs that have been directly affecting user code?
* One point of consideration is the fact that some of our dependencies (notably loopy) do not regularly make releases. I don't think versioning makes sense if we depend on non-versioned libraries.
* We need to keep Zenodo in mind - as long as we have the commit of each repo in our fork it should be fine, but we need to keep it in mind to avoid inadvertently breaking it.

## CW: Big testing PR: MPI on 'the outside'

https://github.com/firedrakeproject/firedrake/pull/3385 describes the changes made. This is valuable for migrating to a pip install as we can properly start using a system MPI.

* Now have a script for running parallel tests over multiple jobs - manages logic and makes sure we limit the total number of cores used.
* This script could also be used by downstream libraries - should be used by any CI on the Firedrake runners to limit the total number of cores.
* See comments on PR.
* Shouldn't use letter characters outside the 26 from the Latin alphabet.
* Changes requested. If these are fixed this PR can be approved and merged.

## CW: `pip` migration plan?

I think we can just:
* Update the install docs
* Make `firedrake-install` warn about not being maintained any more
* Make an announcement in #general so people know
* Help downstream packages to migrate

#### Questions
* Can we drop MPICH at the same time? Downstream packages will need to change their CI anyway (which I can do for them).

Discussion:
* This is fantastic, thank you Connor and Jack!
* Yes if we can drop the requirement to build our own MPI that would be ideal. Default to whatever MPI is on the system we're building on.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS: [Fix hex interior-facet integrals](https://github.com/firedrakeproject/firedrake/pull/3878) - merged

CW: https://github.com/firedrakeproject/firedrake/pull/3976 - merged (we can now rebase and check PRs from JM)

CW: https://github.com/firedrakeproject/firedrake/pull/3982 - merged

IM: https://github.com/firedrakeproject/fiat/pull/130 - approved, merge pending a couple of small comments.


# Date of next meeting
Skipping 2025-01-29. 
1600 UTC [2025-01-29](./Firedrake-meeting-2025-02-05)