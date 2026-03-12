# =====================================================
# STEMIA WestAfrica RNA Surveillance Analyzer v1.0
# Emerging Viral Genomic Surveillance Simulation Tool
# Week 1 Release: RNA Composition Analysis
# =====================================================

# ===============================
# DATASET SECTION
# ===============================

reference_strain = (
"AUGGCUACGUAGCUAGGCUAUGCUAGCUAGGCUAUGCUAGCUAGCUACGGAUCGUAGCUAGCUA"
"GGCUAUGCUAGCUAGGCUACGUAGCUAGCUAUGCUAGCUAGGCUAUGCUAGCUAGCUAUGCUGA"
"AUGCUAGCUAGGCUACGUAGCUAGCUAUGCUAGC"
)

# Replace this with your assigned regional variant
regional_variant = reference_strain

virulence_motif = "GGAUCU"


# ===============================
# MODULE 1: RNA Composition Analyzer
# ===============================

sequence = regional_variant

length = len(sequence)

count_A = sequence.count("A")
count_U = sequence.count("U")
count_C = sequence.count("C")
count_G = sequence.count("G")

gc_content = ((count_G + count_C) / length) * 100

print("===== RNA Composition Report =====")
print("Sequence Length:", length)
print("A:", count_A)
print("U:", count_U)
print("C:", count_C)
print("G:", count_G)
print("GC Content:", round(gc_content, 2), "%")
print("==================================")

