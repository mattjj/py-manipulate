#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

from matplotlib import pyplot as plt
from manipulate import mplot

def sinc(x,A,f,z):
    return A*np.sin(2*np.pi*f*x)/(x**z)

def rundemo():
    mplot(sinc,np.arange(0.01,1,0.01),A=(1,2),f=(1,5),z=(0,1))
    plt.xlabel('x')
    plt.title(u'A sin(2πf x)/x^z')

def runtexversion():
    from matplotlib import rc
    rc('text',usetex=True)
    rc('font',family='serif')
    rundemo()
    plt.xlabel(r'$x$')
    plt.title(r'$\frac{A \sin(2\pi \cdot f \cdot x)}{x^z}$',fontsize=32)

if __name__ == '__main__':
    rundemo()
    plt.show()



























































