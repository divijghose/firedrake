This build process is valid as of January 2026 with firedrake `2025.10.2`

Some general points to note about the following scripts.
* You must install firedrake in the `/work/<project>/...` directory for it to be accessible from the compute nodes.
* The scripts assume that you have already copied the `firedrake-configure` script to your account. It has been tested with the version from Firedrake `2025.10.2`.
* In each script you will need to swap `<project>` and `<user>` for your project ID and username.

# PETSc installation

## PETSc build
The following script will build a Firedrake compatible PETSc using package versions available from the system modules.

Custom PETSc configurations can be built by modifying the arguments to `${PETSC_DIR}/configure`, e.g. adding `--with-64-bit-indices`.
For a complex Firedrake add `--with-scalar-type=complex`, and remove the `--with-hypre` arguments. As of January 2026 the `mumps/5.8.1` module doesn't link properly to a complex PETSc, so the `--with-mumps` arguments should also be removed in this case

```bash
#!/usr/bin/env bash
## Script to build PETSc for Firedrake on Archer2

set -e

# setup:
#  environment variables
#  firedrake configure script
#  environment modules
BUILD_DIR=/work/<project>/<project>/<user>/

export PETSC_DIR=${BUILD_DIR}/petsc
export PETSC_ARCH=arch-fd-default
FIREDRAKE_CONFIGURE=${BUILD_DIR}/firedrake-configure-2025.10.2

cd ${BUILD_DIR}

# Set up the build environment with system modules
module load PrgEnv-gnu/8.4.0
module load cray-python/3.10.10
module load cmake/3.29.4
module load cray-fftw/3.3.10.5
module load cray-hdf5-parallel/1.12.2.7
module load cray-libsci/23.09.1.1
module load cray-parallel-netcdf/1.12.3.7
module load hypre/2.33.0
module load metis/5.1.0
module load mumps/5.8.1
module load parmetis/4.0.3
module load scotch/7.0.10
module load superlu/7.0.1
module load superlu-dist/9.1.0
module list

# Clone PETSc if it does not already exist 
if [ ! -d petsc ] ; then
   git clone https://gitlab.com/petsc/petsc.git
fi

# Checkout firedrake-configure branch
cd petsc
git checkout $(python3 ${FIREDRAKE_CONFIGURE} --no-package-manager --show-petsc-version)

# Configure PETSc, using the default Firedrake configuration
# as a guide but picking up all externals from system modules
# (dropping suitsparse as unavailable)

OPTFLAGS='-O3 -march=native -mtune=native -fPIC'

./configure --PETSC_ARCH=${PETSC_ARCH} \
            --COPTFLAGS="${OPTFLAGS}" \
            --CXXOPTFLAGS="${OPTFLAGS}" \
            --FOPTFLAGS="${OPTFLAGS}" \
            --with-blaslapack=1 \
            --with-c2html=0 \
            --with-debugging=0 \
            --with-fortran-bindings=0 \
            --with-shared-libraries=1 \
            --with-strict-petscerrorcode \
            --with-fftw=1 \
            --with-fftw-include=${FFTW_INC} \
            --with-fftw-lib="-L${FFTW_DIR}" \
            --with-hdf5=1 \
            --with-hdf5-include=${HDF5_DIR}/include \
            --with-hdf5-lib="-L${HDF5_DIR}/include" \
            --with-hypre=1 \
            --with-hypre-include=${HYPRE_DIR}/include \
            --with-hypre-lib="-L${HYPRE_DIR}/lib"  \
            --with-make-np=8 \
            --with-make-test-np=8 \
            --with-make-load=8 \
            --with-metis=1 \
            --with-metis-include=${METIS_DIR}/include \
            --with-metis-lib="-L${METIS_DIR}/lib" \
            --with-mpiexec=srun \
            --with-mumps=1 \
            --with-mumps-include=${MUMPS_DIR}/include \
            --with-mumps-lib="-L${MUMPS_DIR}/lib -lcmumps_gnu_mpi -ldmumps_gnu_mpi -lmumps_common_gnu_mpi -lpord_gnu_mpi -lsmumps_gnu_mpi -lzmumps_gnu_mpi -lesmumps_gnu -lptesmumps_gnu_mpi" \
            --with-parmetis=1 \
            --with-parmetis-include=${PARMETIS_DIR}/include \
            --with-parmetis-lib="-L${PARMETIS_DIR}/lib" \
            --with-pnetcdf=1 \
            --with-pnetcdf-include=${PNETCDF_DIR}/include \
            --with-pnetcdf-lib="-L${PNETCDF_DIR}/lib" \
            --with-ptscotch=1 \
            --with-ptscotch-include=${SCOTCH_DIR}/include \
            --with-ptscotch-lib="-L${SCOTCH_DIR}/lib -lptscotcherr_gnu_mpi -lptscotch_gnu_mpi -lscotcherr_gnu -lscotch_gnu" \
            --with-scalapack=1 \
            --with-superlu=1 \
            --with-superlu-include=${SUPERLU_DIR}/include \
            --with-superlu-lib="-L${SUPERLU_DIR}/lib"  \
            --with-superlu_dist=1 \
            --with-superlu_dist-include=${SUPERLU_DIST_DIR}/include \
            --with-superlu_dist-lib="-L${SUPERLU_DIST_DIR}/lib" 

# Build PETSc
make all
```

## PETSc `make-check`
Now we check the installation by running PETSc's `make-check` tests on the compute nodes.
The following bash script can be submitted to slurm with `sbatch jobscript-petsc-make-check.sh`.
The slurm output will be written to a file called `slurm-petsc-check-%j.out` where `%j` is the job ID.

