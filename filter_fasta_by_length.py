#! /usr/bin/env python3

import argparse as ap
from Bio import SeqIO as seq

# Initialize an argument parser object with description
argParser = ap.ArgumentParser(description="This Python code takes a FASTA file with any number of sequences and a user-specified length cutoff, below which sequences will be removed.")

# Input arguments
argParser.add_argument("-f", "--file", help="Specify name of the FASTA file, e.g., watermelon_genes.fa", required=True)
argParser.add_argument("-c", "--cutoff", help="A user-specified length cutoff, below which sequences will be removed.", type=int, required=True)

# Let's parge the user input arguments
args = argParser.parse_args()

# Parse sequence file
fastaFile = seq.parse(args.file, "fasta")

# Initialize a list for number of sequences found with length < cutoff length
seqFound = []

# Loop over each sequence and check its length with cutoff length
for item in fastaFile:
    if len(item.seq) < args.cutoff:
        seqFound.append(item)

# Find number of sequence that meet -> length < cutoff length
numSeq = len(seqFound)

# Report to user
print("   --- FASTA file name:", args.file)
print("   --- Cutoff length  :", args.cutoff)
print(''.join(["   --- Number of sequences with length < cutoff length: ", str(numSeq)]))
print("   --- Results:")

# Write them using SeqIO library
seq.write(seqFound, "seqFound.fasta", "fasta")

# Open the output file and report it to user
with open("seqFound.fasta", 'r') as F:
    print(F.read())
