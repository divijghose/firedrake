Date and time 2025-05-07 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (KS pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (interpolate, abstract reduced functionals, etc.)
1. JHC, KS: Make docker and pypi accounts and ask CW to invite you.

# Agenda

Present: DH KS IM LC PB DH CW JHC

Apologies: RK

## Discussion-worthy issues/PR

### CW: Testing more configurations

I would like to test a number of different configurations including:

* default
* complex
* macOS
* default-int64
* GPU (coming soon)

What sort of testing coverage do we want for these? In particular, **should we think about not running the entire test suite for complex mode?**

- We want to cover different builds, but running the entire test suite for everything is too big.
- int64 we can check it runs but not that it works at >2billion DoFs
- complex mode actually changes the maths being done so makes sense to run everything. Code changes also often break something in complex so we need to catch that early.
- GPU needs special treatment, but only some functionality will be able to run on GPU anyway.
- SuperLU and hypre will only run on GPU if built for GPU, so we need to check they are set up correctly in both cases.
- We could make a github label for running the GPU CI like with macOS

## DH New adjoint fix from Daiane: https://github.com/firedrakeproject/firedrake/pull/4284
- Approved.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* RCK/PB: [UFL](https://github.com/FEniCS/ufl/pull/370) Approved.
* RCK/PB: [Dual interp](https://github.com/firedrakeproject/firedrake/pull/4197) Approved.
* CW: https://github.com/firedrakeproject/firedrake/pull/4278 Merged.
* CW: https://github.com/firedrakeproject/firedrake/pull/4249 Approved.
* CW: https://github.com/firedrakeproject/firedrake/pull/4270 Pending CI passing.
* CW: https://github.com/firedrakeproject/firedrake/pull/4277 Approved.
* CW: https://github.com/firedrakeproject/firedrake/pull/4285 Closed.
* CW: https://github.com/firedrakeproject/firedrake/pull/4281 Reviewed.

1600 UTC [2025-05-21](./Firedrake-meeting-2025-05-21)