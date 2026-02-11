If the decision is taken to make a breaking API change to Firedrake then if at all possible users should receive a warning for an entire major release cycle.

Changes should also be announced on the `#general` Slack channel to make everyone aware.

### Example

To demonstrate this with an example consider the following case:

* It is January 2026 and a decision has been made to deprecate a feature. The current release is 2025.10.2.
* A warning like the following should be added to the `main` branch:
  ```py
  warnings.warn("Feature X has been deprecated, please use Y instead", FutureWarning)
  ```
* In April version 2026.4.0 is released. Users can now see the deprecation warning and take action.
* Any time following this release the feature (and warning) may now be removed in the `main` branch, to appear in the 2026.10.0 release. If possible it may be valuable to catch instances of the deprecated usage and fail with a helpful error message.

### Exceptions

There are sometimes cases where this deprecation process will not work and functionality will need to break without warning for users. This is to be avoided as much as possible and even more care must be taken to warn the community when such changes occur.