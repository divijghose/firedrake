Date and time 2022-05-05 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (JB to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Add flags to LDFLAGs in PYOP2 compiler class for M1 fix. (this is done)
1. CW: Test PETSc main against current Firedrake (passed on to Koki for when he gets back)
1. JB: Look into updating the `@parallel` test marker


# Agenda

Present: CW (minuter), DH, JB, PK, SV

Apologies:

## DH: M1 build testers

DH: We are planning on buying 4 Mac minis runners (one per build queue). JDB to email Andy Thomas about it. We need to buy 3rd party mounts for them to get them installed.

## DH: 4th year projects

DH: We need to start thinking of useful projects for MSc students to do.

DH: Maybe there is a project for GPU PETSc offloading (+ performance analysis). They could run either on Isambard or Jack's new hardware(?).

JB: There might be excalibur hardware that we could use too.

## JB: Benchmarking and Performance regressions
Connor has been testing out some cool benchmarking with pytest-benchmark which would be useful for performance regression testing. It would be useful to get some input on what sort of benchmarks we want to run regularly to stay on top of performance regressions. So far this functionality has been tested with a few basic tests as a PoC.

Connor: Check [this](https://connorjward.github.io/firedrake/dev/bench/) out.
CW: To create a PR for discussion

Required tests:

- Nonlinear solves
- Hybridisation/GTMG
- Extrusion
- CEED bakeoff problems
- Adjoint

## CW: Repository permissions

Neither I or Koki have the right permissions to merge things in TSFC and this was recently an issue. More generally, does everyone have all the right permissions for things?

DH: Amended now.

## Merge PRs
https://github.com/OP2/PyOP2/pull/663 (merged)

## Date of next meetings

Next meeting: [2022-05-12](./Firedrake-meeting-2022-05-12)

