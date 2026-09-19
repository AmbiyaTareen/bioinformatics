from Bio import SeqIO

def parse_fasta(filepath):
    records = list(SeqIO.parse(filepath, "fasta"))
    
    for record in records:
        print(f"ID: {record.id}")
        print(f"Sequence length: {len(record.seq)}")
        print(f"Sequence: {record.seq[:50]}...")
        print("-" * 40)
    
    return records

if __name__ == "__main__":
    filepath = "sample.fasta"
    records = parse_fasta(filepath)
    print(f"\nTotal sequences found: {len(records)}")