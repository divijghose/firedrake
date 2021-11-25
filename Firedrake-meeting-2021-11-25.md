Date and time 2021-11-18 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (JB minuted last time).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: CW (minuter), NB, LM, DH, KS, JDB

Apologies: SV, RK

## NB: Object versioning

PyOP2: https://github.com/OP2/PyOP2/pull/579

petsc: https://github.com/firedrakeproject/petsc/pull/8

### Halo exchanges

LM: PyOP2 `Dat` objects have two types of halo exchange: global -> local (consistent global state) and local -> global (put partial results into the halo for reduction).

DH: Updating PyOP2 data structures is always collective. Therefore halo updates do not require incrementing the version as it is effectively an implementation detail.

DH: This is useful for RK who wants to optimise external operators by avoiding unnecessary recalculations.

DH: We can consider the `Dat` to be in an invalid state if it needs to call `local_to_global`.

Summary: Neither of the halo exchange types should increment the `Dat` version.

Some other small changes to PyOP2 code recommended.

## NB: Update dual

PR: https://github.com/firedrakeproject/ufl/pull/25

Minor changes requested.

NB: Differentiation for the adjoint is hard. Therefore we raise an error unless the contents is zero.

DH: The dual stuff is unlikely to be deeply nested to establishing a proper tree traversal is not important. Happy to tackle any (potential) performance issues at later date.

## Merge PRs:

None.

## AOB

No meeting next week.

## Date of next meeting

1600 UTC (1600 GMT) [2021-12-09](./Firedrake-meeting-2021-12-09/)