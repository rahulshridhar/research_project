#module: _roots2.py
#author: Rahul Shridhar
#implements bracketing methods:
# - Newton-Raphson
# - Secant
# - Modified Secant

def newton(f, df, x0, es100=.5, imax=1000, debug=False):
    x0 = float(x0)
    iter = 0
    while True:
        xr = x0 - f(x0) / df(x0)
        if xr: ea = abs(1 - x0/xr)
        if debug: print('iter={}, xr={}, ea={:%}'.format(iter, xr, ea))
        if ea*100 < es100 or iter > imax:
            break
        iter += 1
        x0 = xr
    #end while
    return xr
#end newton()

def secant(f, xi1, xi2, es100=.5, imax=1000, debug=False):
    iter = 0
    while True:
        xr = xi2 - ((f(xi2) * (xi1-xi2)) / (f(xi1) - f(xi2)))
        if xr: ea = abs(1 - xi2/xr)
        if debug: print('iter={}, xr={}, ea={:%}'.format(iter, xr, ea))
        if ea*100 < es100 or iter > imax:
            break
        iter += 1
        xi1 = xi2
        xi2 = xr
    #end while
    return xr
#end secant()

def modified_secant(f, x0, p_f, es100=.5, imax=1000, debug=False):
    x0 = float(x0)
    p_f = float(p_f)    #perturbation factor
    iter = 0
    while True:
        xr = x0 - ((p_f * x0 * f(x0)) / (f(x0 + p_f * x0) - f(x0)))
        if xr: ea = abs(1 - x0/xr)
        if debug: print('iter={}, xr={}, ea={:%}'.format(iter, xr, ea))
        if ea*100 < es100 or iter > imax:
            break
        iter += 1
        x0 = xr
    #end while
    return xr
#end modified_secant()
