These are preliminary notes for how to install Firedrake on Isambard AI. This is based on a short period of early access in October 2024 and the installation was not thoroughly tested. PETSc and Firedrake were installed directly in the user's home directory.

## Modules and environment
This guide uses the following system modules and environment variables:
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

For reference at the time that these notes were written, these commands load the following modules:
```
> module list
Currently Loaded Modules:
  1) brics/userenv/2.4   5) craype-arm-grace     9) cray-mpich/8.1.28            13) cray-netcdf-hdf5parallel/4.9.0.9
  2) brics/default/1.0   6) libfabric/1.15.2.0  10) cray-python/3.11.5           14) cray-parallel-netcdf/1.12.3.9
  3) gcc-native/12.3     7) craype-network-ofi  11) cray-libsci/23.12.5          15) xpmem/2.8.2-1.0_3.7__g84a27a5.shasta
  4) craype/2.7.30       8) PrgEnv-gnu/8.5.0    12) cray-hdf5-parallel/1.12.2.9
```

## Install PETSc
For more rapid debugging of installation dependencies this guide uses a separate PETSc installation. We clone the Firedrake fork of the PETSc repo and install in the ususal manner. The following difficulties were encountered:
- The `--with-mpi-dir` PETSc configure option couldn't be used with on IsambardAI since the Cray MPICH has the `mpi{cc,cxx,ftn}` wrappers linked to an ancient GCC. Instead we specify the `--with-{cc,cxx,fc}` options.
- PASTIX won't build, so we don't install it!
```bash
# Setup installation variables
BASE_INSTALL_DIR=$HOME
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
This is not a requirement to complete the installation, but thoroughly recommended!
The code snippet below starts an interactive session and tries running some of the exercises.
Note that `make check` won't work correctly by itself, this isn't documented on Isambard AI docs, but the `--overlap --oversubscribe` flags must be passed to `srun` for anything to work.
```
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

make MPIEXEC_TAIL="--overlap --oversubscribe" check

exit
```
Currently seeing errors from Hypre that look like:
```
xpmem_attach error: : Invalid argument
```
but the residual looks okay.

More concerning, there are errors from HDF5:
```
>   0 ADIOI_CRAY_Calc_aggregator_pfl() ../../../../src/mpi/romio/adio/ad_cray/ad_cray_aggregate.c +77 should not get here : num_comp=1 off=-7926205430001303552
>   0 ADIOI_CRAY_Calc_aggregator_pfl() comps[0]= 1*-7926205430001303552 0--1
> MPICH ERROR [Rank 0] [job id 25331.10] [Fri Oct 18 10:42:04 2024] [nid001001] - Abort(86) (rank 0 in comm 0): application called MPI_Abort(MPI_COMM_WORLD, 86) - process 0
> 
> HDF5: infinite loop closing library
>       L,G_top,S_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top,T_top
```

## Install Firedrake
Once PETSc is installed, Firedrake can be installed honouring the PETSc directory.
It is not possible to install with VTK support as Kitware do not currently release wheels for Linux on ARM.
Frustratingly, this build will probably fail to build `libsupermesh` as the system CMake is incapable of detecting the correct flags to pass to the build process!
This would be fixed by addressing [#3806](https://github.com/firedrakeproject/firedrake/issues/3806)
```bash
export PETSC_DIR=$HOME/petsc
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
```
The above will fail, then we must manually install `libsupermesh`:
```bash
. $HOME/firedrake-real/bin/activate
cd $VIRTUAL_ENV/src/libsupermesh/build

$HOME/petsc/firedrake-real/bin/cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=$HOME/firedrake-real \
    -DMPI_C_COMPILER=$CC \
    -DMPI_CXX_COMPILER=$CXX \
    -DMPI_Fortran_COMPILER=$FORT \
    -DCMAKE_Fortran_COMPILER=$FORT \
    -DMPIEXEC_EXECUTABLE=srun \
    -DCMAKE_Fortran_FLAGS=-fallow-argument-mismatch
make
make install

firedrake-update
```

### Test installed Firedrake
This is not a requirement to complete the installation, but thoroughly recommended!
The code snippet below starts an interactive session and tries running some serial tests and one of the demos.
The Firedrake test suite won't run due to longstanding issues using system MPI distributions that are not vanilla MPICH.
```bash
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

cd $VIRTUAL_ENV/src/firedrake/demos
make
cd helmholtz

# Need to remove the line that creates a VTKFile
python helmholtz.py
srun --overlap -n 2 python helmholtz.py
srun --overlap -n 4 python helmholtz.py

exit
```

The command:
```bash
srun --overlap --oversubscribe -n 3 pytest -v tests/regression/ -m "parallel[3]" -k "poisson_strong or stokes_mini or dg_advection"
```
should run but does not.
This requires further investigation.