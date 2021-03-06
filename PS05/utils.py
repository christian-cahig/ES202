import numpy
from typing import Union

def prob01_ak(
        mode:str,
        k:int=0,
        a_0:Union[None,float,int]=None,
        a_1:Union[None,float,int]=None
    ) -> float:
    
    if mode.lower() not in {"even", "odd"}:
        raise ValueError(f"Argument `mode` must be either 'even' or 'odd' (case insensitive).")
    k = max(0,int(k))
    
    a_k = (-1)**k
    for j in range(k):
        if mode.lower() == "even":
            a_k *= (4*j + 1) / (4*j**2 + 6*j + 2)
        else:
            a_k *= (4*j + 3) / (4*j**2 + 10*j + 6)
    
    if (
        (mode.lower() == "even")
        and (a_0 != None)
    ):
        return a_k * a_0
    elif (
        (mode.lower() == "odd")
        and (a_1 != None)
    ):
        return a_k * a_1
    else:
        return a_k

def prob04_Pk(
        k:int=0,
        a_0:Union[None,float,int]=None
    ) -> float:

    k = max(0,int(k))

    P_k = (-1)**k
    for j in range(k):
        P_k *= (2*j +5) / (j**2 + 7*j + 10)
    
    if a_0 != None:
        return P_k * a_0
    else:
        return P_k