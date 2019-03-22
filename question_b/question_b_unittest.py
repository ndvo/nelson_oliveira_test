import unittest

import question_b


#// Nome do software
#// Mais partes
#// Separador pode não ser o ponto
class Test(unittest.TestCase):

    def test_simple_semantic_versioning(self):
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1.9", "0.1.9"), "8.1.9 is greater than 0.1.9", "Major versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.0.9", "8.1.9"), "8.0.9 is less than 8.1.9", "Minor versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1.8", "8.1.9"), "8.1.8 is less than 8.1.9", "Patch versions integer" )

    def test_simple_incomplete_semantic_versioning(self):
        self.assertEqual(question_b.compare_a2b_human_friendly("8", "0.1.9"), "8 is greater than 0.1.9", "Major versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.0", "8.1.9"), "8.0 is less than 8.1.9", "Minor versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1091.8827", "8.11"), "8.1091.8827 is less than 8.11", "Patch versions integer" )
        
    def test_alphanumeric_semantic_versioning(self):
        self.assertEqual(question_b.compare_a2b_human_friendly("8a.1.9", "8.1.9"), "8a.1.9 is greater than 8.1.9", "Major plus letter" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1.9", "8.1b.9"), "8.1.9 is less than 8.1b.9", "Minor versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1.8c", "8.1.9d"), "8.1.8c is less than 8.1.9d", "Patch versions integer" )

    def test_alphanumeric_incomplete_semantic_versioning(self):
        self.assertEqual(question_b.compare_a2b_human_friendly("8a", "8.1.9"), "8a is greater than 8.1.9", "Major plus letter" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8", "8.1b"), "8 is less than 8.1b", "Minor versions integer" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.0c", "8.1.9d"), "8.0c is less than 8.1.9d", "Patch versions integer" )

    def test_named_semantic_versioning(self):
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1-RC1", "8.1-RC"), "8.1-RC1 is greater than 8.1-RC", "Major plus letter" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1-BETA", "8.1-RC"), "8.1-BETA is less than 8.1-RC", "Major plus letter" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1-RELEASE", "8.1-RC"), "8.1-RELEASE is greater than 8.1-RC", "Major plus letter" )
        self.assertEqual(question_b.compare_a2b_human_friendly("8.1-RELEASE", "8.1-RC"), "8.1-RELEASE is greater than 8.1-RC", "Major plus letter" )



if __name__ == '__main__':
    unittest.main()
