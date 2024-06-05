Date and time 2024-06-05 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick: JB nominates CW)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto
1. JB: move tinyASM to firedrake/preconditioners: [#3604](https://github.com/firedrakeproject/firedrake/pull/3604)
1. ~KS: PETSc + Cython3.0 + numpy2.0 issue: why slow?~ see below

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Minutes

Present: CW (minuter), DH, DD, KS, IM, NB

Apologies: JB, PB

## CW: Cython 3, numpy 2, Python 3.12 performance regression

* CW: This has been found to be a bug in pytest-coverage. It will get fixed in Python 3.12.4.
* DH: That patch will take some time to make it into LTS Ubuntu. We should fix to 3.11 on the runners until that happens. If we do that then we can merge these changes as soon as numpy 2.0 is released.

## DH: Review pyadjoint PRs

Reviewed several. More progress will be made at next week's FEniCS conference.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- JB: [#3604](https://github.com/firedrakeproject/firedrake/pull/3604) Incorperate TinyASM into Firedrake. Josh has picked this over once.
  
  Licensing issues.

- DD: [#3579 (Firedrake)](https://github.com/firedrakeproject/firedrake/pull/3579) L2 Riesz maps as default for adjoint-based gradients.

  Set to automerge.

- DD: [#149 (Pyadjoint)](https://github.com/dolfin-adjoint/pyadjoint/pull/149) Adapting tests for L2 Riesz maps as default.

  Approved and merged. Will fail tests until a container with #3579 is built.

- PB: [FIAT](https://github.com/firedrakeproject/fiat/pull/71)

  Merged.

- PB: [UFL](https://github.com/firedrakeproject/ufl/pull/50)

  Needs merging into upstream, not our fork.

# Date of next meeting

NOT NEXT WEEK!

1600 BST (1500 UTC) [2024-06-19](./Firedrake-meeting-2024-06-19)
