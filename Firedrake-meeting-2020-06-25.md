Date and time 2020-06-25 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. DH: ~Find time to fix to get final complex sprint test passing.~ ~Now passing~ Continue reviewing
1. \*\*: Add `--remove-build-files` to make install smaller; convert this to an issue

# Minutes

Present:

Apologies:

## Status of Complex Sprint Merge (added by RWH)
What still needs to be done?

## RWH - CSE minisymposterium

### Note identical deadlines:
 - Deadline for submission of poster abstracts: August 31, 2020 (11:59 p.m. Eastern Time)
 - Deadline for submission of minisymposterium proposals: August 31, 2020 (11:59 p.m. Eastern Time)
Minisymposterium has to list all poster titles when it is proposed, so poster submissions need to be in already.

### Proposed Solution:
RWH will put together Qualtrics survey to be circulated amongst relevant circles ASAP containing minisymposterium title and abstract which will collect poster abstracts which can then be submitted with the final minisymposterium. RWH just needs minisymposterium title, abstract and submission deadline (e.g. August 25th 2020).

## Tuomas Karna - Equispaced Coordinate Fields (added by RWH)
- Should coordinates be in equispaced function space by default?
- Should `FunctionSpace` constructor have the variant as an argument?

See https://github.com/firedrakeproject/firedrake/pull/1732 

## RWH - Should `cell_node_map` be `None` for a VertexOnlyMesh?
PyOP2 has an apparently implicit Identity map which would ideally be implemented for a VertexOnlyMesh.
To use this you have to set the `map` argument to `None` when creating a PyOP2 `Arg`:
```
class Arg(object):
    ...
    def __init__(self, data=None, map=None, access=None, lgmaps=None, unroll_map=False):
        ...
        :param map:  A :class:`Map` to access this :class:`Arg` or the default
                     if the identity map is to be used.
```
How should this be best utilised (if at all)?

## Date of next meeting
2020-06-30 15:00UTC (16:00BST)
