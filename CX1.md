# Firedrake on CX1.

CX1 is Imperial's entry-level HPC cluster. These are the instructions for building and running Firedrake on CX1.

## Building

```
module load anaconda3/personal
module load bison
module load flex
module load cmake/3.7.0
module load gcc/9.3.0
module load mpi
export PETSC_CONFIGURE_OPTIONS=--download-fblaslapack
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
python firedrake-install --no-package-manager
```
At the moment, although the build script finishes successfully, firedrake fails to import after activating the environment because it cannot import vtk. This is because the binary wheel for vtk installed by pip is linked against a much newer version of libc than what is available on cx1. You therefore have to rebuild this package locally (see section below).
Note that further modules may also be required, see Troubleshooting below.

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

module load gcc/9.3.0
module load mpi

# Change the next line to wherever you put your firedrake/ installation
source $HOME/firedrake/bin/activate

# Start time
echo Start time is `date` > date

mpiexec python $VIRTUAL_ENV/src/firedrake/demos/helmholtz/helmholtz.py
 
# End time
echo End time is `date` >> date
```

## Rebuilding VTK
After build script finishes, activate the environment
```
source firedrake/bin/activate
```
try to import vtk using
```
python -c "import vtk"
```
At the moment this fails complaining about the GLIBC version. To fix this rebuild vtk using the following steps. Ensure that you still have the same modules loaded as recommended above for building firedrake
```
# checkout the vtk source and the right version tag
git clone https://gitlab.kitware.com/vtk/vtk.git
cd vtk
git checkout tags/v9.0.1 -b v9.0.1
# install some build dependencies (easiest to just install in the new firedrake environment)
pip install scikit-build
pip install ninja
# make a directory to build in
mkdir build
cd build
# and configure and build (this may take more than 5 hours!)
cmake -GNinja -DVTK_WHEEL_BUILD=ON -DVTK_PYTHON_VERSION=3 -DVTK_WRAP_PYTHON=ON ../
ninja
python setup.py bdist_wheel
```
The last step should have created a .whl python binary package in dist/, which you can install with (make sure the firedrake environment is activated!):
```
pip install --upgrade dist/vtk-9.0.1-cp39-cp39-linux_x86_64.whl
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

* If you get an error `[Errno 13] Permission denied.` by `shutil.copytree` you can run `module load fix_setxattr` and run the installation again.