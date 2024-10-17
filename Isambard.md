# Isambard is no more!
The Isambard 2 service was [retired](https://gw4-isambard.github.io/docs/) on 30th September 2024. These notes are only for reference.

We have only tried installing on the XCI (ARM/ThunderX2/TX2) system, not the MACS, A64FX or Phase3 portions of the machine.

## Prerequisites
You should familiarise yourself with as much of Spack's functionality as possible. To achieve the same flexibility as we have on desktop installs the Firedrake Spack install leverages a lot of Spack's features. More information about Spack can be found on their [website](https://spack.readthedocs.io/en/latest/index.html).

## Spack
### Environment
- The following clones the Spack repo, loads modules to setup the environment and activates Spack.
```bash
git clone -c feature.manyFiles=true git@github.com:spack/spack.git

module purge
module load Base-opts
module load PrgEnv-gnu
module load pmi-lib
module load cray-python/3.8.5.1
module load cray-mpich

. spack/share/spack/setup-env.sh
```
### Configuration
1. Populate `$SPACK_USER_CONFIG_PATH/cray/compilers.yaml` with
<details>
    <summary>
        <code>$SPACK_USER_CONFIG_PATH/cray/compilers.yaml</code>
    </summary>

```yaml
compilers:
- compiler:
    spec: cce@11.0.4
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: cnl7
    target: any
    modules:
    - PrgEnv-cray
    - cce/11.0.4
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@9.3.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: cnl7
    target: any
    modules:
    - PrgEnv-gnu
    - gcc/9.3.0
    environment: {}
    extra_rpaths: []
```
</details>

1. Populate `$SPACK_USER_CONFIG_PATH/packages.yaml` with
<details>
    <summary>
        <code>$SPACK_USER_CONFIG_PATH/packages.yaml</code>
    </summary>

```yaml
packages:
  all:
    providers:
      mpi: [cray-mpich]
  pkg-config:
    externals:
    - spec: pkg-config@0.29.2
      prefix: /usr
    buildable: False
  pkgconf:
    externals:
    - spec: pkgconf@0.29.2
      prefix: /usr
    buildable: False
  cray-mpich:
    externals:
    - spec: cray-mpich@7.7.17%gcc@9.3.0
      modules:
      - PrgEnv-gnu
      - gcc/9.3.0
      - cray-mpich/7.7.17
    - spec: cray-mpich@7.7.17%cce@11.0.4
      modules:
      - PrgEnv-cray
      - cce/11.0.4
      - cray-mpich/7.7.17
    buildable: False
  cray-libsci:
    externals:
      - spec: cray-libsci@20.09.1
        modules:
        - cray-libsci/20.09.1
      - spec: cray-libsci@19.06.1
        modules:
        - cray-libsci/19.06.1
    buildable: False
  python:
    externals:
      - spec: python@3.8.5.1
        modules:
        - cray-python/3.8.5.1
      - spec: cray-python@3.7.3.2
        modules:
        - cray-python/3.7.3.2
    buildable: False
```
</details>

4. Esure `$SPACK_USER_CONFIG_PATH/upstreams.yaml` does not exist. Upstream (system level installed Spack packages) for Isambard cause the Cray tools (compiler wrappers) to break.

### Firedrake
1. Clone the repo:
    ```bash
    git clone https://github.com/firedrakeproject/firedrake-spack.git
    # or
    git clone git@github.com:firedrakeproject/firedrake-spack.git
    ```
1. Add the repository to spack `spack repo add <repo directory> `
1. Create an spack environment `spack env create -d ./firedrake`
1. Activate that environment `spack env activate -p ./firedrake`
1. To avoid a bunch of errors add a whole bunch of packages to the development package list:
    ```bash
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
1. Add Firedrake:
    ```bash
    spack add py-firedrake@develop \
        %gcc@9.3.0 \
        ^python@3.8.5.1 \
        ^cray-mpich@7.7.17%gcc@9.3.0 \
        ^cray-libsci@20.09.1 \
        ^firedrake.petsc@develop+fftw cflags=\"-O3 -march=native -mtune=native\" cxxflags=\"-O3 -march=native -mtune=native\" fflags=\"-O3 -march=native -mtune=native -ffree-line-length-512\"
    ```
1. Add to `$SPACK_ENV/spack.yaml`:
    ```yaml
    spack:
      packages:
        all:
          compiler: [gcc@9.3.0]
          providers:
            mpi: [cray-mpich]
            blas: [cray-libsci]
            lapack: [cray-libsci]
            scalapack: [cray-libsci]
        netlib-scalapack:
          externals:
            # Pretend cray-libsci is netlib-scalapack
            - spec: netlib-scalapack@20.09.1
              modules:
              - cray-libsci/20.09.1
          buildable: False
    ```
1. Concretize (and log) `spack concretize -f 2>&1 | tee $SPACK_ENV/conc.log`
    * Splitting the concretize and install steps into 2 distinct parts allows you to review what is being installed before the lengthy installation process begins.

1. Install (and log) `spack install --fail-fast 2>&1 | tee $SPACK_ENV/spack-firedrake-install.log`

### Testing
Testing must be run on a compute node. An interactive session can be started using
```bash
qsub -I -q arm-dev -l walltime=00:10:00
```
Alternatively submit a jobscript, see [additional notes](#Additional-notes).
1. Test you can import Firedrake by running `aprun -n 1 python -c "from firedrake import *"`. You must run via `aprun` to make sure the MPI modules are found.
    - If this fails, before trying anything else, deactivate the environment with `spack env deactivate` and reactivate with `spack env activate -p ./firedrake` (as above) and try running `python -c "from firedrake import *"` again. This appears to be a shortcoming of spack.
1. Run the basic functionality tests. Before running you will need to set a few pyop2 variables:
    ```bash
    unset PYOP2_LD
    export PYOP2_CC=`which cc`
    export PYOP2_CXX=`which CC`
    export PYOP2_CFLAGS="-I${CRAY_MPICH_DIR}/include/"
    export PYOP2_LDFLAGS='-shared'
    ```
   Run the tests with:
    ```bash
    cd $SPACK_ENV/py-firedrake
    pytest tests/regression/ -m "not parallel" -k "poisson_strong or stokes_mini or dg_advection"
    ```
    - When running the environment on the compute nodes the variable `$HOME` needs to be set to something like `/work/_projectcode_/_projectcode_/_username_` or `/tmp` as many dependencies expect to find configuration in `$HOME`.
    - We don't run parallel tests due to an issue with the current parallel pytest hook, this is in the process of being fixed.
1. Run the full test suite:
    ```bash
    cd $SPACK_ENV/src/firedrake
    pytest tests -m "not parallel"
    ```

## Additional notes
This page is based off installation notes available [here](https://hackmd.io/62Gsp44mTSmE9JEWl1Zo6w?view).

Other potential problems you may run into:
* At the `spack install` step, Spack may complain about a missing dependency `gnuconfig` for the `libffi` package. It will tell you to add `depends_on('gnuconfig', type='build', when='@3.4.2')` to the package definition (exact version may not be `3.4.2`). You can edit the package file with `spack edit libffi`. This opens the package file located in `spack/var/spack/repos/builtin/packages/libffi/package.py` with $EDITOR. You can see how to add dependencies from the [example in the Spack documentation](https://spack-tutorial.readthedocs.io/en/latest/tutorial_packaging.html#adding-dependencies).
* This guide assumes you are using your own Spack installation. After running `. spack/share/spack/setup-env.sh` you can check you are using the correct Spack installation with `which spack`.

Isambard maintains an installation of Spack, but it is not up to date and does not contain many of the fixes required to install Firedrake. Documentation is available on the [Isambard spack docs](https://gw4-isambard.github.io/docs/user-guide/spack.html) page.
