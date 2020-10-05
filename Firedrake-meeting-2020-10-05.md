Date and time 2020-10-05 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ??: Build master on centos to catch errors
1. RK: Report back on quadrature estimation
1. KS: Complex merge
1. All: This week (5th October) prepare 3mins on "what I do" for incoming meeting attendees


# Minutes

Present: Colin Cotter, David Ham, Connor Ward, Jack Betteridge, Koki Sagiyama, Lawrence Mitchell, Paul Kelly, Sophia Vorderwuelbecke, Rob Kirby, Dan Shapero, Reuben Hill

Apologies:

## "Three Minute" not a thesis, but what I do
Feel free to add your own summary here (JB: I can't type that fast!)

## JB: Numpy bug update
Something very strange happens with ISL/loo.py when you use your own numpy on MacOS. It is finding the system Accelerate numpy, despite the many precautions taken to avoid this.

Can't use docker because it gives you root on HPC.

Should we use S-pack? FeNiCsX have made this decision.

JB will look for solutions when building MPICH as part of PETSc.

Need to make sure that bugs are being reported upstream. *Everyone* needs to make an effort to do this when bugs are found.

## DH: Complex merge
Very close to a merge here, PRs are being held until after complex lands. Which should be this week.

## LM: Reading group
Resumes on Monday 1500 (BST), with Colin leading: [details here](https://github.com/firedrakeproject/firedrake/wiki/Reading-group)


## Date of next meeting
[2020-10-12](./Firedrake-meeting-2020-10-12) 15:00UTC (16:00BST)