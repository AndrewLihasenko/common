import math
import unittest
from homework import Rectangle


rectangle_value = Rectangle(width=35, height=50)
square_value = Rectangle(width=35, height=35)


class Test(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        actual_result = rectangle_value.get_rectangle_perimeter()
        expected_result = (rectangle_value.width +
                           rectangle_value.height) * 2
        self.assertEqual(actual_result, expected_result)

    def test_get_square_perimeter(self):
        actual_result = square_value.get_rectangle_perimeter()
        expected_result = (square_value.width +
                           square_value.height) * 2
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square(self):
        actual_result = rectangle_value.get_rectangle_square()
        expected_result = rectangle_value.width * rectangle_value.height
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square_for_square(self):
        actual_result = square_value.get_rectangle_square()
        expected_result = square_value.width * square_value.height
        self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners_valid_value(self):
        for corners in range(1, 4):
            with self.subTest(i=corners):
                actual_result = rectangle_value.get_sum_of_corners(corners)
                expected_result = corners * 90
                self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners_raises_error(self):
        with self.assertRaises(ValueError):
            corners = 5
            rectangle_value.get_sum_of_corners(corners)

    def test_get_rectangle_diagonal(self):
        actual_result = rectangle_value.get_rectangle_diagonal()
        expected_result = math.sqrt(math.pow(rectangle_value.height, 2) +
                                    math.pow(rectangle_value.width, 2))
        self.assertEqual(actual_result, expected_result)

    def test_get_square_diagonal(self):
        actual_result = square_value.get_rectangle_diagonal()
        expected_result = math.sqrt(math.pow(square_value.height, 2) +
                                    math.pow(square_value.width, 2))
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_circumscribed_circle(self):
        actual_result = rectangle_value.get_radius_of_circumscribed_circle()
        expected_result = (math.sqrt(math.pow(rectangle_value.height, 2) +
                                     math.pow(rectangle_value.width, 2))) / 2
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle_valid_value(self):
        actual_result = square_value.get_radius_of_inscribed_circle()
        diagonal = math.sqrt(math.pow(square_value.height, 2) +
                             math.pow(square_value.width, 2))
        expected_result = diagonal / 2 * math.sqrt(2)
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle_raises_error(self):
        with self.assertRaises(ValueError):
            rectangle_value.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
