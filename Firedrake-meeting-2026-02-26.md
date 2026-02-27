Date and time 2026-02-26 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. DH: Trim github organisation teams member.
1. CW: Draft policy for requirements for contributor/author recognition.

# Agenda

Present: LC DH CW IM AC JHC PB

Apologies:

## CW: firedrake-zenodo

On Monday I spent >2 hours trying to make a Zenodo release for someone. I don't understand the GitHub API tool and it is throwing incomprehensible 404 errors. I would dearly love to not have to do this.

Can we drop firedrake-zenodo? We could replace it with a guide on our website about providing provenance for their software. Josh and I think that citing `pip freeze` and PETSc's `configure.log` might be  sufficient.

- won't be citations if we do this. Github is not an archive, Zenodo is
- Encourage people to do research with Firedrake releases?
- takes a long time for some stuff to be merged.
- Doing this used to be easier, try to fix the regression

## CW: `-ffast-math` the culprit 🫠

https://github.com/firedrakeproject/firedrake/pull/4913

We need to disable it for CI, but do we want to more generally?

- Compiler (only runs on rank 0) was crashing, causes all other ranks to deadlock
- Only happened on CI runners
- Fix was to turn off fast math for GCC. Do we turn this off for other compilers (clang, etc.)? Or only turn it off on the CI runners?
- Only turn it off on the CI runners. See if anyone complains about compiler crashes.

## AC: Compute barycentric coordinates symbolically (with GEM)

Review draft PR: https://github.com/firedrakeproject/fiat/pull/230

- DH: this introduces a GEM dependency into FIAT
- We are okay with this. It avoids us having to produce wrapper classes in finat. GEM is a pure python package inside the same git repository.
- Get review from Rob Kirby

## LC: https://github.com/firedrakeproject/firedrake/pull/4926

## Merge PRs

## Date of next meeting

1600 UTC [2026-03-05](./Firedrake-meeting-2026-03-05)
