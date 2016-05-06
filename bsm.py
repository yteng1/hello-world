#Using Monte Carlo methond pricing stock and derivatives based on Black_shole_Merton Method
import numpy as np
import scipy as sp

def bsmCall_MC(S0,K,T,r,sigma,n):#pricing bls European call price
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    hT = numpy.maximum(ST-K,0)
    C0 = numpy.exp(-r*T)*numpy.sum(hT)/n
    return C0

def bsmPut_MC(S0,K,T,r,sigma,n):#pricing bls European Put price
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    hT = numpy.maximum(K-ST,0)
    C0 = numpy.exp(-r*T)*numpy.sum(hT)/n
    return C0

def bsmStock_MC(S0,T,r,sigma,n):#pricing stock price
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    ST = numpy.mean(ST)
    return ST

# Analytical Black-Scholes-Merton(BSM) Formula
def bsm_Call_Value(S0,K,T,r,sigma):
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2=(log(S0/K)+(r-0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    value=(S0*sp.stats.norm.cdf(d1,0.0,1.0)-K*exp(-r*T)*sp.stats.norm.cdf(d2,0.0,1.0))
    return value

# Vega Function
def bsm_vega(S0,K,T,r,sigma):
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    vega=S0*sp.stats.norm.cdf(d1,0.0,1.0)*np.sqrt(T)
    return vega

# Implied volatility function
def bsm_Call_imp_vol(S0,K,T,r,C0,sigma_est,it=100):
    for i in range(it):
        sigma_est-=((bsm_Call_Value(S0,K,T,r,sigma)-C0)/bsm_vega(S0,K,T,r,sigma_est))
        return sigma_est

    
