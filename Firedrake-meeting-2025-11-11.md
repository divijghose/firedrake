Date and time 2025-11-11 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: LC, AC, CW, PB, DH, IM, JHC, JM

Apologies:

## CW: What to do with KS's old PRs

https://github.com/firedrakeproject/firedrake/pull/4700 etc were closed last week because I assume that KS does not intend on doing anything more with them. It seems like a waste to close them immediately.

- Reopen and let them sit

## JHC (for JM): Mesh independent optimization trick

https://github.com/firedrakeproject/firedrake/pull/4575

- Optimise over a DG superspace, and choose orthonormal basis so that the mass matrix is the identity.
- Big limitation - can't apply constraints, more expensive (since more dofs in a DG space)
- Riesz map cached on ReducedFunctional
- DH: happy to approve in principle, but needs to be brought up to date with main and skip relevant complex tests

## LC: interpolation changes

https://github.com/firedrakeproject/firedrake/pull/4595

- PB: Does manual need updating?
- Fix Dofnotdefined error type hinting
- tensor.zero should happen only once - check adjoint interpolation on mixed spaces works

## Merge PRs

Merged https://github.com/firedrakeproject/firedrake/pull/4720

Merged https://github.com/firedrakeproject/firedrake/pull/4639

https://github.com/firedrakeproject/firedrake/pull/4607: add section in manual about quadrature schemes

## Date of next meeting

1600 UTC [2025-11-18](./Firedrake-meeting-2025-11-18)