[LIKWID](https://github.com/RRZE-HPC/likwid) is a great tool for analysing low-level
performance. It works by collecting the information provided by counters in the CPU
and presenting them to the user as a number of more easily understood metrics.

LIKWID presents the user with a [number of different executables](https://github.com/RRZE-HPC/likwid/wiki),
the most important for us being:

* `likwid-bench` - A benchmarking tool to determine platform-specific metrics such as
                   peak floating-point throughput and memory bandwidth.

* `likwid-perfctr` - A tool that measures hardware performance counters.

## Installing

To install LIKWID follow the instructions [here](https://github.com/RRZE-HPC/likwid#download-build-and-install).
You will also need to install [LIKWID's Python bindings](https://github.com/RRZE-HPC/pylikwid).

## Benchmarking your system

To get an idea of how fast your kernel actually is, it is essential that you
benchmark your system in advance. Some useful metrics you can gather are:

* Peak throughput (single-threaded)

  ```bash
  $ likwid-bench -W S0:2GB:1 -t peakflops
  ```

  Peak vectorised throughput can also be tested with `peakflops_avx` (and similar).

* Peak streaming memory bandwidth (single-threaded)

  ```bash
  $ likwid-bench -W S0:2GB:1 -t load
  ```

  You can also experiment with the bandwidth of different cache levels by varying
  the amount of data being transferred (e.g. `-W S0:2GB:1` -> `-W S0:20MB:1`).

  Note that there are other tests that can be run to determine memory bandwidth
  (e.g. `-t stream`) and these may produce different results depending on the
  number of loads and stores.

Alongside these benchmarks, `likwid-topology` can also give you some insight into how your CPU is laid out.

## Profiling the kernels

To profile the kernels you need to:

*TODO: need to know correct incantations*

1. Initialise LIKWID in your script.

2. Annotate the kernel with LIKWID's [marker API](https://github.com/RRZE-HPC/likwid/wiki/LikwidAPI-and-MarkerAPI#markerapi).
   This ensures that we are not accidentally profiling anything that we don't
   care about. To do this either apply the following diff:

   ```

   ```

   or use the PyOP2 branch `with-likwid-markers`.

3. Run `likwid-perfctr` with the performance group of interest. For example,
   a good starting point is to run:

   ```bash
   $ likwid-perfctr -C S0:1 -g MEM_DP -- python myscript.py
   ```

## Further information

Here are some additional resources you may find useful:

* [LIKWID tutorial on the roofline model](https://github.com/RRZE-HPC/likwid/wiki/Tutorial%3A-Empirical-Roofline-Model)