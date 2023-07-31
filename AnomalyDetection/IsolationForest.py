# This script applies Isolation Forest to the data and prints the indices of the outliers.
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load the data and preprocess it
data = pd.read_csv('output.csv')
X = data.values
X = StandardScaler().fit_transform(X)

# Apply Isolation Forest
isolation_forest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
isolation_forest.fit(X)

# Get the indices of the outliers
outliers_mask = isolation_forest.predict(X) == -1
outliers_indices = np.where(outliers_mask)[0]

# Print the indices of the outliers
print("Outlier indices:", outliers_indices)
