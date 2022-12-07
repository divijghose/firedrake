Date and time 2022-12-07 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Organise Firedrake 2022 (Chartering a coach, events apart from talks?)
1. JB: A Firedrake manual
1. JB: Python 3.11
1. All: Go through TSFC PRs
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements
1. DRS: Fix ROL/pyadjoint versioning issues with Angus Gibson

# Agenda

Present: JB, KS, CW, NB, RK, RNH, DH

Apologies:

# Firedrake 2022

Transport: Try to set up a coach starting from Imperial that will go through different places to collect people. Return on Friday afternoon.

Departure time: 8-9 am since we probably want to be there by 1pm (travel time: 4h30)

# JB: Move PyOP2 and FInAT to firedrakeproject

This should be fine, github will move the PRs, issues, etc. automatically.

# ALL: do things with SV's branches

Notes on Sophia's code: https://hackmd.io/UHCwsYaTTzyaWUIFSe9axg

-> Someone that knows enough about the branches should take this over

# UFL update

- Need to merge FEniCS master: Make a UFL branch merging fenics master and a firedrake branch linked to the UFL branch to check that we don't break anything.

- Fix the accidental merge of a PR into Firedrake UFL and not in FEnICS UFL -> We can take it out. The concern being that people might be using it.

# JB: Issues and new wiki section

JB has been closing a bunch of issues. JB and CW have made a policy section in the wiki about closing installation issues and python version support



## Merge PRs


[Allow for Q and DQ on hexahedral meshes (except dS integrals)](https://github.com/firedrakeproject/firedrake/pull/2618): Approved. Comments have been addressed -> ready to go

[Periodic extrusion](https://github.com/firedrakeproject/firedrake/pull/2582): Reviewed. Add `TorusMesh` and `AnnulusMesh` functions + some docs


## Date of next meeting

1600 UTC [2022-12-14](./Firedrake-meeting-2022-12-14)
