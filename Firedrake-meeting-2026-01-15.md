Date and time 2026-01-15 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Agenda

Present: DH, CW, JHC, PB, IM, AC, KN

Apologies:

## Agenda items

### CW: Durham HPC Days?

Eike:

> I spoke to Tobias Weinzierl last week: would anyone be interested in putting together a session on Firedrake at the Durham HPC Days https://hpc-days.github.io/Durham-HPC-Days-2026/ this summer? This could be a series of talks and/or a tutorial. The conference takes place 15-19 Jun 2026, and the deadline for submitting a session proposal is 31 Jan 2026: https://hpc-days.github.io/Durham-HPC-Days-2026/call-for-sessions/

Format: session 4 talks (20+5 minute). 

Oportunity to showcase the most HPC stuff what we do 

Introduction to Firedrake (maybe 2 sessions)
HPC applications (precondioners Eike, adjoints Josh)

Is this the right audience? Are they going to actually use Firedrake?

Success is not clear, at least for the Firedrake developer team.
No one has expressed initiative, but if Eike wants to put something together he is free to go ahead.

### CW: Reminder: Oxford trip next Tuesday

We will meet for coffee at 11 am. The plan is to work in the same office and have lunch together. 

There'll be Part 2 at the Royal Oak.

### JHC: PSA test time-outs on CI prevent the entire test suite being run!

If an individual test timeouts, the entire pytest job is skipped.
JHC: Timeout errors should not be ignored when merging commits
JHC: These tests have been temporarily skipped. We are still debugging.


### Too many indices for sum factorization [PR](https://github.com/firedrakeproject/fiat/pull/207) needs more work.

Make the maximum sum factorisation index be a variable.
If that variable is exceeded, don't sum factorise but do issue a warning. The warning should specify how to set the sum factorisation index.


### Errors in multidomain assembly [PR](https://github.com/firedrakeproject/firedrake/pull/4763)

KS commented that the error handling for assembling multidomain Forms multidomain should be handled during map composition.

DH: It does not make sense to use `intersect_measures` on meshes that are not topologically related.

We should raise a custom exception except of the NotImplementedError introduced [#4803](github.com/firedrakeproject/firedrake/pull/4803).

The tests in [#4763](https://github.com/firedrakeproject/firedrake/pull/4763) should be updated accordingly.


## Merge PRs


## Date of next meeting

1600 UTC [2026-01-22](./Firedrake-meeting-2026-01-22)
