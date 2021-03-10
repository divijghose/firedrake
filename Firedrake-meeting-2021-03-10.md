Date and time 2021-03-10 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: Crap out the geometric boundary stuff
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present:

Apologies:

## IGG: (Via JB)
Ivan Graham would like to promote the use of Firedrake through a training event, probably hosted "in" Bath for wider GW4 community. Main questions are:
* would the Firedrake team be happy to run such an event, and if so in which form?
* which resources (in terms of tutors and their financial compensation) would be required?
* which technical infrastructure is required (probably just laptops)?
* and when is the best time to run this (maybe in the summer)? JB suggests either avoiding having it at the same time as Firedrake21 or coinciding
* Does anyone have / want to develop some bad cop Helmholtz demo material for such an event?

**_Minutes:_**

Yes.

**How?** Teams might be better, might be useful to set up breakout rooms. Presenting demo with gaps and users do it at the same time. Users ask for help in the chat and then we call them seperately. Usual setup of running it in cloud (doesn't cost a lot and we don't get billed anyways).

**When?** Maybe next term or in summer.

**Spin-off talk of that: Firedrake meeting.** Maybe in September (probably 2nd week/6th or 13th/proposed is the 13th for now), need to work around Americans. Thanksgiving bad idea. Up to a week of afternoons, depending on how many submissions. Let's think about it later.

**What?: Badcop Helmholtz.** What can we do so far with it? They want complex. We only need to switch Jupiter kernels for that. (In theory, but actually docker for complex is failing). Badcop Helmholtz is in 2D primal form, we can just use lu. An additional demo on solver options demo. We want taster session stuff.

## LM: "geometric" BCs

This issue (https://github.com/firedrakeproject/firedrake/issues/1661) arose again. This requests applying BCs to interior facets. The only thing that is fiddly is determining the dofs on those facets, and pushing through a few other minor bits and pieces.

The wrinkle is that this is all much easier if one uses topological BCs: you can just pull everything out of the section straightforwardly. For geometric bcs we have to go via facet indirections and the code is uglier.

Given that geometric bcs don't make any sense really, we could just remove that option.

**_Minutes:_**

LM will "crap out the code".

## CW, JB: redesign of `firedrake-install`

Installing Firedrake on HPC is hard. Could we come up with a more standard and robust way of installing Firedrake?

Spack looks promising but has some barriers to entry.

**_Minutes:_**

**Critical perspective from LM** 
* Gives you isolated environment that has python and so on. How can you install python packages into that? You can either use spack or the python inside the environment to do pip install. For the latter spack does not know what python packages are inside the isolated environment.
* Developer perspective? Spack unload Pyop2, pip install -i and then work on that. Strongest point of current install is that users and developers have the same install script
* On HPC? You can tarball the spack.

**Critical perspective from DH**
* What do we get out of it? How can we make it robust? Besides being easier to use for install firedrake on HPC? Current flakiness comes from special cases in user environments. Spack claims controls the complete environment, does not fall back to system BLAS. Installing vs using different versions of MPI would not be a problem. Spack gives proper dependency tracking, so more precise about the dependencies.
* If spack installs gcc or whatever, install will take ages. Be careful with things that take long because users will think it's failing. 

**Potential idea**
Refactor firedrake-install so that petsc+ builds are more robust (those are actually killing us not the python packages), maybe spack can help us with that for HPC.

## DH/NB: Grad of external operators

**_Minutes:_**

Came out of thinking hard about the chain rule. What changes is when taking Gateaux derivative of external operator. That's got an argument in a slot, where you then have to be able to drop a modified terminal in (so in the argument slot). Problem: Grad of the external operator has different shape, you have to do appropriate broadcast on the argument, so that the return shape changes as well. Good thing we only need to implement one derivative for the external operators in that case. Easy to change in ufl but it might take longer to adapt to that in the later stages of the pipeline. RC will need to adapt his code in consequence.

## Merge PRs:

No time left.

## AOB

## Date of next meeting

[2021-03-17](./Firedrake-meeting-2021-03-17) 16:00UTC (16:00GMT)