Date and time 2020-05-26 15:00UTC (16:00BST)

# Action Items
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. ~JB: Add mechanism for python3.8~ Someone: test this.
1. DH: Find time to fix to get final complex sprint test passing.

# Agenda
Present:

Apologies:

## JB: Move to VTK 9.0?
VTK have now released wheels for all platforms and Python versions we are targeting.
Is anything preventing us moving to VTK 9.0?]]

## LM: First Archer2 eCSE call
Possibly could punt for a combination of IO/checkpointing and communicator coarsening for multigrid (these sound different, but are related technologies I think).

## LM: State of complex
Forward mode tests now pass in both real and complex mode, adjoint passes in real mode. For adjoint in complex mode we need to tape assembly of zero forms (complex numbers) and then explicitly do lots of stuff to ensure functionals that should be real are real.
Proposal: skip pyadjoint tests in complex testing for now (raise NotImplementedError somewhere?)

## Date of next meeting
2020-06-02 15:00UTC (16:00BST)
