import unittest
from groupAnagrams import group_anagrams


class AnagramsUnitTests(unittest.TestCase):
    def test_group_anagrams(self):
        """Default test"""
        result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        self.assertEqual(result, [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    def test_group_anagrams_empty(self):
        """Test for empty"""
        result = group_anagrams([])
        self.assertEqual(result, [])
    def test_group_anagrams_one(self):
        """Test for one group"""
        result = group_anagrams(['a'])
        self.assertEqual(result, [['a']])
    def test_group_anagrams_none(self):
        """Test for none grouped"""
        result = group_anagrams(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.assertEqual(result, [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g']])
    def test_group_anagrams_all(self):
        """Test for all grouped"""
        result = group_anagrams(['asd', 'dsa', 'sad'])
        self.assertEqual(result, [['asd', 'dsa', 'sad']])
    def test_group_anagrams_numeric(self):
        """Test for numeric grouped"""
        result = group_anagrams(['123', '321', '213'])
        self.assertEqual(result, [['123', '321', '213']])
    def test_group_anagrams_duplicates(self):
        """Test for duplicate groups"""
        result = group_anagrams(['a', 'a'])
        self.assertEqual(result, [['a', 'a']])
    def test_catch_list(self):
        with self.assertRaises(ValueError):
            group_anagrams(1)
    def test_catch_list_items(self):
        with self.assertRaises(ValueError):
            group_anagrams([1])

if __name__ == "__main__":
    unittest.main()