This is the draft set of questions for a Firedrake user survey.

The objectives of the survey are as follows:
* Identifying Firedrake users and what they use Firedrake for.
* Identifying impacts of Firedrake beyond academia.
* Identifying user priorities for future developments, and the science and impact that this would enable.

The reasons for undertaking the survey are:
* To inform future developments and prioritise those of the greatest benefit to direct and indirect users.
* To produce evidence of impact for REF and future funding bids in order to resource those developments.
* To increase the level of awareness among the Firedrake user and developer community of what others do, and thereby to foster collaborations and code reuse.

We will publish the results of the survey in a report posted to arXiv. This will contain the full quantitative results of the survey, and text results subject to respondent consent. This report will provide a citable source for the survey results for use in further publications and funding bids.

## About you

* Name
* Email
* Position (multiple choice Undergrad/Masters/Phd student/(Research) faculty/Staff scientist/other (write in))
* Institution 
* Sector (higher education/public sector research/industry/other (write in))

Do you consent to your responses in this survey being published:
* Associated with your name (Yes/No)
* Just associated with your affiliation (Yes/No)
* Anonymised (Yes/No)

In addition, we will publish statistics about the responses to quantitative survey questions from all respondents. These statistics will not identify responses with individual respondents.

## How do you use Firedrake?

What application areas do you apply Firedrake in?

Which PDEs do you solve?

Considering the work that you do using Firedrake, are you aware of any impact that this has outside academia? Impacts can be very broad and might include influencing decisions or practices, direct use of results or code, indirect use of results among others.

(Yes/No, with yes opening the following question:)

Please briefly describe the impact, including who the non-academic beneficiaries are and what the influence on them is.

* Estimate how many people in your immediate research group use Firedrake. (Number)
* Estimate how many people in your institution but not in your immediate research group use Firedrake (Number)

On which of the following sorts of computer do you run Firedrake:

* A laptop/workstation running Linux
* A laptop/workstation running Windows
* A laptop/workstation running MacOS
* A shared server
* A cluster/supercomputer owned by my institution
* A cluster outside my institution (please name it/them).

## Which of the following Firedrake features do know that you use?

(All tick boxes)

### Domains

* 2D Domains
* 3D Domains
* Immersed manifolds
* Extruded domains
* Periodic domains
* Mesh Hierarchies
* Higher order meshes

### Discretisation and assembly features

* HDiv/HCurl elements
* Higher continuity (C1 or more) elements
* The "R" space of spatially constant functions
* Degree 3 or higher elements
* Setting the quadrature degree
* SLATE (element-local linear algebra)
* Complex (currently beta)

### Solver features

* Setting PETSc options
* Algebraic multigrid
* Geometric multigrid
* Python preconditioners
* Hybridisation
* Patch preconditioners

### External package features

* DefCon
* Dolfin-adjoint/pyadjoint
* SLEPc
* Fireshape

### Models built using Firedrake

* Gusto
* Thetis
* Icepack

## User support and engagement

Which of the following ways have you interacted with the Firedrake community:

* Reading the mailing list.
* Asking questions on the mailing list.
* Reading the Slack channel.
* Asking questions on the Slack channel.
* Opening an issue on GitHub.
* Opening a pull request on GitHub.
* Attending an annual Firedrake workshop.
* Attending a Firedrake tutorial.

## Future developments

Select and rank in order of importance to you any of the following features which you would like to see in Firedrake:

* GPU/other accelerator support.
* Reduced latency/better strong scaled performance.
* Better multi-domain simulation support
* Support for coupling external models
* Better I/O and checkpointing.
* External pointwise operators such as implicit constitutive laws.
* Neural net coupling.
* Macroelements/splines
* Lagrangian particle tracking

What other future developments would be particularly valuable to your work?

For the developments which are important to you, what is the new science and/or impact which would be facilitated by those developments?
