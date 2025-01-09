Date and time 2025-01-08 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. RK: sort out Firedrake USA details and website before Christmas time
1. ~CW: fix PyOP2+TSFC failing tests~ DONE
1. CW: Fix artefactsv3 issue
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: CW (minuter), JHC, DD, KS, DH, IM, RK, PB, LC

Apologies:

## PB: Speed up tests

* PB: Has an open PR to speed up `split`.

## KS: UFL MixedMesh abstraction

Mesh class for mixed function spaces.

[MixedMesh](https://github.com/FEniCS/ufl/pull/303)

* DH, KS, CW: Discussion concluding that the abstraction of sticking the mixed-ness inside the mesh (like we do with element) is OK. At the very least adopting `MixedFunctionSpace` would be extremely invasive in Firedrake.
  * The two approaches are effectively "zipping in opposite directions". With the Firedrake approach the structure of `MixedMesh` must match that of `MixedElement` whereas FEniCS do the zipping eagerly to build function spaces that are then combined.
* Following discussion on the PR should use `MeshSequence` (or similar) instead of `MixedMesh` to avoid confusion.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

1. UZ [References](https://github.com/firedrakeproject/firedrake/pull/3924) (already merged)
2. JHC [pyadjoint typo when checking hessian](https://github.com/dolfin-adjoint/pyadjoint/pull/189) (merged)
3. JHC Only evaluate relevant TLM values - [pyadjoint PR](https://github.com/dolfin-adjoint/pyadjoint/pull/190) (merged) & [firedrake PR](https://github.com/firedrakeproject/firedrake/pull/3957) (merged)
4. Reviewed a number of other PRs.

# Date of next meeting
1600 UTC [2025-01-15](./Firedrake-meeting-2025-01-15)
