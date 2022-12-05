When using MacOS one is, generally, forced to use `lldb` for debugging C code on the command line.
A list of `lldb` commands can be found [in this cheat sheet](https://www.nesono.com/sites/default/files/lldb%20cheat%20sheet.pdf), though generally `gdb` commands work as expected.
`lldb` can be used to debug C code that has been generated with Firedrake by doing the following:

1. Apply this patch to PyOP2:

```diff
diff --git a/pyop2/compilation.py b/pyop2/compilation.py
index ecca4318..3bfba50e 100644
--- a/pyop2/compilation.py
+++ b/pyop2/compilation.py
@@ -350,7 +350,7 @@ class Compiler(ABC):
         soname = os.path.join(cachedir, "%s.so" % basename)
         # Link into temporary file, then rename to shared library
         # atomically (avoiding races).
-        tmpname = os.path.join(cachedir, "%s_p%d.so.tmp" % (basename, pid))
+        tmpname = soname # os.path.join(cachedir, "%s_p%d.so.tmp" % (basename, pid))
 
         if configuration['check_src_hashes'] or configuration['debug']:
             matching = self.comm.allreduce(basename, op=_check_op)
@@ -443,7 +443,7 @@ Unable to compile code
 Compile log in %s
 Compile errors in %s""" % (e.cmd, e.returncode, logfile, errfile))
                     # Atomically ensure soname exists
-                    os.rename(tmpname, soname)
+                    # os.rename(tmpname, soname)
             # Wait for compilation to complete
             self.comm.barrier()
             # Load resulting library
```
To quote Lawrence, this diff
> ... turns off the compilation into a temp file and then renaming (which we do for parallel filesystem safety reasons) ... but that renaming defeats the debug symbol tracking on macos where the debug symbols are in a separate file from the shared library

2. Make sure the cache is empty by running `firedrake-clean` with the venv activated.

3. Still on the command line, switch on debugging symbols in PyOP2 and run lldb:
```
export PYOP2_DEBUG=1
lldb -- python script.py
breakpoint set -n name_of_function
run
continue
```
Note that we have to use `breakpoint set -n name_of_function` since our generated code will not necessarily be in the same location as our usual firedrake source code (so we can't do, say `breakpoint set --file test.c --line 12` as listed in [this LLDB cheat sheet](https://www.nesono.com/sites/default/files/lldb%20cheat%20sheet.pdf)).
We have to set `lldb` running with the `run` command (it starts in a repl mode but knows which file it needs to run).
The `continue` command continues after an inital stop due to `exec` (don't ask my why).

Reuben Nixon-Hill, 2022