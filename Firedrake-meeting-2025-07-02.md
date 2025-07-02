Date and time 2025-07-02 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (LC not here, someone else pick)
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

Present: DH, CW, IM, JHC, PB, CJC, KS

Apologies: LC

## CW: Got email from Onno. Is there anything we should do now?

DH: Trying to setup EasyChair.

## CW: PETSc/SLEPc release woes

Example: https://github.com/firedrakeproject/firedrake/actions/runs/16026361480/job/45215200574

The problem is very obscure. I've identified it but the fix is to either always stick to the latest release or build petsc4py and slepc4py differently.

CW: slpec4py build their own petsc4py (3.23.4) regardless of what petsc4py we want.

DH: --download-slepc-commit=... looks fine.

DH: When SLEPc release, are they not supposed to pin the PETSc?

CW: They should be compatible, so pinning is not necessary?

CW: Have a PR to bump the versions, but this requires point release.

DH: Fine, as we need point release for pyadjoint, anyway.

## JHC: Attach `OptionsManager` to a single PETSc Object

[petsctools #7](https://github.com/firedrakeproject/petsctools/pull/7)

Each instance of `OptionsManager` is meant to be used for only one PETSc object, but this isn't enforced anywhere.
In Firedrake the solver classes to connect one `OptionManager` to one PETSc object. This PR adds some free functions to make it easier to do this only with `petsctools`.

In `set_from_options`:

This is a breaking change.

Change to warning?

## JHC: `EnsembleFunction` and friends [#4025](https://github.com/firedrakeproject/firedrake/pull/4025)
Mixed function spaces where the components are distributed over different members of the `Ensemble`.

Also includes `EnsembleFunctionSpace` and the corresponding dual objects.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [GTMGPC restrict](https://github.com/firedrakeproject/firedrake/pull/4373)

## Date of next meeting

1600 UTC [2025-07-09](./Firedrake-meeting-2025-07-09)