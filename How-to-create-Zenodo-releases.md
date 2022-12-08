The procedure is documented in `scripts/firedrake-zenodo`. Below is the summary:

Prerequisite:

- Have FIREDRAKE_GITHUB_TOKEN set to a Github personal access token with public_repo scope.
- Have FIREDRAKE_ZENODO_TOKEN set to a Zenodo personal access token with deposit:write scope.

It would be convenient to add these environment variables to `.bashrc` (or whatever) so that you do not need to `export` every time you make a zenodo release.

With these tokens set and with a JSON file (say `firedrake.json`) supplied by the user:

- Run `firedrake-zenodo --input firedrake.json`.
- Follow the instruction thereafter.