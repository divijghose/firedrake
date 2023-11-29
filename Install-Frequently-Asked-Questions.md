**Q1: I am facing issues with the Firedrake installation. What information should I provide to the Firedrake developers for assistance?**

Please include the **firedrake-install.log**, which you can find in the directory where you invoked firedrake-install from. Additionally,
**configure.log** and **make.log** from PETSc, which you can find in `src/petsc/` inside the directory where the Firedrake virtual environment was created.


**Q2: I am encountering installation failure with Firedrake on MacOS. I opened `firedrake-install.log` and saw the error message `Error configuring SUPERLU_DIST with CMake`. What could be a potential solution?**

Begin by confirming your Xcode version with the terminal command `xcodebuild -version`. If the response is `Xcode 15.0`, a potential solution is to upgrade from Xcode 15 to Xcode 15 beta. Detailed instructions for this can be found [here](https://github.com/firedrakeproject/firedrake/wiki/Installation-Issues-with-Firedrake-on-Xcode-15-for-MacOS-Users).


**Q3: Where can I find additional help or support?**

If you have issues not addressed in the provided resources, feel free to [contact us](https://www.firedrakeproject.org/contact.html).

---
**Archived install issues**
---
Archived install issues are available [here](https://github.com/firedrakeproject/firedrake/wiki/Archived-install-issues).
