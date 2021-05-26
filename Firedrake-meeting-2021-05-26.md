Date and time 2021-05-26 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. DH: Email Jemma, Ivan Re: Training
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present: Jack, Dan, Koki, Nacime, India, David, Lawrence, Connor, Paul, Sophia, Colin, Reuben, Melina

Apologies:

## Welcome to India and Melina:

- India Marsden: MSc student working on dual space
- Melina Giagiozis: MSc student working on adjoint (continuing what Mohammad Usman has done on making some operations "adjointable")

## Build hardware

Significant progress in getting Github Action up and running.

We are hopefully almost there!

## LM: FIAT ownership

Fenics is moving to Basix (runtime basis evaluation library).

Do we want to be FIAT maintainers given that Fenics has dropped it out?

No other users of FIAT other than Fenics/Firedrake. 

Fenics is offering us to take over FIAT. For that, few things need to be fixed in FIAT.

## RNH: FInAT Dual Eval Design

Point of having dual in FInAT is twofold:
 1) Composed structured dual
 2) Can design interface that remove necessity for having to look inside data structure when looking at dual

Matthew Kan's work does not cover all the cases.

Plan for Reuben:

- Merge current state of dual
- Propose API dual evaluation in FInAT
- Implement the code


## RNH: `compile_expression_dual_evaluation` future design

Compiling a dual expression is different than compiling a form. What it does is compile `Interp`.

When `Interp` has a cofunction in its second slot (i.e. actually evaluate the action) we has to pass to the kernel the `dat` associated to the cofunction as well.

So far, in the evaluation process we were passing via some nodes multiples times, the way to deal with that so far has been overwriting (i.e. overwrite the values computed at these nodes). In the case where we apply cofunction on the right, overwriting does not work.

-> Need new access descriptor in PyOP2 (need to bikeshed the name, probably `READ_ONCE`)

## LM: `with RooflineStatistics()` design

In the context of a summer project: Add float counting at the gem level

Possible at the loopy level but very expensive, while we get it for free at the gem level.

Should be possible at the gem level by relying on the contraction order to work out the float counting.

If not possible -> Add some handlers to impero

## Merge PRs

## AOB

## Date of next meeting
[2021-06-02](./Firedrake-meeting-2021-06-02) 15:00UTC (16:00BST)