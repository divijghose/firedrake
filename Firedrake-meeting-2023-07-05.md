Date and time 2023-07-05 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: discuss preparation for Firedrake User meeting
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. RK: Update on [PR#2028](https://github.com/firedrakeproject/firedrake/pull/2028).
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).

# Agenda

Present: 

Apologies:

## DH: Firedrake23

## CW: Codegen issues with the new `Constant`

We need to renumber `Constant`s to have stable form signatures (https://github.com/firedrakeproject/firedrake/issues/2999). Possible fix: https://github.com/firedrakeproject/firedrake/pull/3011.

More generally I also want to know the exact abstraction provided by a `Constant`. When do we expect users to use them? Should it be possible to differentiate w.r.t. them? If we had vector-valued R `Function`s would they ever be required? (I think yes since sometimes identifying the right domain is hard).

## Merge PRs
JB: [#3014](https://github.com/firedrakeproject/firedrake/pull/3014) Oooh, fancy annotation (eg: [1](https://github.com/firedrakeproject/firedrake/commit/d7a7a9d30) [2](https://github.com/firedrakeproject/firedrake/commit/e8386706f)) 

# Date of next meeting

1600 BST (1500 UTC) [2023-07-12](./Firedrake-meeting-2023-07-12)