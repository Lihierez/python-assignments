# Assignment (day 9)
# We saw one example analyzing sequences: find the longest sub-sequence that repeates itself. 
# In the day09 folder create a program that will receive the path to a file in Fasta or GeneBank format, 
# and use the above analyzis to print out the longest sub-sequence that appears twice.

# Then come up with some other "interesting feature" of sequences and add that analyzis too. Make both analyzis optional and let the user control which one is done: (assuming this second analyzis is called blabla you could use the program like this:

# python analyze.py FILE --duplicate --blabla
# What is an "interesting feature" is up to you. It can be a real, scientifically valuable feature, but if that's too difficult it can be some simpe feature like the repetition we have.

# Include a README.md file and the requirements.txt file if necessary.

import argparse
import re

# Read and parse sequence from FASTA or GenBank file, returns the DNA sequence string.
def read_sequence_file(file_path: str):

    with open(file_path, 'r') as file:
        content = file.read()
        
    # Check if it's FASTA format
    if content.startswith('>'):
        # Extract sequence from FASTA
        sequence_lines = content.split('\n')[1:] 
        return ''.join(line.strip() for line in sequence_lines)
    
    # Check if it's GenBank format
    if 'ORIGIN' in content:
        # Extract sequence from GenBank
        origin_section = content.split('ORIGIN')[1]
        sequence = ''.join(re.findall(r'[ATCG]', origin_section.upper()))
        return sequence
    
    raise ValueError("File format not recognized. Please provide a valid FASTA or GenBank file.")


# Find the longest subsequence that appears at least twice in the sequence. Returns tuple of (subsequence, starting_position).
def find_longest_duplicate_subsequence(sequence: str):

    sequence = sequence.upper()
    length = 1
    longest_subseq = ''
    start_pos = -1
    
    while True:
        pattern = f'(?=([ATCG]{{{length}}}).*?\\1)'
        
        matches = list(re.finditer(pattern, sequence))
        
        if matches:
            # Found matches at current length --> continue to next length
            longest_subseq = matches[0].group(1)
            start_pos = matches[0].start()
            length += 1
        else:
            # No matches found --> return last successful match
            if longest_subseq:
                return longest_subseq, start_pos
            return '', -1


#Another feature: Find regions with high GC content. Returns list of tuples containing (start_position, gc_content).
def find_gc_rich_regions(sequence: str, window_size: int = 100, threshold: float = 0.6):

    sequence = sequence.upper()
    gc_regions = []
    
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        gc_count = window.count('G') + window.count('C')
        gc_content = gc_count / window_size
        
        if gc_content >= threshold:
            gc_regions.append((i, gc_content))
    
    return gc_regions


def main():
    parser = argparse.ArgumentParser(description='Analyze DNA sequences for patterns')
    parser.add_argument('file', help='Path to FASTA or GenBank file')
    parser.add_argument('--duplicate', action='store_true', 
                      help='Find longest duplicated subsequence')
    parser.add_argument('--gc', action='store_true',
                      help='Find GC-rich regions')
    
    args = parser.parse_args()
    
    try:
        sequence = read_sequence_file(args.file)
        
        if args.duplicate:
            subseq, pos = find_longest_duplicate_subsequence(sequence)
            if subseq:
                print(f"Longest duplicated subsequence: Sequence: {subseq} Length: {len(subseq)} First occurrence at position: {pos}")
            else:
                print("No significant duplicated subsequence found.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())