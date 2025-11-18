import numpy as np, scipy as sp
from scipy.integrate import odeint #ODE solver

%matplotlib inline

def dy_dt(y, t):
    return t-y


ts = linspace(0, 5, 101)