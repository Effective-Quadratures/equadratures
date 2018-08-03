"""The Exponential distribution."""
import numpy as np
from distribution import Distribution
from recurrence_utils import custom_recurrence_coefficients
from scipy.stats import expon

class Exponential(Distribution):
    """
    The class defines a Exponential object. It is the child of Distribution.
    
    :param double rate:
		Rate parameter of the Exponential distribution.
    """
    def __init__(self, rate=None):
        self.rate = rate
        if (self.rate is not None) and (self.rate > 0.0):
            self.mean = 1.0/self.rate
            self.variance = 1.0/(self.rate)**2
            self.skewness = 2.0
            self.kurtosis = 6.0
            self.bounds = np.array([0.0, np.inf])
        
    def getDescription(self):
        """
        A description of the Exponential distribution.
        
        :param Exponential self:
            An instance of the Exponential class.
        :return:
            A string describing the Exponential distribution.
        """
        text = "An exponential distribution with a rate parameter of"+str(self.rate)+"."
        return text

    def getPDF(self, points=None):
        """
        An exponential probability density function.
        
        :param Exponential self:
            An instance of the Exponential class.
        :param matrix points:
            Matrix of points for defining the probability density function.
        :return:
            An array of N values over the support of the distribution.
        :return:
            Probability density values along the support of the exponential distribution.
        """
        if points is not None:
            return expon.pdf(points, loc=0.0, scale=1.0)
        else: 
            raise(ValueError, 'Please digit an input for getPDF method')

    def getiCDF(self, xx):
        """
        An inverse exponential cumulative density function.
        
        :param Exponential self:
            An instance of the Exponential class.
        :param array xx:
            A numpy array of uniformly distributed samples between [0,1].
        :return:
            Inverse CDF samples associated with the exponential distribution.
        """
        return expon.ppf(xx, loc=0.0, scale=1.0)

    def getCDF(self, points=None):
        """
        An exponential cumulative density function.
        
        :param Exponential self:
            An instance of the Exponential class.
        :param matrix points:
            Matrix of points for defining the cumulative density function.
        :return:
            An array of N values over the support of the distribution.
        :return:
            Cumulative density values along the support of the exponential distribution.
        """
        if points is not None:
            return expon.cdf(points, loc=0.0, scale=1.0)
        else: 
            raise(ValueError, 'Please digit an input for getCDF method')
    def getSamples(self, m=None):
        """
        Generates samples from the Exponential distribution.
         
         :param Expon self:
             An instance of the Exponential class.
         :param integer m:
              Number of random samples. If no value is provided, a default of 5e05 is assumed
         :return:
             A N-by-1 vector that contains the samples.
        """
        if m is not None:
            number = m
        else:
            number = 500000
        return expon.rvs(loc=0.0, scale=1.0, size= number, random_state=None)
