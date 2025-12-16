Date and time 2025-12-16 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (PB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: DH, CW, LC, IM, AC, PB

Apologies: 


## Merge PRs

* CW: https://github.com/firedrakeproject/firedrake/pull/4762
 - Explicitly link MPI in setup.py, remove need to set environment variables. Good! Approved + Merged.
* CW: https://github.com/firedrakeproject/firedrake/pull/4754
 - Bizarre behaviour in Cofunction init regarding val/function_space. Approved + Merged. 
 - Cofunction init deserves a refactor if anyone has the time and energy. 
* CW: https://github.com/firedrakeproject/firedrake/pull/4758
 - Remove Loopy from Zenodo, Add rate limit that is necessary. Approved + Merged.
* CW: https://github.com/firedrakeproject/firedrake/pull/4780
 - Allow `MeshGeometry` to be None for extruded meshes. Approved + Pending Gusto.
* LC: https://github.com/firedrakeproject/firedrake/pull/4779
 - Apply simplifications for when we assemble combinations of Adjoint and Action. Approved + Merged.
 - Need to fix the ability to take action of coefficient and form in UFL - not in this PR.
* LC: https://github.com/firedrakeproject/firedrake/pull/4763
 - Small changes requested. Generally approved, can be merged when done. 

Reviewing further PRs:

PB: Firedrake [#4777](https://github.com/firedrakeproject/firedrake/pull/4777)
PB: FIAT [#202](https://github.com/firedrakeproject/fiat/pull/202)
- Ensure Vector/Tensor/Mixed stays on the outside and the element inside is restricted.
- Merged.

LC: Firedrake [#4739](https://github.com/firedrakeproject/firedrake/pull/4739)
- Symbolic Interpolation docs. Merged.

PB: Firedrake [#4739](https://github.com/firedrakeproject/firedrake/pull/4764)
 - Bug fix. Merged.





## Date of next meeting

1600 UTC [2026-01-06](./Firedrake-meeting-2026-01-06)
