# This script applies DBSCAN to the data and prints the indices of the outliers.

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Load the data and preprocess it
data = pd.read_csv('output.csv')
X = data.values
X = StandardScaler().fit_transform(X)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=10)
dbscan.fit(X)

# Get the indices of the outliers
outliers_mask = np.zeros_like(dbscan.labels_, dtype=bool)
outliers_mask[dbscan.labels_ == -1] = True
outliers_indices = np.where(outliers_mask)[0]

# Print the indices of the outliers
print("Outlier indices:", outliers_indices)
