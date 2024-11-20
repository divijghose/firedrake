Date and time 2024-11-20 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (PB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. CW (formerly JB): Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. JB/UZ: ngsPETSc releases ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-16))
1. PB: Speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30))
1. RK: sort out Firedrake USA details and website before Christmas time
1. CW: tackle Loopy warnings

# Agenda

Present:

Apologies: UZ

## [pyadjoint PR#177](https://github.com/dolfin-adjoint/pyadjoint/pull/177)
Allow `set_working_tape` and `stop_annotating` to be used as function decorators, and implement `no_annotations` in terms of `stop_annotating`.

## CW: Merging JB's big merge

https://github.com/firedrakeproject/firedrake/pull/3817 is very nearly ready I believe. I am keen to get it merged ASAP as it is holding up any changes to PyOP2.

## CW: (related) What is the long-term vision for Firedrake installation?

- I believe that we want to be moving towards `pip install firedrake` (even without a wheel) as the sole installation method.
- `firedrake-install` should be made much more minimal, effectively building PETSc and then called `pip install firedrake`. Importantly this means:
    - The script should not manage `homebrew` or `apt`
    - Extra packages like pytorch, gusto etc should not be installed via special flags. They can just be pip-installed.

Thoughts? If people agree then I can work to rip out a lot of code and incrementally improve the installation process.


## PB: RestrictedFunctionSpace

Ongoing discussion on what is the right interface to restrict any FunctionSpace given the bcs of a problem. 

My proposal: `RestrictedFunctionSpace(MixedFunctionSpace, bcs)`

[PR needs review](https://github.com/firedrakeproject/firedrake/pull/3868)

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

1. UZ: ngsPETSc was not installed via pip [PR#3873](https://github.com/firedrakeproject/firedrake/pull/3873)

2. DD: Disk checkpointing for adjoints with schedules: [Firedrake PR 3812](https://github.com/firedrakeproject/firedrake/pull/3812) + [Pyadjoint PR 173](https://github.com/dolfin-adjoint/pyadjoint/pull/173)

3. KS: [dtype](https://github.com/firedrakeproject/tsfc/pull/327)

# Date of next meeting
1600 UTC [2024-11-20](./Firedrake-meeting-2024-11-27)