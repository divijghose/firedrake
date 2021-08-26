Date and time 2021-08-26 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present: LM, DRS, RK, JB, CW, MG, RNH, NB, SK, KS

Apologies: Sophia, DH

## RNH/LM: should we fully deprecate python Expression kernels?
Suggested in PR review [here](https://github.com/firedrakeproject/firedrake/pull/2115#discussion_r691157510).

LM: Yes. Ask in thetis channel.

Delete it and test.

Maybe put Deprecation warning.

## DRS: OpenBLAS threads warning

Installed with --with-blas=download via PETSc correctly, but see OMP_NUM_THREAD warning.

Try putting mkl pthred mode?

Put petsc library in the search path when `from firedrak import *`.

## SV: SIAM PP
I am not in the meeting because I'm in holidays, but @Rob Kirby and @Dan Shapero please answer my email :)

## Solver hanging issue

JB: If `snes` is created in a loop, the program can hang.

LM: If we accidentally leave python level thing lying around in the `DM`, it might not get collected.

We should create better MFE.

Need more thoughts on ref cycle.

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-09-02](./Firedrake-meeting-2021-09-02/)
