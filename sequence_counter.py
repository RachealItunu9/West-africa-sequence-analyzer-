dna_sequence = "ATGCGATACGCTTGCAGTCAGTACGATCGATCGGCTAGCTAGCGATGCTAGC"
total_base = len("dna_sequence")
print("total_base")
dna_sequence = dna_sequence.upper()
count_A = dna_sequence.count("A")
count_T = dna_sequence.count("T")
count_G = dna_sequence.count("G")
count_C = dna_sequence.count("C")
GC_count = count_G + count_C
print("A:", count_A)
print("T:", count_T)
print("G:", count_G)
print("C", count_C)
print(GC_count/total_base*100)
