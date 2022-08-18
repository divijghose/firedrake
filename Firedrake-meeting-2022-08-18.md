Date and time 2022-08-18 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (RNH to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (ongoing)
1. JB: SIAM CSE23 Minisymposium/minisymposterium
1. ~JB: PETSc branch with GC fix (JB) + IO (KS)~

# Minutes

Present: CW SV JB DH KS RNH NB

Apologies:

## DH Firedrake22
Firedrake 22 will be on 4-6th Jan 2023, Dartington Hall.

Jemma will be at Imperial 7-8th September.

Firedrake training will probably run next term.

## DH + JB: SIAM CSE
Steady progress

## DH: PETSc IO + GC branch
JB: This is done.

DH: There is an issue when writing to file. DH to update with details shortly.

DH: In the process managed to get the graphical debugger in VSCode to work with MPI.

## NB: Interp - Problem with the current maths for adjoint ?

There seems to be a problem noticed with the current theory for the adjoint of Interp.

Context: Let $I(v_1, v_{0}^{*})$ be an `Interp` mapping from $V_1$ to $V_0$ with $v_{0}^{\*} \in V_{0}^{\*}$ (Coargument) and $v_{1} \in V_{1}$. Then the adjoint should map from $V_{0}^{\*}$ to $V_{1}^{\*}$.

RNH: There is an open issue about mis-annotated Hessians https://github.com/firedrakeproject/firedrake/issues/1980, perhaps a clue?

DH: Somewhere in py-adjoint, someone has done something naughty and needs to be sorted out. Problem is probably with the maths.

RNH: Currently very familiar with this code.

Action DH: Produce an MFE for this issue.

## DH: Job advert is now live:
[Look here!](https://www.imperial.ac.uk/jobs/description/NAT01233/research-associate-computational-mathematics)

## DH: Seismologists want subdomains and unstructured hexes
Amongst all the other users who want this...

## RNH: Firedrake UFL is still out of sync with Fenics UFL
DH: Need to sit down and sort this out, somehow an element has been added twice! Need to avoid breaking things for RK. 

## DH: Sleeping AMR issue may have reawoken

## DH: EGU is coming soon

## Merge PRs

## Date of next meetings

Next meeting: 1200 UTC [2022-08-25](./Firedrake-meeting-2022-08-25)