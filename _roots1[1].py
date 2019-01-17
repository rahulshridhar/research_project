#module: _roots1.py
#author: Rahul Shridhar
#implements bracketing methods:
# - bisection
# - false position

def bisect(f, xl, xu, es100=.1, imax=1000, debug=False, tab=10):
    xl,xu = float(xl),float(xu)
    ea = 1.0  #assume 100% relative error to begin
    iter = 0
    x0 = xl
    if debug and tab:
        print('{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}'
              .format('iter','xl','xu','xr','ea', t=tab))
    while True:
        xr = (xl + xu) / 2.
        iter += 1
        if xr: ea = abs(1 - x0/xr)
        if debug:
            print(('{:<{t}}{:<{t}.4}{:<{t}.4}{:<{t}.4}{:<{t}.4%}' if tab
                   else'iter={}, xl={}, xu={}, xr={}, ea={:%}')
                  .format(iter, xl, xu, xr, ea, t=tab))
        test = f(xl)*f(xr)
        test = float(test)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    #end while()
    return xr
#end bisect()

def falsepos(f, xl, xu, es100=.002, imax=1000, debug=False, tab=10):
    xl,xu = float(xl),float(xu)
    ea = 1.0  #assume 100% relative error to begin
    iter = 0
    x0 = xl
    if debug and tab:
        print('{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}'
              .format('iter','xl','xu','xr','ea', t=tab))
    while True:
        xr = xu - ((f(xu) * (xl - xu)) / (f(xl) - f(xu)))
        iter += 1
        if xr: ea = abs(1 - x0/xr)
        if debug:
            print(('{:<{t}}{:<{t}.4}{:<{t}.4}{:<{t}.4}{:<{t}.4%}' if tab
                   else'iter={}, xl={}, xu={}, xr={}, ea={:%}')
                  .format(iter, xl, xu, xr, ea, t=tab))
        test = f(xl)*f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    #end while()
    return xr
#end falsepos()