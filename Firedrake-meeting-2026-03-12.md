Date and time 2026-03-12 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. DH: Trim github organisation teams member.

# Agenda

Present: DH, CW, JHC, IM, PB, DD

Apologies: LC

## JHC: [#4964](https://github.com/firedrakeproject/firedrake/pull/4964) `Ensemble.sequential`

Context manager for running code on each `ensemble.comm` spatial comm in turn.

DH suggestion: add wrapper to give clear error if something is passed in that can't be communicated by MPI. Approved post small comments of requests.

## JHC [#4965](https://github.com/firedrakeproject/firedrake/pull/4965) Refactor of `EnsembleReducedFunctional`

Big refactor to allow using `EnsembleFunction` as a distributed control. Requires breaking up into separate Bcast/Transform/Reduce and composing them back together.

Revisions required to ensure model is clear, adapt code to minimise the API change

## CW: Deprecate `WithGeometry.create`

Sane API cleanup: https://github.com/firedrakeproject/firedrake/pull/4957

Approved

## CW: Refactor periodic meshes (pyop3 prerequisite)

https://github.com/firedrakeproject/firedrake/pull/4836

Still waiting on 4(!) PETSc MRs but good to get this on people's radar. Someone will have to review this...

Warn about breaking API change of relabelling. Otherwise looks sensible.

## Merge PRs

* CW: https://github.com/firedrakeproject/firedrake/pull/4958 - done

## Date of next meeting
Meeting times going forward: Tuesday 4pm unless David has a monthly meeting, in which case Tuesday 3pm. First Tuesday meeting 31st March.

1600 UTC [2026-03-19](./Firedrake-meeting-2026-03-19)
