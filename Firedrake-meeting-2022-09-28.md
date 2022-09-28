Date and time 2022-09-28 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** (RNH pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open next week hopefully)
1. JB: SIAM CSE23 Minisymposium/minisymposterium <- Deadline for abstracts is today!

# Agenda

Present: RNH KS CW DH JB DD

Apologies: SV NB

## DH: Knepley coming to London
Hold onto your livers!

Opportunity to get some PETSc MRs though. 

Discuss Joe Wallwork's work.

## JMC projects - DH

What would we like graduating JMC students to do as projects?
- 3 Maths students doing:
    * Interface for eigenproblems (SLEPc)
    * Pick up Mohammed/Melina adjoint improvements
    * A third thing...
- Need more projects:
    * Small amounts of functionality
    * (Mathematical?) Problems
    * RNH: Dual evaluation
    * RNH: Hdiv + Hcurl element duals (No wait this is done)
    * DH: Lagrangian particles
    * JB: Previous minutes: PETSc GPU offloading and performance analysis

## DH: Firedrake 22
Delay due to the office being slow, can't pay for easy chair, can't set up the web shop.

## SIAM CSE
Abstracts due today!

## DD: Report back about adjoint
Created notebook with comparison of different taping schemes:
- Forward problem
- Forward - no annotation but save data
- Forward - annotate
- Forward - annotate with grad

DH: Some increase in memory consumption is expected. Perhaps not that much though...
... memory consumption doesn't looks so wrong, expecting O(1GB) memory usage. Computing adjoint should roughly double memory consumption.

DH: The adjoint is essentially a memory leak, one way around this is to use checkpointing (cf: Australia, solving Stokes, expensive timesteps, but relatively few). Another way around this is to use "revolve" type checkpointing (DH has nearly done this, but there are bugs), because there are cheap time steps, but lots of them. Alternatively, there is a factor 2 memory use associated with gradient computation. So long as you don't need the Hessian, you can discard the values associated to a block after its use.

DD: Every block has its corresponding dependence, trying to clean this dependence after it is no longer required.

DH: This won't quite work (even though textbooks say this is how it works). Adjoint works in reverse, the current block doesn't just depend on the next block but on some DAG containing anything in the set of all forward blocks. It is however true that when the adjoint of a block is computed nothing else in the adjoint calculation will use the adjoint inputs, or the forward values in the output of the block (aasuming you aren't calculating a Hessian, or something similar).

(JB: Someone should read over the above and check what I minuted makes sense)

See the following issue for a discussion: https://github.com/dolfin-adjoint/pyadjoint/issues/84

## Merge PRs

## Date of next meeting

1600 UTC [2022-10-05](./Firedrake-meeting-2022-10-05)
