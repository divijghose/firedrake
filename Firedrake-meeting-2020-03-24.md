Date and time: 2020-03-24 16:00UTC

# Action items

LM: Setup wiki based agenda templates/minutes
DH: Resurrect mac/mpi4py fix

# Agenda

## Issue labelling

LM: A few people have asked me where a good place to start trying to fix things is. Presently there's no categorisation.

## Github organisation membership cleanup

Do we care?

## Complex
From what I understand the only reason why complex is not merged yet, is that it is an annoying (and slightly boring?) task. Since most people of our team are coding in different parts of firedrake anyways, maybe we could finally get complex on stage by a shorter and less annoying team effort? Would it possible to split this into parts such that everyone ensures type safety in "their" part of firedrake?

## IRKsome
RCK: I can very brief update on generating UFL for higher-order Runge-Kutta methods for whomever is interested.  I think I'm about ready to make the repo public.  Basically, we can do
`F = inner(Dt(u), v)*dx + inner(grad(u), grad(v))*dx - inner(rhs, v)*dx`
for the heat equation, take a Butcher tableau, and get UFL for the corresponding RK method.  Firedrake solver magic should beat down the complicated nasty algebraic system coupling all the stages together.

We probably need form labeling of some sort to do fancier things like IMEX, but I have taken a stab at DAE-type things like the mixed form of heat equation (tested) or unsteady NSE (untested).

## Results of Firedrake user survey?

## Date of next meeting
