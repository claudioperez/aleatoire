import itertools

# Scientific computing libraries
import numpy as np # Array manipulation / matrix computations
import scipy.linalg as linalg # Additional linear algebra functions
import scipy.stats as stats # Probability distributions
import scipy.optimize as optimize 
from autograd import grad # Algorithmic differentiation

import matplotlib.pyplot as plt # Plotting library
from mpl_toolkits.mplot3d import Axes3D

# Convenient references to standard normal functions
phi    = stats.norm.pdf
Phi    = stats.norm.cdf
invPhi = stats.norm.ppf
mvn = stats.multivariate_normal.pdf
MVN = stats.multivariate_normal.cdf