import math
import _plot, _roots1, _roots2, _series2, _error

'''
Colebrook's equation is given as follows:-
0 = 1/sqrt(f) + 2.0 log(E/3.7D + 2.51/(R * sqrt(f)))

Reynolds number R can be calculated as follows:-
R = pVD/u

Solving for f analytically
g(f) = 1/sqrt(f) + 2.0 log(E/3.7D + 2.51 / (R * sqrt(f))) 

'''

E = 0.0000015   #given
D = 0.005       #given
p = 1.23        #given
V = 40          #given
u = 1.79e-5     #given

R = p * V * D/u       #Reynolds number calculation

def g(f):
    return 1/math.sqrt(f) + 2.0 * math.log10(E/(3.7*D) + 2.51 /(R * math.sqrt(f)))

_plot.graph(g, xl=0.008, xu=0.08, title="g(f)", ylabel="g", xlabel="f")
#Graph reveals root to be between 0.02 and 0.03

_plot.graph(g, xl=0.02, xu=0.03, title="g(f)", ylabel="g", xlabel="f")
#Graph reveals root between 0.028 and 0.03

n = 4
es100 = _error.es100(n)

print('false position:')
R1 = _roots1.falsepos(g, xl=0.008, xu=0.08, es100=es100, debug=True, tab=10)
print("R = {}".format(R1))

print("\nusing bisection method:")
R1 = _roots1.bisect(g, xl=0.008, xu=0.08, es100=es100, debug=True, tab=12)
print("R = {}".format(R1))

print("\nusing secant method:")
#Adjusted xi2 to 0.07 instead of 0.08
R1 = _roots2.secant(g, xi1=0.008, xi2=0.07, es100=es100, debug=True)
print("R = {} ".format(R1))

print('\nmodified secant method:')
R1 = _roots2.modified_secant(g, x0=0.008, p_f=0.01, es100=es100, debug=True)
print("R = {} ".format(R1))

print("\nusing newton-rhapson method:")
def dgdf(R): return _series2.cntdif1(g, R, h=0.0001) #estimate deriv.
R1 = _roots2.newton(g, df=dgdf, x0=0.008, es100=es100, debug=True)
print("R = {} ".format(R1))