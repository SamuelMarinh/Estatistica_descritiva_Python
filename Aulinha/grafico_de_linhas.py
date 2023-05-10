import matplotlib.pyplot as plt
import random

# Sample data
eixo_X1 = sorted([random.randint(1, 20) for _ in range(5)])
eixo_y2 = [random.randint(1, 20) for _ in range(5)]
eixo_T = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10']

# Plotting the line
plt.plot(eixo_X1,eixo_y2,'-p')

# Customizing the plot
plt.title("Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
