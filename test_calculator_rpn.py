import unittest
from calculator_rpn import tokenize, infix_to_rpn, eval_rpn, calculate


class TestCalculatorRPN(unittest.TestCase):

    def test_tokenize(self):
        expected_tokens = [
            '3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')',
            '**', '2', '**', '3'
        ]
        self.assertEqual(
            tokenize('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'),
            expected_tokens
        )

    def test_infix_to_rpn(self):
        tokens = tokenize('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3')
        expected_rpn = [
            '3', '4', '2', '*', '1', '5', '-', '2', '3', '**',
            '**', '/', '+'
        ]
        rpn = infix_to_rpn(tokens)
        self.assertEqual(rpn, expected_rpn)

    def test_eval_rpn(self):
        rpn = [
            '3', '4', '2', '*', '1', '5', '-', '2', '3', '**',
            '**', '/', '+'
        ]
        result = eval_rpn(rpn)
        self.assertAlmostEqual(result, 3.0001220703125)

    def test_calculate(self):
        expr = '3 + 4 * 2 / (1 - 5) ** 2 ** 3'
        self.assertAlmostEqual(calculate(expr), 3.0001220703125)

    def test_simple(self):
        self.assertEqual(calculate('2 + 3 * 4'), 14)

    def test_power(self):
        self.assertEqual(calculate('2 ** 3 ** 2'), 512)

    def test_parentheses(self):
        self.assertEqual(calculate('(2 + 3) * 4'), 20)

    def test_division(self):
        self.assertAlmostEqual(calculate('8 / 4 / 2'), 1)

    def test_prioritise(self):
        self.assertEqual(calculate('2 + 2 * 2'), 6)


if __name__ == '__main__':
    unittest.main()
