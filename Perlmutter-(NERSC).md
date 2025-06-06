*As of 06/06/2025. Contributed by Golo Wimmer (Los Alamos National Laboratory)*

- Get the firedrake config file
```
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/refs/tags/2025.4.0.post0/scripts/firedrake-configure
```
- Load appropriate modules
```
module load cmake
module load cray-python
```
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
- Install Firedrake: make a virtual environment, activate it, set environment variables, remove previous existing firedrake and petsc4py cache. Then before installing, make a pip constraints text file which is currently necessary for stable release version due to a petsc4py issue.
```
cd ..
python3 -m venv venv-firedrake
. venv-firedrake/bin/activate
export $(python3 firedrake-configure --no-package-manager --show-env)
pip cache remove petsc4py
pip cache remove firedrake
echo 'Cython<3.1' > constraints.txt
export PIP_CONSTRAINT=constraints.txt
pip install --no-binary h5py 'firedrake[check]'
```
- Update LD_LIBRARY_PATH to void errors along the line of `ImportError: libpetsc.so.3.23: cannot open shared object file: No such file or directory`
```
export LD_LIBRARY_PATH=$PETSC_DIR/arch-firedrake-default/lib:$LD_LIBRARY_PATH
```
- Check if installation was successful. Not that mpiexec is not available on perlmutter, and to run the parallel runs in firedrkae-check, a similar hack as in the guideline for Isambard 3 can be used.
```
firedrake-check
```

#### Guidelines for developer version ####
Changes to the above are marked by (!)

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
- (!): Install firedrake: clone firedrake repo, set up venv, run configuration. New steps: install pets4py; note that for most recent version of petsc, cython constraint is not needed. This will also install libsupermesh as a firedrake requirement, which will throw an argument mismatch error; need to add FC and FF flags to allow for the mismatch. Further, for the firedrake install command, there will be an error along the lines of `error: invalid command 'bdist_wheel'` because the wheel package is missing, and we therefore need to pip install it first. Finally, there will be an error along the lines of `ValueError: invalid pyproject.toml config: project.license.` for the h5py installation, which seems to be related to an invalid licence for stricter PEP 621 validation rules. The simplest way to resolve this seems to be to load an older version of h5py. The same issue may occur for firedrake too. The simplest way to resolve this seems to be to replace the line license = "LGPL-3.0-or-later" inside firedrake/pyproject.toml by license = { text = "LGPL-3.0-or-later" }
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
# Before running the next command, replace `license = "LGPL-3.0-or-later"` inside `firedrake/pyproject.toml` by `license = { text = "LGPL-3.0-or-later" }`
pip install --no-build-isolation --no-binary h5py 'h5py<3.14' --editable './firedrake[check]'
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
pip install --no-binary h5py 'h5py<3.14' 'firedrake[check,vtk]'
```