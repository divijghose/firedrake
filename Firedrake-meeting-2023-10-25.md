Date and time 2023-10-25 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?
1. PB: Spectral on triangles and tetrahedra?


# Minutes

Present: CW, JB, KN, DH, PB, RH, NB, FA, DD

Apologies:

## New docstring and typehint policy
Read more here: https://github.com/firedrakeproject/firedrake/wiki/Docstrings
Docstring policy was discussed at the meeting. The code must follow PEP8 and PEP257(where PEP257 does not conflict numpydoc).
DH agreed with the policy docstring text.

## libersupermesh
The work with libersupermesh is advancing. JB is working on arch platform.

## Zenodo canary fail
JB is going to disable it.


## Merge PRs
- PB: [#3181](https://github.com/firedrakeproject/firedrake/pull/3181) Cofunction coarsening.

  This PR requires PB review. 

- PB: [#3159](https://github.com/firedrakeproject/firedrake/pull/3159) Re-injection of coefficients; no-op for unmodified dat.

  This PR depends on the anterior PR (3181). It was not reviewed once the previous PR required changes.

- PB: [#3164](https://github.com/firedrakeproject/firedrake/pull/3164) Make tests basis-independent.
  
  This PR still requires trivial changes.
  
- JB: [#3041](https://github.com/firedrakeproject/firedrake/pull/3041) FML.

  Approved!
  
- KS: [#3174](https://github.com/firedrakeproject/firedrake/pull/3174) VOM touch up.
  
  This PR discussed the concepts, it was not reviewed.
  
  
# Date of next meeting

1600 GMT (1600 UTC) [2023-11-01](./Firedrake-meeting-2023-11-01)
