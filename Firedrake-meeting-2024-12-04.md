Date and time 2024-12-04 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. CW (formerly JB): Move PyOP2 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. RK: sort out Firedrake USA details and website before Christmas time
1. CW: tackle Loopy warnings - PR almost ready.

# Agenda

Present: DH, DD, KS, PB, CW, IM, FA, CC, RK

Apologies:

## DD: FormSum memory usage [PR 3897](https://github.com/firedrakeproject/firedrake/pull/3897)

Enhance the performance and reduce memory usage for assembling `FormSum`

See PR and discussion. Lots of PyOP2 objects created on the fly and not cached, so take up increasing amounts of memory.
Implementing as in-place addition of arrays is the correct thing to do, but it should be hidden in a method of `pyop2.Dat`. This avoids explicitly dealing with numpy arrays in `assemble`, and is also more future-proof for GPU development - all the implementation is hidden in `Dat`.

## Firedrake US
- RK: Need to decide registration costs.
- DH: CCP can help with funding because this is important for community building.
- RK: SIAM has given funding for Texas and Louisiana grad students.
- Discussion on budget lines and what that means for subsidies. Sustenance, coffee, reg fees etc.

## KS: Finite elements in time.
`ExtrudedMesh` is being updated so that it can handle finite elements in time.
Requires creating a restricted function space to have the appropriate boundary conditions (i.e. the initial conditions) at the bottom boundary (i.e. the initial time).

## CCP
- CCP was funded!
- Can help fund Firedrake US.
- Firedrake + Fenics hackathon planned for around Easter next year in Exeter.
- Lots of other activity to come.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [#3436](https://github.com/firedrakeproject/firedrake/pull/3436) Reviewed last week, docs added. Docs need to be more detailed, including the eq solved, the petsc options, and any appctx entries.

PB: [#3868](https://github.com/firedrakeproject/firedrake/pull/3868) Reviewed last week, changes addressed. Approved.

# Date of next meeting
1600 UTC [2024-12-11](./Firedrake-meeting-2024-12-11)
