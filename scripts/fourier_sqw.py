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
N = 50        # number of terms of Fourier series
res = 500      # resolution of each plot line (> 500)
x0 = 0         # interval initial value
xf = +8*pi     # interval final value

#=====================================================================================
#                                  DEFINING FUNCTION
#-------------------------------------------------------------------------------------
# Square wave (step) function
def sq_wave(x):
    y = -1*np.ones(len(x))
    # y = 1, if -pi < x < pi
    step_it = 0
    while step_it < xf:
        y[np.where(np.logical_and(x>=0+step_it, x<=+pi+step_it))] = 1 
        step_it = step_it + 2*pi
    # y = -1, elsewhere
    #
    return y
# Creating x,y points for the chosen interval
delta_x = (xf - x0)/res
x = np.arange(x0, xf+delta_x, delta_x)
y = sq_wave(x)

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
    if k%2!=0:
        M[k_it, :] = (4/pi) * np.sin(k*x)/k
    Y = Y + M[k_it, :]

#=====================================================================================
#         PLOTTING FUNCTION + FIRST N TERMS OF SERIES + TRANSFORMED FUNCTION
#-------------------------------------------------------------------------------------
fig = plt.figure(figsize=[10,8])
ax = plt.axes(projection="3d")
# Plotting each Fourier Series term
for k_it in range(N):
    if k_it%2==0:
        ax.plot3D(x, 2*k_it*np.ones(res2), M[k_it,:])  # (x, y, z)
        kf = 2*k_it
# Removing axis ticks
ax.set_zticks([])
ax.set_xticks([]) 
ax.set_yticks([]) 
# Plotting function and Series approximation over each other 
ax.plot3D(x, (kf+9)*np.ones(res2), y, 'k--')
ax.plot3D(x, (kf+9)*np.ones(res2), Y, 'tab:gray')
# Setting title
title = r'Square Wave: $SW(x) = \frac{4}{\pi} \left[ \frac{\sin x}{1} + \frac{\sin 3x}{3} +\frac{\sin 5x}{5} + \frac{\sin 7x}{7} + ... \right]$ (N terms = ' + str(N) + ')'
plt.suptitle(title, size=16)
# Adjusting plot margins
plt.subplots_adjust(left=0, right=1, bottom=0, top=.9)
plt.savefig('sqw'+str(N)+'.jpg', dpi=400, bbox_inches='tight')
plt.show()
