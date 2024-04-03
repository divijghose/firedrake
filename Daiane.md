**My notes**

**03/04/2024: /hombrew/openblas does not work for MacOS:**

Steps to reproduce:

python3 firedrake-install --with-blas /opt/homebrew/opt/openblas

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


