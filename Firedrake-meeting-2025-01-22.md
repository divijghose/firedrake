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

Present:

Apologies:

## CW: Firedrake versioning?

Versioning would prevent us from accidentally breaking downstream packages with no warning.

* Should we version Firedrake and FIAT? How often would releases be? Semantic or date-based versioning?
* What about our forks of loopy and UFL?
* What about `firedrake-zenodo`?

One point of consideration is the fact that some of our dependencies (notably loopy) do not regularly make releases. I don't think versioning makes sense if we depend on non-versioned libraries.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS: [Fix hex interior-facet integrals](https://github.com/firedrakeproject/firedrake/pull/3878)

CW: https://github.com/firedrakeproject/firedrake/pull/3976

CW: https://github.com/firedrakeproject/firedrake/pull/3982


# Date of next meeting
1600 UTC [2025-01-29](./Firedrake-meeting-2025-01-29)