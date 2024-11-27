Date and time 2024-11-27 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. CW (formerly JB): Move PyOP2 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. RK: sort out Firedrake USA details and website before Christmas time
1. CW: tackle Loopy warnings

# Agenda

Present:

Apologies:

## CW: Big PyOP2 merge (https://github.com/firedrakeproject/firedrake/pull/3817)

Everything is addressed. This should be ready to go.

## CW: Mac runners (https://github.com/firedrakeproject/firedrake/pull/3881)

## PB: Slow tests

After some profiling, it seems that the main bottlenecks are related to the loopy `linearize` warnings:
![image](https://github.com/user-attachments/assets/13ebacf3-da75-45d5-93e6-6c4cc68920b4)


On top of this, compilation of zany elements is slow mainly due to `gem.optimise.aggressive_unroll`
https://github.com/FInAT/FInAT/blob/d3a9b536233870d8853a6162c4112b07689fcdc1/finat/physically_mapped.py#L277

Simply removing `aggressive_unroll` brings compilation time for the Johnson-Mercier Riesz map from 32 seconds down to 5.5 seconds.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [#3436](https://github.com/firedrakeproject/firedrake/pull/3436)

PB: [#3868](https://github.com/firedrakeproject/firedrake/pull/3868)

DD: [#180](https://github.com/dolfin-adjoint/pyadjoint/pull/180) Fix checkpointing for `MixedCheckpointSchedules` (Pyadjoint)

# Date of next meeting
1600 UTC [2024-12-04](./Firedrake-meeting-2024-12-04)
