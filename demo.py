# Example from Visual Studio Code's official website. 
# https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100) # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))      # Plot the sine of each x point


plt.showme()                  # Display the plot
