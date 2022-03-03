Date and time 2022-02-24 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (SV to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: 

Apologies: 

# SV: Bessel functions
Scott MacLachlan wants Bessel functions
1) Loopy provides a `CWithGNULibcTarget(CTarget)` now. We used `CTarget` for our loopy kernels so far. Do we want to make `CWithGNULibcTarget` the default or do we needs some dance to sniff the compiler version and choose target dependent on that?
2) Target is specified in configuration (in PyOP2) and parameters(in TSFC and Firedrake) now. In Firedrake we choose same target as PyOP2, but in TSFC I didn't do that because I don't think we want to be dependent on PyOP2?
3) In PyOP2 we pass the language standard c99. If we want Bessel functions we need gnu11 I believe. I brute force changed that here https://github.com/OP2/PyOP2/pull/656/commits/e5c5cea78bf5b7ba86d13989fabba782393e37e8, what's the way to do this correctly?

# SV: Logging of local kernels

Disclaimer: I haven't had time to see how big the difference is between allocating the memory in python vs allocating the memory in the C kernels, maybe we need that first before we have a discussion about it.

For the inverse and solve callable I am now allocating the memory for the petsc events in python and faff around with the DLL to set the attributes correctly in the `Callables`. This works well because there are only two Callables and the naming of the events is clear. Doing this is more difficult for Slate and TSFC kernels. I think what we'd need to do in order to do this in a clean way is to save the event names and event id variable names on an attribute on the LocalKernels and then we could iterate over that to generate the events in compilation.py and set accordingly on the DLL.

1) For inverse and solve callable in PyOP2 https://github.com/OP2/PyOP2/pull/646
2) For Slate kernels in Firedrake https://github.com/firedrakeproject/firedrake/pull/2347
3) For TSFC kernels in https://github.com/firedrakeproject/tsfc/pull/267/files

# SV: Vectorisation
Kaushik has proposed a new implementation of vectorisation that is compliant with the already existing `vec` tagging for other targets here https://github.com/inducer/loopy/pull/557.
We need to adapt to those changes in PyOP2.

# DH: Library link issue on M1

## Merge PRs

## AOB

## Date of next meeting  ??Dagstuhl??

1600 UTC (1600 GMT) [2022-03-03](./Firedrake-meeting-2022-03-10/)
