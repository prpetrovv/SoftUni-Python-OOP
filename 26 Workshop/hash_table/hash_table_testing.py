import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(100)
        self.hash_table["hello"] = "Hello World!"
        self.hash_table[98.6] = 37
        self.hash_table[False] = True

    def test_create_hash_table(self):
        self.assertIsNotNone(HashTable(10))

    def test_report_size(self):
        self.assertEqual(len(self.hash_table.array), 3)

    def test_inappropriate_size_error(self):
        with self.assertRaises(ValueError) as ve:
            HashTable(0)
        self.assertEqual("The size cannot be less than 1.", str(ve.exception))

    def test_create_empty_pair_slots(self):
        hash_table = HashTable(4)
        expected = [None, None, None, None]
        actual = hash_table._array
        self.assertEqual(expected, actual)

    def test_insert_key_value_pairs(self):
        hash_table = HashTable(4)
        hash_table["hello"] = "Hello World!"
        self.assertIn(("hello", "Hello World!"), hash_table.array)

    def test_find_value_by_key(self):
        self.assertEqual("Hello World!", self.hash_table["hello"])
        self.assertEqual(37, self.hash_table[98.6])
        self.assertTrue(self.hash_table[False])

    def test_string_representation(self):
        actual = str(self.hash_table)
        expected = "{False:True, 98.6:37, 'hello':'Hello World!'}"
        self.assertEqual(actual, expected)

    def test_delete_item(self):
        self.hash_table.__delitem__("hello")
        self.assertNotIn("hello", self.hash_table.keys)


if __name__ == '__main__':
    unittest.main()
