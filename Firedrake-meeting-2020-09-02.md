Date and time 2020-09-02 15:00UTC (16:00BST)

# Action Items
1. ~Pick Chair and Minuter.~
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Only test PRs on master
1. RH: On complex back merge master to fix conflicts
1. ??: Build master on centos to catch errors


# Agenda

Present: DRS, LM, DH, KS, SK, NB, SV, RCK, JB, PHJK, MK, TG

Apologies: RH

## External Operators:

Need reviews for the PR: https://github.com/firedrakeproject/firedrake/pull/1674

Went through some of the Firedrake code in the meeting:

Actions:

NB: Update dat versioning to cover all cases in PyOP2

NB: Can we make the dependencies one-way? that is dpdu depending on p,
but p not remembering dpdu.

DH: First thought, make derivatives a Derivative(ExternalOperator,
deriv_multiindex) object, now dpdu = deriv(p, (1, 0)) (say). Now form
preprocessing can just say "please evaluate p and also `p_(1, 0)`".
Does this cause problems when computing derivatives that create new
coefficients.



## Date of next meeting
[2020-09-07](./Firedrake-meeting-2020-09-07) 15:00UTC (16:00BST)
