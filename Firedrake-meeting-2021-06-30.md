Date and time 2021-06-30 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. DH: Email Jemma, Ivan Re: Training
1. JW: notebook testing
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present: MG, JW (minutes), KS, JB, DH, SV, RNH, PK, NB, CW, CC

Apologies: LM


## Build Hardware Update

Most of Firedrake now over, plus Gusto. Not Docker, yet.


## Firedrake training

DH, JW, JB, KS have been planning an ARCHER2 Firedrake training in August. JW fixed bugs in notebooks.


## Firedrake 2021

Intention to hold online in week of 13th Sept. Could use a similar format to FEniCS: short zoom talks and social stuff in 'gather town'.

Talks will be in the afternoon, given users and developers are in Europe and US. Should we do posters, too? Would be at the same time as a social session in gather town. If so, how much of the workshop should be devoted to talks and how much to posters? Don't want to do talks only.

JB: How about we use Retrium to get feedback on what users like/dislike about Firedrake?

DH: How about we have a day where we go 2pm-5pm followed by poster session/drinks and a day where we go 2pm-4pm and do engagement/retrium/panel thing afterwards + gather town? Possibly a Firedrake hackathon on the third day.


## SV: Update loopy fork

I finally got around to modify firedrake-update to handle the switch to new loopy branch.
We need to merge 1) https://github.com/OP2/PyOP2/pull/627 and then 2) https://github.com/firedrakeproject/firedrake/pull/2130


## Merge petsc upstream?

Passing, seems fine.


## Update on cofunction

CC asked for update. DH: We have a roll-your-own-DAG visitor in TSFC we could use.


## Merge PRs


## AOB


## Date of next meeting
[2021-07-07](./Firedrake-meeting-2021-07-07) 15:00UTC (16:00BST)
