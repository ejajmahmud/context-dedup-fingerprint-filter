"""Core SimHash Semantic Deduplication Filter."""
from typing import List, Set, Tuple
import hashlib
import re

class ContextDedupFingerprintFilter:
    def __init__(self, threshold_hamming_distance: int = 3):
        self.threshold = threshold_hamming_distance
        self.fingerprints: List[int] = []

    def compute_simhash(self, text: str) -> int:
        words = re.findall(r"\w+", text.lower())
        if not words:
            return 0
        v = [0] * 64
        for word in words:
            h = int(hashlib.md5(word.encode("utf-8")).hexdigest()[:16], 16)
            for i in range(64):
                bit = (h >> i) & 1
                v[i] += 1 if bit == 1 else -1

        fingerprint = 0
        for i in range(64):
            if v[i] > 0:
                fingerprint |= (1 << i)
        return fingerprint

    def hamming_distance(self, h1: int, h2: int) -> int:
        x = h1 ^ h2
        return bin(x).count("1")

    def is_duplicate(self, text: str) -> bool:
        fp = self.compute_simhash(text)
        for existing in self.fingerprints:
            if self.hamming_distance(fp, existing) <= self.threshold:
                return True
        self.fingerprints.append(fp)
        return False

    def filter_unique(self, documents: List[str]) -> List[str]:
        unique = []
        for doc in documents:
            if not self.is_duplicate(doc):
                unique.append(doc)
        return unique
