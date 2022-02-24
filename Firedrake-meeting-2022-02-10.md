Date and time 2022-02-10 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (CW to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Minutes

Present: DH, RK, SV, JB, LM, CW, PK, DRS, CJC, KS

Apologies: 

## CW: Minimum Python version support

[3.6 is now end-of-life](https://www.python.org/downloads/release/python-3615/). Should we continue to support it?

Original discussion: https://github.com/firedrakeproject/firedrake/pull/2339

Ubuntu 18.04 uses 3.6 by default.

functools.cached_property is available only >= 3.8 etc...

Maybe it's not worth spending time specifically supporting 3.6 should it break.

Add to the install script that current supported version is >=3.8

## PB (via JB): Correct way to disable SLATE in complex
See PR[#2344](https://github.com/firedrakeproject/firedrake/pull/2344)

Slate is not quite complex ready.

PR looks fine -> merged.

## SV discussions in PyOP2?

Direct people to Firedrake Discussion page on the other package pages.

Add note on this on the Firedrake website.

## Merge PRs
SV: https://github.com/firedrakeproject/firedrake/pull/2317

SV: https://github.com/OP2/PyOP2/pull/646

JB: https://github.com/firedrakeproject/firedrake/pull/2311 (hopefully v. quick)

## KS: Update PETSc/Slepc
https://github.com/firedrakeproject/firedrake/pull/2282

## KS: TSFC refactor
https://github.com/firedrakeproject/firedrake/pull/2200

https://github.com/firedrakeproject/tsfc/pull/261

## AOB

## Date of next meeting

1600 UTC (1600 GMT) [2022-02-24](./Firedrake-meeting-2022-02-24/)
