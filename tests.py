from os import replace
import unittest
from substring_replacer import find_replacement, process_text


class TestSubstringReplacer(unittest.TestCase):

    # def test_find_replacement_with_substring(self):
    #     replacement = find_replacement("cat")
    #     self.assertIn("cat", replacement)
    #     # print(replacement)

    # def test_find_replacement_no_substring(self):
    #     replacement = find_replacement("zzzy")
    #     self.assertEqual(replacement, "zzzy")

    def test_process_text_with_string(self):
        input = "The cat sat on the mat."
        result = process_text(input)
        self.assertIn("cat", result)
        self.assertIn("mat", result)
        print(result)
        self.assertTrue(all(isinstance(v, str) for v in result.values()))

    # def test_process_text_with_list(self):
    #     input = ["cat", "dog", "bird", "apple"]
    #     result = process_text(input)
    #     self.assertIn("cat", result)
    #     self.assertIn("dog", result)
    #     print(result)
    #     self.assertTrue(all(isinstance(v, str) for v in result.values()))


# run tests
if __name__ == "__main__":
    unittest.main()
