Date and time 2021-04-21 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: ~Crap out the geometric boundary stuff~ done: please review https://github.com/firedrakeproject/firedrake/pull/2007
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Minutes

Present: Jack Betteridge, Reuben Nixon-Hill, David Ham, Mariana Clare, Koki Sagiyama, Daniel Shapera, Lawrence Mitchell, Sophia V, Rob Kirby, Connor Ward, Kaushik Kulkarni, Thomas Gibson, Nacime Bouziani

Apologies:

## MC Getting EquationBC to work with pyadjoint
Using the branch `equation_bc_tape_mc` (and some changes to pyadjoint) we are now able to correctly tape EquationBC. However, there are a few issues calculating the derivative mainly because EquationBC was not designed to be used with `_la_solve` which is what pyadjoint uses when calculating the derivative. It also seems like `evaluate_adj_components` is never called on BC blocks which seems confusing. [MC]

 - DH: DirichletBC requires thinking about "un-symmetrised BCs" and "symmetristation process as a preconditioner". Noted that statement "adjoint problem always has homogenous boundary conditions" is untrue. (Specific mathematical details were run through but too quickly to minute). Suggest using BC as a control to test.
 - DH: EquationBC more complex to deal with. KS and DH think need an "assemble BC" option.
 - DH: In general having cofunctions will make some of these problems go away by being able to apply BCs by having cofunctions as forcing term.

## Loopy Sprint
 - Status: have PyOP2 tests passing. Now looking at firedrake. Dealing with changes to loopy where loopy "programs" can now contain multiple "kernels" with their own "entrypoints": may need mixture of loopy and firedrake/pyop2/tsfc changes to deal with.
 - Unclear how difficult the outstanding firedrake issues will be to fix.
 - Some loopy fixes are breaking downstream packages because they relied on now deprecated language features.
 - Problem with PyOP2 discovered where a recent update to the decorator package breaks some pyop2 tests. Decorator package now pinned to before this change. Decorators are being used for hand-rolled argument type checking.
   - DH notes that all this is relic of mistaken belief that users will write their own PyOP2 code so argument checking probably doesn't have to be quite as strict.
 - Problem with PyOP2 tests rediscovered where tests are not independent from one another - abuse of pytest's fixtures which ought to be fixed. Notably in PyOP2 matrix tests. This stops tests from being run in parallel.

## LM: UFLv2 being discussed (so called '2FL')
 - Discussions between LM and FEniCSx developers
 - Hope to tidy some corners of UFL
 - Redo composition of FiniteElements and visitor infrastructure
 - DH would like to see removal of bolted on language features which are in python anyway
 - LM opinion: surface language close to correct with some corner case issues, but would like to rewrite some of the internals. If you write variational forms you shouldn't have to change much. If you transform UFL a lot then you might need to adapt.
 - DH described changes that India Marsden is currently making in defining new forms, of which cofunctions, matrices, external operator and `interp` are examples. This gets around needing to completely rewrite the form infrastructure of UFL (i.e. we leave the primal-space language alone). The dual space language, i.e. language of form manipulations, is much smaller than the primal space language: reckon we need differentiation and addition only which are fairly easy to define.
 - LM keen to see UFL's differentiation implementation use fewer operations if possible, e.g. for residual assembly (which needs speed ups in other places too)
 - Changes to type hierarchy would be nice
   - DH highlights that the fundamental distinction of expressions and forms seems correct: adding additional features is hard because of existing inheritance structures.
   - LM notes FiniteElement is a bit of a mess

## DH: Firedrake / Slepc interface
Would make a nice 4th year project to improve the interface. Believe the interface is reasonably straightforward as long as you start from a generalised nonlinear eigenproblem, write out what a generalised solver for that would look like, and work towards specific case (i.e. will need a strong student).

## Merge PRs:

## AOB

## Date of next meeting

[2021-04-28](./Firedrake-meeting-2021-04-28) 15:00UTC (16:00BST)