```bash
#!/bin/bash
#
#SBATCH --account=<project>
#SBATCH --partition=standard
#SBATCH --qos=short
#
#SBATCH --job-name=petsc-check
#SBATCH --output=slurm-%x-%j.out
#SBATCH --error=slurm-%x-%j.out
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#
#SBATCH --time=00:20:00
#
#SBATCH --distribution=block:block
#
#SBATCH --hint=nomultithread
#
#SBATCH --exclusive
#
#SBATCH --requeue

# exit on first error
set -e

module load PrgEnv-gnu/8.4.0

BUILD_DIR=/work/<project>/<project>/<user>
PETSC_DIR=${BUILD_DIR}/petsc
PETSC_ARCH=arch-fd-default

echo PETSC_DIR=${PETSC_DIR}
echo PETSC_ARCH=${PETSC_ARCH}

cd ${PETSC_DIR}
# avoid srun warning messages causing tests to fail on output diffs
MPIEXEC_TAIL="--quiet --slurmd-debug=quiet" make check
```

# Firedrake installation

## Firedrake build

```bash
#!/usr/bin/env bash

set -e

# setup:
#  environment modules
#  environment variables
#  firedrake configure script
BUILD_DIR=/work/<project>/<project>/<user>

FDVERSION=2025.10.2
FDVENV=fd-default

export PETSC_DIR=${BUILD_DIR}/petsc
export PETSC_ARCH=arch-${FDVENV}
PETSC4PY_DIR=${PETSC_DIR}/src/binding/petsc4py

FIREDRAKE_CONFIGURE=${BUILD_DIR}/firedrake-configure-${FDVERSION}

module load PrgEnv-gnu/8.4.0
module load cray-python/3.10.10
module load cray-hdf5-parallel/1.12.2.7
module load cmake/3.29.4
module load cray-libsci/23.09.1.1
module list

# # Change to the build directory
cd ${BUILD_DIR}

# # Create the firedrake venv
# We want to use system packages like mpi4py and numpy so that they
# are linked to the vendor libraries (e.g. MPI and BLAS/LAPACK)
python3 -m venv --system-site-packages ${FDVENV}

# # Activate the firedrake venv
. ${FDVENV}/bin/activate

# # Clean up pip environment
echo -e "\nClean up pip cache\n"
pip cache purge

# Need to add the petsc and mpich paths manually
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${PETSC_DIR}/${PETSC_ARCH}/lib/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CRAY_MPICH_DIR}/lib-abi-mpich

export CC=mpicc CXX=mpicxx

# Clone Firedrake
echo -e "\nClone Firedrake\n"
cd ${VIRTUAL_ENV}
git clone --depth 1 --branch ${FDVERSION} \
    https://github.com/firedrakeproject/firedrake.git \
    ${VIRTUAL_ENV}/src/firedrake

export HDF5_MPI=ON

echo -e "\nInstall Firedrake\n"
echo -e "Output will be written to build-firedrake.log\n"
unbuffer pip install --verbose \
    --no-binary h5py \
    --editable \
    "${VIRTUAL_ENV}/src/firedrake[check]" \
    | tee build-firedrake.log
```

## `firedrake-check`

Now we check the installation by running Firedrake's `firedrake-check` tests on the compute nodes.
The following bash script can be submitted to slurm with `sbatch jobscript-firedrake-check.sh`.
The slurm output will be written to a file called `slurm-firedrake-check-%j.out` where `%j` is the job ID.

```bash
#!/bin/bash
#
#SBATCH --account=<project>
#SBATCH --partition=standard
#SBATCH --qos=short
#
#SBATCH --job-name=firedrake-check
#SBATCH --output=slurm-%x-%j.out
#SBATCH --error=slurm-%x-%j.out
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=3
#
#SBATCH --time=00:20:00
#
#SBATCH --distribution=block:block
#
#SBATCH --hint=nomultithread
#
#SBATCH --exclusive
#
#SBATCH --requeue

# exit on first error
set -e

# setup firedrake environment

module load PrgEnv-gnu/8.4.0

BUILD_DIR=/work/<project>/<project>/<user>
FDVENV=fd-default

export PETSC_DIR=${BUILD_DIR}/petsc
export PETSC_ARCH=arch-${FDVENV}
VENV=${BUILD_DIR}/${FDVENV}

echo "PETSC_DIR=${PETSC_DIR}"
echo "PETSC_ARCH=${PETSC_ARCH}"
echo "VENV=${VENV}"
. ${VENV}/bin/activate

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${PETSC_DIR}/${PETSC_ARCH}/lib/

# Firedrake needs access to the MPI shared libraries
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CRAY_MPICH_DIR}/lib-abi-mpich

# Default value set to placate warning when firedrake imports
export OMP_NUM_THREADS=1

# set the cache directories. They must be in /work to be
# available from the compute nodes. Create them in the
# venv directory so different builds don't conflict.
if [ -z ${PYOP2_CACHE_DIR} ] ; then
   export PYOP2_CACHE_DIR=${VIRTUAL_ENV}/.cache/pyop2
fi

if [ -z ${FIREDRAKE_TSFC_KERNEL_CACHE_DIR} ] ; then
   export FIREDRAKE_TSFC_KERNEL_CACHE_DIR=${VIRTUAL_ENV}/.cache/tsfc
fi

if [ -z ${XDG_CACHE_HOME} ] ; then
   export XDG_CACHE_HOME=${VIRTUAL_ENV}/.cache/
fi

# run firedrake-check using slurm mpi executable
echo -e "\nfiredrake-check"
firedrake-check --mpiexec='srun -n'
```