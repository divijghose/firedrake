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

## Results of Firedrake user survey?

## ufl.Filtered
Koki: A new ufl operator to dof-wise select/drop rows when assembling.

Structurally,
Filtered(v, filter)
compares to:
Indexed(v, multiindex)

In terms of its functionality (selecting dofs (or rows) to assemble)
this can be viewed as a generalisation of indexing and lgmap thing for BC.

`fs_filter` branches in firedrake, ufl, tsfc.
`firedrake/tests/filter/test_filter.py`

## Mixed-dimensional stuff in dolfin

Some discussions/proposals are ongoing (driven by Francesco Ballerin) to decide how to do mixed-domain stuff in fenicsx. See proposal here: https://docs.google.com/document/d/1pMdMOs2RjTYherVeG9cfACQ4g67HOpYkxQTj4J5Ivjg/edit#heading=h.a9dv1a5yscnd

It seems that we should engage with this effort (at least at the frontend level).

## Date of next meeting
