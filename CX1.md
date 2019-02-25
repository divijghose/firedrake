# Firedrake on CX1.

CX1 is Imperial's entry-level HPC cluster. These are the instructions for building and running Firedrake on CX1.

## Building

```
module load anaconda3
module load gcc
module load mpi
export I_MPI_CC=gcc
export I_MPI_CXX=g++
export I_MPI_F90='gfortran -I/apps/intel/2017/compilers_and_libraries_2017.0.098/linux/mpi/intel64/include/ilp64/gfortran/5.1.0'
export I_MPI_FC="$I_MPI_F90"
export I_MPI_F77="$I_MPI_F90"
export PETSC_CONFIGURE_OPTIONS=--download-fblaslapack
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
python firedrake-install --no-package-manager
ln -s /apps/anaconda3/4.1.1/lib/libpython3.5m.so.1.0 firedrake/lib/
```

## Running
The following is a sample pbs script running the Helmholtz demo. Don't forget to run make in the `firedrake/src/firedrake/demos` directory before submitting. Note, that we don't load the anaconda3 module as it puts libraries in our path that conflict with our firedrake build.
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

# Change the next line to wherever you put your firedrake/
source $HOME/src/firedrake/bin/activate

# Start time
echo Start time is `date` > date

mpiexec python $VIRTUAL_ENV/src/firedrake/demos/helmholtz/helmholtz.py
 
# End time
echo End time is `date` >> date
```

## Troubleshooting
* An unsuccessful installation may be due to the default modules on cx1. E.g. to resolve an error of form 

```
-- Configuring incomplete, errors occurred!CMake Error at CMakeLists.txt:16                                                                                         (CMAKE_MINIMUM_REQUIRED):
      CMake 3.1 or higher is required.  You are running version 2.8.12.2
```

add `module load cmake/3.1.3` to the modules to be loaded when building firedrake.


* If an error of type

```PETSC ERROR: Caught signal number 4 Illegal instruction: Likely due to memory corruption```

occurs, this can be resolved by activating the virtual environment and running `firedrake-clean`.