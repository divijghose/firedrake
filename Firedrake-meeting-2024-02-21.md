Date and time 2024-02-21 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116). Currently failing its test without output. DH to continue working on this.
1. ~DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).~ Merged.
1. DH: Order more Firedrake stickers
1. ALL: Submit abstract for PDESoft [PDESoft](https://pdesoft.org))

# Minutes

Present: CW (minuter), DD, JB, KS, DH, RK, FA, NB, IM, PB

Apologies:

## DH: Update on outstanding action items

* See above.

## NB: External operators

Firedrake PR: [#3394](https://github.com/firedrakeproject/firedrake/pull/3394)

* Approved and merged!

## DH: Review old pull requests

* Done. Several old pull requests have been closed.

## DH: Review old issues

* Skipped.

## JB: We should enable merge queues

* JB: Would allow for merging bugfixes and getting them into the Docker container.
* Action point: JB to give this a go.

## JB + CW: Point query status?

* DH: Plan is to either replace `.at()` implementation to use a VoM or to just remove it.
* CW: Templating approach for point location is necessary due to Newton iteration (loopy doesn't do `while` loops). It should be possible to reduce the amount of templating by a substantial amount though.
* Limitations of VoM vs `.at()` described [here](https://github.com/firedrakeproject/firedrake/issues/3080). Limitation 1 is solved and limitation 2 is questionable.

## PB + JB: Slow tests

We want to keep the slow tests, can we make them faster?

[Speed up some tests PR #3416](https://github.com/firedrakeproject/firedrake/pull/3416) (depends on #3295, listed below)

* DH: Looks fine, and test coverage is still good. Get things passing and then it can be merged.
* JB: Checking exact iteration counts in tests is potentially dodgy as upstream changes to PETSc may "break" our code. No better alternative really exists though.

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- PB: [3412](https://github.com/firedrakeproject/firedrake/pull/3412)

  * Merged

- PB: [3295](https://github.com/firedrakeproject/firedrake/pull/3295)

  * Merged

- PB: [3341](https://github.com/firedrakeproject/firedrake/pull/3341)

  * Merged

- PB: [FInAT](https://github.com/FInAT/FInAT/pull/122)

  * Needs documenting, otherwise good to go

- PB: [TSFC](https://github.com/firedrakeproject/tsfc/pull/306)

  * Need to change the Firedrake notebook that touches this

- NB: Interpolation block tags: [Firedrake #3420](https://github.com/firedrakeproject/firedrake/pull/3420) and [Pyadjoint #136](https://github.com/dolfin-adjoint/pyadjoint/pull/136)

  * Merged the Firedrake PR, should wait for containers to be built before merging 

# Date of next meeting

1600 GMT (1600 UTC) [2024-02-28](./Firedrake-meeting-2024-02-28)
