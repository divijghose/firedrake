1. Create and check out a new Firedrake branch:
    ```
    $ cd firedrake/src/firedrake
    $ git checkout master
    $ git pull
    $ git checkout -b check-my-subpackage-changes
    ```
1. Modify the [`firedrake-install` line in `firedrake/.github/workflows/build.yml`](https://github.com/firedrakeproject/firedrake/blob/master/.github/workflows/build.yml#L51) to include the argument `--package-branch <subpackage> <branch>` (e.g. `--package-branch tsfc add-new-feature`). Note that these branches must exist on the main package repository. Branches in forked repositories will not be found. Note that if PETSc is the repository getting tested then additional steps are required (see below).
1. Commit and push this change.
1. Create a draft pull request on the Firedrake repository for this branch. Be sure to call the pull request something like "DO NOT MERGE Test new TSFC feature" or similar ([example](https://github.com/firedrakeproject/firedrake/pull/2781)).

### Testing PETSc branches

By default we do not recompile PETSc when the test suite is run. To force it to rebuild (and for `--package-branch petsc <branch>` to be respected) one needs to make additional modifications to the `build.yml` file:

- Delete the line `--honour-petsc-dir \` from the arguments to `firedrake-install`.
- Make sure to `unset PETSC_DIR PETSC_ARCH SLEPC_DIR` for each step.

An example can be found [here](https://github.com/firedrakeproject/firedrake/pull/3140/files).