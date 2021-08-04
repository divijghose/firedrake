Date and time 2021-08-04 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present: MG, DS, JB, RK, KS, DH, CW

Apologies:

## JB: Firedrake training
- 60 were registered as of yesterday
- DH: by _this_ week double-check Jupiter server is running. Action DH: will do Friday
- JB: Arrange close of registration and pre-tutorial drop-in session

## Firedrake 2021
- website is up
- announcements to mailing list, Slack, fenics-slack, NA digest, SIAM CSE mailing list
- registration is not up yet (bureaucracy)
    - Action DH: Harass admin about setting this up
- abstract submission is open
    - All core developers expected to submit an abstract (should be obvious what)

## JB: Follow up on all of last weeks items:
- RNH: Loopy breaking Interpolation Kernels
    - Action ??: Produce MFE (minimum failing example)
- ~CW: What is the data representation of a `MixedDat`?~
    - Next week
- ~CW: Proposal: A new type system for PyOP2~
    - Next week
- ~RNH - Workers dying when running tests~
    - Action ??: Produce MFE
- ~RNH - FInAT dual evaluation feedback~

## RNH: Issue [#2095](https://github.com/firedrakeproject/firedrake/issues/2095) Loopy breaking Interpolation Kernels
> Complex data types are getting into real mode PyOP2 Kernels (can't create a "Real" interpolator for example).
> - issue removing complex node in expression compiler seems to insufficient (in form compiler it is at least called twice, see https://github.com/firedrakeproject/tsfc/blob/94aa4d548bd1cc5520a8490692e12f190287ea86/tsfc/ufl_utils.py#L119 I think)

## DH: Master is failing
JB: Merge #2165

## Merge PRs:
#2166 - Merged

#2158 - Tests are hanging, but we don't know which

## AOB
DS: What's up with the loopy language warning?

DH: Ask Sophia when back

DS: Will attempt fixing in a PR



## Date of next meeting
[2021-08-11](./Firedrake-meeting-2021-08-11) 15:00UTC (16:00BST)
