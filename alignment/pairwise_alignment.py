# Global alignment - aligns full length of both sequences

from Bio import SeqIO
from Bio import pairwise2

for record in SeqIO.parse("sample.fasta", "fasta"):
    if record.id=="seq1":
        seq1=record.seq 
    elif record.id=="seq2":
        seq2=record.seq
        
alignments= pairwise2.align.globalxx(seq1, seq2)
print(pairwise2.format_alignment(*alignments[0]))
