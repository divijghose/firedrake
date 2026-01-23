# **THIS PAGE IS ARCHIVED AND IS KEPT ONLY FOR FUTURE REFERENCE**


Previously a script based installation has been used to install Firedrake on ARCHER2, this is no longer recommended and we now encourage you to use Spack. (The old repository is available [here](https://github.com/firedrakeproject/firedrake-archer2))

# Spack install Firedrake on ARCHER2
We will work with the in a directory `/work/[budget code]/[budget code]/[$USER]/workspace`, where `[budget code]` is replaced by your project code and `[$USER]` is your username.
## Prerequisites
You should familiarise yourself with as much of Spack's functionality as possible. To achieve the same flexibility as we have on desktop installs the Firedrake Spack install leverages a lot of Spack's features. More information about Spack can be found on their [website](https://spack.readthedocs.io/en/latest/index.html).

## Spack
Start in a directory on the WORK filesystem, not HOME as it is not accessible from the compute nodes. You may wish to set `SPACK_USER_CONFIG_PATH` which defaults to `~/.spack` to change where spack looks for user level configuration files. Changing `SPACK_USER_CONFIG_PATH` isn't necessary if everything is correctly configured within the spack environment.

### Environment
We recommend using the GNU toolchain and GCC compilers at version 10.2.0, see [additional notes](#Additional-notes) for more info.

The following clones the Spack repo, loads modules to setup the environment and activates Spack.

```bash
git clone -c feature.manyFiles=true git@github.com:spack/spack.git

module purge
module load load-epcc-module

# Load programming environment and compiler
module load PrgEnv-gnu/8.1.0
module swap gcc gcc/10.2.0

module swap cray-mpich cray-mpich/8.1.9
module swap cray-dsmml cray-dsmml/0.2.1
module swap cray-libsci cray-libsci/21.08.1.2
module load xpmem
module load cmake/3.21.3
module load cray-python/3.9.4.1

. spack/share/spack/setup-env.sh
```

If you want to use a different BLAS and LAPACK and Scalapack library you don't need to load cray-libsci and you should run `module unload cray-libsci`. For instance the AMD optimised CPU libraries (AOCL) could be loaded instead `module load aocl/3.1`

If you _really_ want to try the other compilers replace the two isolated lines under `# Load programming environment and compiler` with
```
module load PrgEnv-aocc/8.1.0
module swap aocc aocc/3.0.0
# or
module load PrgEnv-cray/8.1.0
module swap cce cce/12.0.3
```
for the AMD or Cray compilers respectively.

### Configuration
1. Populate `$SPACK_USER_CONFIG_PATH/cray/compilers.yaml` with the following YAML. Note that this contains most of the available compilers, you only need to configure for the compilers you will use.
<details>
    <summary>
        <code>$SPACK_USER_CONFIG_PATH/cray/compilers.yaml</code>
    </summary>

```yaml
compilers:
- compiler:
    spec: aocc@2.2.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags:
      cflags: null
      cxxflags: null
      fflags: null
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-aocc
    - aocc/2.2.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: aocc@2.2.0.1
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags:
      cflags: null
      cxxflags: null
      fflags: null
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-aocc
    - aocc/2.2.0.1
    environment: {}
    extra_rpaths: []
- compiler:
    spec: aocc@3.0.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags:
      cflags: -Wno-unused-command-line-argument -mllvm -eliminate-similar-expr=false
      cxxflags: -Wno-unused-command-line-argument -mllvm -eliminate-similar-expr=false
      fflags: -Wno-unused-command-line-argument -mllvm -eliminate-similar-expr=false
      ldflags: -Wl,-rpath,/opt/cray/libfabric/1.11.0.4.71/lib64 -L/opt/cray/libfabric/1.11.0.4.71/lib64 -lfabric
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-aocc
    - aocc/3.0.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: cce@11.0.4
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-cray
    - cce/11.0.4
    environment: {}
    extra_rpaths: []
- compiler:
    spec: cce@12.0.3
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-cray
    - cce/12.0.3
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
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-gnu
    - gcc/9.3.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@10.2.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-gnu
    - gcc/10.2.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@10.3.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-gnu
    - gcc/10.3.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@11.2.0
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-gnu
    - gcc/11.2.0
    environment: {}
    extra_rpaths: []
- compiler:
    spec: rocmcc@2.14-nosmp
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-amd
    - rocmcc/2.14-nosmp
    environment: {}
    extra_rpaths: []
- compiler:
    spec: rocmcc@2.14
    paths:
      cc: cc
      cxx: CC
      f77: ftn
      fc: ftn
    flags: {}
    operating_system: sles15
    target: any
    modules:
    - PrgEnv-amd
    - rocmcc/2.14
    environment: {}
    extra_rpaths: []
```

</details>


2. Populate `$SPACK_USER_CONFIG_PATH/packages.yaml` with the following
<details>
    <summary>
        <code>$SPACK_USER_CONFIG_PATH/packages.yaml</code>
    </summary>

```yaml
packages:
  all:
    providers:
      mpi: [cray-mpich]
  cray-mpich:
    externals:
    - spec: cray-mpich@8.1.9%gcc@10.2.0
      modules:
      - PrgEnv-gnu
      - gcc/10.2.0
      - cray-mpich/8.1.9
    - spec: cray-mpich@8.1.6%aocc@3.0.0
      # Pretend mpich is version 8.1.6 due to the following bug in spack
      # https://github.com/spack/spack/issues/29459
      # Only with aocc compiler
      modules:
      - PrgEnv-aocc
      - aocc/3.0.0
      - cray-mpich/8.1.9
      prefix: /opt/cray/pe/mpich/8.1.9/ofi/aocc/3.0
    - spec: cray-mpich@8.1.9%cce@12.0.3
      modules:
      - PrgEnv-cray
      - cce/12.0.3
      - cray-mpich/8.1.9
    buildable: False
  cray-libsci:
    externals:
      - spec: cray-libsci@21.04.1.1
        modules:
        - cray-libsci/21.04.1.1
      - spec: cray-libsci@21.08.1.2
        modules:
        - cray-libsci/21.08.1.2
        environment:
          append_path:
          - PE_PKGCONFIG_PRODUCTS: PE_MPICH
    buildable: False
  amdblis:
    externals:
    - spec: amdblis@3.1
      modules:
      - aocl/3.1
    buildable: False
  amdfftw:
    externals:
    - spec: amdfftw@3.1
      modules:
      - aocl/3.1
    buildable: False
  amdlibflame:
    externals:
    - spec: amdlibflame@3.1
      modules:
      - aocl/3.1
    buildable: False
  amdlibm:
    externals:
    - spec: amdlibm@3.1
      modules:
      - aocl/3.1
    buildable: False
  amdscalapack:
    externals:
    - spec: amdscalapack@3.1
      modules:
      - aocl/3.1
    buildable: False
  aocl-sparse:
    externals:
    - spec: aocl-sparse@3.1
      modules:
      - aocl/3.1
    buildable: False
  python:
    externals:
      - spec: python@3.9.4.1
        modules:
        - cray-python/3.9.4.1
      - spec: python@3.8.5.0
        modules:
        - cray-python/3.8.5.0
    buildable: False
  flex:
    externals:
    - spec: flex@2.6.4+lex
      prefix: /usr
  # System texinfo causes issues!
  # texinfo:
  #   externals:
  #   - spec: texinfo@6.5
  #     prefix: /usr
  automake:
    externals:
    - spec: automake@1.15.1
      prefix: /usr
  binutils:
    externals:
    - spec: binutils@2.35.1
      prefix: /usr
  bison:
    externals:
    - spec: bison@3.0.4
      prefix: /usr
  libtool:
    externals:
    - spec: libtool@2.4.6
      prefix: /usr
  m4:
    externals:
    - spec: m4@1.4.18
      prefix: /usr
  openssh:
    externals:
    - spec: openssh@7.9p1
      prefix: /usr
  gawk:
    externals:
    - spec: gawk@4.2.1
      prefix: /usr
  pkg-config:
    externals:
    - spec: pkg-config@0.29.2
      prefix: /usr
    buildable: False
  pkgconf:
    externals:
    - spec: pkg-config@0.29.2
      prefix: /usr
    buildable: False
  openssl:
    externals:
    - spec: openssl@1.1.0i-fips
      prefix: /usr
  groff:
    externals:
    - spec: groff@1.22.3
      prefix: /usr
  autoconf:
    externals:
    - spec: autoconf@2.69
      prefix: /usr
  findutils:
    externals:
    - spec: findutils@4.6.0
      prefix: /usr
  git:
    externals:
    - spec: git@2.26.2~tcltk
      prefix: /usr
  tar:
    externals:
    - spec: tar@1.30
      prefix: /usr
  subversion:
    externals:
    - spec: subversion@1.10.0
      prefix: /usr
  cmake:
    externals:
    - spec: cmake@3.10.2
      prefix: /usr
    - spec: cmake@3.21.3
      prefix: /work/y07/shared/utils/core/cmake/3.21.3
  gmake:
    externals:
    - spec: gmake@4.2.1
      prefix: /usr
  diffutils:
    externals:
    - spec: diffutils@3.6
      prefix: /usr
```
</details>

## Firedrake
### Installation
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
1. To work around the fact that `/home` is not accessible from compute nodes the location of the firedrake repo needs to be set inside `$SPACK_ENV/spack.yaml`:
    ```yaml
    spack:
      repos:
      - /work/[budget code]/[budget code]/[$USER]/workspace/firedrake-spack
    ```
    Where the path should point to the repo cloned in step 1.
1. Then custom configure the packages inside `$SPACK_ENV/spack.yaml`:
    ```yaml
    spack:
      include:
      - packages.yaml
    ```
1. And create `$SPACK_ENV/packages.yaml` with contents:
    ```yaml
    packages:
      all:
        compiler: [gcc@10.2.0]
        providers:
          mpi: [cray-mpich]
          blas: [cray-libsci]
          lapack: [cray-libsci]
          scalapack: [cray-libsci]
      netlib-scalapack:
        externals:
          # Pretend cray-libsci is netlib-scalapack
          - spec: netlib-scalapack@21.08.1.2
            modules:
            - cray-libsci/21.08.1.2
        buildable: False
      py-numpy:
        externals:
        - spec: py-numpy@1.20.1
          modules:
          - cray-libsci/21.08.1.2
          - cray-python/3.9.4.1
          prefix: /opt/cray/pe/python/3.9.4.1/
        buildable: False
      py-scipy:
        externals:
        - spec: py-scipy@1.6.2
          modules:
          - cray-libsci/21.08.1.2
          - cray-python/3.9.4.1
          prefix: /opt/cray/pe/python/3.9.4.1/
        buildable: False
    ```
    If using AMD or Cray compilers replace the compiler above (`[gcc@10.2.0]`) with  `[aocc@3.0.0]` or `[cce@12.0.3]`.

1. Add Firedrake to the spec for the environment
    ```
    spack add py-firedrake@develop \
        %gcc@10.2.0 \
        ^python@3.9.4.1 \
        ^cray-mpich@8.1.9%gcc@10.2.0 \
        ^cray-libsci@21.08.1.2 \
        ^firedrake.petsc@develop+fftw \
            cflags=\"-O3 -march=native -mtune=native\" \
            cxxflags=\"-O3 -march=native -mtune=native\" \
            fflags=\"-O3 -march=native -mtune=native -ffree-line-length-512\"
    ```

1. Concretize (and log) `spack concretize -f 2>&1 | tee $SPACK_ENV/conc.log`
    * Splitting the concretize and install steps into 2 distinct parts allows you to review what is being installed before the lengthy installation process begins.

1. Install (and log) `spack install --fail-fast 2>&1 | tee $SPACK_ENV/spack-firedrake-install.log`

### Testing
Testing must be run on a compute node. An interactive session can be started using
```bash
srun --nodes=1 --exclusive --time=00:20:00 \
               --partition=standard --qos=short --reservation=shortqos \
               --account=[budget code] --pty /bin/bash
```
Alternatively submit a jobscript, see [additional notes](#Additional-notes).
1. Test you can import Firedrake by running `python -c "from firedrake import *"`
    - If this fails, before trying anything else, deactivate the environment with `spack env deactivate` and reactivate with `spack env activate -p ./firedrake` (as above) and try running `python -c "from firedrake import *"` again. This appears to be a shortcoming of spack.
1. Run the basic functionality tests:
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

## Interoperability with `pip`
If you pip install a Python package on ARCHER2 with or without the Spack environment active, it will get installed as a user, and as such be located in the `$HOME` directory. This is an issue since the `$HOME` directory is not mounted on the compute nodes.

The obvious solution to this is not to use pip to install the package and instead attempt to add it to the environment. If the PyPI package is named `foo`, the corresponding Spack package is likely called `py-foo`. Spack's builtin repository can be searched by executing `spack list foo` or `spack list py-foo`.

If the package is not present the correct solution is to create one and upstream it into Spack's builtin package repository. There are instructions in Spack's documentation on how to do this.

## Additional notes:
This page is based off installation notes available [here](https://hackmd.io/Sg3fYXuCTl61d_LAg4QnMw?view). These notes contain more details of bugs you may encounter and how to build with other compilers.

Example jobscript:
```bash
#!/bin/bash
#SBATCH -p standard
#SBATCH -A [budget code]
#SBATCH -J spack
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --qos=standard
#SBATCH -t 0:10:00

myScript="run.sh"

module purge
module load load-epcc-module

module load PrgEnv-gnu/8.1.0
module swap gcc gcc/10.2.0

module swap cray-mpich cray-mpich/8.1.9
module swap cray-dsmml cray-dsmml/0.2.1
module swap cray-libsci cray-libsci/21.08.1.2
module load xpmem
module load cmake/3.21.3
module load cray-python/3.9.4.1

export HOME=/work/[budget code]/[budget code]/[$USER]
source /work/[budget code]/[budget code]/[$USER]/workspace/spack/share/spack/setup-env.sh
spack env activate /work/[budget code]/[budget code]/[$USER]/workspace/firedrake

./${myScript}
```
