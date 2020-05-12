Date and time 2020-05-12 15:00UTC (16:00BST)

# Action Items
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. ~DRS: Open PR for stream plot~ See PR #1670. Review required
1. ~JB: Add mechanism for python3.8~ Someone: test this.
1. DH: Find time to fix to get final complex sprint test passing.
1. ~ALL: Someone to look at TSFC merge needed as part of complex sprint.~ Miklos approved. 
1. ~DH: Find time to sort out Jenkins to run in real and complex mode.~
1. ~LM: Add any action items that may have been accidentally removed.~
1. DRS: Put animation in notebook (Burger's equation)

# Minutes
Present: David Ham, Lawrence Mitchell, Colin Cotter, Daniel R. Shapero, Jack Betteridge, Koki Sagiyama, Nacime Bouziani, Paul Kelly, Reuben Hill, Robert Kirby, Sophia Vorderwuelbecke, Tom Gregory

Apologies:

## Complex
Jenkins:
working in real/complex modes.
Hoping to get the following working:
- complex docker container
- pyadjoint in parallel

loopy:
LM fixed conflicts when back merging, but many things are broken.
-> cherry pick type changes?

Other branches:
ufl: merged
tsfc: good to go
PyOP2: straightforward

All:
If you want your branch tested on Jenkins, use "Draft Pull Request" feature on Github.

## NB: Pointwise operators PRs
Plan:
Merge PyOP2 and tsfc first, and, while waiting for ufl to be merged in FEniCS/ufl, review firedrake branch.

NB:
Make a PR in FEniCS/ufl

## DRS: Update on checkpointing
Desirable to be able to save multiple meshes (and associated data)
PETSc currently designs namespace etc. following convention of standard visualisation tools.

DRS:
Wait for some more PETSc development

## LM: Replacement for expressions compiler
Expression assinment.
Assignment to mixed functions is required, e.g., for RK time integration.
LM explained four assignment types, L=R.
For mixed function assignment, we need a kernel for each set in the mixed set.

Comments on caching:
Firedrake caches for:
- assembly
- interpolation (with Interpolator object)
- pointwise assignement

Three types of caching:
1. on disk (very slow)
2. in memory (slow)
3. on the form

For large time dependent problems, this must be done efficiently. 

## KS: ufl.Filtered -> ufl.Transformed
PR created: https://github.com/FEniCS/ufl/pull/22

KS:
Add documentation to ufl/doc.

## Date of next meeting
2020-05-19 15:00UTC (16:00BST)
