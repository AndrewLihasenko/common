import math
import unittest
from homework import Rectangle


class RectangleTestCases(unittest.TestCase):
    def setUp(self):
        self.rectangle_value = Rectangle(width=35, height=50)
        self.square_value = Rectangle(width=35, height=35)

    def test_get_rectangle_perimeter(self):
        actual_result = self.rectangle_value.get_rectangle_perimeter()
        expected_result = (self.rectangle_value.width +
                           self.rectangle_value.height) * 2
        self.assertEqual(actual_result, expected_result)

    def test_get_square_perimeter(self):
        actual_result = self.square_value.get_rectangle_perimeter()
        expected_result = (self.square_value.width +
                           self.square_value.height) * 2
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square(self):
        actual_result = self.rectangle_value.get_rectangle_square()
        expected_result = self.rectangle_value.width * self.rectangle_value.height
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square_for_square(self):
        actual_result = self.square_value.get_rectangle_square()
        expected_result = self.square_value.width * self.square_value.height
        self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners_valid_value(self):
        for corners in range(1, 4):
            with self.subTest(i=corners):
                actual_result = self.rectangle_value.get_sum_of_corners(corners)
                expected_result = corners * 90
                self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners_raises_error(self):
        with self.assertRaises(ValueError):
            corners = 5
            self.rectangle_value.get_sum_of_corners(corners)

    def test_get_rectangle_diagonal(self):
        actual_result = self.rectangle_value.get_rectangle_diagonal()
        expected_result = math.sqrt(math.pow(self.rectangle_value.height, 2) +
                                    math.pow(self.rectangle_value.width, 2))
        self.assertEqual(actual_result, expected_result)

    def test_get_square_diagonal(self):
        actual_result = self.square_value.get_rectangle_diagonal()
        expected_result = math.sqrt(math.pow(self.square_value.height, 2) +
                                    math.pow(self.square_value.width, 2))
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_circumscribed_circle(self):
        actual_result = self.rectangle_value.get_radius_of_circumscribed_circle()
        expected_result = (math.sqrt(math.pow(self.rectangle_value.height, 2) +
                                     math.pow(self.rectangle_value.width, 2))) / 2
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle_valid_value(self):
        actual_result = self.square_value.get_radius_of_inscribed_circle()
        expected_result = self.square_value.width / 2
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle_raises_error(self):
        with self.assertRaises(ValueError):
            self.rectangle_value.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()

