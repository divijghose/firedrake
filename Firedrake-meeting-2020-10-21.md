Date and time 2020-10-21 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. ~RK: Report back on quadrature estimation~
1. ~KS: Complex merge~
1. DH: Online Firedrake 2021
1. DS: Extrusion lift operator


# Agenda

Present:  RNH, RCK, DAH, PHJK, SV, DRS, LM, JDB, CW, CJC

Apologies: NB, KS

## RCK

FIAT quadrature degree fields done for some elements.

DAH: someone has to be able to inform the UFL elements of their
degree.

Stepping stone proposal towards element oracles: visitors get mapping
that takes UFL elements into extra things. This doesn't put a hard
dependency in UFL on anything else.

## Firedrake 2021: online

Some kind of multi-afternoon thing to catch the US crowd. Not research
talks, but posters + panels?


## RNH: Unlock slack history
Has anyone got some spare money sloshing about that could be used to unlock the slack history? Might save a fair bit of time in certain occasions. (Fyi RNH == Reuben Nixon-Hill - formerly minuted as RWH)

DAH: Somewhat expensive (although Jack points out
https://slack.com/intl/en-gb/help/articles/206646877-Slack-for-education)



## DRS: Extruding functions

Ed Bueler made the PR -- makes assumptions about node ordering that are worth talking about

Node ordering for Base x R is defined to work.

## RNH: Strange test failures
`tests/regression/test_aw.py::test_aw[conforming]` is failing on
https://github.com/firedrakeproject/firedrake/pull/1867 and
https://github.com/firedrakeproject/firedrake/pull/1884 which don't
touch the relevant code

LM: Can anyone reproduce these fails in the Jenkins-based docker container?

### DRS: [NASA proposal call](https://nspires.nasaprs.com/external/solicitations/summary.do?solId=%7b958CF134-D655-E512-B5AD-84501D14A0C1%7d&path=&method=init)

DRS suggests expanding the demos to cover more geosciences data.
Connecting to remote-sensing is a good idea.

Data assimilation?

DRS: to write a letter of intent.

## Merge PRs:

## AOB
## Date of next meeting: 2020-10-28

**Notice change of time for those not in the UK still on Summer time**

[2020-10-28](./Firedrake-meeting-2020-10-28) 16:00UTC (16:00GMT)
