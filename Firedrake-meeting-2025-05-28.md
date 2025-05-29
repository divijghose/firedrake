Date and time 2025-05-07 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (IM pick - nominate CW to pick for me)
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

# Minutes

Present: CW (minuter), DH, JHC, KS, LC

Apologies: IM, PB

## Discussion-worthy issues/PR

### PETSc user meeting

* CW: Late May, early June is preferred
* DH: Want to run both conferences together back to back. Model is to go to conference hall. We will have to tender for different places. Looking
* DH: Monday lunchtime to Friday lunchtime is typically best. Maybe go to the end of Friday. Firedrake will fill 2.5 days out of 4.5 easily.
* DH: Devito are maybe interested in being involved. Depending on size may need a parallel track.
* CW: Would be great to have a shared poster session on the Wednesday.
* DH: Potentially 1-5 June. Should be outside exams.
* **TODO CW**: Get in touch with PETSc to check that the dates work. Also ask on Firedrake Slack to see if it's an issue.

### #4320 is ready, just fails that CCP link check.

Merged.

### [#4341](https://github.com/firedrakeproject/firedrake/pull/4341) VOM to Vom permutation matrix
Failing `test_slate_hybridization.py::test_slate_hybridization_wrong_option` for seemingly unrelated reasons

* Small comments. Generally very happy!

### CW: petsctools

[#4194](https://github.com/firedrakeproject/firedrake/pull/4194) ready for review.

* **TODO CW**: Consider conditionally deprecating `OptionsManager` depending on the Python version

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS : fix kwarg name https://github.com/FEniCS/ufl/pull/381 - merged

KS : add apply_coefficient_split() https://github.com/FEniCS/ufl/pull/341

* DH: don't get to have a return value for pre-order traversals. Wrapper called on `(o_in, parent_out, *args_in)`, call `method` to get `o_out` but wrapper then discards this. Pre-order 'passes down the tree not up'.
* DH: pre-order traversal should fail if more than one child node exists - only works in the case of a modified terminal
* DH: suggests to call `preorder_terminal`
* Decided that `preorder` is not necessary. Instead just implement the traversal inside the relevant `DAGTraverser`.

1600 UTC [2025-06-04](./Firedrake-meeting-2025-06-04)
