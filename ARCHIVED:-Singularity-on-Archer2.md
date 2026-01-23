# **THIS PAGE IS ARCHIVED AND IS KEPT ONLY FOR FUTURE REFERENCE**

This page assumes that you already have a singularity container with Firedrake called `firedrake.sif`, and you now want to run it on Archer2.
See the [Singularity](https://github.com/firedrakeproject/firedrake/wiki/singularity) page for how to build a Firedrake container

### Environment setup
These commands must be run before launching the container (either in job script or from interactive session).
If the container is failing with link errors then check to see if the LD_LIBRARY_PATH or BIND variables need updating here: [https://docs.archer2.ac.uk/user-guide/containers/#running-parallel-mpi-jobs-using-singularity-containers](https://docs.archer2.ac.uk/user-guide/containers/#running-parallel-mpi-jobs-using-singularity-containers)
```
module purge
module load load-epcc-module

module load PrgEnv-gnu

module swap cray-mpich cray-mpich-abi
module load cray-dsmml
module load cray-libsci
module load xpmem

module list                                                                                                                                 

cat <<EOF >.gitconfig
[safe]
   directory = *
EOF

# Set the LD_LIBRARY_PATH environment variable within the Singularity container
# to ensure that it used the correct MPI libraries.
export SINGULARITYENV_LD_LIBRARY_PATH="/opt/cray/pe/mpich/8.1.23/ofi/gnu/9.1/lib-abi-mpich:/opt/cray/pe/mpich/8.1.23/gtl/lib:/opt/cray/libfabric/1.12.1.2.2.0.0/lib64:/opt/cray/pe/gcc-libs:/opt/cray/pe/gcc-libs:/opt/cray/pe/lib64:/opt/cray/pe/lib64:/opt/cray/xpmem/default/lib64:/usr/lib64/libibverbs:/usr/lib64:/usr/lib64"

# This makes sure HPE Cray Slingshot interconnect libraries are available
# from inside the container.
export SINGULARITY_BIND="/opt/cray,/var/spool,/opt/cray/pe/mpich/8.1.23/ofi/gnu/9.1/lib-abi-mpich:/opt/cray/pe/mpich/8.1.23/gtl/lib,/etc/host.conf,/etc/libibverbs.d/mlx5.driver,/etc/libnl/classid,/etc/resolv.conf,/opt/cray/libfabric/1.12.1.2.2.0.0/lib64/libfabric.so.1,/opt/cray/pe/gcc-libs/libatomic.so.1,/opt/cray/pe/gcc-libs/libgcc_s.so.1,/opt/cray/pe/gcc-libs/libgfortran.so.5,/opt/cray/pe/gcc-libs/ libquadmath.so.0,/opt/cray/pe/lib64/libpals.so.0,/opt/cray/pe/lib64/libpmi2.so.0,/opt/cray/pe/lib64/libpmi.so.0,/opt/cray/xpmem/default/lib64/libxpmem.so.0,/run/munge/munge.socket.2,/usr/lib64/libibverbs/libmlx5-rdmav34.so,/usr/lib64/libibverbs.so.1,/usr/lib64/libkeyutils.so.1,/usr/lib64/liblnetconfig.so.4,/usr/lib64/liblustreapi.so,/usr/lib64/libmunge.so.2,/usr/lib64/libnl-3.so.200,/usr/lib64/libnl-genl-3.so.200,/usr/lib64/libnl-route-3.so.200,/usr/lib64/librdmacm.so.1,/usr/lib64/libyaml-0.so.2"

# set environment variables inside the Singularity container for firedrake et al.

# Don't multithread
export SINGULARITYENV_OMP_NUM_THREADS=1

# Use the mpi compilers from the firedrake container
export SINGULARITYENV_PYOP2_CC=/home/firedrake/firedrake/bin/mpicc
export SINGULARITYENV_PYOP2_CXX=/home/firedrake/firedrake/bin/mpicxx

# Save caches locally so they persist across `singularity run` calls
export SINGULARITYENV_PYOP2_CACHE_DIR=/home/firedrake/work/.cache/pyop2_cache
export SINGULARITYENV_FIREDRAKE_TSFC_KERNEL_CACHE_DIR=/home/firedrake/work/.cache/tsfc
```
`PYOP2_CACHE_DIR` and `FIREDRAKE_TSFC_KERNEL_CACHE_DIR` default to the `$HOME` directory on the host and is automatically mounted inside the singularity container. This is an issue on Archer2, since `$HOME` is not mounted on compute nodes. Instead we create the caches in the directory that the container is run from, assuming that `--bind $PWD:/home/firedrake/work` was passed to `singularity run`. Saving the caches here also means that they persist between container invocations, so we don't end up compiling all the kernels at every container invocation.

### Testing Firedrake
Run the reduced set of tests from the documentation page from an interactive session.
1. Launch a single-core interactive job (we currently can't run the parallel tests on Archer2 because the cray-mpich won't allow nested calls to `MPI_Init`).
The Archer2 documentation shows two methods for launching interactive jobs. Use the first method using `salloc` (https://docs.archer2.ac.uk/user-guide/scheduler/#using-salloc-to-reserve-resources).
```
salloc --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --exclusive \
    --time=00:20:00 --partition=standard --qos=short --account=<account number>
```
NB: As of May 2023, when trying to run a container from an interactive job launched using the second method using `srun` (https://docs.archer2.ac.uk/user-guide/scheduler/#using-srun-directly) SLURM was failing to reallocate the resources from the interactive job to the `srun <options> singularity <options>` call so didn't actually run anything.

2. Run the commands above to setup the modules and environment ready for the Singularity container.

3. Check that firedrake is available inside the container:
```
srun --oversubscribe --hint=nomultithread --distribution=block:block --ntasks=1 \
    singularity run --bind $PWD:/home/firedrake/work --home $PWD firedrake.sif \
        /home/firedrake/firedrake/bin/python \
            -c "from firedrake import *"
```

4. Run the smoke-tests:
```
srun --oversubscribe --hint=nomultithread --distribution=block:block --ntasks=1 \
    singularity run --bind $PWD:/home/firedrake/work --home $PWD firedrake.sif \
        /home/firedrake/firedrake/bin/python \
            -m pytest /home/firedrake/firedrake/src/firedrake/tests/regression/ -v \
            -o cache_dir=/home/firedrake/work/.cache \
            -k "not parallel and (poisson_strong or stokes_mini or dg_advection)"
```
5. Hope everything has worked.


### Running Firedrake in an interactive job.
Run Firedrake in parallel from an interactive job.

1. Launch an interactive job (enter the required `nodes` and `ntasks-per-node` arguments):
```
salloc --nodes=${nnodes} --ntasks-per-node=${ntasks} --cpus-per-task=1 --exclusive \
    --time=00:20:00 --partition=standard --qos=short --account=<account number>
```

2. Run the commands above to setup the modules and environment ready for the Singularity container.

3. Navigate to the directory where you want to run.

4. Run your script (`$SIFDIR` is an environment variable for the directory that contains the Singularity image):
```
srun --oversubscribe --hint=nomultithread --distribution=block:block \
     --nodes=${nnodes} --ntasks-per-node=${ntasks} \
        singularity run --bind $PWD:/home/firedrake/work --home $PWD $SIFDIR/firedrake.sif \
            /home/firedrake/firedrake/bin/python \
                myscript.py --my_args
```
5. Hope everything has worked.
