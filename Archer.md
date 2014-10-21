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

### Results

![PETSc stream scaling](images/scaling.png)

```
STREAM Triad numbers (compiled with gcc 4.9.1 cc -O2 -fPIC)
# nprocs MB/s
1 15218.5798
2 26044.8373
3 32489.4984
4 34929.4147
5 36030.9600
6 36560.5192
7 36858.5365
8 37011.9665
9 37076.0461
10 37128.6869
11 37185.4419
12 37259.8940
13 40288.8719
14 43310.2500
15 46454.4082
16 49586.8287
17 52627.4048
18 55711.5052
19 58812.1194
20 61829.0734
21 64976.4766
22 68109.9680
23 71058.1668
24 74103.9701
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