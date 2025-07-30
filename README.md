# the-tell-tail-part

A bitwise proof of the Collatz Conjecture via tail collapse analysis. The least significant bits tell the tale - exhaustive verification included.

## Paper

"A Bitwise Structural Proof of the Collatz Conjecture"

### Available Formats

- **Published Version**: [Zenodo DOI: 10.5281/zenodo.16617039](https://zenodo.org/records/16617039)
- **With Line Numbers**: [PDF](paper/with_line_numbers/Bitwise_Structural_Proof_of_the_Collatz_Conjecture.pdf)
- **Without Line Numbers**: [PDF](paper/without_line_numbers/Bitwise_Structural_Proof_of_the_Collatz_Conjecture.pdf)

## Verification Code

- `verify_collatz.py` - Main verification program
- Results for k=8, 12, 16 included

## Usage

```bash
python verify_collatz.py -k 8   # Verify all 8-bit patterns
python verify_collatz.py -k 16  # Verify all 16-bit patterns (default)