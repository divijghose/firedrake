Date and time 2025-11-18 1600 UTC+1

# Action Items
1. **Pick Chair and Minuter** (LC to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: CW (minuter), LC, DH, AC, DRS, IM, PB

Apologies:

## CW: pyadjoint release

https://github.com/dolfin-adjoint/pyadjoint/issues/238

tested in https://github.com/firedrakeproject/firedrake/pull/4724

any objections?

DH: Nope. Go ahead. JD has said that he is happy for us to make releases as and when we like.

## DRS: example codes

See also [jupytext](https://jupytext.readthedocs.io/en/latest/)

DH: Need to make sure that notebooks shown on the website have output. And push them to the notebooks repository in the same way as we do for Colab. This could be done during website generation step.

Do nothing for the demos, would need to rst -> jupytext which is a LOT of work and has limited benefit.

Takeaway: We are interested in switching the format of Jupyter notebooks. Not for the demos though.

## CW: what is in our global namespace?

Discussion resulting from https://github.com/firedrakeproject/firedrake/pull/4722:
* what goes into the top level `firedrake` namespace? what goes into `firedrake.output`, `firedrake.ml` etc?

We kind of liked
```py
import firedrake as fd
from firedrake.dsl import *
```
so that we can namespace most things but still have access to the 'language' elements without needing a prefix. However, does this include `FunctionSpace`, `Function`, etc? We struggled to draw the line.

Regardless we definitely need to define an `__all__` in the `__init__.py` so we don't get all the modules (like `mesh`) imported.

## Merge PRs

* https://github.com/dolfin-adjoint/pyadjoint/pull/233 - merged
* https://github.com/firedrakeproject/firedrake/pull/4722 - approved but needs an announcement when it goes in

## Date of next meeting

**Note: next Tuesday is likely going to be a strike day**

1600 UTC [2025-11-25](./Firedrake-meeting-2025-11-25)
