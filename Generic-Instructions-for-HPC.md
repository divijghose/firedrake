## THE FOLLOWING INSTRUCTIONS ARE OUT-OF-DATE

### [Spack](https://spack.readthedocs.io/en/latest/index.html):
1. Follow [getting started](https://spack.readthedocs.io/en/latest/getting_started.html) guide
    - Ensure develop branch is installed
    - Ensure desired [compilers](https://spack.readthedocs.io/en/latest/getting_started.html#compiler-configuration) are known to spack, should be picked up by `spack compiler find`
    - Ensure [system packages](https://spack.readthedocs.io/en/latest/getting_started.html#system-packages) (that you don't want spack to install) are known to spack, some may be picked up by `spack external find`, others may require manual intervention.
2. You may want to specify the system MPI as the correct MPI for spack to use. This appears to be quite difficult, a starting template for the `~/.spack/packages.yaml`might be:
    ```yaml
    packages:
      mpich:
      externals:
      - spec: mpich@4.0
        prefix: /opt/mpich
      buildable: False
    ```
    If Spack's PETSc package doesn't think this spec line is suitable it _will_ try to build its own MPICH.

Make sure the spack `setup-env.sh` file has been sourced and you can run spack commands before moving to the next section.

### [Firedrake-repo](https://github.com/firedrakeproject/firedrake-spack)
1. Clone the above repo, using
 ```bash
git clone https://github.com/firedrakeproject/firedrake-spack.git
# or
git clone git@github.com:firedrakeproject/firedrake-spack.git
```
1. Add the repository to spack `spack repo add <repo directory> `
1. Create an spack environment `spack env create -d ./firedrake`
1. Activate that environment `spack env activate -p ./firedrake`
    * To avoid a bunch of errors add a whole bunch of packages to the development package list:
    ```
    spack develop py-firedrake@develop
    spack develop libsupermesh@develop
    spack develop petsc@develop
    spack develop chaco@petsc
    spack develop py-fiat@develop
    spack develop py-finat@develop
    spack develop py-islpy@develop
    spack develop py-petsc4py@develop
    spack develop py-pyadjoint@develop
    spack develop py-pyop2@develop
    spack develop py-coffee@develop
    spack develop py-loopy@develop
    spack develop py-cgen@develop

    spack develop py-codepy@develop
    spack develop py-genpy@develop
    spack develop py-tsfc@develop
    spack develop py-ufl@develop
    ```
    *
1. Install firedrake using `spack add py-firedrake@develop %gcc ^mpich ^openblas`
    * `%gcc` specifies the compiler, you may wish to specify a version (eg: `%gcc@11.2.0`), ommiting this will use the default compiler
    * `^mpich` specifies which MPI to use. If you set an MPI system package be sure to use this (eg: `^openmpi@3.1`)
    * `^openblas` specifies which BLAS/LAPACK library to use. If you set an BLAS/LAPACK system package be sure to use this (eg: `^intel-mkl@2019.1`)
    * You can further specify the Python version by adding `^python@3.10` for Python 3.10 or setting the system python if it's set up in system packages
1. `spack install` Will install everything
    - Add `--fail-fast` to stop at the first package with an install error
    - Adding `2>&1 | tee spack-firedrake-install.log` to the end of the command will save all output to a log file that you can send if you need someone else to look over the output.
    - ```spack install --fail-fast  2>&1 | tee spack-firedrake-install.log ```
1. Test you can import Firedrake by running `python -c "from firedrake import *"`
    - If this fails, before trying anything else, deactivate the environment with `spack env deactivate` and reactivate with `spack env activate -p ./firedrake` (as above) and try running `python -c "from firedrake import *"` again. This appears to be a shortcoming of spack (related to[#10801](https://github.com/spack/spack/issues/10801)?).
1. Run the basic functionality tests:
    ```bash
    cd $SPACK_ENV/py-firedrake
    pytest tests/regression/ -k "poisson_strong or stokes_mini or dg_advection"
    ```
1. Run the full test suite:
    ```bash
    cd $SPACK_ENV/src/firedrake
    pytest tests
    ```
