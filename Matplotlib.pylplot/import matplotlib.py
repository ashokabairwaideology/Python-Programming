import matplotlib.pyplot as plt
import numpy as np

N = 8
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.random.rand(N)

# Normal bar plot
plt.bar(x, y)
plt.xlabel('Number')
plt.ylabel('Values')
plt.title('Bar Plot with Numeric X-axis')
plt.show()

# Bar plot with color
plt.bar(x, y, color='g')
plt.xlabel('Number')
plt.ylabel('Values')
plt.title('Green Bar Plot with Numeric X-axis')
plt.show()

# Bar plot with string x-axis
plt.bar(np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']), y, color='r')
plt.xlabel('Letters')
plt.ylabel('Values')
plt.title('Red Bar Plot with String X-axis')
plt.show()

# Combined bar plot
x_combined = np.arange(26)
y_combined = np.random.randint(0, 50, 26)
plt.bar(x_combined, y_combined, alpha=0.6)
plt.xlabel('Index')
plt.ylabel('Random Values')
plt.title('Combined Bar Plot with Adjusted Titles')
plt.show()