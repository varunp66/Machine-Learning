from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

x = np.array([112, 232, 233, 456, 643,643, 654, 6534])
y = np.array([33432, 34345, 55643, 34555, 76543, 67644, 75354, 75456])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x,y, 'ro' , color='blue')   # Display the points

plt.ylable('Price')
plt.xlable('Size of House')

plt.axis([0.600, 0.500])

plt.plot(x, x*slope+intercept, 'green')   #This will make the linear regression

plt.plot()

plt.show()
