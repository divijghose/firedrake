We are reading through [Joachim Schöberl's thesis](https://www.asc.tuwien.ac.at/~schoeberl/wiki/publications/diss.pdf) on parameter robust multigrid methods.

The scheduled time is Mondays at 14:00 BST. [This calendar](https://calendar.google.com/calendar/embed?src=qbaqqtn2iiu5l6qjbf2t4aafa8%40group.calendar.google.com) contains details.

Discussion is via Zoom:

- Meeting ID: 958 2789 9769
- Password: 982161

## Notes and queries as we go

### Chapter 1

#### 2020-05-25

In the analysis of the multigrid methods, the theory is that of Hackbusch (approximation and smoothing properties). These days, tighter bounds are available. Matt likes the paper of [Brannick et al.](https://arxiv.org/abs/1703.10240), which expands on theory originally developed in [Falgout, Vassilevski, and Zikatanov (2005)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nla.437) and also covered in [Xu and Zikatanov's algebraic multigrid review](https://arxiv.org/abs/1611.01917).

Schöberl considers the parameter-dependent problem requiring that A<sup>ε</sup> is coercive. Patrick wonders if we can consider how the theory maps on to the case where we only have that the eigenvalues of A<sup>ε</sup> are bounded away from zero.

A request that we carefully unpick, when going through proofs, all of the constants in the inequalities of the form a ≼ b (so that we see where all the bits came from).

### Chapter 2

#### 2020-06-01
We covered the basics of finite element approximation and showed how conforming discretisations can fail for parameter dependent problems. Ivan notes that his [masters thesis](https://aaltodoc.aalto.fi/bitstream/handle/123456789/31490/master_Yashchuk_Ivan_2018.pdf?sequence=1&isAllowed=y) contains an example of this for the case of the Poisson equation with varying coefficients (in section 3.3).

We got a little hung up on Hilbert space interpolation. Gonzalo suggests that this is going to be used in the multigrid convergence proof later (this theory is in [Bramble](https://doi.org/10.2307/2153359)). [Brenner & Scott](https://doi.org/10.1007/978-0-387-75934-0) have a reasonably self-contained overview of Hilbert space interpolation and its relation to finite elements in Chapter 14 of their book.

#### 2020-06-08

We introduced more finite element theory. In particular Scott-Zhang interpolation, inverse inequalities, and partition of unity methods. We then started on theory for parameter-dependent problems and the migration to a mixed formulation. We showed that the mixed problem B<sup>ε</sup> has parameter-dependent continuity constant in the parameter-dependent V×εQ-norm. We finished with discussion of the remark before Theorem 2.8 and the introduction of the dual ||·||<sub>Q,0</sub> norm, which is introduced such that ΛV has closed range with respect to this new norm. Gonzalo wrote up some more detailed notes [explaining this point](docs/operators-dense-range-inf-sup.pdf).
