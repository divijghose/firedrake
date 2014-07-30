# Firedrake on Archer

Add the following to your `.pbs` file to load the Firedrake environment:
```
module swap PrgEnv-cray PrgEnv-gnu
module swap python anaconda
module add firedrake 
```

# PETSc

## Running the stream benchmark

As the `fdrake` user, start an interactive backend session:
```
qsub -IVl select=1,walltime=0:20:00 -A y07
```
and execute the following:
```
module load fdrake-build-env
cd $PETSC_DIR
make streams NPMAX=24 MPIEXEC=aprun
```

# Troubleshooting

Problem:
```
pkg-config error:
Package sci_mpi_mp was not found in the pkg-config search path.
```
Solution:
```
export PKG_CONFIG_PATH=/opt/cray/libsci/12.2.0/GNU/48/sandybridge/lib/pkgconfig:$PKG_CONFIG_PATH
```