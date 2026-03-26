import pandas as pd
from scipy.io import arff

data = arff.loadarff('Training Dataset.arff')
df = pd.DataFrame(data[0])

df.to_csv('dataset.csv', index=False)

print("Converted successfully!")