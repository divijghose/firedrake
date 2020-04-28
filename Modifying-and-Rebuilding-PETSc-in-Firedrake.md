By default, every firedrake installation comes with a clone of the [firedrake project fork of petsc](https://github.com/firedrakeproject/petsc) in `[firedrake-install-dir]/src/petsc` on the `firedrake` branch.

# Rebuilding PETSc

It is possible to make experimental changes to the firedrake installation of PETSc, though PETSc must be rebuilt for the changes to have the desired effect. 

The time consuming way to do this is to run `firedrake-update --rebuild`. The PETSc mirror will be updated and completely rebuilt - often taking over an hour. 

**Note: If the PETSc ABI has changed (in principal whenever the PETSc release version's second number has changed) `firedrake-update --rebuild` must be done.** 

Most of the time though, you can speed things up a lot with the below procedure

 1. Make desired modifications
 2. Activate the firedrake venv
 3. Navigate to `[firedrake-install-dir]/src/petsc`
 4. Run `make PETSC_DIR=[firedrake-install-dir]/src/petsc PETSC_ARCH=default all`. _This should take less than 10 minutes._
 5. Run the suggested `make PETSC_DIR=[firedrake-install-dir]/src/petsc PETSC_ARCH=default check` check (or similar - the log text from successfully performing step 4 should tell you the exact command) to make sure the libraries are working. _This should take less that 2 minutes._

## Troubleshooting Notes

### If the desired modifications (step 1) are on a separate branch
The branch used must have a working remote (such that `git pull` will work) or else `firedrake-update` will fail.

### If `make` (step 4.) fails
Try the following:
 1. Remove the regularly troublesome `PASTIX` headers with `rm -rf default/include/pastix*.h` in the `[firedrake-install-dir]/src/petsc` directory
 2. Run `make reconfigure` - **warning! This may take up to an hour**
 3. Run the `make ...` command recommended in the log text from `make reconfigure` (it will probably be `make PETSC_DIR=[firedrake-install-dir]/src/petsc PETSC_ARCH=default all`)

### If you have modified the API and therefore need to update `petsc4py`
TBC - This only updates PETSc. Something along the lines of 
> you just edit and `pip install -U -no-deps .` in the relevant directory