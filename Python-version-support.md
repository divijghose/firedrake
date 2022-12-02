Firedrake (and associated packages) aims to support the same range of Python versions as [Python itself](https://devguide.python.org/versions/#versions). Once a Python version reaches end-of-life Firedrake may not run correctly as it may rely on newer language features.

## Ubuntu/Debian LTS

Ubuntu and Debian LTS versions receive security updates for a longer period of time than Python versions are supported. As such it is possible for the Python version provided by the distro to not be actively supported. To resolve this issue we recommend using the [deadsnakes ppa](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) to install a more up-to-date Python.