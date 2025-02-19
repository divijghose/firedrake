Date and time 2025-02-19 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (PB to pick?)
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

Present: DH, KS, DD, CW, JHC, LC, PB, RK, IM

Apologies:

## CW: `pip`... `install`... `FIREDRAKE`!!!

[#4011](https://github.com/firedrakeproject/firedrake/pull/4011)

I am looking for beta testers and would like to merge this next week. I can do an announcement to users on Slack after the meeting. They need to know in advance because there are some breaking changes they have to be aware of (e.g. OpenMPI not MPICH in the containers).

Outstanding questions:

* `firedrake-zenodo` will not work until we have version numbers: installing packages in non-editable mode discards git information which `firedrake-zenodo` relies on.
* Similarly `make check` also will not work without an editable install. Do we mention it on the website still?


Firedrake team beta test over the next week. Announce on slack that this will be the main install method from next Wednesday.
Open discussion on git in tandem with announcement on slack, so that discussion on firedrake-install going away (etc) persists. 
When announcing on Slack, tag users that are maintainers of downstream packages to review and update their instructions.

Script firedrake-configure provides the correct options/packages/environment variables that need to be in place for install.

### Questions
* How would the downstream package install work (sp. Irksome)?
Ans: pip install irksome (link to repo)
Suggestion: Add options to packages that allows eg pip install firedrake[irksome]. Question about if this would work correctly for the dependencies to resolve.

* On firedrake-configure, what does the no package manager option do
Ans: Instructs petsc to download the packages (excluding MPI). 

* CW: make-check - needs to be in editable mode for the tests to exist.
Ans: Maybe pip manifest could allow us to put the smoke tests/makefile in the regular pip install? We should be able to allow standard users to run make check. 

* CW: firedrake-zenodo - needs to be in editable more
Ans: Just add to doc that zenodo only works in editable modes at the moment, but will be fixed later this year. 

* firedrake-install script
Ans: Will exist in the April release but likely to be removed in October release as otherwise users unlikely to switch. 

General: This is great!


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [Subclass LinearSolver](https://github.com/firedrakeproject/firedrake/pull/4012) - review comments to be addressed.

PB: [Fix maxpy](https://github.com/firedrakeproject/firedrake/pull/4056) - Makes sense but not currently passing tests

Discussion on docs PR re immersed mesh - merged. 

Discussion on Jax - resolve to not allow skips in certain cases and to change the pip install firedrake PR to deal with this. 

# Date of next meeting
1600 UTC [2025-02-25](./Firedrake-meeting-2025-02-26) ???