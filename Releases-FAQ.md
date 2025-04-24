### Should my change go into ``main`` or ``release``?

Since ``release`` is supposed to be stable w.r.t. API, only fixes should be merged into it. Any new features or API changes should be merged into ``main``.

Note that if you are submitting code to be added to ``release`` then a near-identical PR should be submitted to ``main`` with the same fixes.

### When should a new major version be released?

Major Firedrake releases are made roughly every 6 months. The releases are (ideally) timed to happen shortly after PETSc makes a minor release (e.g. ``3.22.5 -> 3.23.0``) such that any breaking API changes in the release may be fixed.

### When should a patch release be made?

Patch releases are made in an ad hoc fashion when they are deemed necessary. In particular they should follow shortly after fixes are submitted to `release`.

### How is a major release made?

To make a major version release the steps are:

1. Prepare a PR into `release`:
    1. Create a new branch off of `release`.
    1. Merge `main` into this new branch.
    1. Resolve and remove any `# TODO RELEASE` comments.
    1. Update the `version` attribute in the `pyproject.toml`.
1. Once this is merged create a GitHub release with the new version number.
1. Check that the release workflow runs without error.

### How is a patch release made?

To make a patch release follow the same steps as above for a major release but do not merge `main`.
