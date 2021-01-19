# Firedrake reading group

An informal reading group around many things finite element. Hosted
online. Email [Lawrence
Mitchell](mailto:lawrence.mitchell@durham.ac.uk) if you'd like to
participate.

Scheduled time: Mondays 15:00 BST (starting 12th October 2020). [This calendar](https://calendar.google.com/calendar/embed?src=qbaqqtn2iiu5l6qjbf2t4aafa8%40group.calendar.google.com) contains details.

Hosted via Zoom:

- Meeting ID: 928 2384 2685
- Passcode: 494089

## Upcoming sessions

## Possible papers

Please add your own, or claim one to present.


- Bonizzoni and Kanschat, [_H<sup>1</sup>-conforming finite element cochain complexes and commuting quasi-interpolation operators on cartesian meshes_ (2020)](https://arxiv.org/abs/2010.00524).
- Li, Zhang, and Zhang, [_A constrained transport divergence-free finite element method for Incompressible MHD equations_ (2020)](https://arxiv.org/abs/2008.09244).

- Xu, [_The method of subspace corrections_ (2001)](https://doi.org/10.1016/S0377-0427(00)00518-5).
- Hiptmair and Pechstein, [_Discrete regular decompositions of tetrahedral discrete 1-forms_ (2017)](https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2017/2017-47_fp.pdf). This paper introduces, in a rather didactic way, a lot of modern analysis tools for development and analysis of preconditioners for H(div) and H(curl) problems.

## Past editions

2020-12-14 DAH went over a proposal to properly add dual spaces in
UFL, and the consequences thereof. Now [available on the
arxiv](https://arxiv.org/abs/2101.05158).

2020-12-07 CJC covered some of the (relatively new) developments in
parallel in time stuff, going over the [introduction to
ParaDIAG](https://arxiv.org/abs/2005.09158) from Martin Gander and friends.

2020-11-30 FW covered one paper on the new hotness of using neural
nets for everything: Zongyi Li, Nikola Kovachki, Kamyar
Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart,
Anima Anandkumar, [_Fourier Neural Operator for Parametric Partial
Differential Equations_ (2020)](https://arxiv.org/abs/2010.08895)

2020-11-23 FW covered the (now sadly bitrotted) automated adaptivity
that used to be implemented in Dolfin, described in Marie E. Rognes
and Anders Logg, [_Automated Goal-Oriented Error Control I: Stationary
Variational Problems_ (2013)](https://doi.org/10.1137/10081962X).

2020-11-09 EM went through Mardal and Winther, [_Preconditioning
discretizations of systems of partial differential equations_
(2011)](https://doi.org/10.1002/nla.716).

2020-10-26 & 2020-11-02 IP talked us through the construction and analysis of the Stokes-Darcy element introduced in Mardal, Tai, and Winther, [_A robust finite element method for Darcy-Stokes flow_ (2002)](https://doi.org/10.1137/S0036142901383910). (Available in Firedrake as `FunctionSpace(triangular_mesh, "MTW", 3)`).

2020-10-12 & 2020-10-19. CJC talked us through the main points of Demkowicz and Gopalakrishnan, [_An overview of the discontinuous Petrov Galerkin method_ (2014)](https://doi.org/10.1007/978-3-319-01818-8_6).

Summer 2020. We read through [Joachim
Schöberl's](https://www.asc.tuwien.ac.at/~schoeberl/wiki/index.php/Joachim_Schöberl)
thesis on parameter-robust multigrid methods. Some [notes are
collected](schoeberl-thesis).

Autumn/Winter 2019. We read [Doug
Arnold's](http://www-users.math.umn.edu/~arnold/) book on [Finite
Element Exterior Calculus](http://bookstore.siam.org/cb93/).
