# Firedrake on CX2.

CX2 is Imperial's SGI cluster. These are the instructions for building and running Firedrake on CX2.

## Building

```
module load gcc
module load mpi
module load git
export MPICC_CC=gcc
export MPICXX_CXX=g++
export MPIF08_F08='gfortran -I/apps/intel/2017/compilers_and_libraries_2017.0.098/linux/mpi/intel64/include/ilp64/gfortran/5.1.0'
export MPIF90_F90="$MPIF08_F08"
export PETSC_CONFIGURE_OPTIONS=--download-fblaslapack
export PATH=$HOME/.local/bin:$PATH
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
pip install virtualenv
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
python firedrake-install --no-package-manager
```

## Running
The following is a sample pbs script running the Helmholtz demo:
```
#!/bin/bash
# Job name
#PBS -N helmholtz_demo
# Time required in hh:mm:ss
#PBS -l walltime=00:02:00
# Resource requirements
#PBS -l select=1:ncpus=4:mpiprocs=4:ompthreads=1:mem=15999Mb
# Files to contain standard error and standard output
#PBS -o stdout
#PBS -e stderr
# Mail notification
#PBS -m ae
#PBS -M david.ham@imperial.ac.uk
  
echo Working Directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
rm -f stdout* stderr*

module load gcc
module load mpi
source $HOME/src/firedrake/bin/activate

# Start time
echo Start time is `date` > date
 
mpiexec python $VIRTUAL_ENV/src/firedrake/demos/helmholtz/helmholtz.py
 
# End time
echo End time is `date` >> date
```