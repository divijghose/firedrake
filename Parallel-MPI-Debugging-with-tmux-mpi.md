Having trouble with something not working in firedrake in parallel and want to debug?

`tmux-mpi` (available [here](https://github.com/wrs20/tmux-mpi)) is a really handy tool that lets you launch a `tmux` session for a chosen number of MPI ranks - you get a `tmux` terminal "window" for each MPI rank which tracks the process running on that rank.
This is super useful for debugging.

This wiki note assumes you are aware of `tmux`: it's a handy tool for creating terminal sessions with tabs and windows entirely within a terminal window (the `tmux` "windows" are not actual windows - they're all accessed within a single terminal. It's really cool!).
`tmux` sessions can be detached from and reattached to, e.g for running processes on a remote computer where you don't want to maintain an SSH session.
For more see the [tmux documentation](https://github.com/tmux/tmux/wiki).

From here it is assumed you have installed `tmux-mpi` and checked it works.

We will consider a simple python script called `test.py`

```python
import sys
import petsc4py
petsc4py.init(sys.argv)
from petsc4py import PETSc
if PETSc.COMM_WORLD.rank == 0:
    PETSc.Vec().create(comm=PETSc.COMM_SELF).view()
```

If you try to run this you will get an error:

```
$ python test.py
Vec Object: 1 MPI processes
  type not yet set
[0]PETSC ERROR: ------------------------------------------------------------------------
[0]PETSC ERROR: Caught signal number 11 SEGV: Segmentation Violation, probably memory access out of range
[0]PETSC ERROR: Try option -start_in_debugger or -on_error_attach_debugger
[0]PETSC ERROR: or see https://www.mcs.anl.gov/petsc/documentation/faq.html#valgrind
[0]PETSC ERROR: or try http://valgrind.org on GNU/linux and Apple Mac OS X to find memory corruption errors
[0]PETSC ERROR: configure using --with-debugging=yes, recompile, link, and run
[0]PETSC ERROR: to get more information on the crash.
[0]PETSC ERROR: Run with -malloc_debug to check if memory corruption is causing the crash.
application called MPI_Abort(MPI_COMM_WORLD, 50176059) - process 0
[unset]: write_line error; fd=-1 buf=:cmd=abort exitcode=50176059
:
system msg for write_line failure : Bad file descriptor
```

or in parallel

```
$ mpiexec -n -3 python test.py
Vec Object: 1 MPI processes
  type not yet set
[0]PETSC ERROR: ------------------------------------------------------------------------
[0]PETSC ERROR: Caught signal number 11 SEGV: Segmentation Violation, probably memory access out of range
[0]PETSC ERROR: Try option -start_in_debugger or -on_error_attach_debugger
[0]PETSC ERROR: or see https://www.mcs.anl.gov/petsc/documentation/faq.html#valgrind
[0]PETSC ERROR: or try http://valgrind.org on GNU/linux and Apple Mac OS X to find memory corruption errors
[0]PETSC ERROR: configure using --with-debugging=yes, recompile, link, and run
[0]PETSC ERROR: to get more information on the crash.
[0]PETSC ERROR: Run with -malloc_debug to check if memory corruption is causing the crash.
application called MPI_Abort(MPI_COMM_WORLD, 50176059) - process 0
```

# Debugging Python Code

This is really straightforward and works on most platforms.

To debug, in a python debugger, the `mpiexec -n -3 python test.py` example:

  1. Install `pdb++` (see https://pypi.org/project/pdbpp/) which is much better than standard `pdb`
  2. Start a `tmux` session with a `tmux` "window" for each MPI rank, each of which opens in the debugger with `$ tmux-mpi 3 $(which python) -m pdb test.py`
  3. Open a new terminal on the same computer and attach to the `tmux` session with `tmux attach -t tmux-mpi`. You should see that `pdb++` has stopped at the initial import: 
```
[2] > /Users/rwh10/firedrake/src/firedrake/deleteme.py(1)<module>()
-> import sys
(Pdb++)
```
Different "windows" can be jumped between with the shortcut `ctrl-b n` and you can then step through the program on each rank. 
Note you need to do this manually - you can't expect a step on one rank to step on another rank!

If you don't want to jump straight into the debugger but run through to a `pdb` breakpoint (set with either `breakpoint()` in recent python versions or via `import pdb; pdb.set_trace()` in general) then you can omit the `-m pdb` and simply run `$ tmux-mpi 3 $(which python) test.py`.

# Debugging C Code - *NOT ON MACOS*

This requires you to be on a platform where your debugger is `gdb` since MPICH (which firedrake uses by default) does not play nicely with `lldb` and will give very confusing results.
In practice this means that *you cannot easily debug MPI C code on MacOS*.

To debug, in a C debugger, the `mpiexec -n -3 python test.py` example:

  1. Run `$ tmux-mpi 3 gdb --ex run --args $(which python) test.py` - this will create a `tmux` session with 3 `tmux` "windows" each running `test.py` in `gdb`
  2. Open a new terminal on the same computer and attach to the `tmux` session with `tmux attach -t tmux-mpi`. The program will have breaked when the seg fault happened on rank 0 whilst the other ranks continue to run - you'll be able to see this by switching windows with `ctrl-b n` until you see
```
...
[New Thread 0x7fffa4073700 (LWP 22242)]
[New Thread 0x7fffa1872700 (LWP 22243)]
Vec Object: 1 MPI processes
  type not yet set

Thread 1 "python" received signal SIGSEGV, Segmentation fault.
0x0000000000000000 in ?? ()
(gdb)
```
The other ranks can be broken at any time with an interupt signal (`ctrl-C`) to see where you are.

This is particularly useful when trying to debug hanging programs where no rank processes have actually errored.

Note that I have yet to get PETSc's `-start-in-debugger` argument, which should cause the program on all ranks to start in the debugger, working

`$ tmux-mpi 3 gdb --ex run --args $(which python) test.py -start-in-debugger`

or indeed any arguments such as PETSc's `-on_error_attach_debugger`.

Please update this and let me know if you manage to get it working!

 - Reuben Nixon-Hill May 2021