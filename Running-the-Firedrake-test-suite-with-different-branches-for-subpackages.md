1. Create and check out a new Firedrake branch:
    ```
    $ cd firedrake/src/firedrake
    $ git checkout master
    $ git pull
    $ git checkout -b check-my-subpackage-changes
    ```
1. Modify the [`firedrake-install` line in `firedrake/.github/workflows/build.yml`](https://github.com/firedrakeproject/firedrake/blob/master/.github/workflows/build.yml#L51) to include the argument `--package-branch <subpackage> <branch>` (e.g. `--package-branch tsfc add-new-feature`).
1. Commit and push this change.
1. Create a draft pull request on the Firedrake repository for this branch. Be sure to call the pull request something like "DO NOT MERGE Test new TSFC feature" or similar ([example](https://github.com/firedrakeproject/firedrake/pull/2781)).