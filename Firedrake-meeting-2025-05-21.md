Date and time 2025-05-07 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (JHC pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))
1. All: Do post merge works (interpolate, abstract reduced functionals, etc.)

# Agenda

Present: DH, IM, JHC, KS, PB

Apologies: LC

## Discussion-worthy issues/PR

## KS: ufl.DAGTraverser

https://github.com/FEniCS/ufl/pull/365

- Need to persuade FEniCSx team of the fix of performance regression - message sent. 
- Discussion on performance - some necessary remaining overhead causing 10-15% time increase.  


## PB: Fix R space assembly

Recent changes in quadrature degree estimation broke assembly of mixed R-spaces on extruded meshes.

It seems like `kernel.info.coefficients` does not store split coefficients if we have an extruded mesh. Do we want to instead make sure that they are properly split?

https://github.com/firedrakeproject/firedrake/pull/4331

- Change approved
- Maybe it isn't a situation that should be hit, but this will do the right thing if it is.

Discussion about Constants and the Adjoint

- Constants that are not defined on a mesh do not have a parallel scope.
- Adjoint requires the ability to take the derivative, producing an Argument in the "Constant Space", which we need to modify programmatically in the process of taking the adjoint and all associated tasks - not trivial
- There are scenarios where you could end up with a two form where one argument is in a constant space - we do not have the information to assemble this described at the moment.
- In summary, this is not a small task - we need first class constants in UFL. 
- Conversely, why can't we just use something in the R space. Doesn't work eg for same value on two meshes. Also inner product on R space is not the same as inner product on floats due to scaling by volume of domain. 
- Potential fix by extending Function.assign to work between R space functions on different meshes. Overloaded operation that can be taped. 



## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*


KS: Extract codim-1 submesh: https://github.com/firedrakeproject/firedrake/pull/4329

Q: DH - How do we know this produces a valid mesh
A: KS/DH - Meshes have lack certain abilities (like interior facet integrals) if they are invalid. Also you may be restricted with the degrees of freedom that make sense to use on the mesh. 

JHC - Add more details for edge case that is noted in code
DH - Documentation?


Reviewing Demos:

RK/PB Patch Demos
 - Passing, reviewed by PB, previously reviewed by DH
 - Merged

RK/PB Rayleigh Benard Demo
 - Failing due to Irksome reason, PB on it
 - Need to add Irksome to CI for the demos to run
 - Reviewed, some changes required


1600 UTC [2025-05-28](./Firedrake-meeting-2025-05-28)