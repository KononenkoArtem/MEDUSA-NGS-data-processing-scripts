import csv  # Import for reading CSV files.
import numpy as np  # Import for numerical operations.
import matplotlib.pyplot as plt  # Import for creating plots.
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting.

# Define the genetic code mapping codons to modifications.
code = {
    "cyclopropylmethyl": ["TAA", "TCC"], 
    "cyclobutylmethyl": ["TAT", "TCG"], 
    "3,4-diclorophenylmethyl": ["TAC", "TAG"], 
    "butyl": ["TTA", "TGC"],
    "isobutyl": ["TTT", "TGG"],
    "phenetyl": ["TTC", "TGT"],
    "4-fluorophenylmethyl": ["TCA", "TCT"],
    "4-hydroxyphenylmethyl": ["TGA", "TTG"]
}

# Input file paths for the NGS data.
input_file1 = "sequence_count_round3_filepath.csv"
input_file2 = "sequence_count_round6_filepath.csv"
input_file3 = "sequence_count_round7_filepath.csv"

# Define a function to analyze sequence data and count occurrences of modifications.
def analyse(code, input_file):
    data = []
    # Read the CSV file and extract the top 100 rows (after the header).
    with open(input_file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(reader):
            if i < 101:  # Limit to 100 rows for processing.
                data.append(row)
            else:
                break
    data = data[1:]  # Exclude the header row.
    print(data)  # Debugging: Print raw data.

    # Process the sequence data.
    data_processed = []
    for e in data:
        # Extract codons from fixed positions in the sequence.
        data_processed.append([[e[0][6:9], e[0][12:15], e[0][18:21], e[0][24:27]], e[1]])

    print(data_processed)  # Debugging: Print processed data.

    # Count occurrences of each modification.
    occurences = {}
    for key, values in code.items():
        count = 0
        for sublist in data_processed:
            # Check if any codon matches the current modification.
            for value in sublist[0]:
                if value in values:
                    count += int(sublist[1])  # Increment count based on the sequence count.
        occurences[key] = count
    return occurences

# Analyze the three rounds of data.
r3 = analyse(code, input_file1)
r6 = analyse(code, input_file2)
r7 = analyse(code, input_file3)

# Normalize the frequencies for each round.
y1 = list(map(lambda x: x / sum(r3.values()), r3.values()))
y2 = list(map(lambda x: x / sum(r6.values()), r6.values()))
y3 = list(map(lambda x: x / sum(r7.values()), r7.values()))

# Define a function to plot a 3D bar chart.
def plot_3d_bars_with_labels(x_labels, y_values_lists):
    # Create a figure and 3D axes for plotting.
    fig = plt.figure(figsize=(8, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')

    num_datasets = len(y_values_lists)  # Number of datasets (rounds).
    num_bars = len(x_labels)  # Number of modifications (x-axis labels).
    bar_width = 0.5  # Width of each bar.
    bar_depth = 0.05  # Depth of each bar.

    colors = ['#999999', '#0F80FF', '#FB0280']  # Define colors for each round.

    # Plot each dataset as a set of 3D bars.
    for i, y_values in enumerate(y_values_lists):
        x_indices = np.arange(num_bars)  # X positions for the bars.
        y_indices = np.full(num_bars, i)  # Fixed y positions for the current dataset.
        z_values = np.zeros(num_bars)  # Bars start at z=0.
        ax.bar3d(
            x_indices, y_indices, z_values,  # Position of the bars.
            bar_width, bar_depth, y_values,  # Size and height of the bars.
            color=colors[i], alpha=0.8, zsort='average'  # Color and transparency.
        )

    # Set axis ticks and labels.
    ax.set_yticks(np.arange(num_datasets))
    ax.set_yticklabels(['Round 3', 'Round 6', 'Round 7'], fontsize=8, rotation=0, va='center', ha="left")

    ax.set_xticks(np.arange(num_bars))
    ax.set_xticklabels(x_labels, fontsize=8, rotation=90, ha='right')

    # Adjust the viewing angle for better readability.
    ax.view_init(elev=38, azim=93)

    # Add axis labels.
    ax.set_zlabel("Frequency (Normalized)", fontsize=8)

    # Adjust layout for better appearance.
    plt.subplots_adjust(left=0.2, right=0.95, top=0.9, bottom=0.2)
    plt.show()

# Prepare labels and values for plotting.
labels = r3.keys()  # Modification labels.
y_values_lists = [y1, y2, y3]  # Normalized frequencies for each round.

# Plot the data using the defined function.
plot_3d_bars_with_labels(labels, y_values_lists)