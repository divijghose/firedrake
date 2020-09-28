Date and time 2020-09-28 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ~KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.~ Parked.
1. \*\*: ~Think about the correct mathematical formulation for Filtered~ Not needed.
1. ~DH: Only test PRs on master~ Done by LM! Branches now only tested as PRs (with merge commits only tested on Jenkins).
1. ??: Build master on centos to catch errors
1. RK: Report back on quadrature estimation
1. KS: Complex merge
1. All: In 1 week (5th October) prepare 3mins on "what I do" for incoming meeting attendees


# Agenda

Present:

Apologies: Nacime (No WIFI)

## LM: Clean up old branches please and use naming convention.
Suggest doing e.g. `ReubenHill/branchname`

## RH: Complex
Aim to get tests passing and merged before next meeting unless very major issues appear. Koki todo.

Call for ideas for what to do with complex - RK has potential use cases - otherwise get a masters student involved.

## RK: Quadrature Estimation Report
Ciarlet element refactor in FIAT caused loss of ability to specify certain element properties such as quadrature order and element degree distinction.

RK has a question about correctly describing tensor product elements - DH has explanation for RK which he explained in meeting.

Discussion leads inevitably to desire to have an element oracle.

First step is to get this into FIAT for simplex elements - RK todo.

## Clean up and assign action items on Agenda
~Many action items remain unassigned, some have been lost, some have not been reported back on in a while.~ Done

## JB: Numpy bug update
Aaargh!

Too many packages pull in their own numpy which make's JB's aim to link against a common numpy very hard.
PIP is VERY bad at keeping track of dependencies and behaves weirdly a build time (lots of building then throwing away!).
JB suggestion - tell everyone to build with `--no-binary-numpy` (possibly misspelt) flag.
`--no-build-isolation` flag also discussed (see https://pip.pypa.io/en/stable/reference/pip/)
JB also has concerns about testing - will report back later.

There are known `clang` issues with non ansi C. Please keep reporting upstream (and to JB).

Also known `make` issues - may be to do with it being too old and no gnu `make`. Do we need to add `make` to the list of things we install with firedrake?

## LM: Reading group plug
Please respond. Will read Numerical Analysis papers.



## Date of next meeting
[2020-10-05](./Firedrake-meeting-2020-10-05) 15:00UTC (16:00BST)