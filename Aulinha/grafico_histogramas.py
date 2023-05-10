import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=25, color='b')

plt.title("Plot")
plt.xlabel("X-axis")
plt.ylabel("Frequency")

plt.show()