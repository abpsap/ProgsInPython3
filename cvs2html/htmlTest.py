import unittest
from format_op import format_inp

class formatTest(unittest.TestCase):

    def testFormat(self):
        self.assertEqual(format_inp(), None)
        self.assertEqual(format_inp(['An', 'simple', 'sentence', 'Example', 'Here'], 'h2'), ['<h2>', '<b>', 'An', '</b>', 'simple sentence Example', '<b>', 'Here', '</b>', '</h2>'])

if __name__ == "__main__": 
    unittest.main()
