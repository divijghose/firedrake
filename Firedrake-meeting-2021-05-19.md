Date and time 2021-05-19 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. DH: Email Jemma, Ivan Re: Training
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Minutes

Present: JB, LM, DH, RNH, CW, KS, NB, SK, SV, PK

Apologies:

## Build hardware

DH: It's coming, hopefully soon, but it's being chased

LM: No power supply in Durham yet

## Excalibur Phase2

DH: Deadline is end of September, closed call.

LM: Is it really £8m/3 or is that figure 80%?

> DH: `<expletive>`

DH: We are having diplomatic discussions with Fenics group for a joint bid, rather than compete. Current thinking is GPUs will be central to the bid, all the bits are there, but we need the plumbing.

LM: Will the other members of the GenX be going forward with phase 2?

DH: Not enough money, notionally it's 4 PostDocs total.

## Master still failing
DH: Can we ignore it until the new build hardware is in?

Action RNH: PR to skip failing test: `tests/demos/test_demos_run.py::test_demo_runs[qg_1layer_wave.py.rst]`

## Merge PRs

#2080 CW: Add shape, dtype and intent to parloop cache key - Merged

#2071 SV: Docs actions - Still draft

DH: Do we want to separate out different parts of the CI?

LM: Definitely linting should remain separate

#2074 Dave Acreman: Change colour bar range for DG advection example plot - Merged

#2063 Joe Wallwork: Annotate supermesh projection - Changes requested, code duplication

#2059 RNH: Interpolation onto a Vertex Only Mesh - Where should the code for making a quadrature element live? Design decisions still need to be made here

#2055 Joe Wallwork: Various annotation fixes for Constant and Function - Waiting for upstream changes in pyadjoint, rebase and fix conflicts to pass tests

#2047 JB: Limit Threading - Merged

#2054 CW: Deprecate create_assembly_callable - Merged

## AOB

## Date of next meeting
[2021-05-26](./Firedrake-meeting-2021-05-26) 15:00UTC (16:00BST)