**Improved FAQ:**

---

**Q1: I'm experiencing problems during the Firedrake installation. What details should I share with the Firedrake developers?**

When seeking assistance, please provide the following logs:

- **firedrake-install.log**: Located in the directory where you initiated the firedrake-install process.
- **configure.log** and **make.log** from PETSc: These can be found in `src/petsc/` within the directory where the Firedrake virtual environment was established.

---

**Q2: How do I install Firedrake if I already have Conda installed, and it is causing issues?**

We have received feedback from a user who successfully installed Firedrake despite having Conda on their system. Here is an approach that has worked well:

The installation page makes it sound very complicated to install firedrake if conda is already installed on the system. But the following steps worked really nicely for a number of people in our lab (running Linux):

_* `deactivate conda`_

_* modify the PATH variable by deleting the anaconda entries that are put at the very beginning of the path_

_* install firedrake_

_After that, all that needs to happen in the shell is to 'deactivate conda' and 'source firedrake/bin/activate'._

Thank you, [martintruffer](https://github.com/martintruffer), for the helpful advice!

For more detailed help on managing Conda while installing Firedrake, you can refer to the Firedrake [installation guide](https://www.firedrakeproject.org/download.html).

**Q4: Where can I seek further assistance or support?**

If you encounter issues not covered in the resources mentioned above, please don't hesitate to [contact us](https://www.firedrakeproject.org/contact.html).


---

**For Archived Installation Issues:**

For a history of installation-related problems and solutions, you can refer to our [Archived Install Issues page](https://github.com/firedrakeproject/firedrake/wiki/Archived-install-issues).

---


