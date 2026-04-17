Date and time 2026-04-14 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (PB to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. ALL: Change the `MultiFunction` in `ufl2unicode` with a `DAGTraverser`

# Minutes

Present: CW AC DH PB JHC

Apologies: IM

## Misc

- DH has trimmed github team members for active contributors.

## Firedrake/PETSc meeting abstracts

- Deadline approaching!
- Discussion on topics.

## Multifunction misbehaviour

* Discussion of these PRs: https://github.com/firedrakeproject/firedrake/pull/5022, https://github.com/firedrakeproject/Irksome/pull/208
* Someone needs to go through and replace all `MultiFunction` instances with `DAGTraverser`.
* The priority should be the `Multifunction` for `ufl2unicode` because that is now the only one that Firedrake instantiates at import.

## Merge PRs

* CW: https://github.com/firedrakeproject/firedrake/pull/5028
* CW: Periodic mesh renumbering approved but postponed to post-release.
* PB: Discussion of ngsPETSc boundary region handling.

## Date of next meeting
Meeting times going forward: Tuesday 4pm unless David has a monthly meeting, in which case Tuesday 3pm. Next 3pm Meeting 28 April.

1600 UTC+0100 [2026-04-21](./Firedrake-meeting-2026-04-21)