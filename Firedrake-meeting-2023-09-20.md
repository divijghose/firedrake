Date and time 2023-09-20 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject (update!)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).

# Agenda

Present: 

Apologies: 

## JB: Need to merge Tom Bendall's update of BDMC PR
I didn't have sufficient permission

## JB: Scheduled GH Actions time out after something like 60 days of inactivity
Noticed this when the website wasn't being updated automatically.
I think [this keepalive workflow](https://github.com/marketplace/actions/keepalive-workflow) would work for us. This is largely a reminder for me to do this, but bringing it to everyone's attention: **Rebuilding the website currently requires a manual step**

## NB: Dualspace PRs

Firedrake: https://github.com/firedrakeproject/firedrake/pull/2294

Pyadjoint: https://github.com/dolfin-adjoint/pyadjoint/pull/70

## CW: Homebrew Python seems to be broken

We are failing to install on some machines as the latest homebrew Python cannot programmatically create a venv. It's weird. I have been asking users to install with pyenv instead and even written a [wiki article explaining how](https://github.com/firedrakeproject/firedrake/wiki/Installing-pyenv). Should we recommend pyenv instead of homebrew on the website?

## Merge PRs

- [Cross-mesh interpolation extrusion fix and extra tests #3092](https://github.com/firedrakeproject/firedrake/pull/3092)

# Date of next meeting

1600 BST (1500 UTC) [2023-09-27](./Firedrake-meeting-2023-09-27)