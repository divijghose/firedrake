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

## Merge PRs

### CW Annotate Firedrake functions with PETSc events

Once this gets merged we should be able to generate flame graphs from Firedrake scripts.

https://github.com/firedrakeproject/firedrake/pull/2051 and https://github.com/OP2/PyOP2/pull/623

## AOB

## Date of next meeting
 [2021-06-09](./Firedrake-meeting-2021-06-09) 15:00UTC (16:00BST)