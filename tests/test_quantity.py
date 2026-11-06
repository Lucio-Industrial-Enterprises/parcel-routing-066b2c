import unittest

from warehouse.quantity import parse_quantity


class ParseQuantityTests(unittest.TestCase):
    def test_valid_positive_integer(self):
        self.assertEqual(parse_quantity("3"), 3)

    def test_strips_whitespace(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    # --- regression tests for zero and negative values ---

    def test_zero_raises(self):
        """Zero is not a valid pick-list quantity."""
        with self.assertRaises(ValueError):
            parse_quantity("0")

    def test_negative_raises(self):
        """Negative quantities must be rejected."""
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_negative_large_raises(self):
        """Large negative values must also be rejected."""
        with self.assertRaises(ValueError):
            parse_quantity("-999")
