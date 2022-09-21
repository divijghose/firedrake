Date and time 2022-09-21 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** (SV pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open next week hopefully)
1. JB: SIAM CSE23 Minisymposium/minisymposterium

# Agenda

Present:

Apologies: 

## DH: Minisymposterium at CSE
Koki to organise via slack

## TK: Firedrake Overheads
See #general for discussion on strong scaling - TK managed to get impressive strong scaling
 - Overheads in assign, assembly and parloops which TK has coded around
 - Able to get to 80% scaling efficiency with 200 MPI processes
 - Good argument for switching `assign` to only allow numpy assignments (quick win)

CW has some thoughts given he's rewriting pyop2 (too quick to minute!)

TK not sure if issues are to do with checks and function calls at runtime in python
 - DH says certainly some python overhead due to manipulation of `Arg`s

DH: `LinearSolver` being faster than `LinearVariationalSolver` sounds like a bug.
 - Either there is a significant difference we haven't thought of, or we're doing something dumb.

TK: Could make a special version of `LinearVariationalSolver` that has his optimisations.
 - DH: Better would be to rewrite assemble as necessary which ought to be possible.

DH: Parloop caching?
 - CW: Fact we're using python makes a big difference vs C

IDEA: wrap cached assignments/interpolations in `Expression`.

## JB: Status of PETSc/petsc4py GC MR
Post rebase memory leaks fixed. Code reorganisation has been requested I will try and get this done this week.

## JB: Anyone running PETSc main?
JB getting segfaults since change of C style guide
 - Not that we can tell...

## Daiane Dolci: Pyadjoint Questions to do with time steppers recreating blocks for every time step
DH: If you know your timestep loop structure you can improve memory usage. At the moment we leak solve blocks - pyadjoint doesn't know about what's repeated (e.g. loops in your code like a time step...)
 - Can try writing an explicit continuous adjoint that knows about your time stepper
 - Can also try to debug why storing solutions on the tape is causing so much memory usage (e.g. interpolate)
   - Daiane will report back next time

## Merge PRs
Irksome: https://github.com/firedrakeproject/Irksome/pull/53

## Date of next meeting

1600 UTC [2022-09-28](./Firedrake-meeting-2022-09-28)
