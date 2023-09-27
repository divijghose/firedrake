Date and time 2023-09-27 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (IM to pick minuter?)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. JB: Scheduled GitHub actions to avoid inactivity timeout for website repo ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-20#jb-scheduled-gh-actions-time-out-after-something-like-60-days-of-inactivity))
1. ~~CW: Update website since homebrew Python is now dodgy.~~ merged
1. DH: Order more Firedrake stickers

# Minutes

Present: CW (minuter), JB, KS, DH, DD, RNH, RK, PB, DS, NB, UZ

Apologies:

## JMC MEng/Applied MSc projects

- DH: Coupled domain stuff.
- JB: ROL stuff?
- RNH: Point evaluation for bendy meshes.
- DH: Similarly mesh-to-mesh interpolation with more complicated nodes.

## CW/JB: libsupermesh needs updating

A MacOS user has [failed to build libsupermesh](https://github.com/firedrakeproject/firedrake/issues/3123) due to the fact that the libspatialindex inside of libsupermesh is very old. How should we proceed? Why do we have 2 libspatialindex's ([here](https://github.com/firedrakeproject/libspatialindex) and [here](https://github.com/firedrakeproject/libsupermesh/tree/master/spatialindex-1.8.5))??

- JB: I don't think RTree PyPI package will save us: The headers are not bundled in the wheel, so libsupermesh cannot link.
- Action point JB: submit a PR that bundles the headers with RTree so we can link to it. We can then find the right files by importing `rtree` and asking where its files are.
- DH: But libsupermesh uses non-public API bits of libspatialindex. We should see if we can drop it and use mesh-to-mesh interpolation instead.

## DH: How to fix MacOS build

- RNH: MacOS command line tools version 15 is apparently buggy.
- Action point: Fix PNetCDF build by defaulting to downloading BLAS with MacOS (`--with-blas=download`).
- Action point KS: xfail tests and update PETSc fork.

## NB: Interpolate PR

[#2297](https://github.com/firedrakeproject/firedrake/pull/2297)

## Merge PRs

- CW: https://github.com/OP2/PyOP2/pull/708
- RNH: [Switch off annotation when making an interpolator #3087](https://github.com/firedrakeproject/firedrake/pull/3087)
- UZ: [Netgen curved mesh #3096](https://github.com/firedrakeproject/firedrake/pull/3096)
- KS: https://github.com/firedrakeproject/firedrake/pull/3128
- KS: https://github.com/firedrakeproject/firedrake/pull/3129
- AG: https://github.com/dolfin-adjoint/pyadjoint/pull/118 merged

# Date of next meeting

1600 BST (1500 UTC) [2023-10-04](./Firedrake-meeting-2023-10-04)
