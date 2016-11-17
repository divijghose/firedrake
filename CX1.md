# Firedrake on CX2.

CX1 is Imperial's entry-level HPC cluster. These are the instructions for building and running Firedrake on CX1.

## Building

```
module load gcc
module load mpi
export I_MPI_CC=gcc
export I_MPI_F77=gfortran
export I_MPI_CXX=g++
export I_MPI_F90=gfortran
export I_MPI_FC=gfortran
export PETSC_CONFIGURE_OPTIONS=--download-fblaslapack
module load python/2.7.11
python firedrake-install --no-package-manager --honour-pythonpath
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
export I_MPI_CC=gcc
export I_MPI_CXX=g++

module load python/2.7.11
# Change the next line to wherever you put your Firedrake/
source $HOME/src/firedrake_cx1/bin/activate

# Start time
echo Start time is `date` > date
 
mpiexec python $VIRTUALENV/src/firedrake/demos/helmholtz/helmholtz.py
 
# End time
echo End time is `date` >> date
```