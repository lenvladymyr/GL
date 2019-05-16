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

```cpu``` to describe CPU utilisation \n
```mem``` to describe memory utilisation \n
```-h [--help]``` to call help page

# Example

```
$ ./metrics.py mem

total 3981299712
available 1681469440
percent 57.8
used 1919762432
free 175157248
active 1908318208
inactive 1195720704
buffers 388591616
cached 1497788416
shared 120569856
slab 500903936
```

