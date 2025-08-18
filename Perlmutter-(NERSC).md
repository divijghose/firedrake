*As of 08/18/2025 (and 06/06/2025 for developer version further below). Contributed by Golo Wimmer (Los Alamos National Laboratory)*

- Get the most recent firedrake config file
```
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/refs/tags/<VERSION>/scripts/firedrake-configure
```
- Load appropriate modules
```
module load cmake
module load cray-python
```
Other modules that should be loaded by default include `cray-mpich` and `gcc`.

- Get correct petsc version
```
git clone --branch $(python3 firedrake-configure --no-package-manager --show-petsc-version) https://gitlab.com/petsc/petsc.git
```
- Configure petsc. this step can be amended to include additional libraries such as hppdm (and slepc as needed for hppdm). Since no libraries are assumed to be installed, this step takes a while.
```
cd petsc
python3 ../firedrake-configure --no-package-manager --show-petsc-configure-options | xargs -L1 ./configure --download-hpddm --download-slepc
```
- Compile petsc
```
PETSC_DIR=$PWD
make PETSC_DIR=$PETSC_DIR PETSC_ARCH=arch-firedrake-default all
```
- Test petsc (optional; using command given at the end of petsc install)
```
make PETSC_DIR=path_to_directory_in_which_petsc_was_installed/petsc PETSC_ARCH=arch-firedrake-default check
```
- Install Firedrake: make a virtual environment, activate it, set environment variables, remove previous existing firedrake and petsc4py cache. Also set environment variables to avoid "Error: Type mismatch between actual argument at (1) and actual argument at (2) (INTEGER(1)/INTEGER(4))." in libsupermesh install
```
cd ..
python3 -m venv venv-firedrake
. venv-firedrake/bin/activate
export $(python3 firedrake-configure --no-package-manager --show-env)
pip cache remove petsc4py
pip cache remove firedrake
export FCFLAGS="-w -fallow-argument-mismatch -O2"
export FFLAGS="-w -fallow-argument-mismatch -O2"
pip install --no-binary h5py 'firedrake[check]'
```
- Install python packages (e.g., `pip install vtk`)

- Update LD_LIBRARY_PATH to void errors along the line of `ImportError: libpetsc.so.3.23: cannot open shared object file: No such file or directory`
```
export LD_LIBRARY_PATH=$PETSC_DIR/arch-firedrake-default/lib:$LD_LIBRARY_PATH
```
- Check if installation was successful. Note that mpiexec is not available on perlmutter, and to run the parallel runs in firedrake-check, a similar hack as in the guideline for Isambard 3 can be used.
```
firedrake-check
```
- Trouble shooting: There may be an mpich version issue, which leads to errors along the lines of (when importing firedrake)
```
    from mpi4py import MPI
ImportError: libmpi.so.12: cannot open shared object file: No such file or directory
```
To resolve this, reinstall mpich within firedrake venv
```
pip uninstall mpi4py -y
CC=cc MPICC=cc pip install --no-binary=mpi4py mpi4py
```

#### Guidelines for developer version ####
Changes to (a previous version of) the above are marked by (!)

- (!) Get firedrake developer config file
```
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-configure
```
- Load appropriate modules
```
module load cmake
module load cray-python
```
- (!) Get most recent petsc version
```
git clone https://gitlab.com/petsc/petsc.git
```
- Configure petsc as before (optionally e.g., with slepc and hpddm)
```
cd petsc
python3 ../firedrake-configure --no-package-manager --show-petsc-configure-options | xargs -L1 ./configure --download-hpddm --download-slepc
```
- Compile petsc
```
PETSC_DIR=$PWD
make PETSC_DIR=$PETSC_DIR PETSC_ARCH=arch-firedrake-default all
```
- Test petsc (optional; using command given at the end of petsc install)
```
make PETSC_DIR=path_to_directory_in_which_petsc_was_installed/petsc PETSC_ARCH=arch-firedrake-default check
```
- (!): Install firedrake: clone firedrake repo, set up venv, run configuration. New steps: install pets4py; note that for most recent version of petsc, cython constraint is not needed. This will also install libsupermesh as a firedrake requirement, which will throw an argument mismatch error; need to add FC and FF flags to allow for the mismatch. Further, for the firedrake install command, there will be an error along the lines of `error: invalid command 'bdist_wheel'` because the wheel package is missing, and we therefore need to pip install it first.
```
cd ..
git clone https://github.com/firedrakeproject/firedrake.git
python3 -m venv venv-firedrake
. venv-firedrake/bin/activate
export $(python3 firedrake-configure --no-package-manager --show-env)
pip cache remove petsc4py
pip cache remove firedrake
pip install $PETSC_DIR/src/binding/petsc4py
export FCFLAGS="-w -fallow-argument-mismatch -O2"
export FFLAGS="-w -fallow-argument-mismatch -O2"
pip install -r ./firedrake/requirements-build.txt
pip install wheel
pip install --no-build-isolation --no-binary h5py h5py --editable './firedrake[check]'
```
- Update LD_LIBRARY_PATH
```
export LD_LIBRARY_PATH=$PETSC_DIR/arch-firedrake-default/lib:$LD_LIBRARY_PATH
```
- Check if installation was successful.
```
firedrake-check
```
- (!) Install additional packages such as vtk
```
pip install --no-binary h5py h5py 'firedrake[check,vtk]'
```