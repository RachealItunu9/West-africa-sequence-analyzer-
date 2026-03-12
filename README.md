# West-africa-sequence-analyzer-
Sequence analyzer to detect a motif
RNA Sequence Mutation & Virulence Motif Analysis

Project Overview

This project is a Python-based bioinformatics script designed to analyze RNA sequences. It compares a reference strain with a regional variant, identifies mutations between the sequences, and detects the presence of a virulence-associated motif.

The program performs three main analyses:

1. RNA Composition Analysis – Calculates nucleotide composition and GC content.
2. Mutation Detection – Identifies differences between the reference strain and the regional variant.
3. Virulence Motif Detection – Searches for a specific RNA motif associated with virulence.

This type of analysis is commonly used in molecular biology, virology, and pathogen genomics to track mutations and detect important sequence features

Features

- RNA nucleotide composition analysis
- GC content calculation
- Comparison of two RNA sequences
- Mutation detection with position reporting
- Virulence motif detection
- Clear formatted output for easy interpretation

Technologies Used

- Python 3
- Basic bioinformatics sequence analysis concepts

Program Modules

1. RNA Composition Analysis

This module analyzes nucleotide composition in both the reference strain and regional variant.

It calculates:

- Total sequence length
- Number of Adenine (A)
- Number of Uracil (U)
- Number of Cytosine (C)
- Number of Guanine (G)
- GC Content Percentage

GC content is calculated using the formula:

GC Content (%) = (G + C) / Total Sequence Length × 100
2. Mutation Detection

This module compares the reference strain with the regional variant base by base.

If differences are found, the script reports:

- Mutation position
- Original base (reference)
- Mutated base (variant)

Example output:

Mutation Detection Report

Total Mutations Detected: 2

Position 5: C → G
Position 8: A → U

This type of analysis is commonly used to study genetic variation between viral strains or bacterial isolates.



3. Virulence Motif Detection

The script also searches for a specific virulence motif:

GGAUCU

If the motif is detected in the regional strain, the script reports:

- Motif sequence
- Position of the motif in the RNA strand

Example output:

Virulence Motif Detection

Motif Detected!
Motif Sequence: GGAUCU
Motif Position: 4

Motif detection is useful in pathogen genomics and disease research, where certain sequence patterns are linked to pathogenicity.

Example Output

===== RNA Composition Report =====
Reference Sequence Length: 170
A: 45
U: 40
C: 42
G: 43
GC Content: 50.0 %

===== RNA Composition Report =====
Regional Sequence Length: 170
A: 44
U: 41
C: 42
G: 43
GC Content: 50.0 %

Mutation Detection Report
Total Mutations Detected: 2
Position 4: C → G
Position 6: A → U

Virulence Motif Detection
Motif Detected!
Motif Sequence: GGAUCU
Motif Position: 3

How to Run the Script

1. Install Python 3 on your system.

2. Clone the repository:

git clone https://github.com/yourusername/rna-mutation-analysis.git

3. Navigate to the project folder:

cd rna-mutation-analysis

4. Run the script:

python rna_analysis.py


Possible Future Improvements

Future versions of this project could include:

- Reading RNA sequences from FASTA files
- Alignment algorithms for more complex comparisons
- Visualization of mutation positions
- Translation of RNA to protein sequences
- Integration with real biological datasets
- Mutation frequency analysis across multiple strains


Educational Purpose

This project demonstrates fundamental concepts in bioinformatics, including:

- Sequence analysis
- Mutation detection
- Nucleotide composition analysis
- Motif searching

It can serve as a simple educational tool for students learning computational biology and molecular genetics.

Author

Racheal Itunu Soyemi 
Final-Year Biochemistry Student
University of Ibadan 
Co-director – STEMIA (STEM Mentorship, Internship, and Innovation Hub)


License

This project is released for educational and research purposes.
