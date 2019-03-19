import unittest

import question_a



class Test(unittest.TestCase):

    def test_overlapp(self):
        self.assertEqual(question_a.collide((-1, 0), (0, 1)), True, "Should identify collision due to coincident edges" )
        self.assertEqual(question_a.collide((-1, -8), (10, -2)), True, "Should identify collision regardless of the input order." )
        self.assertEqual(question_a.collide((10, 0), (2, 1)), True, "Should identify collision when one line is contained in the other." )
        self.assertEqual(question_a.collide((0, 0), (0, 0)), True, "Should identify collision with a single point." )
        self.assertEqual(question_a.collide((-1, 0), (0, 1)), True, "Should identify no collision regardless of the input order." )
        self.assertEqual(question_a.collide((-1, 0), (2, 1)), False, "Should identify no collision regardless of the input order." )

    def test_match(self):
        self.assertEqual(question_a.cli_match("(3,4), (2,1)"), ((3,4), (2,1)), "Should identify points with parenthesis and comma")
        self.assertEqual(question_a.cli_match("(-3,4), (+2,1)"), ((-3,4), (2,1)), "Should identify points with parenthesis and comma")
        self.assertEqual(question_a.cli_match("(-301238947,4), (+2,110293874)"), ((-301238947,4), (2,110293874)), "Should identify points with multiple numbers")
        self.assertEqual(question_a.cli_match("-301238947 4 +2 110293874"), ((-301238947,4), (2,110293874)), "Should identify regardless of commas or parenthesis")


if __name__ == '__main__':
    unittest.main()
