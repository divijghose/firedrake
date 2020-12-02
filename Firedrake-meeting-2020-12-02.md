Date and time 2020-12-02 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors

# Agenda

Present: CW, RK, KK, KS, DH, JB, RNH, DS, SV, PK, CC, LM

Apologies:

## LM: Excalibur [performance workshop](http://www.peano-framework.org/index.php/workshops/2021-performance-analysis-workshop-from-analysis-to-insight/)

Might be of interest to some (organised at Durham). Daniel Ruprecht (now at Hamburg) got in touch because he has a PhD student who would be keen to join at Firedrake team.

Do we want to send a virtual 'team'?

There are tutorials in the morning on profiling tools. In the afternoon you try to get it working on your code.

CW is interested and maybe others so a team will definitely be sent.

## LM: Memory issues observed on various supercomputers

It _might_ actually be a bug that has appeared in PETSc, but we don't yet have a concrete "always works" testcase.

Florian Wechsung (NYU) and Angus Gibson (ANU) have both been reporting issues recently.

Infiniband libraries do not have forking. 
A nice solution to this would be to have a libclang JIT thing that you could call. 
The less nice option is to fork before calling MPI_Init. 
This would involve handling Firedrake imports to make sure they don't touch `subprocess`. In particular PyOP2.

Status of JIT C compilation is unknown but likely to be painful.

Shared by PK: https://clang.llvm.org/docs/LibTooling.html

DH: [libgcc JIT](https://gcc.gnu.org/onlinedocs/jit/) looks promising. CW to look into it this week.

## RK: External operators

Can now drop volume potentials into UFL. The next thing is to use non-local operators.

The code is currently a bit messy and needs tidying before merge into Naseem's branch.

## Merge PRs:

Several merged.

## AOB

DH is talking at 3pm (UK) on Monday about dual spaces/interpolation. This has implications for simplifying UFL and the relevant algebra.

## Date of next meeting

[2020-12-09](./Firedrake-meeting-2020-12-09) 16:00UTC (16:00GMT)