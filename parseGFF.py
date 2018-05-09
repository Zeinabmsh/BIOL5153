#!/usr/bin/env python3

# How to run: python parseGFF.py -f watermelon.fsa -g watermelon.gff

import sys
from Bio import SeqIO
import argparse


def closeFile(F):
    """close GFF file.
    """

    print("Closing " + F + " file.")
    waterMFile.close()


def parseData(waterMData, genomeData):
    """Loop over read data line by line.
    """

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


def reafGFFData(F):
    """Connect to watermelon.gff file and read all lines.
    """

    print("Reading " + F + " file.")
    with open(F) as waterMFile:
        waterMData = waterMFile.readlines()
    return waterMData


def getGnomeData(F):
    """Read and return gnome file content.
       Input: F (gnome file name)
    """

    print("Reading Genome File: " + F)
    with open(F, 'r') as genomeFile:
        genomeData = genomeFile.read()
        print (genomeData)

    return genomeData


def getArgParse():
    """Parse input arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--gnome_file", help='Reading genome file.', type=str)
    parser.add_argument("-g", "--GFF_file", help='Reading GFF file.', type=str)
    parser.add_argument("-v", "--verbose", help='Verbose state [0 | 1]', default=1, type=int)
    args = parser.parse_args()
    return args


def main():
    """Main Function.
    """

    args = getArgParse()

    genomeData = getGnomeData(args.gnome_file)

    waterMData = reafGFFData(args.GFF_file)

    parseData(waterMData, genomeData)

    print("Program ended.")


if __name__ == "__main__":
    main()
