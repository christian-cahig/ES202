import numpy

g = 32.17
k = 4.0
m = 2.0 / g

lambda_1 = (-1.0 + numpy.sqrt(1.0 - 4.0*k*m)) / (2.0*m)
lambda_2 = (-1.0 - numpy.sqrt(1.0 - 4.0*k*m)) / (2.0*m)
C_3 = (-8.0) / (256.0 + 4096*m**2 - 128.0*m*k + k**2)
C_4 = (-64.0*m + k) / (256.0 + 4096*m**2 - 128.0*m*k + k**2)
C_1 = (lambda_2*C_3 - 8.0*C_4 + 3.0 + 3.0*lambda_2) / (lambda_1 - lambda_2)
C_2 = (-lambda_1*C_3 + 8.0*C_4 - 3.0 - 3.0*lambda_1) / (lambda_1 - lambda_2)

def y(t:float) -> float:
    return C_1*numpy.exp(lambda_1*t) + \
        C_2*numpy.exp(lambda_2*t) + \
        C_3*numpy.cos(8.0*t) + C_4*numpy.sin(8.0*t)

def y_prime(t:float) -> float:
    return lambda_1*C_1*numpy.exp(lambda_1*t) + \
        lambda_2*C_2*numpy.exp(lambda_2*t) + \
        8.0*C_4*numpy.cos(8.0*t) - 8.0*C_3*numpy.sin(8.0*t)

print(f"Initial position: {y(0)}\nInitial velocity: {y_prime(0)}")