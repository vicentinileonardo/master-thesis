import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the reduced latency matrix
'''
latency_matrix = {
    "eastus": {"italynorth": 96, "japaneast": 169, "francecentral": 87, "eastus": 0, "westus": 71},
    "francecentral": {"italynorth": 25, "japaneast": 251, "francecentral": 0, "eastus": 90, "westus": 150},
    "italynorth": {"italynorth": 0, "japaneast": 249, "francecentral": 24, "eastus": 97, "westus": 165},
    "japaneast": {"italynorth": 252, "japaneast": 0, "francecentral": 252, "eastus": 170, "westus": 108},
    "westus": {"italynorth": 165, "japaneast": 108, "francecentral": 150, "eastus": 71, "westus": 0}
}
'''

latency_matrix = {
    "francecentral": {"italynorth": 25, "japaneast": 251, "francecentral": 0, "westus": 150},
    "italynorth": {"italynorth": 0, "japaneast": 249, "francecentral": 24, "westus": 165},
    "japaneast": {"italynorth": 252, "japaneast": 0, "francecentral": 252, "westus": 108},
    "westus": {"italynorth": 165, "japaneast": 108, "francecentral": 150, "westus": 0}
}

# Extract region names and latency values
regions = list(latency_matrix.keys())
matrix = np.array([[latency_matrix[row][col] for col in regions] for row in regions])

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(matrix, annot=True, fmt="d", cmap="RdYlGn_r", xticklabels=regions, yticklabels=regions)
plt.title("Inter-Region Latency Matrix (ms)")
plt.xlabel("Destination Region")
plt.ylabel("Source Region")

# Save the figure to a file
plt.savefig("latency_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()
