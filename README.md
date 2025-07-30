# the-tell-tail-part

A bitwise proof of the Collatz Conjecture via tail collapse analysis. The least significant bits tell the tale - exhaustive verification included.

## Paper

"A Bitwise Structural Proof of the Collatz Conjecture" - [link to arXiv when available]

## Verification Code

- `verify_collatz.py` - Main verification program
- Results for k=8, 12, 16 included

## Usage

```bash
python verify_collatz.py -k 8   # Verify all 8-bit patterns
python verify_collatz.py -k 16  # Verify all 16-bit patterns (default)