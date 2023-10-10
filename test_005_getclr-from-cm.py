import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Choose a colormap from Matplotlib
colormap = plt.cm.viridis

# Set number of colors
num_colors = 20

# Create a ListedColormap with discrete colors
discrete_cmap = ListedColormap(colormap(np.linspace(0, 1, num_colors)))

# Output RGB values
for i, rgb in enumerate(discrete_cmap.colors):
    print(f"Color {i + 1}: RGB = {rgb}")


# Plot a colorbar to visualize
plt.imshow([[i] for i in range(num_colors)], cmap=discrete_cmap, aspect='auto')
plt.colorbar(ticks=range(num_colors))
plt.show()