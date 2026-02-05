Date and time 2026-02-05 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (IM to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: CW (minuter), JHC, IM, LC, PB, DH, AC

Apologies:

## Agenda items

### DH: Location decided for PETSc+Firedrake conference

* DH: Oxford. £1000 for everything for the full week. Budget allows for a 60% student discount. Non-accommodation prices £420, student £170. It will be possible to register for just Firedrake or PETSc (3 days each).

### PB: FIAT reference data repository 

I would like to update the FIAT regression tests. The issue is that the reference data lives in a separate bitbucket repo that is owned by the fenics project. For the moment, I just need write access to this repo, but it'd be good if we can migrate this to our own organization. https://bitbucket.org/fenics-project/fiat-reference-data/src/master/

* DH: PB to pull the repo and push to a new repo in the firedrakeproject organisation.

### LC: Cross-mesh Hdiv / Hcurl

https://github.com/firedrakeproject/firedrake/pull/4804

* Reviewed

### LC: mixed cross-mesh operator

https://github.com/firedrakeproject/firedrake/pull/4792

* Merged

### LC: matfree interpolation operator

https://github.com/firedrakeproject/firedrake/pull/4778

* Approved.

## Merge PRs

PB: finat.ufl fixes [FIAT #122](https://github.com/firedrakeproject/fiat/pull/122)

* Merged.

## Date of next meeting

1600 UTC [2026-02-12](./Firedrake-meeting-2026-02-12)
