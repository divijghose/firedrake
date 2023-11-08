Date and time 2023-11-08 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?

# Minutes

Present: JB, DH, RK, PB, NB, RNH, DD, KS, CJW, IM, FA

Apologies:

## DH: Meeting next week
Will go ahead JB to chair.


## JB: PETSc and SLEPc forks need to be kept in sync
https://github.com/firedrakeproject/petsc/blob/firedrake/include/petscversion.h

https://github.com/firedrakeproject/slepc/blob/firedrake/include/slepcversion.h

This is resolved, but should be kept in mind for the future!

## Merge PRs
DD: There are Matthew Scroggs PRs to adapt firedrake, tsfc and finat to the latest UFL element interface.

FInAT PR: [111](https://github.com/FInAT/FInAT/pull/111) *...

tsfc PR: [302](https://github.com/firedrakeproject/tsfc/pull/302) *...

Firedrake PR: [3166](https://github.com/firedrakeproject/firedrake/pull/3166) * Various changes requested. Need to ensure we do not break users code with these changes by changing the API without warning. There is also a mystery as to why some classes have (or maybe have not?) changed name.

Action item UZ: Review, check and merge upstream NGSolve changes required for UFL update.

DD: UFL upstream [PR 46](https://github.com/firedrakeproject/ufl/pull/46) Depends on above being merged ^^

DD: Adding `__str__` method in `SolverVarFormBlock`. [3199](https://github.com/firedrakeproject/firedrake/pull/3199). Need to do validation on `ufl2unicode`, specifically the RHS, so that errors are not raised.

PB: TransferManager: Re-injection of coefficients [3159](https://github.com/firedrakeproject/firedrake/pull/3159) Merged.

RNH: [#3204](https://github.com/firedrakeproject/firedrake/pull/3204)

CW: [3209](https://github.com/firedrakeproject/firedrake/pull/3209)

# Date of next meeting

1600 GMT (1600 UTC) [2023-11-15](./Firedrake-meeting-2023-11-15)
