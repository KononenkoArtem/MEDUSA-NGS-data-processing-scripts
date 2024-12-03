import csv  # Import the CSV module for handling CSV file writing.

# Define input and output file paths.
input_file = "input_filepath.fastq"  # Path to the awk-pre-filtered .fastq file.
output_file = 'output_filepath.csv'  # Path to save the processed output as a .csv file.

# Open and read the .fastq file line by line.
with open(input_file, "r") as file:
    data = file.readlines()  # Read all lines into a list.
print(data)  # Print the raw data for verification.

# Trimmed sequences list to store sequences after extracting the desired portion.
trimmed_sequences = []  
i = 0  # Initialize index counter.

# Extract sequences from every third line (assuming the FASTQ structure).
# This captures the sequence starting from the 19th character (index 18, 0-based).
while i != len(data):
    trimmed_sequences.append([data[i][18:]])  # Extract and append trimmed sequences.
    i += 3  # Move to the next sequence line by skipping 3 lines.

# Create a dictionary to count occurrences of each unique sequence.
sequence_counts = {}
for e in trimmed_sequences:
    if e[0] in sequence_counts:
        sequence_counts[e[0]] += 1  # Increment count if sequence already exists.
    else:
        sequence_counts[e[0]] = 1  # Initialize count for a new sequence.

# Print sequence count results.
print("--------------------------Sequence Count -------------------------------")    
sorted_sequence_counts = dict(sorted(sequence_counts.items(), key=lambda x: x[1], reverse=True))  
# Sort sequences by count in descending order.

print(sorted_sequence_counts)  # Print the sorted dictionary.
print("Number of reads -> " + str(len(trimmed_sequences)))  # Print total number of reads.
print("Number of unique sequences -> " + str(len(sorted_sequence_counts)))  # Print unique sequence count.

# Write the results to a CSV file for easy viewing and further analysis.
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)  # Create a CSV writer object.
    writer.writerow(["Sequence", "Sequence Count"])  # Write the header row.
    for key, value in sorted_sequence_counts.items():  # Write each sequence and its count.
        writer.writerow([key, value])