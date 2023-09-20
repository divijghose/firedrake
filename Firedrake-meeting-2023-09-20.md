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

Present: JB, RNH, DH, MK, CW, DD, KS, IM

Apologies: 

## Move repos update
PyOP3 to go into firedrakeproject 

## Comments on DefElement

DefElement now compares implementations of Finite Elements between Fiat and other sources.

## JB: Need to merge Tom Bendall's update of Firedrake BDMC PR
I didn't have sufficient permission

Brought up during Gusto hackathon.
Safe to merge FIAT branch- done. 
FInAT also done. 
JB merging in master to retrigger tsfc tests - to be reviewed again.

(Later in meeting) All tests passing, to be merged. 

## JB: Scheduled GH Actions time out after something like 60 days of inactivity
Noticed this when the website wasn't being updated automatically.
I think [this keepalive workflow](https://github.com/marketplace/actions/keepalive-workflow) would work for us. This is largely a reminder for me to do this, but bringing it to everyone's attention: **Rebuilding the website currently requires a manual step**

JB to do this

## NB: Dualspace PRs

Firedrake: https://github.com/firedrakeproject/firedrake/pull/2294

NB to :
- make copy work for Cofunction.
- change uses of vector to dat where possible. 
- Remove case for a ConstantValue in a dual space

Pyadjoint: https://github.com/dolfin-adjoint/pyadjoint/pull/70

Merged.

## CW: Homebrew Python seems to be broken

We are failing to install on some machines as the latest homebrew Python cannot programmatically create a venv. It's weird. I have been asking users to install with pyenv instead and even written a [wiki article explaining how](https://github.com/firedrakeproject/firedrake/wiki/Installing-pyenv). Should we recommend pyenv instead of homebrew on the website?

Use 3.11 as example to enable users copypasting.

## Merge PRs

- [Cross-mesh interpolation extrusion fix and extra tests #3092](https://github.com/firedrakeproject/firedrake/pull/3092)

Small bug, added as a comment.

- CW: https://github.com/firedrakeproject/firedrake/pull/3109

Merged.
- CW: https://github.com/firedrakeproject/tsfc/pull/298 and https://github.com/firedrakeproject/firedrake/pull/3110

CW to resolve conflicts.


# Date of next meeting

1600 BST (1500 UTC) [2023-09-27](./Firedrake-meeting-2023-09-27)