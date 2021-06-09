Date and time 2021-06-09 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. DH: Email Jemma, Ivan Re: Training
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present:

Apologies: Nacime (travelling to France)

## SV Loopy has merged their part of the loopy sprint

I moved their master branch to our fork here: https://github.com/firedrakeproject/loopy/tree/test-new-loopy-master

The test run on it is here: https://jenkins.ese.ic.ac.uk/blue/organizations/jenkins/firedrake/detail/PR-2105/1/pipeline
First time round we got = 3260 failed, 650 passed, 1120 skipped, 270 xfailed, 893 warnings, 585 errors 
Loopycompat needed to adapt to interface changes. New run is on now.


The diff says:
"This branch is 1516 commits ahead, 96 commits behind firedrake." because we squashed merge

I double checked the commits the last we have got from them is `b04cecf` from May 4, 2021

I think we agreed to wait until the new test hardware up to change anything about this?
Maybe we should squash merge the changes from after May 4, 2021 in any case?

---

DH: We don't actually want to run on their `master` branch. We want a nominal fork that automatically updates to `master` when we have confirmed that CI passes using it.
SV: They are happy to take some of our tests to make sure that they don't break compatibility with Firedrake.
DH: But they're not going to want to build PETSc in their CI. If they ran the tests on our Docker container they would have to switch out the Loopy which is slightly involved. Also there is still the risk of breaking Firedrake for our users.

DH: We want to hard update our fork to `master` but this would break `firedrake-update`.

Process decided upon: Check if current branch is `firedrake` and if so then switch to `main` and then pull. This won't affect other branches. Also put out PSA on Firedrake mailing list.

DH: This can be done before waiting for build hardware due to delays in getting it set up.

## Merge PRs

### CW Annotate Firedrake functions with PETSc events

Once this gets merged we should be able to generate flame graphs from Firedrake scripts.

https://github.com/firedrakeproject/firedrake/pull/2051 and https://github.com/OP2/PyOP2/pull/623

Merged.

## AOB

DS: Has been working on validating PETSc options in petsc4py.

## Date of next meeting
 [2021-06-16](./Firedrake-meeting-2021-06-16) 15:00UTC (16:00BST)
