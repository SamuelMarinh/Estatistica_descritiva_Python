import matplotlib.pyplot as plt
import random

# Sample data
eixo_y = [random.randint(1, 20) for _ in range(10)]
eixo_x = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10']

# Plotting the line
plt.pie(eixo_y, labels=eixo_x, radius=1)

# Customizing the plot
plt.title("Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
