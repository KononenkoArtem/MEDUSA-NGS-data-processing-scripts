# MEDUSA-NGS-data-processing-scripts
This repository contains Python scripts for the quantification of sequences from awk-pre-filtered .fastq high-throughput sequencing files and for downstream data analysis. A more detailed description of the purpose of each script is provided in the README file.

Dependencies

The scripts rely on the following Python libraries:
	•	csv: For reading and writing CSV files, enabling seamless import/export of sequence and data tables.
	•	Levenshtein: To compute the Levenshtein (edit) distance between pairs of sequences, which is essential for analyzing sequence similarity.
	•	logomaker: For generating sequence logos from alignment data, providing visual representations of sequence patterns.
	•	numpy: Used for numerical computations and data manipulation, particularly for normalizing frequency distributions.
	•	matplotlib: For creating visualizations such as bar plots and sequence logos, enabling data interpretation through graphical outputs.
	•	mpl_toolkits.mplot3d: To generate 3D bar plots, facilitating the visualization of comparative frequency data.
	•	pandas: For efficient data manipulation and analysis, particularly when working with tabular data.
	•	umap.umap_: For dimensionality reduction, useful for UMAP analysis to visualize high-dimensional data in lower dimensions.
 	

Input data

The primary input data was awk-pre-filtered .fastq high-throughput sequencing files.
The following awk command was used to filter the sequences (example):
>MiSeq Data filtering:
Regular expression reverse sequence:
CATAGACTAGCAACTTTCACC[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]AGGAGTGAT

Awk code reverse sequence:
awk '/CATAGACTAGCAACTTTCACC[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]A[A,T,G,C][A,T,G,C][T,G,C][A,T,G,C][A,T,G,C]AGGAGTGAT/ {print; getline; print; getline; print}' medusa_r7_502703_S1_R1_001.fastq > medusa_r7_502703_S1_R1_001_filtered.fastq

Regular expression forward sequence:
CCTCTACCACCTACATCACTCCT[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]GGTGAAAG

Awk code forward sequence:
awk '/CCTCTACCACCTACATCACTCCT[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]GGTGAAAG/ {print; getline; print; getline; print}' medusa_r7_502703_S1_R2_001.fastq > medusa_r7_502703_S1_R2_001_filtered.fastq

>NovaSeq Data filtering:
Regular expression forward sequence:
CCTCTACCACCTACATCACTCCT[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]GG

Awk code reverse sequence:
awk '/CCTCTACCACCTACATCACTCCT[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]T[A,T,G,C][A,T,G,C][A,G,C][A,T,G,C][A,T,G,C]GG/ {print; getline; print; getline; print}' r3medusa502701_FKDL230051171-1A_H2FM2DRX3_L1_2.fq > r3medusa502701_filtered_L1_2.fastq

Description of the scripts 
                   
1.	consensus_logo_generator.py - This script generates a sequence logo representing the consensus sequence derived from a set of sequences. It uses the logomaker library to create a visual representation of sequence motifs, where the sequence counts are weighted for each position to highlight the most prevalent nucleotides.
2.	levenshtein_distances_matrix_generator.py - This script calculates the Levenshtein distance matrix between sequences, which is used to quantify the similarity between pairs of sequences. It then outputs the distance matrix along with the sequence names and associated scores to a CSV file, providing a useful metric for sequence comparison and clustering.
3.	sequence_counter.py - This script reads a .fastq file (pre-filtered using AWK) containing sequences, counts the frequency of each unique sequence, and stores the results in a CSV file. The script uses the csv module to process the sequences and outputs a sorted list of unique sequences with their respective counts.
4.	side_chains_frequencies_calc.py - This script analyzes side-chain frequencies in sequence data, specifically the frequency of modifications based on predefined codons. It processes input data, calculates how often specific side-chain modifications appear throughout different rounds of selection, and outputs the results as 3D bar plot.
5.	UMAP_presentation.py - This script performs UMAP (Uniform Manifold Approximation and Projection) analysis on high-dimensional sequence data to reduce the data to lower dimensions for visualization. 
