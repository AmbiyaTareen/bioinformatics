from Bio import SeqIO

VALID_BASES = set("ATGCN")

def parse_fasta(filepath):
    try:
        records = list(SeqIO.parse(filepath, "fasta"))
    except FileNotFoundError:
        print(f"Error: '{filepath}' doesn't exist. Check the path and try again.")
        return []
    except ValueError as e:
        print(f"Error: '{filepath}' doesn't look like a valid FASTA file.")
        print(f"Details: {e}")
        return []

    if len(records) == 0:
        print(f"Error: '{filepath}' was found but contains no sequences.")
        return []

    valid_records = []
    for record in records:
        seq_str = str(record.seq).upper()
        invalid_chars = set(seq_str) - VALID_BASES
        if invalid_chars:
            print(f"Warning: '{record.id}' contains invalid characters {invalid_chars} — skipping.")
            continue
        valid_records.append(record)

    for record in valid_records:
        print(f"ID: {record.id}")
        print(f"Sequence length: {len(record.seq)}")
        print(f"Sequence: {record.seq[:50]}...")
        print("-" * 40)

    return valid_records

if __name__ == "__main__":
    for test_file in ["sample.fasta", "missing_test.fasta", "empty_test.fasta", "garbage_test.fasta", "bad_chars_test.fasta"]:
        print(f"\n=== Testing: {test_file} ===")
        records = parse_fasta(test_file)
        print(f"Total valid sequences found: {len(records)}")

"""
    Parses a FASTA file and validates sequence content.

    Handles:
    - Missing file (FileNotFoundError)
    - Malformed FASTA structure (ValueError)
    - Empty file (zero records parsed)
    - Invalid sequence characters (anything outside A/T/G/C/N)

    Records with invalid characters are skipped entirely and not
    included in the return list — no partial/salvaged sequences.

    Returns:
        list of valid SeqRecord objects. Empty list if file
        doesn't exist, isn't FASTA, or is empty.
    """