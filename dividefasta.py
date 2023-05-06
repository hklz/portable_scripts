import argparse
import os

def parse_fasta_file(fasta_file):
    """
    Parses a FASTA file and returns a dictionary with sequence numbers as keys and sequences as values.

    :param fasta_file: Path to the input FASTA file containing multiple sequences
    :return: A dictionary with sequence numbers as keys and sequences as values
    """
    with open(fasta_file, 'r') as file:
        content = file.read().splitlines()
        sequences = {}
        seq_number = 0

        for line in content:
            if line.startswith('>'):  # Check if the line is a header
                seq_number += 1  # Increment the sequence number
                sequences[seq_number] = ''  # Initialize an empty sequence for the current sequence number
            else:
                sequences[seq_number] += line  # Append the current line (sequence) to the sequence with the current number

    return sequences

def write_individual_fasta_files(sequences, output_dir, prefix):
    """
    Writes individual FASTA files for each sequence in the given dictionary.

    :param sequences: A dictionary with sequence numbers as keys and sequences as values
    :param output_dir: Path to the output directory where individual FASTA files will be written
    :param prefix: The prefix to add to the sequence names
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for seq_number, sequence in sequences.items():
        output_file = os.path.join(output_dir, f"{prefix}_seq_{seq_number}.fasta")
        with open(output_file, 'w') as file:
            file.write(f">{prefix}_seq_{seq_number}\n{sequence}\n")

def main():
    parser = argparse.ArgumentParser(description="Separate a FASTA file with multiple sequences into individual FASTA files")
    parser.add_argument("input_file", help="Path to the input FASTA file containing multiple sequences")
    parser.add_argument("output_dir", help="Path to the output directory where individual FASTA files will be written")
    parser.add_argument("prefix", help="Prefix to add to the sequence names")
    args = parser.parse_args()

    fasta_file = args.input_file
    output_dir = args.output_dir
    prefix = args.prefix

    sequences = parse_fasta_file(fasta_file)
    write_individual_fasta_files(sequences, output_dir, prefix)

if __name__ == "__main__":
    main()
