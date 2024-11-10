import unittest
from math_quiz import get_random_number, get_random_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_get_random_number_with_negative_range(self):
        # Test if random numbers can include negative values
        min_val = -10
        max_val = -1
        for _ in range(1000):
            rand_num = get_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator_distribution(self):
        # Test distribution of operators over a large sample size
        operators_count = {'+': 0, '-': 0, '*': 0}
        iterations = 10000
        
        for _ in range(iterations):
            oper = get_random_operator()
            self.assertIn(oper, ['+', '-', '*'])
            operators_count[oper] += 1
        
        # Check if all operators are selected reasonably evenly
        for op, count in operators_count.items():
            self.assertTrue(count > 0.2 * iterations, f"Operator {op} is underrepresented")

    def test_generate_problem_with_unexpected_operator(self):
        # Test generate_problem with an unsupported operator
        with self.assertRaises(ValueError) as context:
            generate_problem(5, 3, '/')
        
        # Check if the error message is correct
        self.assertEqual(str(context.exception), "Invalid operator")

    def test_generate_problem_with_zero_values(self):
        # Ensure that zero values are handled correctly
        problem, answer = generate_problem(0, 5, '+')
        self.assertEqual(problem, '0 + 5')
        self.assertEqual(answer, 5)

        problem, answer = generate_problem(10, 0, '*')
        self.assertEqual(problem, '10 * 0')
        self.assertEqual(answer, 0)


if __name__ == "__main__":
    unittest.main()
