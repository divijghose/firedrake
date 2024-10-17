These are preliminary notes for how to install Firedrake on Isambard AI. This is based on a short period of early access in October 2024 and the installation was not thoroughly tested.

# JBTODO: These are currently my notes, needs tidying

## Modules and environment
```bash
module load PrgEnv-gnu
module load cray-mpich
module load cray-python
unset PYTHONPATH

module load cray-libsci
module load cray-hdf5-parallel
module load cray-netcdf-hdf5parallel
module load cray-parallel-netcdf

module load xpmem

# Set preferred executables
CC=/opt/cray/pe/craype/2.7.30/bin/cc
CXX=/opt/cray/pe/craype/2.7.30/bin/CC
FORT=/opt/cray/pe/craype/2.7.30/bin/ftn
PYTHON=/opt/cray/pe/python/3.11.5/bin/python
```

## Install PETSc
```bash
# Setup installation variables
BASE_INSTALL_DIR=$PWD
MAKE_NP=32 # Use up to 32 cores when building

# Clone Firedrake fork of repositories
git clone https://github.com/firedrakeproject/petsc.git

# Issues:
# + mpi-dir on IsambardAI has the mpi{cc,cxx,ftn} wrappers linked to an ancient GCC
# + PASTIX won't build
cd $BASE_INSTALL_DIR/petsc
$PYTHON ./configure \
    --with-cc=$CC \
    --with-cxx=$CXX \
    --with-fc=$FORT \
    --with-python-exec=$PYTHON \
    --COPTFLAGS=-O3 -mcpu=neoverse-v2 \
    --CXXOPTFLAGS=-O3 -mcpu=neoverse-v2 \
    --FOPTFLAGS=-O3 -mcpu=neoverse-v2 \
    --with-c2html=0 \
    --with-debugging=0 \
    --with-fortran-bindings=0 \
    --with-make-np=$MAKE_NP \
    --with-shared-libraries=1 \
    --with-zlib \
    --with-blaslapack-include=$CRAY_PE_LIBSCI_PREFIX_DIR/include \
    --with-blaslapack-lib=$CRAY_PE_LIBSCI_PREFIX_DIR/lib/libsci_gnu.so \
    --with-hdf5-dir=$HDF5_DIR \
    --with-hdf5-dir=$HDF5_DIR \
    --with-netcdf-dir=$NETCDF_DIR \
    --with-pnetcdf-dir=$PNETCDF_DIR \
    --download-cmake \
    --download-hwloc \
    --download-hypre \
    --download-metis \
    --download-mumps \
    --download-ptscotch \
    --download-scalapack \
    --download-suitesparse \
    --download-superlu_dist \
    PETSC_ARCH=real

make PETSC_DIR=$BASE_INSTALL_DIR/petsc PETSC_ARCH=real all
```

### Test installed PETSc
```
# Optional, but recommended: check
srun --time=00:05:00 --pty /bin/bash --login
module load PrgEnv-gnu
module load cray-mpich
module load cray-python
unset PYTHONPATH

module load cray-libsci
module load cray-hdf5-parallel
module load cray-netcdf-hdf5parallel
module load cray-parallel-netcdf

module load xpmem

# Set preferred executables
CC=/opt/cray/pe/craype/2.7.30/bin/cc
CXX=/opt/cray/pe/craype/2.7.30/bin/CC
FORT=/opt/cray/pe/craype/2.7.30/bin/ftn
PYTHON=/opt/cray/pe/python/3.11.5/bin/python

# Doesn't work!
make test

cd src/snes/tutorials
make ex19
./ex19
srun --overlap -n 2 ./ex19

exit
```

## Install Firedrake
```bash
export PETSC_DIR=$BASE_INSTALL_DIR/petsc
export PETSC_ARCH=real

cd ..
# Fetch and install Firedrake
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install

$PYTHON firedrake-install \
    --no-package-manager \
    --honour-petsc-dir \
    --mpicc=$CC \
    --mpicxx=$CXX \
    --mpif90=$FORT \
    --mpiexec=srun \
    --no-vtk \
    --venv-name=firedrake-real

# libsupermesh
cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=$HOME/firedrake-real \
    -DMPI_C_COMPILER=$CC \
    -DMPI_CXX_COMPILER=$CXX \
    -DMPI_Fortran_COMPILER=$FORT \
    -DCMAKE_Fortran_COMPILER=$FORT \
    -DMPIEXEC_EXECUTABLE=srun \
    -DCMAKE_Fortran_FLAGS=-fallow-argument-mismatch

firedrake-update
```
### Test installed Firedrake
```bash
# Optional, but recommended: check
srun --time=00:15:00 --pty /bin/bash --login
module load PrgEnv-gnu
module load cray-mpich
module load cray-python
unset PYTHONPATH

module load cray-libsci
module load cray-hdf5-parallel
module load cray-netcdf-hdf5parallel
module load cray-parallel-netcdf

module load xpmem

# Set preferred executables
CC=/opt/cray/pe/craype/2.7.30/bin/cc
CXX=/opt/cray/pe/craype/2.7.30/bin/CC
FORT=/opt/cray/pe/craype/2.7.30/bin/ftn
PYTHON=/opt/cray/pe/python/3.11.5/bin/python

export PETSC_DIR=$HOME/petsc
export PETSC_ARCH=real

. $HOME/firedrake-real/bin/activate

cd $VIRTUAL_ENV/src/firedrake
pytest -v tests/regression/ -m "not parallel" -k "poisson_strong or stokes_mini or dg_advection"
# Doesn't work:
srun --overlap -n 3 pytest -v tests/regression/ -m "parallel[3]" -k "poisson_strong or stokes_mini or dg_advection"

cd $VIRTUAL_ENV/src/firedrake/demos
make
cd helmholtz

# Need to remove the line that creates a VTKFile
python helmholtz.py
srun --overlap -n 2 python helmholtz.py
srun --overlap -n 4 python helmholtz.py


exit
```