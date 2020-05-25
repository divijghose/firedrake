We are reading through [Joachim Schöberl's thesis](https://www.asc.tuwien.ac.at/~schoeberl/wiki/publications/diss.pdf) on parameter robust multigrid methods.

The scheduled time is Mondays at 14:00 BST. [This calendar](https://calendar.google.com/calendar/embed?src=qbaqqtn2iiu5l6qjbf2t4aafa8%40group.calendar.google.com) contains details.

Discussion is via Zoom:

- Meeting ID: 958 2789 9769
- Password: 982161

## Notes and queries as we go

### Chapter 1

In the analysis of the multigrid methods, the theory is that of Hackbusch (approximation and smoothing properties). These days, tighter bounds are available. Matt likes the paper of [Brannick et al.](https://arxiv.org/abs/1703.10240), which expands on theory originally developed in [Falgout, Vassilevski, and Zikatanov (2005)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nla.437) and also covered in [Xu and Zikatanov's algebraic multigrid review](https://arxiv.org/abs/1611.01917).

Schöberl considers the parameter-dependent problem requiring that A<sup>ε</sup> is coercive. Patrick wonders if we can consider how the theory maps on to the case where we only have that the eigenvalues of A<sup>ε</sup> are bounded away from zero.

