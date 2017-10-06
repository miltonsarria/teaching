### many of the tools for continuous-time system analysis is in scipy.signal here there is an alternative tool that can be used


**To install the control system library for python**

Install fortran compiler

```
sudo apt-get install gfortran
```

You will also need to install BLAS and LAPACK

```
sudo apt-get install libblas-dev liblapack-dev
```

```
pip install slycot   # optional

pip install control
```

go to documentation 

http://python-control.readthedocs.io/en/latest/


Note: *the slycot library only works on some platforms, mostly linux-based. Users should check to insure that slycot is installed correctly by running the command:*

```
python -c "import slycot"
```
