We are close to merge the complex branch onto master, remaining tasks being:

* ensure type safety in each part of Firedrake,
* reduce the size of tests to make complex tests run in a reasonable amount of time.

The purpose of this sprint is to make these happen, each working on their favorite parts of Firedrake.

We will also be hosting a pre-sprint meeting to discuss the workflow.

# Where?
This sprint and the pre-sprint meeting are going to happen on **Zoom**, and we are going to provide the participants with the links to the Zoom meetings on Slack general channel beforehand.

# Pre-sprint meeting minutes
Friday 17th April 2020 at 16:00 (UK time, GMT+1)

**Action items @ALL**
* Run installation see below
* Run tests -> create issues
* Allocate problems of failing tests to yourself

**Potential error causes**
* C-string codes, e.g. containing hard coded doubles
* Implicit real assumptions, math is invalid for complex, e.g. u*v*dx has to be proper inner product 
* Interfacing to external libraries which do not supply complex version e.g. for libspatialindex the coords have to be casted to doubles

**Further problems**
* Petsc only has single scalar type/always rebuild Petsc
  * Test system needs to do tests for both modes (=complex/real) -> boil down tests where possible
  * Docker image generation will take longer, -> decide if we want to put complex in docker
  * Installation will take longer
* Merge claras changes of loopy prolongation/restriction for multigrid, @Lawrence

**Additional notes**
* Out of scope for now: what is the most performant caching (at the moment TSFC turns of loopy caching)
* Complex does complex valued pdes on real domains, nothing on complex domains

**First task allocation**
* David: be prepared for questions
* Reuben, Nacime, Koki, Darko: collect failing tests
* Alberto: PyOP2/adjoint?
* Lawrence: multigrid
* Sophia: loopy
 

# Sprint dates
Afternoons (UK time, GMT+1) of the week beginning 20th April 2020

# Install
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/complex-sprint/scripts/firedrake-install

python3 firedrake-install --complex --package-branch loopy complex --package-branch tsfc complex-sprint --package-branch PyOP2 complex-sprint --package-branch firedrake complex-sprint

(TODO: Check loopy branch at the pre-sprint meeting)

# Participants

**Please add your name if you would be able to attend**

* David Ham
* Lawrence Mitchell
* Nacime Bouziani
* Sophia Vorderwuelbecke
* Reuben Hill
* Koki Sagiyama
* Alberto Paganini