Date and time 2021-09-09 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Firedrake 2021 Ask the other three (out of 24) if they'd like to give a talk.

# Minutes

Present:

Apologies: LM

## DRS: build + compile fail on M1

#2196 shows the hacks needed to make Firedrake compile and run on an M1 mac. The change to the build script is fairly straightforward. What to do about `-march=native` failing on M1? Removing this flag, even for other macs?

I tried to debug this problem by running a simple test script with an unmodified PyOP2 and with `PYOP2_DEBUG=1`, but this makes the problem go away.

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-09-16](./Firedrake-meeting-2021-09-16/)
