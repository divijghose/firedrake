Date and time: 2020-03-31 15:00UTC (16:00BST)

# Action items

1. ALL: triage the open issues and confirm if they are indeed still open (and perhaps provide labels).
2. ~LM: Should probably check that firedrake-contributors doesn't give push to master on any of the organisational repos.~
3. DH: pull out list of people who have filled in survey. We can then decide if we want to chase some.
4. SV: update known list of firedrake citing papers that actually use firedrake. Already known papers live here: https://github.com/firedrakeproject/firedrake/blob/master/docs/source/_static/firedrake-apps.bib
5. KY: Write up maths of what `Filtered` is supposed to do, what it enables, and why it is needed.
6. KY, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
7. LM: write up some of the issues (parallel GC) and where to start looking.
8. JB: Add brief note to docs on disabling GC in parallel.

# Minutes

Present: David Ham, Lawrence Mitchell, Ivan Yashchuk, Jack Betteridge, Koki Sagiyama, Nacime Bouziani, Paul Kelly, Reuben Hill, Sophia Vorderwuelbecke, Thomas Gregory, Colin Cotter,

## LM: dual evaluation/interpolation update

Mostly working. An ideal implementation would use FInAT

## DH: Sprint to merge complex

Organisation via Koki.

Action KY: set up sprint to happen (week of 20th April), afternoons thereof. Let people know via mailing list/slack that this is happening. Set up wiki page for people to say that they will participate.

Idea to plan in meeting on 17th April 15:00UTC (16:00BST)

## RH: How to handle functionspaces on points

Only support DG0. Need to fix up in FIAT where tabulation on points results in errors. Point location is `unit` (or `()`).

## Date of next meeting

[2020-04-07](./Firedrake-meeting-2020-04-07) 15:00UTC (16:00BST)