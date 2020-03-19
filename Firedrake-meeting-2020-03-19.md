Date and time: 2020-03-19 15:00UTC

# Minutes
## Present

Paul Kelly, David Ham, Rob Kirby, Lawrence Mitchell, Joe Wallwork, Nacime Bouziani, Patrick Farrell, Reuben Hill, Sophia Vorderwuelbecke, Jack Betteridge, Koki Sagiyama, Dan Shapero, Julian Andrej, Tuomas Karna, Alberto Paganini, ...

## Ongoing (remote) working practice

Not having an agenda with 17+ people on the call is problematic. Solution: move to formal agenda, maintained as wiki page that anyone can add items to.

Day to day, to keep things ticking over:

- maintain normal informal discussions going via slack/email/etc...
- plan to schedule virtual coffee/watercooler discussion time in slack (#random) at 16.30UTC each day (join as you wish). Anyone can [sign up for an account](https://firedrakeproject.herokuapp.com).

## Report from Dagstuhl meeting

Some of us (PK, DH, LM, SV) attended a Dagstuhl seminar on [Tensor computations](https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=20111), somewhat short-handed due to global pandemic, but nonetheless very interesting.

In particular tensor contractions + tensor decompositions.

Idea is to develop a document/whitepaper advocating a symbolic language for
tensors and tensor contractions. Common symbolic layer + ammunition
for directions for funding/proposals <=> excalibur research agenda.

## Excalibur call

Software for exascale. Met Office and UKAEA got large pots.

Call: working groups for demonstrator application.
Phase 1 project involving Firedrake was funded. 15 months, 1 FTE.

Consortium is Devito, PyFR, OP2, Firedrake, (+ Exeter). Pitch:
continuum mechanics + outer loop.

Demonstrator will be Firedrake + defcon. PDRA is Jack Betteridge.

Need to formulate research agenda: writing call for £5-7M "phase 2".

Comparing ARCHER2 to Isambard. Start with Isambard, since ARCHER2
doesn't presently exist.

## State of Firedrake

Some mac-based install issues still.

GC-based issues in parallel. "Fixed" by JB for test suit: setup/teardown hook in pytest that disables GC for duration of parallel tests. This works for problems that people encounter but is suboptimal: should be documented, but we should figure out a proper way of handling things. There is a [project page for this](https://github.com/firedrakeproject/firedrake/projects/6).

## New code

DH has an applied masters student looking at putting dual evaluation in FInAT. PF is trying with student to do the minimal to get the FIAT-exposed dual evaluation working in tsfc interpolation code, to avoid [this issue](https://github.com/firedrakeproject/firedrake/issues/1625).

## Date/Location of next meeting

[Webex](https://webex.com) seemed to work quite well (hangouts free tier tops out at 10 people). Desktop client is more featureful than web browser.

Next meeting [2020-03-24 16:00UTC](./Firedrake-meeting-2020-03-24).