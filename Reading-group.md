# Firedrake reading group

An informal reading group around many things finite element. Hosted
online. Email [Lawrence
Mitchell](mailto:lawrence.mitchell@durham.ac.uk) if you'd like to
participate. Suggestions of papers and scheduling discussions also take place in the `#readinggroup` channel on the [Firedrake slack](https://www.firedrakeproject.org/contact.html#slack-slack-badge).

Scheduled time: Mondays 15:00UTC (4pm UK time). [This calendar](https://calendar.google.com/calendar/embed?src=qbaqqtn2iiu5l6qjbf2t4aafa8%40group.calendar.google.com) contains details.

Hosted via Zoom:

- Meeting ID: 928 2384 2685
- Passcode: 494089

## Upcoming sessions

July/August: Summer break


## Past editions

2021-07-12 Colin Cotter leading _Interpolating between Optimal Transport and MMD using Sinkhorn Divergences_ https://arxiv.org/abs/1810.08278

2021-06-21 Lawrence Mitchell leading _A GenEO Domain Decomposition method for Saddle Point problems_ https://arxiv.org/abs/1911.01858

2021-06-14 Scott MacLachlan leading _Textbook efficiency: massively parallel matrix-free multigrid for the Stokes system_ https://arxiv.org/abs/2010.13513

2021-05-10 Lawrence Mitchell leading _Fast parallel solution of fully implicit Runge-Kutta and discontinuous Galerkin in time for numerical PDEs, Part II: nonlinearities and DAEs_, Ben S. Southworth, Oliver Krzysik, Will Pazner https://arxiv.org/pdf/2101.01776.pdf the result is not quite as neat as the linear case (you do need all the stage vectors), but the results looked pretty good. Should again be implementable inside [irksome](https://github.com/firedrakeproject/irksome).

2021-04-26 Lawrence Mitchell leading _Fast parallel solution of fully implicit Runge-Kutta and discontinuous Galerkin in time for numerical PDEs, Part I: the linear setting_, Ben S. Southworth, Oliver Krzysik, Will Pazner, Hans De Sterck https://arxiv.org/pdf/2101.00512.pdf might be reasonably be implementable as a PC inside [irksome](https://github.com/firedrakeproject/irksome).

2021-04-12 & 2021-04-19 Alberto Paganini went through _An overview on deep learning-based approximation methods for partial differential equations_, Christian Beck, Martin Hutzenthaler, Arnulf Jentzen, and Benno Kuckuck https://arxiv.org/pdf/2012.12348.pdf This mathematical paper summarises known theorems about approximation of PDEs using neural networks. It also has a substantial bibliography with pointers to applications in many areas.

2021-03-15 Francis Aznaran went through _Positivity-preserving methods for population models_, Sergio Blanes, Arieh Iserles, Shev Macnamara https://arxiv.org/pdf/2102.08242.pdf it turns out to be quite tricky, approximations of operator exponentials and Padé approximations were at the forefront.

2021-03-08 Thomas Gibson and Jack Betteridge went through _Multigrid preconditioners for the hybridized Discontinuous Galerkin discretisation of the shallow water equations_, Jack D. Betteridge, Thomas H. Gibson, Ivan G. Graham, Eike H. Mueller https://arxiv.org/pdf/2004.09389.pdf

2021-02-22 Alexei Gazca went over _Multilevel methods for nonuniformly elliptic operators_, Long Chen, Ricardo H. Nochetto, Enrique Otarola, Abner J. Salgado https://arxiv.org/pdf/1403.4278. You can do fractional laplacians with one extra space dimension (should be able to do 3D+1 in Firedrake with a few additions in UFL for geometry terms).

2021-02-15 Matt Knepley went over _Accurate Discretization Of Poroelasticity Without Darcy Stability -- Stokes-Biot Stability Revisited_, Kent-Andre Mardal, Marie E. Rognes, Travis B. Thompson https://arxiv.org/pdf/2007.10012.pdf the headline message is that you can use more element pairs than you thought you could and still have a parameter-robust discretisation.

2021-02-01 Lawrence Mitchell went over _Space-time block preconditioning for incompressible flow_, Danieli, Southworth, Wathen https://arxiv.org/abs/2101.07003

2020-12-14 David Ham went over a proposal to properly add dual spaces in
UFL, and the consequences thereof. Now [available on the
arxiv](https://arxiv.org/abs/2101.05158).

2020-12-07 Colin Cotter covered some of the (relatively new) developments in
parallel in time stuff, going over the [introduction to
ParaDIAG](https://arxiv.org/abs/2005.09158) from Martin Gander and friends.

2020-11-30 Florian Wechsung covered one paper on the new hotness of using neural
nets for everything: Zongyi Li, Nikola Kovachki, Kamyar
Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart,
Anima Anandkumar, [_Fourier Neural Operator for Parametric Partial
Differential Equations_ (2020)](https://arxiv.org/abs/2010.08895)

2020-11-23 Florian Wechsung covered the (now sadly bitrotted) automated adaptivity
that used to be implemented in Dolfin, described in Marie E. Rognes
and Anders Logg, [_Automated Goal-Oriented Error Control I: Stationary
Variational Problems_ (2013)](https://doi.org/10.1137/10081962X).

2020-11-09 Eder Medina went through Mardal and Winther, [_Preconditioning
discretizations of systems of partial differential equations_
(2011)](https://doi.org/10.1002/nla.716).

2020-10-26 & 2020-11-02 Ioannis Papadopoulos talked us through the construction and analysis of the Stokes-Darcy element introduced in Mardal, Tai, and Winther, [_A robust finite element method for Darcy-Stokes flow_ (2002)](https://doi.org/10.1137/S0036142901383910). (Available in Firedrake as `FunctionSpace(triangular_mesh, "MTW", 3)`).

2020-10-12 & 2020-10-19. Colin Cotter talked us through the main points of Demkowicz and Gopalakrishnan, [_An overview of the discontinuous Petrov Galerkin method_ (2014)](https://doi.org/10.1007/978-3-319-01818-8_6).

Summer 2020. We read through [Joachim
Schöberl's](https://www.asc.tuwien.ac.at/~schoeberl/wiki/index.php/Joachim_Schöberl)
thesis on parameter-robust multigrid methods. Some [notes are
collected](schoeberl-thesis).

Autumn/Winter 2019. We read [Doug
Arnold's](http://www-users.math.umn.edu/~arnold/) book on [Finite
Element Exterior Calculus](http://bookstore.siam.org/cb93/).
