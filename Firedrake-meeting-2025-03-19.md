Date and time 2025-03-19 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present:

Apologies:

## CW: Root in Docker

https://github.com/firedrakeproject/firedrake/pull/4104

Seems to work fairly well. I have tested with a number of downstream packages.

## CW: Remove part of CI

https://github.com/firedrakeproject/firedrake/pull/4086

## JHC: Various adjoint fixes

1. [#4126](https://github.com/firedrakeproject/firedrake/pull/4126) Ensure `Function.subfunctions` is always taped. Currently, subfunctions are not taped if they are first accessed before annotation is enabled. This PR corrects that and adds a test.

2. ~~[#4128](https://github.com/firedrakeproject/firedrake/pull/4128) Variational solver should either complain if `bounds` are passed to `solve`, or remove them from the `kwargs` if they are `None`.~~ Merged.

3. [#4130](https://github.com/firedrakeproject/firedrake/pull/4130) Only pass `solver_parameters` to the adjoint solver once, and make sure it's the one processed by `OptionsManager`.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

CW: [#4083](https://github.com/firedrakeproject/firedrake/pull/4083)

IM: [FIAT #134](https://github.com/firedrakeproject/fiat/pull/134)

AO: [#4115](https://github.com/firedrakeproject/firedrake/pull/4115/)

PB: [#4012](https://github.com/firedrakeproject/firedrake/pull/4012)

PB: [#4056](https://github.com/firedrakeproject/firedrake/pull/4056)

PB: [#3973](https://github.com/firedrakeproject/firedrake/pull/3973)

# Date of next meeting
1600 UTC [2025-03-26](./Firedrake-meeting-2025-03-26)??? (TBD, many core developers will be away)