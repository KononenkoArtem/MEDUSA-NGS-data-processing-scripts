import pandas as pd
from umap.umap_ import UMAP
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
data = pd.read_csv('sequence_counts_file.csv', header=None, names=['sequence', 'count'])

# Remove sequences that are less than 32 characters
data = data[data['sequence'].str.len() == 32]

# Remove sequences that occur only once
data = data[data['count'] > data['count'].sum() * 0.000005]

# Truncate the sequences by removing 5 letters from the left and 2 letters from the right
data['sequence'] = data['sequence'].apply(lambda x: x[6:-2])

# Convert sequences to 24-dimensional vectors
def convert_sequence_to_vector(sequence):
    vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(sequence)):
        if i == 0 or i == 6 or i == 12 or i == 18:
            if sequence[i] == "T":
                if sequence[i:i+3] == "TAA" or sequence[i:i+3] == "TCC": # cyclopropyl methyl amine = 1
                    vector[i] = 1
                if sequence[i:i+3] == "TAT" or sequence[i:i+3] == "TCG": # cyclobutyl methyl amine = 2
                    vector[i] = 2
                if sequence[i:i+3] == "TAC" or sequence[i:i+3] == "TAG": # 3,4-diclorobenzyl methyl amine = 3
                    vector[i] = 3
                if sequence[i:i+3] == "TTC" or sequence[i:i+3] == "TGT": # phenetyl amine = 4
                    vector[i] = 4
                if sequence[i:i+3] == "TCA" or sequence[i:i+3] == "TCT": # 4-fluorobenzyl methyl amine = 5
                    vector[i] = 5
                if sequence[i:i+3] == "TGA" or sequence[i:i+3] == "TTG": # tyramine = 6
                    vector[i] = 6                                       
                if sequence[i:i+3] == "TTA" or sequence[i:i+3] == "TGC": # butyl amine = 7
                    vector[i] = 7
                if sequence[i:i+3] == "TTT" or sequence[i:i+3] == "TGG": # isobutyl amine = 8
                    vector[i] = 8 
        elif sequence[i] == "T": # T = 9
            vector[i] = 9
        elif sequence[i] == "A": # A = 10
            vector[i] = 10
        elif sequence[i] == "G": # G = 11
            vector[i] = 11
        elif sequence[i] == "C": # C = 12
            vector[i] = 12                
    return vector

data['vector'] = data['sequence'].apply(convert_sequence_to_vector)

# Convert the vector column to a numpy array
vectors = np.array(data['vector'].tolist())

# Apply UMAP
umap_model = UMAP(n_neighbors=20, min_dist=0.1, n_components=2)
umap_embedding = umap_model.fit_transform(vectors)

# Normalize the count values for color gradient
normalized_counts = (data['count'] - data['count'].min()) / (data['count'].max() - data['count'].min())

# Sort the data by vector in ascending order
data_sorted = data.sort_values('count')

# Plot the UMAP projection
plt.scatter(umap_embedding[data_sorted.index, 0], umap_embedding[data_sorted.index, 1],
            c=normalized_counts[data_sorted.index],
            cmap='viridis', alpha=0.9)

plt.title('UMAP Projection focused medusa r7')
plt.colorbar(label='Normalized Count')
plt.show()
