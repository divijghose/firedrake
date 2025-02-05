Date and time 2025-01-22 1600 UTC

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
1. CW: Fix artefactsv3 issue
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: RK, DH, DD, IM, LC, CW, JHC, KN, AO

Apologies:

## Firedrake USA

* Abstract Submission: Core developers must submit the abstract.
* Invitations: RB will send emails to potential attendees.

## DH: Firedrake Release Strategy
* Goal: Minimize user impact when merging PRs.
* Strategy: Follow PETSc's release. Also, consider the PETSc's releases while addressing potential issues that impact Firedrake.

**Proposed Schedule:**
*  Major releases every six months (April and October).
*  Patch releases as needed (e.g., for bug fixes).
*  Release structure to align with the calendar.

* Collab Compatibility: This should align with Firedrake releases, which will track PETSc’s main releases.

## KS: UFL DAG Visitor Draft

[draft](https://github.com/FEniCS/ufl/pull/341)

Next Steps:
* DH will revisit the PR next week.
* KS needs to demonstrate how the implementation works.
* KS should check how TSFC handles similar cases.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

CW: https://github.com/firedrakeproject/firedrake/pull/3915

* CW will fix a minor issue.
* DH approves merging into master.
* Approval can happen later.

PB: [FEniCS style bcs](https://github.com/firedrakeproject/firedrake/pull/3995)

* Documentation needs improvement.
* Code readability should be enhanced.

PB: [finat.ufl value_shape part 2](https://github.com/firedrakeproject/fiat/pull/122) See: [Firedrake upstream test PR](https://github.com/firedrakeproject/firedrake/pull/3979)

KS: [fix slate](https://github.com/firedrakeproject/firedrake/pull/4003)

Requires testing in Gusto.


# Date of next meeting
1600 UTC [2025-02-12](./Firedrake-meeting-2025-02-12)