**Improved FAQ:**

---

**Q1: I'm experiencing problems during the Firedrake installation. What details should I share with the Firedrake developers?**

When seeking assistance, please provide the following logs:

- **firedrake-install.log**: Located in the directory where you initiated the firedrake-install process.
- **configure.log** and **make.log** from PETSc: These can be found in `src/petsc/` within the directory where the Firedrake virtual environment was established.

---

**Q2: My Firedrake installation is failing on MacOS, and I have seen in `firedrake-install.log` error messages when trying to install `OPENBLAS`. How should I proceed?**

* **Script Modification**: Open the firedrake-install script and at [line 786](https://github.com/firedrakeproject/firedrake/blob/1bbd9dfa3b9a7dc7e501cc094b93067e89c6448c/scripts/firedrake-install#L786) replace from:
    ```
    petsc_options.add("--CFLAGS=-Wno-implicit-function-declaration")
    ```
    to:
    ```
    petsc_options.add("--CFLAGS=-Wno-implicit-function-declaration -Wno-int-conversion -Wunused-but-set-variable")
    ```
    Hopefully, this modification will address the issues with OpenBLAS.

---

**Q3: Where can I seek further assistance or support?**

If you encounter issues not covered in the resources mentioned above, please don't hesitate to [contact us](https://www.firedrakeproject.org/contact.html).

---

**For Archived Installation Issues:**

For a history of installation-related problems and solutions, you can refer to our [Archived Install Issues page](https://github.com/firedrakeproject/firedrake/wiki/Archived-install-issues).

---