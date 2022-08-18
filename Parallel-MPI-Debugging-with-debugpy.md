Visual Studio code has very advanced visual debugging capabilities using the `debugpy` debugger. This also supports parallel debugging with MPI. 

### Configuration

You need a one-off workspace configuration in VS Code. From the `Run and Debug` tab choose `Add Configuration...` and then add the following configurations to `launch.json`:

```json
        {
            "name": "Python Attach 0",
            "type": "python",
            "request": "attach",
            "port": 3000,
            "host": "localhost",
        },
        {
            "name": "Python Attach 1",
            "type": "python",
            "request": "attach",
            "port": 3001,
            "host": "localhost"
        }
```
If you want to debug more than 2 MPI ranks, add more configurations with corresponding increasing port numbers.

### Preparing the program to be debugged.

The Python program to be debugged needs the following code added, usually right at the start:

```python
from mpi4py.MPI import COMM_WORLD
import debugpy
debugpy.listen(3000 + COMM_WORLD.rank)
debugpy.wait_for_client()
```
This causes each MPI process to listen for a debugger on an appropriate port and to block pending the debugger attaching.

### Launching the program and the debugger

Run the program under MPIexec in the usual way. E.g.:
```console
$ mpiexec -n 2 $VIRTUAL_ENV/bin/python myscript.py
```

The processes should start and pause waiting for the debugger.

In Visual Studio Code, set a breakpoint where you would like execution to pause. Next, launch both (or all of) the `Python Attach` debugger configurations. This will show you 2 (or the number of MPI ranks) call stacks. You can switch the debugger between them using the dropdown on the debugger control window. You're now ready to debug!


