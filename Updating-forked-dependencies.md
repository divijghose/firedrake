## Motivation

Firedrake maintains forks of some of its dependencies (e.g. [PETSc](https://github.com/firedrakeproject/petsc)). This is so we can control the release schedule and protect users from breaking upstream changes whilst also be able to use the latest versions of these projects if we require specific changes.

## Process

These forked repositories should be updated every few months using the following steps:

### Prerequisites

1. Have appropriate permissions to be able to push to the forked repository.
1. `git clone` a local copy of the forked repository.
1. Add the upstream repository as an extra `git remote`:
    ```
    $ git remote add upstream <upstream URL>
    ```

### Steps

1. Make sure that the right branch is checked out and up-to-date (we assume throughout that this branch is called `firedrake`):
    ```
    $ git checkout firedrake
    $ git pull
    ```
1. Update the `upstream` remote:
    ```
    $ git fetch upstream
    ```
1. Update the local branch:
    ```
    $ git merge upstream/main
    ```
    Note that `git merge` should be used here instead of `git rebase` to avoid rewriting the commit history and breaking `firedrake-update`.
1. Create, checkout and push a new branch that is identical to the current one:
    ```
    $ git checkout -b <github username>/upstream-update
    $ git push -u origin <github username>/upstream-update
    ```
1. Create a pull request to the forked repository using this branch ([example](https://github.com/firedrakeproject/petsc/pull/15)).
1. Check that the Firedrake test suite passes using this branch following [these instructions](https://github.com/firedrakeproject/firedrake/wiki/Running-the-Firedrake-test-suite-with-different-branches-for-subpackages).
1. Merge the pull request, updating the forked repository. You should also close the associated Firedrake pull request opened to run the test suite (see above).