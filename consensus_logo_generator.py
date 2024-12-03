import csv  # To read the input CSV file.
import logomaker  # To create sequence logos.
import matplotlib.pyplot as plt  # To display the sequence logo.

# Read sequences from the CSV file
sequences = []  # List to store sequences.
with open('frequency_wighted_sequence_list_filepath.csv', "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        sequences.append(row[0])  # Append each sequence from the first column.

# Create a counts matrix from the sequences
counts_matrix = logomaker.alignment_to_matrix(sequences, to_type='counts')

# Convert the counts matrix to a frequency matrix
freq_matrix = logomaker.transform_matrix(counts_matrix, from_type='counts', to_type='probability')

# Generate the sequence logo
logo = logomaker.Logo(freq_matrix)

# Style the logo
logo.style_spines(visible=False)  # Hide unnecessary borders.
logo.style_spines(spines=['left'], visible=True, bounds=[0, 1])  # Show only the left border.
logo.style_xticks(rotation=90, fmt='%s')  # Rotate x-axis labels.

# Display the logo
plt.show()