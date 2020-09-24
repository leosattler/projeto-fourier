#=====================================================================================
#                                       IMPORTS
#-------------------------------------------------------------------------------------
import numpy as np
pi = np.pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#=====================================================================================
#                                       INPUTS
#-------------------------------------------------------------------------------------
N = 20         # number of terms of Fourier series
res = 500      # resolution of each plot line (> 500)
x0 = -pi         # interval initial value
xf = +pi     # interval final value

#=====================================================================================
#                                  DEFINING FUNCTION
#-------------------------------------------------------------------------------------
# Square wave (step) function
def func(x):
    y = x
    #
    return y
# Creating x,y points for the chosen interval
delta_x = (xf - x0)/res
x = np.arange(x0, xf+delta_x, delta_x)
y = func(x)

#=====================================================================================
#                         DEFINING FOURIER SERIES OF FUNCTION
#-------------------------------------------------------------------------------------
# real resolution = res + 1 (due to np.arange)
res2 = res+1
# Matrix of Fourier terms values
M = np.zeros([N, res2])
# Array for sum of Fourier terms (final series approximation)
Y = np.zeros(len(x))
# Loop over Fourier terms 
for k_it in range(N):
    k = k_it + 1
    if k%2==0:
        M[k_it, :] = -np.sin(k*x)/k
    else:
        M[k_it, :] = np.sin(k*x)/k
    Y = Y + M[k_it, :]
    
#=====================================================================================
#                     PLOTTING FUNCTION + FIRST N TERMS OF SERIES
#-------------------------------------------------------------------------------------
fig = plt.figure(figsize=[10,8])
ax = plt.axes(projection="3d")
# Plotting each Fourier Series term
for k_it in range(N):
    #if k_it%2==0:
    ax.plot3D(x, 2*k_it*np.ones(res2), 2*M[k_it,:])  # (x, y, z)
    kf = 2*k_it
# Removing axis ticks
ax.set_zticks([])
ax.set_xticks([]) 
ax.set_yticks([]) 
# Plotting function and Series approximation over each other 
ax.plot3D(x, (kf+9)*np.ones(res2), y, 'k--')
ax.plot3D(x, (kf+9)*np.ones(res2), 2*Y, 'tab:gray')
# Setting title
title = r'f(x) = x: $F(x) = 2 \left[ \frac{\sin x}{1} - \frac{\sin 2x}{2} +\frac{\sin 3x}{3} - \frac{\sin 4x}{4} + ... \right]$ (N terms = ' + str(N) + ')'
plt.suptitle(title, size=16)
# Adjusting plot margins
plt.subplots_adjust(left=0, right=1, bottom=0, top=.9)
plt.savefig('x'+str(N)+'.jpg', dpi=400, bbox_inches='tight')
plt.show()
