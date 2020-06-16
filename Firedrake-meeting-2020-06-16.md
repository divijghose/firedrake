Date and time 2020-06-16 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ Continue reviewing
1. \*\*: Add `--remove-build-files` to make install smaller; convert this to an issue

# Minutes
Present: David Ham, Lawrence Mitchell, Dan Shapero, Jack Betteridge, Koki Sagiyama, Rob Kirby, Reuben Hill, Paul Kelly, Nacime Bouziani, Tom Gregory, Sophia Vorderwuelbecke

Apologies:

## DH: Github features

Github is rolling out ["Discussions"](https://github.blog/2020-05-06-new-from-satellite-2020-github-codespaces-github-discussions-securing-code-in-private-repositories-and-more/). Perhaps we should migrate user questions rather than having issues for things.

## DRS: decision tree for installing

Going in right direction. Merge instructions for uploading configure/update.log etc...

## RH: gc issues in vertex mesh

The DMSwarm interaction with gc is not a worry, but other nondeterministic things

## KS: ufl.Transformed

`Mapping` just a `Projection` (`V \to V`).

Proposal that in UFL it just says "here is a projection that decomposes V". Then we have enough maths to define the properties that this object has.

Implementation puts it probably between local and global assembly.

User interface for Mapping -> mimic DirichletBC?

DirichletBC(V, g, subdomain)

Mapping(V, V', g, subdomain)

Question: is it ever the case that V != V'.

Two parts:

1. Symbolics (what is the UFL thing and how does it transform, etc...)
2. Implementation. There is a hierarchy here.
     0. What features does this enable for users?
     1. What does the user interface look for different levels of things: `DirichletBC` replacement, rotated boundaries, etc...
     2. What does the implementation of these things look like (and where does it go?).

## CSE minisymposterium

Symbolic etc... code generation.

JDB: talk to Matt Knepley/Chris Richardson

LM: ping DUNE/NGSolve folk.

## Date of next meeting
2020-06-23 15:00UTC (16:00BST)
