#Using Monte Carlo methond pricing stock and derivatives based on Black_shole_Merton Method
import numpy

def bsmCall_MC(S0,K,T,r,sigma,n):#pricing bls European call price
    import numpy
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    hT = numpy.maximum(ST-K,0)
    C0 = numpy.exp(-r*T)*numpy.sum(hT)/n
    return C0

def bsmPut_MC(S0,K,T,r,sigma,n):#pricing bls European Put price
    import numpy
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    hT = numpy.maximum(K-ST,0)
    C0 = numpy.exp(-r*T)*numpy.sum(hT)/n
    return C0

def bsmStock_MC(S0,T,r,sigma,n):#pricing stock price
    import numpy
    z = numpy.random.standard_normal(n)
    ST = S0*numpy.exp((r-0.5*sigma**2)*T+sigma*numpy.sqrt(T)*z)
    ST = numpy.mean(ST)
    return ST