# Firedrake on CX2.

CX2 is Imperial's SGI cluster. These are the instructions for building and running Firedrake on CX2.

## Building

```
module load gcc
module load mpi
export MPICC_CC=gcc
export MPICXX_CXX=g++
export MPIF08_F08=gfortran
export MPIF90_F90=gfortran
export PETSC_CONFIGURE_OPTIONS=--download-fblaslapack
export PATH=$HOME/.local/bin:$PATH
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
pip install virtualenv
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
firedrake-install --no-package-manager
```