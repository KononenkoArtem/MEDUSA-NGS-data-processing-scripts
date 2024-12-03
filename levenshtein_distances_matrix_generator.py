import Levenshtein  # Library for calculating Levenshtein (edit) distance between strings.
import csv  # Library for reading from and writing to CSV files.

# Function to read sequences and their associated scores from a CSV file.
def csv_reader(file_path):
    sequences = []  # List to store the sequences.
    scores = []  # List to store the scores corresponding to the sequences.
    with open(file_path, newline="") as csvfile:  # Open the input CSV file.
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")  # Initialize the CSV reader.
        for row in reader:  # Iterate over each row in the CSV file.
            sequences.append(row[0])  # Append the first column (sequence) to the list.
            scores.append(row[1])  # Append the second column (score) to the list.
            print(row)  # Print the row (optional, for debugging).
    return sequences, scores  # Return the sequences and scores as separate lists.

# Function to calculate a matrix of Levenshtein distances between sequences.
def calculate_distances(sequences):
    num_sequences = len(sequences)  # Number of sequences to process.
    # Initialize a 2D matrix of size (num_sequences x num_sequences) filled with zeros.
    distance_matrix = [[0] * num_sequences for _ in range(num_sequences)]

    for i in range(num_sequences):  # Loop through each sequence (row index).
        for j in range(num_sequences):  # Loop through each sequence (column index).
            if i != j:  # Skip calculating distance for a sequence compared to itself.
                # Calculate Levenshtein distance between sequence i and sequence j.
                distance = Levenshtein.distance(sequences[i], sequences[j])
                distance_matrix[i][j] = distance  # Store the calculated distance in the matrix.

    return distance_matrix  # Return the distance matrix.

# Function to write the distance matrix and associated data to a CSV file.
def write(matrix, scores, sequences, output_file):
    with open(output_file, 'w', newline='') as csvfile2:  # Open the output CSV file for writing.
        csv_writer = csv.writer(csvfile2)  # Initialize the CSV writer.

        # Write the header row with sequence scores.
        csv_writer.writerow([''] + scores)  # The first column is empty; the rest are scores.

        # Write the data rows with sequence scores, sequence names, and distance values.
        for i, row in enumerate(matrix):  # Enumerate over the distance matrix rows.
            csv_writer.writerow([scores[i], sequences[i]] + row)  # Write the score, sequence, and distances.

# Main execution block.
if __name__ == "__main__":
    # File path for the input CSV containing sequences and scores.
    input_file = "/path/to/input/top100_for_levenshtein.csv"
    sequences, scores = csv_reader(input_file)  # Read sequences and scores from the input file.
   
    # Calculate the Levenshtein distance matrix for the sequences.
    distance_matrix = calculate_distances(sequences)

    # File path for the output CSV to store the distance matrix.
    output_file = "/path/to/output/top100_levenshtein.csv"
    write(distance_matrix, scores, sequences, output_file)  # Write the data to the output file.

    # Print confirmation message.
    print(f"Levenshtein distances matrix with sequence names written to {output_file}")