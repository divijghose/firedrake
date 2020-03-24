Date and time: 2020-03-24 16:00UTC

# Action items

1. ~LM: Setup wiki based agenda templates/minutes~
2. ~DH: Resurrect mac/mpi4py fix~

# Minutes

Present: David Ham, Lawrence Mitchell, Daniel Shapero, Eder Medina, Jack Betteridge, Nacime Bouziani, Paul Kelly, Reuben Hill, Rob Kirby, Stefan Kramer, Sophia Vorderwuelbecke, Thomas Gregory, Koki Sagiyama, Julian Andrej

## Issue labelling

LM: A few people have asked me where a good place to start trying to fix things is. Presently there's no categorisation.

A bunch of open issues should probably just be closed. 

Action ALL: triage the open issues and confirm if they are indeed still open (and perhaps provide labels).

## Github organisation membership cleanup

LM: Do we care?
DH: probably don't care.

Action LM: Should probably check that firedrake-contributors doesn't give push to master on any of the organisational repos.

## Complex

SV: From what I understand the only reason why complex is not merged yet, is that it is an annoying (and slightly boring?) task. Since most people of our team are coding in different parts of firedrake anyways, maybe we could finally get complex on stage by a shorter and less annoying team effort? Would it possible to split this into parts such that everyone ensures type safety in "their" part of firedrake?

LM: Infrastructure part to do with testing.
DH: Should be able to cull without reducing coverage.

Proposal: sprint to do it week beginning 20th April.

## Results of Firedrake user survey?

DH: has not looked that recently. 45 responses as of 2020-03-24

Action DH: pull out list of people who have filled in survey. We can then decide if we want to chase some.

Action SV: update known list of firedrake citing papers that actually use firedrake. Already known papers live here: https://github.com/firedrakeproject/firedrake/blob/master/docs/source/_static/firedrake-apps.bib

We can then intersect and chase.

## ufl.Filtered
Koki: A new ufl operator to dof-wise select/drop rows when assembling.

Structurally,
Filtered(v, filter)
compares to:
Indexed(v, multiindex)

In terms of its functionality (selecting dofs (or rows) to assemble)
this can be viewed as a generalisation of indexing and lgmap thing for BC.

`fs_filter` branches in firedrake, ufl, tsfc.
[`firedrake/tests/filter/test_filter.py`](https://github.com/firedrakeproject/firedrake/blob/048d1a83dc74638ff088405197c5e488434e24e3/tests/filter/test_filter.py)

### Rationale

Slightly unclear from presentation.

Action KY: Write up maths of what this is supposed to do, what it enables, and why it is needed.

## Mixed-dimensional stuff in dolfin

LM: Some discussions/proposals are ongoing (driven by Francesco Ballerin) to decide how to do mixed-domain stuff in fenicsx. See proposal here: https://docs.google.com/document/d/1pMdMOs2RjTYherVeG9cfACQ4g67HOpYkxQTj4J5Ivjg/edit#heading=h.a9dv1a5yscnd

It seems that we should engage with this effort (at least at the frontend level).

LM: What was our strawman?

DH: Initially we thought we should integrate on the parent mesh.
KY: Integration domain should match the domain of the test function.

Implies that trace is a thing, and we need to figure out what we want from it.

Action KY, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).

## Parallel GC

DRS: What is involved in fixing this and can it be divied up easily?

Action LM: write up some of the issues and where to start looking.

Action JB: Add brief note to docs on disabling GC in parallel.

## Date of next meeting

[2020-03-31](./Firedrake-meeting-2020-03-31) 15:00UTC (16:00BST)