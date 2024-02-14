Date and time 2024-02-14 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL: Submit abstract for PDESoft [PDESoft](https://pdesoft.org))

# Minutes


Present: JB, KS, DD, PB, IM, NB, DH.

DH: David has worked in the Andreas PR. Some tests are failing.

All: Pay attention to the PDESoft deadline. 

NB has to finish the docstring to advance on his PR.

JB wants to do more tests before asking the [PR 3348](https://github.com/firedrakeproject/firedrake/pull/3348) to be merged. 

JB proposes cutting the slow tests. He is working on this in the PR [3385](https://github.com/firedrakeproject/firedrake/pull/3385). JB raised that the tests involving iteration should be reviewed to verify if this number is suitable.

All: If anyone verifies that a test is slower than necessary, try to improve it and make a PR.

Apologies:

## DH: Update on outstanding action items

## DH: Review old pull requests

## DH: Review old issues

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

DD: Firedrake [PR 3398](https://github.com/firedrakeproject/firedrake/pull/3398)
- Daiane needs to work on the suggestion of Pablo. 

DD: Firedrake tests in pyadjoint [PR 133](https://github.com/dolfin-adjoint/pyadjoint/pull/133)
- See David's review changes.

KS: [I/O](https://github.com/firedrakeproject/firedrake/pull/3363)
Discussion about `test_io_backward_compat_bases_parms` being more readable. `test_io_backward_compat_bases_parms` is difficult to debug. 

CW: PR [3405](https://github.com/firedrakeproject/firedrake/pull/3405) was approved.

PB: PR [3404](https://github.com/firedrakeproject/firedrake/pull/3404) was approved.

JM: PR [3376](https://github.com/firedrakeproject/firedrake/pull/3376) was approved.

# Date of next meeting

1600 GMT (1600 UTC) [2024-02-21](./Firedrake-meeting-2024-02-21)