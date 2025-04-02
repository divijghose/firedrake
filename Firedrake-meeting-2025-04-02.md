Date and time 2025-04-02 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (IM pick)
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

## Release

https://github.com/orgs/firedrakeproject/projects/9

## JHC [Firedrake #4177](https://github.com/firedrakeproject/firedrake/pull/4177). Subfunctions adjoint evaluation.
Description in PR. More fiddly `FloatingType` details again.

Minutes

JHC: simple fix but involved lots of work to figure it out so there's a long description in the PR.

CW: Add a comment in the code with similar level of detail as the PR description.

CW: self.idx -> self.subfunction_index in `FunctionMergeBlock`.

## CW petsc4py suggestion

[#4175](https://github.com/firedrakeproject/firedrake/pull/4175) (information in PR summary)

Be warned: be prepared to think hard pip thoughts

Minutes

CW: Proposal: a shim package `petsctools` to install petsc4py directly from PETSc (as opposed to using pip).

DH: There are problems with a separate PETSc install.

DH: We can pip install petsc4py by specifying the system PETSc dir. For Ubuntu the plan is to install a PPA PETSc (much harder for Mac).

DH: As long as the user can override the specific version, we could by default dynamically figure out the PETSc version.

DH: We need to consider this further. The user should might not get the versions right. 

CW: We consider more flexible minimal PETSc requirements/versions.

DH: Firedrake release branch should be as new user friendly as possible. 

CW: I'll think some more.

## PB: UFL performance regression

https://github.com/FEniCS/ufl/pull/367/files

PB: I still need to get the caching interface.

DH: use object id to memoize visited nodes in the tree.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- JHC: [Firedrake #4178](https://github.com/firedrakeproject/firedrake/pull/4178). Only pass solver parameters to adjoint solve block once.

- KS: https://github.com/FEniCS/ufl/pull/368. Cleanup BaseFormOperator arguments. Merged.

- CW: https://github.com/firedrakeproject/firedrake/pull/4189 We check links in the docs, sometimes we get failures due to the other sites changing, other times sites are temporarily down. This PR deploys the website even if the link check fails.

- PB: [Restrict PC](https://github.com/firedrakeproject/firedrake/pull/4169) Not discussed

- PB: [FIAT mimetic spectral](https://github.com/firedrakeproject/fiat/pull/139) Merged

- DH: [Adjoint documentation](https://github.com/firedrakeproject/firedrake/pull/4168) Merged

- DH: [Fix streamline plots](https://github.com/firedrakeproject/firedrake/pull/4188) Reviewed, merge when it passes CI



1600 UTC [2025-04-23](./Firedrake-meeting-2025-04-23)