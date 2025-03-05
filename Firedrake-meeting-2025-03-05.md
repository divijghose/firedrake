Date and time 2025-03-05 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
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

Present: DH, AO, JHC, DID, IM, LC, KS

Apologies: CW, PB

## CW: Switch to being root user in the Docker containers

From Francesco Ballarin:
> And on the topic of docker: can anyone remind me what is the rationale for having a firedrake user and a local installation in $HOME/.local, rather than a simpler setup that uses directly the root user and installing everything in /usr?
I do understand that outside of a docker image we'd never use the root user for security reasons, but the docker container itself is isolated from the rest and, if security was a concern, the current firedrake user isn't really secure either (since it must allow to sudo without password).
I also do understand that in the previous iteration of docker images there was a firedrake virtualenv which probably justified a standalone user. But now, with that virtualenv gone, is there really a point in installing to $HOME/.local rather than the system wide path?

I agree with him. It causes needless complication (like having to set `PYTHONPATH` on GitHub-hosted runners) to get things to work properly. This is causing issues for some users ([example](https://github.com/firedrakeproject/firedrake/discussions/4057#discussioncomment-12361270)).

What do people think?

DH + JHC: Can probably try and see if anything breaks.

## pip install

SLEPc has slipped out of Firedrake.

Need SLEPc in CI.

Need to document SLEPc installation: [issue](https://github.com/firedrakeproject/firedrake/issues/4097).

CW: [Install slepc4py into vanilla container and tidy up test suite](https://github.com/firedrakeproject/firedrake/issues/4097)

- DH left a comment.
- CI currently not passing.

JHC: firedrake-check spits out "Option left" warnings.

CW: [Copy conftest.py into firedrake_check so markers are recognised](https://github.com/firedrakeproject/firedrake/pull/4092)

DH: Enabled auto-merge.

## CI

We currently leak docker container.

OSError: [Errno 28] No space left on device: '/tmp/pip-unpack-fg1j5x1y/attrs-25.1.0-py3-none-any.whl'

Error: Process completed with exit code 1.

## netgen

netgen demo has outdated install instructions: [issue](https://github.com/firedrakeproject/firedrake/issues/4098).

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [#4073](https://github.com/firedrakeproject/firedrake/pull/4073)

PB: [#4012](https://github.com/firedrakeproject/firedrake/pull/4012) (depends on #4073)

PB: [#4082](https://github.com/firedrakeproject/firedrake/pull/4082)

Will do PB's PRs when PB is present.

DD: ~[#4088](https://github.com/firedrakeproject/firedrake/pull/4088)~ Merged.

DD: ~[UFL #355](https://github.com/FEniCS/ufl/pull/355)~ Merged.

~[#4095](https://github.com/firedrakeproject/firedrake/pull/4095)~ Merged.


# Date of next meeting
1600 UTC [2025-03-12](./Firedrake-meeting-2025-03-12)