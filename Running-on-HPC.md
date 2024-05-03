# Running on HPC

The recommended installation on HPC is to use the Spack package manager.

You should familiarise yourself with as much of Spack's functionality as possible. To achieve the same flexibility as we have on desktop installs the Firedrake Spack install leverages a lot of Spack's features. More information about Spack can be found on their [website](https://spack.readthedocs.io/en/latest/index.html).

## Spack guides for specific machines:
- [ARCHER2](./archer2)
- [Isambard](./isambard)
- [Generic instructions](./Generic-Instructions-for-HPC)

## Container installs

For platforms where Apptainer/Singularity is installed it is possible to convert the Firedrake Docker image for use with the `singularity` program. Details of this procedure are on the [Apptainer/Singularity page](./singularity).

## Other systems

[NextGen cluster](./Building-on-the-NextGen-cluster-(Department-of-Mathematics,-Imperial-College-London))