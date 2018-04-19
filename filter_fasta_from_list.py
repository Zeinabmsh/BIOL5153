#! /usr/bin/env python3

import sys
import argparse as ap
from Bio import SeqIO as seq

# Initialize an argument parser object with description
argParser = ap.ArgumentParser(description="This Python code takes a FASTA file and a file with a list of sequence identifiers to be removed from FASTA file.")

# Input arguments
argParser.add_argument("-f", "--file", help="Specify name of the FASTA file, e.g., watermelon_genes.fa", required=True)
argParser.add_argument("-l", "--list", help="Filename with a list of sequence identifiers to be removed from FASTA file.", required=True)

# Let's parge the user input arguments
args = argParser.parse_args()

with open(args.list, 'r') as F:
    listedSeq = [item.strip() for item in F.readlines() if len(item.strip()) > 1]

# Parse sequence file
try:
    fastaFile = seq.parse(args.file, "fasta")
except:
    print('   --- The FASTA file cannot be parsed.')

counter = 0
with open('result_file.fasta', "w") as F:
    for item in fastaFile:
        seqName = item.id
        seqLength = len(item.seq)

        # Skip the sequence if its length is zero or it is listed in listedSeq file
        if ( (seqLength == 0) or (seqName in listedSeq) ):
            continue

        # Otherwise, write it to outputfile
        seq.write([item], F, "fasta")
        counter += 1

# Report to user
print(''.join(["   --- Number of sequences not in the list file: ", str(counter)]))
print("   --- Results:")

# Open the output file and report it to user
with open("result_file.fasta", 'r') as F:
    print(F.read())
