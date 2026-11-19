"""CLI for Dedup Filter."""
import argparse
from .core import ContextDedupFingerprintFilter

def main():
    parser = argparse.ArgumentParser(description="Context Dedup Fingerprint Filter CLI")
    parser.add_argument("--demo", action="store_true", help="Run dedup demo")
    args = parser.parse_args()

    f = ContextDedupFingerprintFilter(threshold_hamming_distance=3)
    docs = [
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy dog!", # Near identical
        "A completely different document about database scaling architectures."
    ]
    unique = f.filter_unique(docs)
    print(f"Original docs: {len(docs)}, Unique docs kept: {len(unique)}")

if __name__ == "__main__":
    main()
