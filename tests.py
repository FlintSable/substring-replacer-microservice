from os import replace
import unittest
from substring_replacer import find_replacement, process_text


class TestSubstringReplacer(unittest.TestCase):

    def test_find_replacement_with_substring(self):
        replacement = find_replacement("cat")
        self.assertIn("cat", replacement)
        # print(replacement)

    def test_find_replacement_no_substring(self):
        replacement = find_replacement("zzzy")
        self.assertEqual(replacement, "zzzy")


# run tests
if __name__ == "__main__":
    unittest.main()
