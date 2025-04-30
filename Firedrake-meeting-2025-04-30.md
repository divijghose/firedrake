Date and time 2025-04-23 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW pick)
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

Present: DH, RK, PB, CW, IM, KS

Apologies: JHC

## Discussion-worthy issues/PR


### We now have release.

Congratulations and thanks CW!

### CW: Need PyPI owners for packages

If some of you can create PyPI accounts then I can add you to the PyPI projects that I currently maintain (increase the bus factor).

Also Zenodo, Docker, more?

Docker: DH and CW

Zenodo: CW probably has access?

Ask LM how zenodo works.

- Give access to JHC and KS for now

- Action JHC and KS: create an account, setup 2FA, etc.

- Irksome release? -- One possible thing RK can do while in the UK.

### RCK: [Irksome-izing demos](https://github.com/firedrakeproject/firedrake/pull/4262) 

Do we want to replace/remove existing non-Irksome demos?  Naming conventions, etc.

The demo shows how to write custom time steppings, so probably it is not a good idea to completely replace them.

Instead put a cross-link for Irksome versions of the demos?

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

* RCK/PB: [UFL](https://github.com/FEniCS/ufl/pull/370) 
* RCK/PB: [Dual interp](https://github.com/firedrakeproject/firedrake/pull/4197)
* PB: [Fix block sizes](https://github.com/firedrakeproject/firedrake/pull/4253)

1600 UTC [2025-05-07](./Firedrake-meeting-2025-05-07)