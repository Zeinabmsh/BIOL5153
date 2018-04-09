#!/usr/bin/env python3

import sys
from Bio import SeqIO

# Read genome file
print("Reading genome file.")
genomeFile = open("watermelon.fsa", 'r')
genomeData = genomeFile.read()
print (genomeData)

# Connect to watermelon.gff file and read all lines
print("Reading watermelon.gff file.")
waterMFile = open("watermelon.gff")
waterMData = waterMFile.readlines()

# Loop over read data line by line
for item in waterMData:
   # Split each item by tabs "\t"
   spList = item.split("\t")
   
   # Extract start and end index
   startIndex = int(spList[3])
   endIndex   = int(spList[4])

   # Extract name and gene
   name = (spList[0])
   gene = (spList[8])
   
   print("===>" + name + gene + genomeData[startIndex:endIndex])


# close GFF file
print("Closing watermelon.gff file.")
waterMFile.close()
print("Program ended.")
