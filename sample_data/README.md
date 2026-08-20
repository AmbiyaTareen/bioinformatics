# Sample Data

Test files used to validate `parser_with_errorhandling.py`. Each file exercises a specific case the parser is expected to handle.

| File | Purpose | Expected behavior |
|---|---|---|
| `sample.fasta` | Valid FASTA file (3 sequences: seq1, seq2, seq3) | Parses cleanly — returns sequence IDs, lengths, and content with no errors |
| `empty_test.fasta` | Empty file | Raises a `ValueError` for an empty/malformed FASTA |
| `garbage_test.fasta` | Non-FASTA content (no `>` headers, junk text) | Raises a `ValueError` for malformed FASTA format |
| `bad_chars_test.fasta` | Sequence containing characters outside A/T/G/C/N | Raises a `ValueError` on invalid sequence content |
| *(no file)* — missing file case | N/A | Point the parser at a nonexistent filename, e.g. `nonexistent.fasta`, to trigger `FileNotFoundError` |

## Running the tests

```bash
python parser_with_errorhandling.py sample_data/sample.fasta
python parser_with_errorhandling.py sample_data/empty_test.fasta
python parser_with_errorhandling.py sample_data/garbage_test.fasta
python parser_with_errorhandling.py sample_data/bad_chars_test.fasta
python parser_with_errorhandling.py sample_data/nonexistent.fasta
```

Same test set used in the Dockerized version — see the Docker video walkthrough for a live run of all five cases inside a container.