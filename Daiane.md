**My notes**

**10/04/2024: Firedrake install is failling with the latest petsc version:**
```
Building wheels for collected packages: petsc4py
  Created temporary directory: /tmp/pip-wheel-w7qsdtw2
  Destination directory: /tmp/pip-wheel-w7qsdtw2
  Building wheel for petsc4py (pyproject.toml): started
  Running command Building wheel for petsc4py (pyproject.toml)
  running bdist_wheel
  running build
  running build_src
  removing Cython 0.29.36 from sys.modules
  fetching build requirement 'Cython >= 3.0.0'
  ********************************************************************************

    You need Cython >= 3.0.0 (you have version 0.29.36)

      $ /home/ma/d/ddolci/firedrake_test/bin/python -m pip install --upgrade cython

  ********************************************************************************
  error: unsatisfied build requirement 'Cython >= 3.0.0'
  error: subprocess-exited-with-error
  
  × Building wheel for petsc4py (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /home/ma/d/ddolci/firedrake_test/bin/python /home/ma/d/ddolci/firedrake_test/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py build_wheel /tmp/tmp24ampttt
  cwd: /home/ma/d/ddolci/firedrake_test/src/petsc4py
  Building wheel for petsc4py (pyproject.toml): finished with status 'error'
  ERROR: Failed building wheel for petsc4py
Failed to build petsc4py
ERROR: Could not build wheels for petsc4py, which is required to install pyproject.toml-based projects
Exception information:
Traceback (most recent call last):
  File "/home/ma/d/ddolci/firedrake_test/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 180, in exc_logging_wrapper
    status = run_func(*args)
             ^^^^^^^^^^^^^^^
  File "/home/ma/d/ddolci/firedrake_test/lib/python3.11/site-packages/pip/_internal/cli/req_command.py", line 245, in wrapper
    return func(self, options, args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ma/d/ddolci/firedrake_test/lib/python3.11/site-packages/pip/_internal/commands/install.py", line 429, in run
    raise InstallationError(
pip._internal.exceptions.InstallationError: Could not build wheels for petsc4py, which is required to install pyproject.toml-based projects
Remote version of pip: 24.0
Local version of pip:  24.0
Was pip installed by pip? True
Removed build tracker: '/tmp/pip-build-tracker-y0wbl3fl'

2024-04-10 14:02:20,781 INFO   

Install log saved in /home/ma/d/ddolci/firedrake-install.log

```

---

**03/04/2024: /hombrew/openblas does not work for MacOS:**

Steps to reproduce:

```
python3 firedrake-install --with-blas /opt/homebrew/opt/openblas
```
Error:

```
*********************************************************************************************
           UNABLE to CONFIGURE with GIVEN OPTIONS (see configure.log for details):
---------------------------------------------------------------------------------------------
                         Error running make; make install on PNETCDF
*********************************************************************************************
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/configure.py", line 462, in petsc_configure
    framework.configure(out = sys.stdout)
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/framework.py", line 1452, in configure
    self.processChildren()
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/framework.py", line 1440, in processChildren
    self.serialEvaluation(self.childGraph)
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/framework.py", line 1415, in serialEvaluation
    child.configure()
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 1337, in configure
    self.executeTest(self.configureLibrary)
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/base.py", line 138, in executeTest
    ret = test(*args,**kargs)
          ^^^^^^^^^^^^^^^^^^^
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 1023, in configureLibrary
    for location, directory, lib, incl in self.generateGuesses():
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 591, in generateGuesses
    d = self.checkDownload()
        ^^^^^^^^^^^^^^^^^^^^
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 725, in checkDownload
    return self.getInstallDir()
           ^^^^^^^^^^^^^^^^^^^^
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 527, in getInstallDir
    installDir = self.Install()
                 ^^^^^^^^^^^^^^
  File "/Users/ddolci/tes_fire_install/firedrake_test/src/petsc/config/BuildSystem/config/package.py", line 1875, in Install
    raise RuntimeError('Error running make; make install on '+self.PACKAGE)
```


