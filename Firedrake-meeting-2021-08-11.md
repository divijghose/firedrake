Date and time 2021-08-11 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present:

Apologies:

## CW: What is the data representation of a `MixedDat`?

From [this issue](https://github.com/OP2/PyOP2/issues/626) it is suggested that the data part of a `MixedDat` is just the concatenation of several `Dats`. So a `MixedDat` containing 3 `Dats` of length `n` and `dim=3` would have shape `(3, n, 3)`. How does this work if the `Dats` have different `dims`?

## CW: Proposal: A new type system for PyOP2

See [here](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2021-07-28#cw-proposal-a-new-type-system-for-pyop2).
This has now likely been superceded by https://github.com/OP2/PyOP2/pull/624#issuecomment-896047790.

## CW: What belongs in the Firedrake wiki?

We have written a [guide](https://github.com/firedrakeproject/firedrake/wiki/Kernel-profiling-with-LIKWID) to profiling Firedrake with LIKWID and put it in the Firedrake wiki. Does it belong here or should it be put on the website?

## Merge PRs:
SV: Can we merge #2111, please? :)

## AOB

## Date of next meeting

[2021-08-18](./Firedrake-meeting-2021-08-18) 15:00UTC (16:00BST)