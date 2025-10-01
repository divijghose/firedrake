To make a new release, see the process detailed [here](./Make-a-release).

### Should my change go into `main` or `release`?

Since `release` is supposed to be stable w.r.t. API, only fixes and documentation changes should be merged into it. Any new features or API changes should be merged into `main`.

If you want your code to be available in both `release` and `main` then you should merge your code first into `release` and then create a subsequent PR merging (a branch off of) `release` into `main`.

### When should a new major version be released?

Major Firedrake releases are made roughly every 6 months. The releases are (ideally) timed to happen shortly after PETSc makes a minor release (e.g. `3.22.5 -> 3.23.0`) such that any breaking API changes in the release may be fixed.

### When should a patch release be made?

Patch releases are made in an ad hoc fashion when they are deemed necessary. In particular they should follow shortly after fixes are submitted to `release`.