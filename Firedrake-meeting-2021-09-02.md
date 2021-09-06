Date and time 2021-09-02 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present: DH, LM, NB, DRS, RK, SK, KS, CJC

Apologies: RNH

## Firedrake 2021

24 registered, of which 21 are willing to talk.

**Action** DH: Ask the other three if they'd like to give a talk.

## Dead lock issue

Want petsc4py level solution -> hand craft gc? (JB and CJW)

## External Operator DH

RK: Want to recreate some solutions from a paper using ExternalOperator. Have some lower level implementation.

Want to handle some (non)linear PDE: Form[sol, external_op(sol), ...] = 0

**ExternalOperator branch 1**

Would require DAG rotation.

Does not work yet (NB is working on this, will take several months?)



RK: Want to handle a mixed system with purely algebraic component (no weak form for that component)

**ExternalOperator branch 2 (Dualspace branch)**

For matfree, need to pass : (Gateaux drivative multiindex , tuple that indicates which multiindex is actioned out)

tuple:

(0, 1) -> matrix (both arguments are alive).

(0, None) -> multiindex 1 is actioned out.

(None, 0) -> for adjoint.

RK's plan: 

- Write paper with the handrolled PETSc KSP etc
- Come back later to use ExternalOperator.

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-09-09](./Firedrake-meeting-2021-09-09/)
