# Metrics script
Script is used for getting CPU and memory utilisation metrics
# Setup
1. It needs to istall [pip](http://pip.readthedocs.org/en/latest/), [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and [psutil](https://psutil.readthedocs.io/en/latest/)

2. Create a virtualenv for the projct:
```
$ virtualenv --python=python3.7 metrics; cd metrics; source bin/activate;
```
# Usage

Script accept 1 mandatory parameter:

```
cpu
```
to describe CPU utilisation

```
mem
```
to describe memory utilisation
```
-h [--help]
```
to call help page
