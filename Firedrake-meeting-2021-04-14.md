Date and time 2021-04-14 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: ~Crap out the geometric boundary stuff~ done: please review https://github.com/firedrakeproject/firedrake/pull/2007
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Minutes

Present: Lawrence, David, Keith, Koki, Nacime, Sophia, Reuben, Jack, Pablo

Apologies: Rob

## Loopy sprint:

The sprint is happening next week.

Sophia: Arrange a meeting to prepare the sprint -> Advertise it in the loopy slack channel

## Continuous Integration:

CI needs to be replaced for various reasons. Currently, the build testing is done via Jenkins.

We have got the money to replace it, we need to figure out how much work would that represent.

An alternative would be `Github Actions`, we would need to migrate little pieces from build into Github Actions. It runs the way end user would install.

-> Prototyping can be done using a machine on campus


## Merge PRs:

- CW: [Refactoring assemble](https://github.com/firedrakeproject/firedrake/pull/1983): **Merged**
        -> Cache parloops directly on the form and do other optimizations.
                -> Consequence: Speed up significantly `assemble()` (x4-5) at the cost of a small overhead for the internal API `create_assembly_callable()` (x2).

- [Annotate +=, *=, etc.](https://github.com/firedrakeproject/firedrake/pull/1995): **Merged**
        -> Annotate augmented assignments. It basically puts an `AssignBlock` on the tape and encode the augmented assignment in the `assign` input. Adjoint does not do the right thing for `*=` and `/=` for nonlinear assignments.

- [Interior bcs](https://github.com/firedrakeproject/firedrake/pull/2007): **Review needed**
        -> Remove the non topological identification of boundaries that consists in identifying the boundary nodes as those where the basis functions cancel out (implying that the nodes are dependent from the basis functions). Instead we only keep the topological association.

## AOB

## Date of next meeting

[2021-04-21](./Firedrake-meeting-2021-04-21) 15:00UTC (16:00BST)