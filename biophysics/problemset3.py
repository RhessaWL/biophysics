import numpy as np, scipy as sp
from scipy.integrate import odeint #ODE solver
from pylab import *

#matplotlib inline

def dy_dt(y, t):
    return t-y


ts = np.linspace(0, 5, 101)
y0=1.0 # initial condition
ys = odeint(dy_dt, y0, ts) #ODE engine arugments

plot(ts, ys)
xlabel('t')
ylabel('y')