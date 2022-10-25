Date and time 2022-10-12 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** (KS pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open next week hopefully)
1. ALL: Rename split (`.split` -> `.subfunctions`)

# Minutes

Present: RK, NB, DH, KS, CC, JB, RNH, PK, PB, CW, DS

Apologies:

## Firedrake 2022

Abstract submission is open

-> Need to work out venue's equipment allows for recorded talkd

## RNH: Travel and Accommodation at CSE23
> Might as well book early. Figure UK people will take the Eurostar? 
> The conference have a [link](https://www.siam.org/conferences/cm/lodging-and-support/hotel-transportation-information/cse23-hotel-transportation-information) for group booking hotels using the RAI hotels service. Alternatively we can look into an AirBnB somewhere north of the RAI conference centre.

-> Eurostar can't be booked yet!

> Also it claims to start on a Sunday and run to a Friday. Does anyone know more precisely when it's likely to start and end? Sunday start seems unlikely to me.

-> Conference stats with a reception on Sunday


## JB: A Firedrake manual
> Should Firedrake have a manual, like the PETSc manual, for citing/acknowledging those currently working o nthe project, rather than just pointing to the 2016 paper? I think the consensus in the small discussion last week w/Matt was yes, but wanted to bring this to attention of everyone.

Yes it should. We could use the website document and put it on Arxiv.

Jack: Work out how to generate PDF from our sphinx documentation

## Periodic mesh for tokamak application

Golo Wimmer is looking for mesh capabilities that would enable mesh alignment for fusion application (the domain is a tokamak).

Right solution is a mix between extruded and periodic mesh. Koki has been working on it. Mostly has to do with PyOP2.

## Sophia's PhD viva

Should be on November 10th (Thursday)!

## Postdoc positions

-> DS's colleague (Brad Lipovsky) is looking for a postdoc to work on surface meltwater-induced hydrofracture of ice shelves. Description is here: https://apply.interfolio.com/114088.

-> Eike Mueller is also looking for a postdoc: Contact DH for more info

## Merge PRs

- [#2543](https://github.com/firedrakeproject/firedrake/pull/2543): In progress (associated with [#2580](https://github.com/firedrakeproject/firedrake/pull/2580))
- [#125](https://github.com/FEniCS/ufl/pull/125): Approved by Lawrence -> Should be merged if tests passing



## Date of next meeting

David is away for the next 2 weeks.

1600 UTC [2022-10-26](./Firedrake-meeting-2022-10-26)
