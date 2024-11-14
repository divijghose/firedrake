Date and time 2024-11-13 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (DD to pick -> PB)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. DH: Finish UFL element.value_shape() update
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. JB/UZ: ngsPETSc releases ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-16))
1. PB: Speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30))
1. RK: sort out Firedrake USA details and website before Christmas time
1. CW: tackle Loopy warnings

# Agenda

Present: PB, FA, RK, DH, DD, KS, IM, LC, CW

Apologies: CW (will be 20 minutes late), JB

## Issues

[Skipping Jacobian reassembly](https://github.com/firedrakeproject/firedrake/issues/3813) DH: Nontrivial, it is low priority, high risk of getting it wrong. KH: easy if we inspect Parloop arguments.

[Checkpointing referencing](https://github.com/firedrakeproject/firedrake/issues/3780) Suggestions: CW: use `strip_form_data`. DH: change block_varible.output to a property.

[#3779](https://github.com/firedrakeproject/firedrake/issues/3779) closed as there was no follow-up.

## Ongoing PRs

[UFL update](https://github.com/firedrakeproject/firedrake/pull/3862) KS: droppping gdim will break checkpointing, this has to be addressed by filtering the previosuly generated hashes.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


KS:[Firedrake](https://github.com/firedrakeproject/firedrake/pull/3855) adds tests

KS:[TSFC](https://github.com/firedrakeproject/tsfc/pull/327) adds dtype to nodes, requested fixes to type comparison 

UZ: [ngsPETSc pip](https://github.com/firedrakeproject/firedrake/pull/3857) approved, merged

# Date of next meeting
1600 UTC [2024-11-20](./Firedrake-meeting-2024-11-20)