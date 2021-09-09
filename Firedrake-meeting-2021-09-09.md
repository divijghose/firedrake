Date and time 2021-09-09 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Firedrake 2021 Ask the other three (out of 24) if they'd like to give a talk.

# Minutes

Present: DH, DRS, SV, KS, JB, SK, NB, RK

Apologies: LM

## Firedrake 21
Have a schedule, it's been distributed.

Action DH: Need to send links for gather.town & zoom. Also setup retrium. Allocate chairs

## DRS: build + compile fail on M1

#2196 shows the hacks needed to make Firedrake compile and run on an M1 mac. The change to the build script is fairly straightforward. What to do about `-march=native` failing on M1? Remove this flag, even for other macs?

I tried to debug this problem by running a simple test script with an unmodified PyOP2 and with `PYOP2_DEBUG=1`, but this makes the problem go away.

JB: Can use `-mcpu=<something>` to optimise for M1

DH: How should we sniff the CPU in PyOP2?

JB: `platform.uname().machine` is used in the install script

Action DRS: Create PR for M1 fixes

## Merge PRs:

PR #2208: Should be fine, merged

PR #2202: RNH required

PR #2201: Failing: Subtle bug, fixed in Firedrake, now failing in pyadjoint

PR #2200: Failing: Part of refactor, related to TSFC PR #261. Big diff but commits are small, have meeting to resolve.

PR #2190: We need to think carefully about how we want users to cite Firedrake from the repo, the 2016 paper isn't sufficient.

PR #2176: Waiting on upstream PETSc change, PETSc has been merged, just remove branch pointer (done live)

PR #2101: KS: This needs a fix, but don't know how




## AOB

## Performance regression
DH: Finat dual evaluation results in regression on the CI, something goes wrong with GCC. We will just wait for sparse tensor stuff to land.

JB: Can we just update GCC in the docker container?

## Fun fact
DH: `test_tlm.py::test_time_dependent` is not, in fact, testing the tlm. It's testing the adjoint. It's also failing on Melina's Branch

## Date of next meeting

**NO MEETING NEXT WEEK DUE TO FIREDRAKE21**

1500 UTC (1600 BST) [2021-09-23](./Firedrake-meeting-2021-09-23/)
