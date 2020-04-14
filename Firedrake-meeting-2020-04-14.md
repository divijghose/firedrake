Date and time 2020-04-14 15:00UTC (16:00BST)

# Action Items

1. ALL: triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like (and hence what is needed in UFL, and whether it matches the existing fenics efforts).
1. ~DH: intersect survey with new publications list and figure out who to prod.~
1. ~NB: have a go at this (object versioning) in PyOP2.~
1. DRS: ~~Make a project page~~ see the [related Firedrake issue](https://github.com/firedrakeproject/firedrake/issues/1649), and start having a good at load/store plex objects. To make smart checkpoints
1. ~JB: Add info to download page.~
1. ~JB: Add a section on `firedrake-update --help`~
1. KS: turn document (PDF) on `Filtered` into issue where we can discuss this further asynchronously.

# Minutes
Present: Jack Betteridge, Dan Shapero, David Ham, Koki Sagiyama, Nacime Bouziani, Paul Kelly, Reuben Hill

Apologies: Sophia Vorderwuelbecke

Not an Imperial College (+ others) work day, no obligation to attend

## DH: State of build testing.
Will discuss at next meeting when LM is present

## DH: Complex sprint next week.
Meeting Friday 17th 1600 (BST) to plan

Webpage: [Complex Sprint](https://github.com/firedrakeproject/firedrake/wiki/MergeComplexSprint)

Master needs to be merged into Complex before week beginning 20th, action point KS.

Complex still contains hand coded C kernels.

## RWH: Mesh Topology Fun
See [PR](https://github.com/firedrakeproject/firedrake/pull/1652).

Geometric dimension not specified when creating a mesh topology (defaults to topological dimension for a UFL cell).
No current way to tell UFL about the geometric dimension.

> Are we actually interested in the Geometric dimension or the value shape of FD? (DH).

LM to comment further on this issue.
Firedrake mesh topology requires a UFL mesh, hence argument is that Firedrake mesh topology needs to know geometric dimension.
DH to comment further on issue also.

## RWH: Separate slack help/dev chat? 
> RH: am I being annoying on Slack?

> DH: Short answer, no, Slack is not currently "too busy", continue current posting

## KS: Filtered Writeup (Update):
Will discuss at next meeting when larger group (LM, SK, +others) are present.

KS to join Thetis meeting

## Date of next meeting

2020-04-21 15:00UTC (16:00BST)
Will be during complex sprint