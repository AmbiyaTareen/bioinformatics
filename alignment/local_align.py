# Local alignment - aligns best matching regions of both sequences

from Bio import SeqIO
from Bio.Align import PairwiseAligner

for record in SeqIO.parse("sample.fasta", "fasta"):
    if record.id == "seq1":
        seq1 = record.seq
    elif record.id == "seq2":
        seq2 = record.seq

aligner = PairwiseAligner()
aligner.mode = "local"

alignments = aligner.align(seq1, seq2)
print(alignments[0])
print("Score:", alignments[0].score)