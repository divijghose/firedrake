Date and time: 2020-04-07 15:00UTC (16:00BST)

# Action items

1. ALL: triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ~DH: pull out list of people who have filled in survey. We can then decide if we want to chase some.~
1. ~SV: update known list of firedrake citing papers that actually use firedrake. Already known papers live here: https://github.com/firedrakeproject/firedrake/blob/master/docs/source/_static/firedrake-apps.bib~ [PR open here](https://github.com/firedrakeproject/firedrake/pull/1644)
1. ~KS: Write up maths of what `Filtered` is supposed to do, what it enables, and why it is needed.~
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. ~LM: write up some of the issues (parallel GC) and where to start looking.~ Some more details in [the related Firedrake issue](https://github.com/firedrakeproject/firedrake/issues/1617#issuecomment-610417523)
1. ~JB: Add brief note to docs on disabling GC in parallel.~

# Minutes

Present: Lawrence Mitchell, Dan Shapero, David Ham, Jack Betteridge, Koki Sagiyama, Nacime Bouziani, Paul Kelly, Reuben Hill, Stefan Kramer, Sophia Vorderwuelbecke, Thomas Gibson, Ivan Yashchuk, Rob Kirby

## DH: Survey update

Has got people who filled out survey.

Action DH: intersect with new publications list and figure out who to prod.

## NB: Update of the neural network weights for the PointnetOperator (a type of ExternalOperator)

Allows putting evaluation of neural net into a residual/jacobian. Two mechanisms:

1. Pretrained network
2. Network trained on the fly (controls are weights)

For 2, the weights of the model need to be updated as the model is trained. Question: how should the weights be updated?

DH: Nacime needs object versioning.

Mechanism: attach integer state to `DataCarrier` objects in pyop2. Increment it whenever the state "might" change (via parloop update or property access).

Action NB: have a go at this in PyOP2.

## DRS: Would like to know what's involved in making DumbCheckpoint less dumb?

DRS: Make a project page and start having a good at load/store pelx objects.

## JB: Building documentation, style guides, contributing guides and other things of this nature

`firedrake-update --documentation-dependencies`

Action JB: Add info to download page.
Action JB: Add a section on `firedrake-update --help`

## RK: Update on Irksome (Implicit Runge-Kutta methods in Firedrake)

Code here: https://github.com/rckirby/Irksome/

Does "all-at-once" for the stage equations.

Docs example: https://github.com/finite-element/finite-element-course/blob/master/doc/Makefile

## KS: Filtered writeup

Question: what if we want to impose no-normal flow strongly rather than weakly as is done in the example?

Question DH: should we really be defining the rotation for each dof to be applied? We think this would allow things to do strong bcs instead. And make the weak application simpler.

Action KS: turn document (PDF) into issue where we can discuss this further asynchronously.

## Date of next meeting

2020-04-14 15:00UTC (16:00BST). Put things on the agenda if you want it (otherwise it will not happen).