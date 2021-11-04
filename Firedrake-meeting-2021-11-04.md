Date and time 2021-11-04 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Minutes

Present: CW, KS, LM, NB, SV, JDB, TG, DH

Apologies:

##  DH: Mac build disaster

DH: Wrong BLAS getting used in builds sometimes. This can be hard to reproduce.

JDB: Several edits to firedrake-install made when M1 fixes introduced.

Everyone with a Mac: Run firedrake-install (having run `brew uninstall openblas`) and see if it breaks.


## NB: Object versioning

PR: https://github.com/OP2/PyOP2/pull/579

NB: Motivation is to avoid backward propagation when not required. Initially started with `Global` but has tried to extend to `Dat` and `Mat`.

LM: PETSc objects have a state counter that could be exposed from petsc4py. For matrices we could just look at this.

LM: Modifying 'core' parts of iteration set can still invalidate the halo for other partitions. Therefore we should have something that combines `halo_valid` and object versioning.

## Merge PRs:

## AOB

## Date of next meeting

1500 UTC (1600 BST) [2021-11-11](./Firedrake-meeting-2021-11-11/)
