The NextGen clustor has different specifications on the login and compute nodes, so it is best to build Firedrake on the compute nodes by submitting a job via a pbs script.

On NextGen, it is necessary to build and run Firedrake using the clustor or clustor2 filesystems to avoid quota issues. On the clustor filesystem, the path to your own user space is given by

/home/clustor/ma/a/abc12

upon replacing abc12 by your Imperial shortcode and a by the first letter of that shortcode. In these instructions we assume that you want to build in a directory called 
/home/clustor/ma/a/abc12/work

You will need to amend the scripts below to the appropriate name.

Currently, there is a problem with the standard build relating to hdf5 (used for CheckpointFile) on NextGen. The solution is to build your own Python and build Firedrake's PETSc using a different version of hdf5.

The steps are:

On the login node, to start building Python,

cd /home/clustor/ma/a/abc12/work
git clone https://github.com/python/cpython.git
git checkout 3.11

Then, submit the following pbs script (appropriately edited)

#!/bin/bash
#PBS -N build_p
#PBS -m be
#PBS -q standard
cd /home/clustor/ma/a/abc12/work/cpython
export XDG_CACHE_HOME=/home/clustor/ma/a/abc12/work
./configure --enable-loadable-sqlite-extensions --prefix /home/clustor/ma/a/abc12/work
make
make install

If this was successful, on the login node, to start building Firedrake,

cd /home/clustor/ma/a/abc12/work
curl -O https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-1.12.2/src/hdf5-1.12.2.tar.bz2
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install

Then, submit the following pbs script (appropriately edited). The "medium" queue is required because building petsc4py requires more memory than available on the "standard" queue.

#!/bin/bash
#PBS -N build_fd
#PBS -m be
#PBS -q medium
cd /home/clustor/ma/a/abc12/work
export XDG_CACHE_HOME=/home/clustor/ma/a/abc12/work
export PETSC_CONFIGURE_OPTIONS="--download-hdf5=/home/clustor/ma/a/abc12/work/hdf5-1.12.2.tar.bz2"
/home/clustor/ma/a/abc12/cpython/python firedrake-install --disable-ssh --no-package-manager &> /home/clustor/ma/a/abc12/work/fdbuild.out

