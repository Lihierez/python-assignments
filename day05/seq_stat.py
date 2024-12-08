import sys

def seq_statistics(): 
    # get files by arguments
    files = [arg for arg in sys.argv[1:] if arg.endswith(".txt")]
    
    if not files:
        print("Usage: python script.py <file1.txt> <file2.txt> ... (TXT files only)")
        return
       
    total_A = total_T = total_G = total_C = total_unknown = 0

    for file in files:
        file_name = file.split('/')[-1]
        try:
            with open(file, 'r') as f:
                seq = ''.join(line.strip() for line in f.readlines())
        except FileNotFoundError:
            print(f"ERROR: File {file_name} not found.")
            continue

        seq = seq.upper()

        A_count = seq.count('A')
        T_count = seq.count('T')
        G_count = seq.count('G')
        C_count = seq.count('C')
        unknown_count = len(seq) - (A_count + T_count + G_count + C_count)

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

        total_A += A_count
        total_T += T_count
        total_G += G_count
        total_C += C_count
        total_unknown += unknown_count

    global_total = total_A + total_T + total_G + total_C + total_unknown
    if global_total:
        print("All files summary:")
        print(f"A: {total_A} ({total_A / global_total * 100:.1f}%)")
        print(f"T: {total_T} ({total_T / global_total * 100:.1f}%)")
        print(f"G: {total_G} ({total_G / global_total * 100:.1f}%)")
        print(f"C: {total_C} ({total_C / global_total * 100:.1f}%)")
        print(f"Unknown: {total_unknown} ({total_unknown / global_total * 100:.1f}%)")
        print(f"Total: {global_total}")

if __name__ == "__main__":
    seq_statistics()


import os

#use pytest to write tests that will validate the code.

def test_seq_statistics(capsys):
    original_argv = sys.argv
    
    # test file
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("ATGCGATGCA\n")

    sys.argv = ['script.py', test_file]
    
    try:
        seq_statistics()
        captured = capsys.readouterr()
        assert "A: 3 (30.0%)" in captured.out
        assert "T: 2 (20.0%)" in captured.out
        assert "G: 3 (30.0%)" in captured.out
        assert "C: 2 (20.0%)" in captured.out
    finally:
        sys.argv = original_argv
        os.remove(test_file)