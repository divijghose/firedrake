
### How is a major release made?

To make a major version release the steps are:

1. Prepare a PR into `release`:
    1. Create a new branch off of `release`.
    1. Merge `main` into this new branch.
    1. Resolve and remove any `# TODO RELEASE` comments.
    1. Update the `version` attribute in the `pyproject.toml`.
1. Once this is merged create a GitHub release from the `release` branch with the new version number.
1. Check that the release workflow runs without error.
1. Merge the PR. **IMPORTANT: The commits must not be squashed.**

### How is a patch release made?

To make a patch release follow the same steps as above for a major release but do not merge `master`.
