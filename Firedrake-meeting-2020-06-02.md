Date and time 2020-06-02 15:00UTC (16:00BST)

# Action Items
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing fenics efforts).
Need to convince Michal Habera that we a re doing something sensible (see minutes)
1. ~JB: Add mechanism for python3.8~ Someone: test this: Has someone tested this? Yes, Dan
1. DH: ~Find time to fix to get final complex sprint test passing.~ Now passing

# Minutes
Present:
Lawrence Mitchell,
Dan Shapero,
Stephan Kramer,
Colin Cotter,
Koki Sagiyama,
Jack Betteridge,
Robert Kirby,
Reuben Hill,
Ivan Yashchuk,
Paul Kelly,
David Ham,
Nacime Bouziani,
Sophia Vorderwuelbecke (ultra flaky internet, will try to join if possible),
Thomas Gregory,
Patrick Farrell

Apologies:

## KS: Github action
First push:
https://github.com/firedrakeproject/firedrake/runs/727319093?check_suite_focus=true

Failed with:
Unable to obtain Zenodo record for doi 10.5281/zenodo.1322546

and I can't figure out why it fails here.

Zenodo website is powered by a hamster, hence the failure.
Rerunning that section fixes the issue.

Now we want to put this onto Azure to burn some of Gerard's money

## KS: UFL
Looking at PR:
https://github.com/FEniCS/ufl/pull/22

There is some confusion over what a projection is.
We need to find a way of convincing Fenics developers that this is the correct thing:
Explain that `filter` is splitting the function space, what happens on each bit is a separate matter.
There is a clear distinction between the strong boundary condition and the equation enforced weakly on the space(?).
Discuss in terms of a geometric decomposition, talking about "trace" may be confusing.

There is a need to introduce the concept of basis functions, even though UFL "doesn't know" about basis functions.
At the UFL level all this is doing is expressing functions spaces as direct sums.

Rename `Transformed` to `Decomposed`.

Do we want `Filter` to work on UFL expressions, rather than functions?

Action KS: try an alternative description and make agreed changes.

Action Others: Think about the correct mathematical formulation for Filtered

## DS: Has tested Python 3.8 install and is testing IcePack on this installation

## JB: VTK 9.0 wheel may not be coming to PyPI due to size

## DH: Firedrake install size is very large
There isn't much we can do here.
This is mainly due to PETSc.

Action Someone: Add `--remove-build-files` to make install smaller

## Date of next meeting
2020-06-09 15:00UTC (16:00BST)
