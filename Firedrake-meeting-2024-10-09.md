Date and time 2024-10-09 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick (again))
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))

# Agenda

Present: DH, JB, CW, PB, IM, RK, KS, CJC, UZ

Apologies:

## JB: Has spec'd some runners

AMD HPC grade processors 32 cores, more memory channels

No GPU

JB: [this](https://www.novatech.co.uk/savedbuild/5d1a496f-9b01-48ee-8aa2-22a03413366c)

DH: self-hosted, linux:

[related PR](https://github.com/firedrakeproject/firedrake/pull/3787)

[gusto](https://github.com/firedrakeproject/gusto/pull/559)

[gust_case_studies](https://github.com/firedrakeproject/gusto_case_studies/pull/29)

[libsupermesh](https://github.com/firedrakeproject/libsupermesh/pull/5)

[irksome](https://github.com/firedrakeproject/Irksome/pull/97)

## JB: Triage issues in meetings?
There are a lot of open issues with no action and no triage. (Maybe some of them are 4th year/MSc projects...) Should we start triaging during meetings?

Not today.

Nacime's PRs (not sure how active he will be, so wait a bit)

Reuben's PRs: 

[Fix voting algorithm](https://github.com/firedrakeproject/firedrake/pull/3293)

Action Leo (with CW)

[Correct transpose](https://github.com/firedrakeproject/firedrake/pull/3167)

Action JB (rebase and test)

[Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)

Action Leo

[Cubit](https://github.com/firedrakeproject/firedrake/pull/2116)

...

## JB: Revisiting old PRs
We never off-boarded Rueben's branches and we should probably off-board Nacime's now. (And don't forget Sophia's branches!)

## JB/CW/UZ: Move ngsPETSc tests out of Firedrake

DH: Yes.

## JB: Pin PETSc/SLEPc forks to releases rather than arbitrary commits
Fixes are ported to releases and there is 1 minor release per month. I believe this will make installation a bit more stable in the run up to wheel. Thoughts?

Yes.

## PB/RK: Issues with sphinx in FInAT
Doc build is broken, we suspect is due to an API change.
https://github.com/FInAT/FInAT/actions/runs/11236557144/job/31237402300

Look for inter sphinx_mapping in firedrake: docs/source/conf.py:

...
'python': https:.. ....
...

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*
- JB: ~[#3730](https://github.com/firedrakeproject/firedrake/pull/3730) (and corresponding [PyOP2 #724](https://github.com/OP2/PyOP2/pull/724))~
- JB/KS: Need merging in this order: 
  - ~Firedrake PETSc [#22](https://github.com/firedrakeproject/petsc/pull/22)~,
  - ~Firedrake SLEPc [#8](https://github.com/firedrakeproject/slepc/pull/8)~, 
  - ~Update IO in Firedrake for PETSc changes [#3792](https://github.com/firedrakeproject/firedrake/pull/3792)~,
  - ~Unpin mpi4py [#3777](https://github.com/firedrakeproject/firedrake/pull/3777),~
  - ~Allow installing with Python 3.13 [#3791](https://github.com/firedrakeproject/firedrake/pull/3791)~
- PB: ~[#3736](https://github.com/firedrakeproject/firedrake/pull/3736) Reviewed last week.~
- PB: ~[#3771](https://github.com/firedrakeproject/firedrake/pull/3771) Reviewed last week.~

# Date of next meeting
1600 BST (1500 UTC) [2024-10-16](./Firedrake-meeting-2024-10-16)