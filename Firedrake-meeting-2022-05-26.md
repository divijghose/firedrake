Date and time 2022-05-26 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (SV to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS: Test PETSc main against current Firedrake
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022

# Agenda

Present: DH, RNH, CW (minuter), PK, KS, JB, SV

Apologies:

## https://github.com/firedrakeproject/firedrake/issues/2452

- KS: Can use a `PetscSection` to save DMSwarm points.
- DH: This will work if you remove vertices from ghost cells.
- DH: Firedrake uses its own geometry rather than PETSc's. When loading from disk you only need to store topological information and then you can reconstruct the geometric/numbering information afterwards.

## RNH: Updated VertexOnlyMesh API
See discussion #2450 and specifically [this comment on API proposal](https://github.com/firedrakeproject/firedrake/discussions/2450#discussioncomment-2818569)

- DH: Remove `point_migration` keyword argument as this is premature optimisation.
- DH: `redundant=True` should also be strongly encouraged since, if you have so many points as to need it, the locate-cell functionality will kill performance.

## SV: block optimisation in Slate
merge fix BOP https://github.com/firedrakeproject/firedrake/pull/2446

- KS: To take a look at the code. 
- SV: Needs to rerun performance measurements.

## DH: Stringifying UFL is not nice

- DH: `str(expr)` is really hard to read. Now we're on Python 3 we can produce unicode (e.g. integral signs).
- DH: `to_latex` is not really sufficient.

## JB: numpy and scipy switching to Mazon for building

- JB: Also scipy needed for tests to pass.
- DH: Best to default install scipy.

## Merge PRs


## Date of next meetings
No meeting next week due to bank holiday (UK)
Next meeting: [2022-06-09](./Firedrake-meeting-2022-06-15) (JB, KS, SV at ECCOMAS the week before)


