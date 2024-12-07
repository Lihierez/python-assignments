#insert the function all the files pathes.
#files in FASTA formate

def seq_statistics(*files):
    total_A = total_T = total_G = total_C = total_unknown = 0

    for file in files:
        file_name = file.split('/')[-1]
        with open(file, 'r') as f:
            lines = f.readlines()  # Read all lines from the file

        # Validate file content
        if not lines or not lines[0].startswith(">"):
            print(f"ERROR: {file_name} does not appear to be a valid FASTA file.")
            continue

        # Skip the header and combine all sequence lines
        seq = ''.join(line.strip() for line in lines[1:])
        seq = seq.upper()  # Convert to uppercase for case-insensitivity

        # File-specific counts
        A_count = T_count = G_count = C_count = unknown_count = 0
        for nuc in seq:
            if nuc == 'A':
                A_count += 1
            elif nuc == 'T':
                T_count += 1
            elif nuc == 'G':
                G_count += 1
            elif nuc == 'C':
                C_count += 1
            else:
                unknown_count += 1

        # File-specific totals and percentages
        total_nuc = len(seq)
        A_perc = A_count / total_nuc * 100 if total_nuc else 0
        T_perc = T_count / total_nuc * 100 if total_nuc else 0
        G_perc = G_count / total_nuc * 100 if total_nuc else 0
        C_perc = C_count / total_nuc * 100 if total_nuc else 0
        unknown_perc = unknown_count / total_nuc * 100 if total_nuc else 0

        print(f"{file_name}")
        print(f"A: {A_count} ({A_perc:.1f}%)")
        print(f"T: {T_count} ({T_perc:.1f}%)")
        print(f"G: {G_count} ({G_perc:.1f}%)")
        print(f"C: {C_count} ({C_perc:.1f}%)")
        print(f"Unknown: {unknown_count} ({unknown_perc:.1f}%)")
        print(f"Total: {total_nuc}\n")

        # Update global counts
        total_A += A_count
        total_T += T_count
        total_G += G_count
        total_C += C_count
        total_unknown += unknown_count

    # Global statistics
    global_total = total_A + total_T + total_G + total_C + total_unknown
    if global_total:
        print("All files summary:")
        print(f"A: {total_A} ({total_A / global_total * 100:.1f}%)")
        print(f"T: {total_T} ({total_T / global_total * 100:.1f}%)")
        print(f"G: {total_G} ({total_G / global_total * 100:.1f}%)")
        print(f"C: {total_C} ({total_C / global_total * 100:.1f}%)")
        print(f"Unknown: {total_unknown} ({total_unknown / global_total * 100:.1f}%)")
        print(f"Total: {global_total}")


seq_statistics("/Users/lihierez/Python course/python-assignments/day05/RamdomSeq1.txt", "/Users/lihierez/Python course/python-assignments/day05/RamdomSeq2.txt")