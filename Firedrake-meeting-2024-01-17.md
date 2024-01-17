Date and time 2024-01-17 1600 GMT (1600 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to minute)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
  1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))? JB: Waiting for https://github.com/Toblerity/rtree/pull/292
1. NB: Update on what is needed for Interp/ExternalOperator to be merged


# Agenda

Present: DH, DID, JB, CW, NB, FA, IM, JHC, KS

Apologies:

## JB: PDESoft in Cambridge
Info + registration at [this link](https://pdesoft.org/)

Required for SysgenX.

Happening in July.

ALL: submit abstract.

## JB: Make VTK a soft dependency
https://github.com/firedrakeproject/firedrake/pull/3324

VTK wheels are not available on some platforms.

DH: netcdf is like HDF5, so it itself is not required by Firedrake, but by Gusto.

JB: Move checkpointing.py to output folder.

## JB: Progress on RTree
[PR](https://github.com/Toblerity/rtree/pull/292) closer to being merged. See [libsupermesh](https://github.com/firedrakeproject/libsupermesh/pull/4) and [firedrake](https://github.com/firedrakeproject/firedrake/pull/3138) PRs for progress on our side.

JB: continue working with the firedrake branch.

## CW: Status of "backend" for adjoint
See [relevant issue](https://github.com/firedrakeproject/firedrake/issues/3325). Surely "backend" is a redundant concept now?

Yes. Someone needs to replace all backend with whatever.

expunge vectors in adjoint -> use Cofunctions.

expunge Function.vector -> suggest using PETSc.vec or dat.data.

## JB: Firedrake team
Add Daiane to "Active" and move Sophia to "Former". We should make sure we are not forgetting anyone else either!

DID: Do this adding her own photo.

## NB: Interp

- Firedrake [PR](https://github.com/firedrakeproject/firedrake/pull/2297)

- Pyadjoint [PR](https://github.com/dolfin-adjoint/pyadjoint/pull/127)

Documentation is failing.

DH: probably just take "optional" out?

## Merge PRs 

*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

JB: [#3152](https://github.com/firedrakeproject/firedrake/pull/3152) Firedrake public interface to GC + [PyOP2#712](https://github.com/OP2/PyOP2/pull/712) this has been reviewed and iterated several times.

# Date of next meeting

1600 GMT (1600 UTC) [2024-01-24](./Firedrake-meeting-2024-01-24)