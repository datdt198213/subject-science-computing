import numpy as np
from scipy.optimize import curve_fit

# Define the equation for the curve
def func(x, a, b, c):
    return a + b*x + c*x**2

# Define the data set
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([1, 3, 5, 4, 3])

# Use curve_fit to find the parameter set that minimizes SSE
popt, pcov = curve_fit(func, xdata, ydata)

# Print the parameter set
print(popt)