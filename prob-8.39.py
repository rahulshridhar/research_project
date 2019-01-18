import math
import _plot, _roots1, _roots2, _series2, _error

'''
The upward velocity of a rocket can be calculated as follows:
v = u ln (m/(m-q*t)) - gt

To determine the time at which velocity is 1000m/sec
'''

u = 2200  #given
v = 1000       #given
m = 160000        #given
q = 2680         #given
g1 = 9.81

def g(t):
    return u * math.log(m/(m-q*t)) - g1 * t - v

_plot.graph(g, xl=10, xu=50, title="g(t)", ylabel="g", xlabel="t")
#Graph reveals root to be between 25 and 30

_plot.graph(g, xl=25, xu=30, title="g(t)", ylabel="g", xlabel="t")
#Graph reveals root between 25 and 26, approximately 25.9

n = 4
es100 = _error.es100(n)

print('false position:')
R1 = _roots1.falsepos(g, xl=10, xu=50, es100=es100, debug=True, tab=10)
print("R = {}".format(R1))

print("\nusing bisection method:")
R1 = _roots1.bisect(g, xl=10, xu=50, es100=es100, debug=True, tab=12)
print("R = {}".format(R1))

print("\nusing secant method:")
R1 = _roots2.secant(g, xi1=10, xi2=50, es100=es100, debug=True)
print("R = {} ".format(R1))

print('\nmodified secant method:')
R1 = _roots2.modified_secant(g, x0=10, p_f=0.01, es100=es100, debug=True)
print("R = {} ".format(R1))

print("\nusing newton-rhapson method:")
def dgdf(R): return _series2.cntdif1(g, R, h=0.0001) #estimate deriv.
R1 = _roots2.newton(g, df=dgdf, x0=10, es100=es100, debug=True)
print("R = {} ".format(R1))
