import json
import numpy as np
import scipy.stats
import scipy.special
from scipy.special import gamma as gamma_func

def _weibull_mean(shape,scale):
    r"""
    \mathrm{E}(X)=\lambda \Gamma\left(1+\frac{1}{k}\right)
    """
    return scale*gamma_func(1+1/shape)

def _weibull_variance(shape, scale):
    r"""
    given $\lambda$ (`scale`) and $k$ (`shape`), the variance is computed as:
    \operatorname{var}(X)=\lambda^{2}\left[\Gamma\left(1+\frac{2}{k}\right)-\left(\Gamma\left(1+\frac{1}{k}\right)\right)^{2}\right]
    """
    return scale**2 * (gamma_func(1+2/shape)-gamma_func(1+1/shape)**2)

def weibull_shape(mean,stdDev=None,cov=None):
    if stdDev is None:
        stdDev = cov*mean
    return (stdDev/mean)**(-1.086)

def weibull_scale(mean,stdDev=None,cov=None):
    if stdDev is None:
        stdDev = cov*mean
    scale =  lambda shape: mean/(gamma_func(1+1/shape))
    return scale(weibull_shape(mean, stdDev))

def normal(mean, stdDev,**kwds):

    return scipy.stats.norm(loc=mean, scale=stdDev)

def lognormal(mean, stdDev, **kwds):
    s = np.sqrt(np.log(stdDev**2/mean**2 + 1))
    mu = mean**2/np.sqrt(stdDev**2+mean**2)
    return scipy.stats.lognorm(s=s,scale=mu)

def gumbel(alphaparam=None, betaparam=None, mean=None, stdDev=None,**kwds):
    if mean is not None and stdDev is not None:
        scale = np.sqrt(6)/np.pi*stdDev
        return scipy.stats.gumbel_r(
            loc=mean-np.euler_gamma*scale,
            scale=scale
        )

mapping = {
    'gumbel': gumbel,
    'normal': normal,
    'lognormal': lognormal
}

def load_rv_from_dicts(s):
    return [
        mapping[d['distribution']](**d) for d in s
    ]
