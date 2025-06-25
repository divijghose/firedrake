Date and time 2025-06-25 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
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

Present: DH, KS, IM, DRS, JHC, CW, LC

Apologies: PB

## CW: `petsc_raises`

https://github.com/firedrakeproject/firedrake/pull/4384

DH: Upgrade Python on firedrake CI?
CW: We're currently using Ubuntu latest. We'd need to use Pyenv, which slows down CI.
DH: Don't upgrade Python, this is only a problem for 8 months until new Ubuntu.

## DRS: hard to debug error

https://github.com/danshapero/mantle-convection-test

DRS: mantle convection example not working. Also failing on RK. Was working on install from April. Failing on most recent docker. 
DRS: Failing in line search. Can fix sometimes by increasing max number of iterations.
JHC: With line search off, does it still fail?
DH: Residual is exploding. Is the problem ill-conditioned?
JHC: Is the problem non-dimensionalised? Mantle problems have large dimensions
DRS: It is. Rayleigh number is 10^6. Everything else is O(1).
JHC: Is the nonlinearity causing the ill-conditioning?
DRS: Was working on older installs. 
JHC: Look at MUMPS version. If on Ubuntu you could be on an older MUMPS.
DH: Try passing `--no-package-manager` to `firedrake-configure`. This will configure PETSc closer to how we did it a few months ago.

## KS: Submesh PRs

Small dependency:

UFL: https://github.com/FEniCS/ufl/pull/382

KS: small PR to fix UFL indexing
DH: Looks fine, need to ask fenics

Core implementation:

UFL: https://github.com/FEniCS/ufl/pull/264

DH: renamed `MixedMesh` to `MeshSequence` in PR title
DH: Needs more documentation for `extra_measures` parameter. It is publicly-facing
DH: Once we have submeshes, we can do integrals of quantities defined on different meshes. For facets, an exterior facet of a subdomain may be an interior facet of another subdomain. We integrate over intersections of primary measures and `extra_measures`.
KS: updated form signature
DH: correct variable names to `hashdata`
Looks good, just add documentation and also run by fenics

Firedrake: https://github.com/firedrakeproject/firedrake/pull/3478

KS: large file is output from benchmark
DH: probably not the right way to do this
DH:  `extra_measures` dict should contain Measure and not strings
This is nearly there, just need to pester fenics people (mainly Jørgen).


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* CW: https://github.com/firedrakeproject/petsctools/pull/5

CW: Is the API change fine?
DH: API change is necessary. PR is approved.

* DH: https://github.com/firedrakeproject/firedrake/pull/4385

DH: Pytest doesn't respect namespaces

* PB: https://github.com/firedrakeproject/firedrake/pull/4405

DH: Lots of special-casing just for a single PETSc mat type. Is it necessary?
DH: Also need more tests.
KS: we should grab lgmap and underlying data in cython and change that.

* DH: https://github.com/dolfin-adjoint/pyadjoint/pull/210

DH: Australians noticed that if you use single memory output you get the wrong answer.
DH: checkpoints were being discarded using `marked_in_path`.
DH: fix was to split flags in `BlockVariable`.
DH: I need to add their MFE in as a test.

## Date of next meeting

1600 UTC [2025-07-02](./Firedrake-meeting-2025-07-02)