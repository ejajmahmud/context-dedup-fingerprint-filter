"""Tests for Dedup Filter."""
import unittest
from context_dedup_fingerprint_filter.core import ContextDedupFingerprintFilter

class TestContextDedupFingerprintFilter(unittest.TestCase):
    def test_dedup_filter(self):
        f = ContextDedupFingerprintFilter(threshold_hamming_distance=2)
        d1 = "Python programming language is awesome and powerful"
        d2 = "Python programming language is awesome and powerful." # punctuation variation
        d3 = "Quantum computing harnesses superposition and entanglement"
        
        filtered = f.filter_unique([d1, d2, d3])
        self.assertEqual(len(filtered), 2)
        self.assertIn(d1, filtered)
        self.assertIn(d3, filtered)
