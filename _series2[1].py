
'''
module: _series2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on truncation errors & the taylor series
- implemented from algorithms/pseudocode provided
'''

#1st order finite divided differences

def fwddif1(f, xi, h):
    "computes 1st forward finite difference"
    return (f(xi+h) - f(xi)) / float(h)

def bwddif1(f, xi, h):
    "computes 1st backward finite difference"
    return (f(xi) - f(xi-h)) / float(h)

def cntdif1(f, xi, h):
    "computes 1st centered finite difference"
    return (f(xi+h) - f(xi-h)) / float(2*h)

def Af( df1, xi, Ax):
    "computes the error propagation delta f(x)"
    #dfdx1: 1st derivative of f(x)
    #xi: reference point
    #Ax: delta x, the given error estimate
    return abs(df1(xi)) * Ax