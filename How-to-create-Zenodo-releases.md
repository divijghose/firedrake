The procedure is documented in `scripts/firedrake-zenodo`. Below is the summary:

Prerequisite:

- Have FIREDRAKE_GITHUB_TOKEN set to a Github personal access token with public_repo scope.
- Have FIREDRAKE_ZENODO_TOKEN set to a Zenodo personal access token with deposit:write scope.

It would be convenient to add these environment variables to `.bashrc` (or whatever) so that you do not need to `export` every time you make a zenodo release.

With these tokens set and with a JSON file (say `firedrake.json`) supplied by the user:

- Run `firedrake-zenodo --input firedrake.json`.
- Follow the instruction thereafter.

## Common issues

### Missing releases

You may see errors like "A release of petsc is referenced but not corresponding release on GitHub can be found.". This means that you have to manually create the releases on the Firedrake fork. To do this (assuming `REPO` is `petsc`, `loopy`, etc):

```
$ git clone git@REPO_URL
$ cd REPO
$ git remote add firedrake git@github.com:firedrakeproject/REPO
$ git fetch firedrake
$ git push --tags firedrake
```
Then go to GitHub and create a release with the right name (note that some packages prepend a 'v' in their version name).