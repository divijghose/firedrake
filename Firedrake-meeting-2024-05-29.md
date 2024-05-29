Date and time 2024-05-29 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto
1. JB: move tinyASM to firedrake/preconditioners
1. KS: PETSc + Cython3.0 + numpy2.0 issue: why slow?

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Minutes

Present: DH, KS, DD, CW, JB, PB, IM

Apologies: NB

## Firedrake meeting
DH: Big names coming: L. Ridgeway Scott, Matt Knepley
PB: Scott MacLachlan
DH: Leeds offering to host in 2025, although FiredrakeUSA 2025 in Texas

## PETSc Meeting
DH: Matt has been prodded about the one reverted commit that we are holding onto (details of commit in PR)

## Performance Regression
CW: Full test suite with cold or hot cache is slower on Python3.12 running on Ubuntu 24.04 when compared to Python3.11 on Ubuntu 22.04.

## Eindhoven
DH: Worked out how to do Josh's new project


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- PB: [#3596](https://github.com/firedrakeproject/firedrake/pull/3596) Changes requested (approved).
- DD: [#3595](https://github.com/firedrakeproject/firedrake/pull/3595) Merged.
- CC: [#3577](https://github.com/firedrakeproject/firedrake/pull/3577) Gather functional, changes requested (approved).
- CC: [#3587](https://github.com/firedrakeproject/firedrake/pull/3587) Lists in ensemble reduced functional, changes requested.
- DD: [#3562](https://github.com/firedrakeproject/firedrake/pull/3562) FWI Demo, warnings required, changes requested.

# Date of next meeting

1600 BST (1500 UTC) [2024-06-05](./Firedrake-meeting-2024-06-05)