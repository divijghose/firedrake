Date and time 2022-02-24 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (KS to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: 

Apologies: 

# SV: Bessel functions
Scott MacLachlan wants Bessel functions
1) Loopy provides a `CWithGNULibcTarget(CTarget)` now. We used `CTarget` for our loopy kernels so far. Do we want to make `CWithGNULibcTarget` the default or do we needs some dance to sniff the compiler version and choose target dependent on that?
2) Target is specified in configuration (in PyOP2) and parameters(in TSFC and Firedrake) now. In Firedrake we choose same target as PyOP2, but in TSFC I didn't do that because I don't think we want to be dependent on PyOP2?
3) In PyOP2 we pass the language standard c99. If we want Bessel functions we need gnu11 I believe. I brute force changed that here https://github.com/OP2/PyOP2/pull/656/commits/e5c5cea78bf5b7ba86d13989fabba782393e37e8, what's the way to do this correctly?



## Merge PRs

## AOB

## Date of next meeting  ??Dagstuhl??

1600 UTC (1600 GMT) [2022-03-03](./Firedrake-meeting-2022-03-10/)
