from time import time
from math import exp,sqrt,log
import random
from numpy import *

def MC_SDE(S0,K,T,r,sigma,M,I):
    '''
    Parameters
    ===========
    S0 - current stock price
    K - Strike price
    T - Time to mature
    r - risk free rate
    sigma - historical volatility
    M - number of time steps
    I - number of simulation times

    Returns
    =======
    C0 - averaged european call option price
    S - All simulated path

    '''
    dt = T/M
    random.seed()
    S=S0*exp(cumsum((r-0.5*sigma**2)*dt+sigma*sqrt(dt)*random.standard_normal((M+1,I)),axis=0))
    S[0]=S0
    C0 = exp(-r*T)*sum(maximum(S[-1]-K,0))/I
    return C0,S


