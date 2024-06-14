# DESCRIPTION:
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# My Solution

def dna_to_rna(dna):
    d = {"G":"G", "C":"C", "A":"A", "T":"U"}
    rna = ""

    for p in dna:
        rna += d[p]

    return rna
