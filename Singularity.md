Process for running Firedrake scripts on ARCHER2 using a singularity container, rather than installing Firedrake

## Convert the Docker container

A two step procedure is required for performing the image conversion. This example uses the `firedrake-vanilla` container, but `firedrake`, `firedrake-notebooks` and `firedrake-complex` should also work correctly.

1. Build the image in a sandbox from the Dockerhub
`singularity build --sandbox ./firedrake-vanilla docker://firedrakeproject/firedrake-vanilla`

2. Convert the sandboxed image to a Singularity container
`singularity build firedrake-vanilla.sif ./firedrake-vanilla`

## Running

Example jobscript for running on ARCHER2:

```bash
#!/bin/bash
#SBATCH -p standard
#SBATCH -A account
#SBATCH -J singularity
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --qos=standard
#SBATCH -t 0:10:00

myScript="HPC_demo.py"

module purge
module load load-epcc-module

module load PrgEnv-gnu/8.1.0
module swap gcc gcc/10.2.0

module swap cray-mpich cray-mpich-abi/8.1.9
module swap cray-dsmml cray-dsmml/0.2.1
module swap cray-libsci cray-libsci/21.08.1.2
module load xpmem

cat <<EOF >.gitconfig
[safe]
	directory = *
EOF

export SINGULARITYENV_LD_LIBRARY_PATH=/opt/cray/pe/mpich/8.1.9/ofi/gnu/9.1/lib-abi-mpich:/opt/cray/pe/pmi/6.0.10/lib:/opt/cray/libfabric/1.11.0.4.71/lib64:/usr/lib64/host:/usr/lib/x86_64-linux-gnu/libibverbs:/.singularity.d/libs:/opt/cray/pe/gcc-libs
export SINGULARITY_BIND="/opt/cray,/usr/lib64/libibverbs.so.1,/usr/lib64/librdmacm.so.1,/usr/lib64/libnl-3.so.200,/usr/lib64/libnl-route-3.so.200,/usr/lib64/libpals.so.0,/var/spool/slurmd/mpi_cray_shasta,/usr/lib64/libibverbs/libmlx5-rdmav25.so,/etc/libibverbs.d,/opt/gcc"

export SINGULARITYENV_OMP_NUM_THREADS=1
export SINGULARITYENV_PYOP2_CACHE_DIR=/tmp/$USER/pyop2
export SINGULARITYENV_PYOP2_CC=/home/firedrake/firedrake/bin/mpicc
export SINGULARITYENV_PYOP2_CXX=/home/firedrake/firedrake/bin/mpicxx
export SINGULARITYENV_FIREDRAKE_TSFC_KERNEL_CACHE_DIR=/tmp/$USER/tsfc

srun --ntasks-per-node 128  \
    singularity run --bind $PWD:/home/firedrake/work --home $PWD firedrake-vanilla.sif \
        /home/firedrake/firedrake/bin/python \
            /home/firedrake/work/${myScript}
```

If you save this jobscript as `firedrake_jobscript.slm` it can be submitted to the queue by executing
```bash
sbatch firedrake_jobscript.slm
```
on the login node.

Key points to note:
- We assume the script referenced bt the bash variable `myScript` is in the current directory and that directory is somewhere in the ARCHER2 `/work` filesystem _not_ the `/home` filesystem.
- We use `cray-mpich-abi` in place of `cray-mpich`.
- A `.gitconfig` file is created marking all directories as safe for git. This is necessary since the Docker container runs as the `firedrake` user, but Singularity runs as the current user. Without it each rank spews many errors, sometimes crashing the interconnect. Since the `$PWD` is mounted as home the Singularity container sees this file as `$HOME/.gitconfig`.
- `export SINGULARITYENV_LD_LIBRARY_PATH` and `export SINGULARITY_BIND` are ARCHER2 specific and essential.
- A `SINGULARITYENV_FOO` environment variable sets the environment variable `FOO` instide the singularity container.
- `PYOP2_CACHE_DIR` and `FIREDRAKE_TSFC_KERNEL_CACHE_DIR` deafult to the `$HOME` directory on the **host** and is automatically mounted inside the singularity container. This is an issue on ARCHER2, since `$HOME` is not mounted on compute nodes. To ensure the location is writable these are set to directories in `/tmp`. Any writable alternative location could be used (for instance `$PWD`).
- `PYOP2_CC` and `PYOP2_CXX` are set to ensure the container compiler are used.
- The argument `--bind $PWD:/home/firedrake/work` is necessary to mount the current directory somewhere sensible within the container so that the script on the host filesystem can be executed in the container.
- The argument `--home $PWD` ensures that any files written to `$HOME` in the container are written to the current directory. USeful when output files are written to a relative path rather than absolute, since the default user directory inside the container is normally `$HOME`.
