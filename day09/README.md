# DNA Sequence Analyzer
This program analyzes DNA sequences from FASTA or GenBank files for 2 kind of patterns.

## Features:
1. **Longest Duplicated Subsequence:** Finds the longest DNA subsequence that appears at least twice in the input sequence.
2. **GC-Rich Regions:** Identifies regions with high GC content, which can be indicative of regulatory regions or other functional elements.

## Usage:
```
python analyze.py FILE [--duplicate] [--gc]
```

## Arguments:
1. **FILE:** Path to input file: FASTA format ((starting with '>') or GenBank format (containing 'ORIGIN' section)
2. **--duplicate:** Find longest duplicated subsequence
3. **--gc:** Find GC-rich regions

## Example:
```
python analyze.py sequence.fasta --duplicate --gc
```
