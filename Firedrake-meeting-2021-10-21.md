Date and time 2021-10-21 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: DH, LM, JB, TG, CW, PK, DRS, SV, KS

Apologies:

## JB: Further BLAS issues

Noticed a few more issues with BLAS/Accelerate appearing on Slack, all MacOS. Has there been another significant update, or is there a Firedrake regression?

JB: We want openblas from homebrew and link

LM: Had to explicitly set `--with-blas=/path/to/homebrew/openblas`.

brew installs blas -> set blas library -> numpy uses it 

The above logic somehow is not working.

Can we just install MacOS in github action (but no test suite)?

DRS: homebrew did something bad.


## KS: Refactor TSFC (for Subspace support)

Firedrake: https://github.com/firedrakeproject/firedrake/pull/2200

tsfc: https://github.com/firedrakeproject/tsfc/pull/261

No functionality changes. 

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-10-28](./Firedrake-meeting-2021-10-28/)