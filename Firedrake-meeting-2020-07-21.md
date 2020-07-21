Date and time 2020-07-21 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. DH: Provide RWH with abstract and title for SIAM-CSE minisymposterium to make into qualtrics survey
1. DH: Provide JB with contacts for SIAM-CSE Exascale simulation themed minisymposium - Jack is in discussion with Tiemo. 
1. DRS: ~set up wiki page for AGU submissions~ to [Addressing Challenges for the Next Generation of Earth System Models](https://agu.confex.com/agu/fm20/prelim.cgi/Session/103241) session, [wiki page for AGU 2020](https://github.com/firedrakeproject/firedrake/wiki/American-Geophysical-Union-Fall-Meeting-2020)
1. PEF: status of BDMC branches - FIAT is ok, Firedrake needs some tests introduced to make these BDMC changes land. 


# Minutes

Present: David Ham, Reuben Hill, Jack Betteridge, Nacime Bouziani, Lawrence Mitchell, Patrick Farrell, Dan Shapero, Sophia Vdw, Koki Sagiyama, Tom Gregory, MKan, mohamadusman

Apologies:

## RWH - Rename `split()` to `ufl_split()` or similar?
(Apologies if discussed before) Apparently the difference between `split()` and `v.split()` catches lots of people out. Is there any reason to not rename one of the functions?

We need to be careful with the potential to diverge from FEniCS here. If we can come up with a suitable alternative name for one of these split variants, we may be able to provide that as an alternative to the user. We need an appropriate name in order to do this - Reuben was volunteered to think on some ideas. 

As this is an issue that most new users encounter sooner or later, we should consider proposing a change in this notation as part of FEniCS-X. 

## RWH - Add link to firedrake youtube channel in documentation
See https://github.com/firedrakeproject/firedrake/pull/1785

## DRS - installation debugging flowchart

Is near completion. Discussions were had on how best to convince new users that everything is running fine - `make alltest` can take quite a while. Is a smaller critical subset of tests possible?

## JB: PR #1786
Smaller Firedrake, newer VTK

Work continues on removal of some build files and having a smaller install of Firedrake, especially with HPC users in mind. Work in VTK wheels is also progressing. 

### The NumPy Disaster

An issue was found where if the user has multiple versions of gfortran installed, we may encounter some incompatibilities, especially when building NumPy. Among other issues, this has been shown to cause a segfault if NumPy and PETSc are imported in in the 'wrong' order. We may need to build OpenBLAS via PETSc and build our NumPy and SciPy from there. Jack will look into the specifics of how long installing SciPy directly would take, and how best to ship wheels for SciPy if this is necessary. 

## Date of next meeting

With some key members on holiday, we have no plans to hold a meeting for the next two weeks. Our next meeting is:

2020-08-11 15:00UTC (16:00BST)
