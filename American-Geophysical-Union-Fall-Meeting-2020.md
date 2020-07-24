The session [Addressing Challenges for the Next Generation of Earth System Models](https://agu.confex.com/agu/fm20/prelim.cgi/Session/103241) could be a good fit for some Firedrake talks.
In particular the abstract specifically mentions domain-specific languages.
**The due date is July 29**.
If you're interested in working on a presentation please put your name down under the topic below, or if you'd like to present on a topic you don't see then feel free to create it.

### Extruded meshes are lovely

Firedrake implements a fortuitous combination of extruded meshes, language extensions to UFL for manipulating forms defined on these meshes, tensor product finite elements, and specialized codegen optimizations like sum factorization.
We'll describe how these features are invaluable for implementing models across the geophysical sciences, many of which exhibit a layered structure in the vertical dimension.
In particular, they are used in the atmospheric model Gusto, the ocean model Thetis, and the ice sheet model Icepack.

People: Daniel Shapero, Tuomas Kärnä

### Automating Code Generation for Point Evaluation in Geoscience Models

Firedrake is a code generation system which enables straightforward and scalable model development using finite element methods via high level abstractions of mathematical concepts. Several software packages build on Firedrake for applications in the geophysical sciences: the ice sheet model Icepack, the atmospheric model Gusto, and the ocean model Thetis. In the past, assimilating sparse point data (as opposed to gridded data) into models discretised using the finite element method has been challenging. We present progress towards evaluating, manipulating, assimilating and creating equation systems with large numbers of point measurements into these models. Examples of such data sets include measurements of ice sheet elevation from satellite altimetry and measurements of ocean salinity and temperature from drifting buoys. Our framework is compatible with the automated adjoint system pyadjoint, facilitating automated code generation for inverse problems with point data. This work is part of a broader project aiming to use Domain Specific Languages (DSLs) to automate diagnostics of geoscientific models with very large output data sets.

People: Reuben Hill