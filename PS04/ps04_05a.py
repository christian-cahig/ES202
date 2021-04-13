import numpy

C = 1e-6
L = 1

def Q(t:float) -> float:
    return -50.0*C*numpy.exp(t / numpy.sqrt(L*C)) - \
        50.0*C*numpy.exp(-t / numpy.sqrt(L*C)) + \
        100.0*C

def I(t:float) -> float:
    return -50.0*numpy.sqrt(C/L)*numpy.exp(t / numpy.sqrt(L*C)) + \
        50.0*numpy.sqrt(C/L)*numpy.exp(-t / numpy.sqrt(L*C))

print(f"Initial charge: {Q(0)} C\nInitial current: {I(0)} A")
print(f"At t=0.001 s,\n   charge: {Q(0.001)} C\n   current: {I(0.001)} A")