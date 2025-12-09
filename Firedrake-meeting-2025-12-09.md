Date and time 2025-12-09 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (LC to pick -> PB)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: DH, JHC, CW, LC, PB, IM, AC

Apologies:

## [Data Assimilation hackathon at RAL (Spring 2026)](https://www.cosec.ac.uk/what-is-cosec/cosec-fellowship-programme/cosec-2025-fellows/jemima-tabeart/)

DH: organized by CoSeC fellow Jemima Tabeart (TU Eindhoven)

CW: we should add this to the Firedrake calendar


## JHC: Covariance operators and noise generation [#4716](https://github.com/firedrakeproject/firedrake/pull/4716)

Autoregressive covariance operators for a) generating correlated noise and b) weighting norms in optimisation problems. (Changes suggested)

Includes noise generation code from [#3799](https://github.com/firedrakeproject/firedrake/pull/3799) (Changes suggested)

PB: we should automate `BrokenElement(VectorElement) -> VectorElement(BrokenElement)` in finat.ufl

PB: once could a CholeskyFactor node to Slate to avoid the parloop (not for this PR)

DH: The VOM mass matrix is always the identity, this should be special case.

JHC: add demos in the Spring hackathon.


## CW: Comm fixes (quite a big conceptual change)

https://github.com/firedrakeproject/firedrake/pull/4766 (approved)

DH: we should comment on pytest-order when we merge this

## LC: interpolate a two-form

https://github.com/firedrakeproject/firedrake/pull/4770 (approved)

## Merge PRs

## In person meeting in Oxford (20 Jan 2026)


## Date of next meeting

1600 UTC [2025-12-16](./Firedrake-meeting-2025-12-16)
