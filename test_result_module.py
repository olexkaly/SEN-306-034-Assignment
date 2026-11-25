import unittest

from result_module import calculate_total_score
from result_module import generate_result
from result_module import calculate_gpa


class TestResultModule(unittest.TestCase):

    def test_total_score(self):
        result = calculate_total_score(18, 17, 52)
        self.assertEqual(result, 87)

    def test_minimum_total(self):
        result = calculate_total_score(0, 0, 0)
        self.assertEqual(result, 0)

    def test_maximum_total(self):
        result = calculate_total_score(20, 20, 60)
        self.assertEqual(result, 100)

    def test_invalid_assignment(self):
        with self.assertRaises(ValueError):
            calculate_total_score(21, 17, 52)

    def test_invalid_test(self):
        with self.assertRaises(ValueError):
            calculate_total_score(18, 21, 52)

    def test_invalid_examination(self):
        with self.assertRaises(ValueError):
            calculate_total_score(18, 17, 61)

    def test_negative_score(self):
        with self.assertRaises(ValueError):
            calculate_total_score(-1, 17, 52)

    def test_invalid_score_type(self):
        with self.assertRaises(TypeError):
            calculate_total_score("18", 17, 52)

    def test_generate_result(self):
        result = generate_result(
            "John",
            "CSC/2026/001",
            "SWE 306",
            18,
            17,
            52
        )

        self.assertEqual(result["total"], 87)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["grade_point"], 5)

    def test_invalid_student(self):
        with self.assertRaises(ValueError):
            generate_result(
                "",
                "CSC/2026/001",
                "SWE 306",
                18,
                17,
                52
            )

    def test_gpa(self):
        courses = [
            {"grade_point": 5, "credit_unit": 3},
            {"grade_point": 4, "credit_unit": 2},
            {"grade_point": 3, "credit_unit": 3}
        ]

        self.assertEqual(calculate_gpa(courses), 4.0)

    def test_empty_courses(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])

    def test_invalid_grade_point(self):
        courses = [
            {"grade_point": 6, "credit_unit": 3}
        ]

        with self.assertRaises(ValueError):
            calculate_gpa(courses)

    def test_invalid_credit_unit(self):
        courses = [
            {"grade_point": 5, "credit_unit": 0}
        ]

        with self.assertRaises(ValueError):
            calculate_gpa(courses)


if __name__ == "__main__":
    unittest.main()