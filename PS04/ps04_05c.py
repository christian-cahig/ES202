import numpy

C = 1e-6
L = 1

C_4 = (100.0*C) / (1.0 - 1.0e6*L*C)
C_1 = 500.0 * numpy.sqrt(L*C) * C_4
C_2 = 500.0 * numpy.sqrt(L*C) * C_4

print(f"C_1 = {C_1}; C_2 = {C_2}; C_4 = {C_4}")

def Q(t:float) -> float:
    return C_1*numpy.exp(t / numpy.sqrt(L*C)) + \
        C_2*numpy.exp(-t / numpy.sqrt(L*C)) + \
        C_4*numpy.sin(1000*t)

def I(t:float) -> float:
    return (C_1/numpy.sqrt(L*C))*numpy.exp(t / numpy.sqrt(L*C)) - \
        (C_2/numpy.sqrt(L*C))*numpy.exp(-t / numpy.sqrt(L*C)) + \
        1000*C_4*numpy.cos(1000*t)

print(f"Initial charge: {Q(0)} C\nInitial current: {I(0)} A")
print(f"At t=0.001 s,\n   charge: {Q(0.001)} C\n   current: {I(0.001)} A")