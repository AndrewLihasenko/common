import math
import unittest
from homework import Rectangle


rect_valid_value = Rectangle(width=25, height=25)


class Test(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        actual_result = rect_valid_value.get_rectangle_perimeter()
        expected_result = (rect_valid_value.width +
                           rect_valid_value.height) * 2
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square(self):
        actual_result = rect_valid_value.get_rectangle_square()
        expected_result = rect_valid_value.width * rect_valid_value.height
        self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners(self):
        corners = 3
        actual_result = rect_valid_value.get_sum_of_corners(corners)
        if corners < 5:
            expected_result = corners * 90
            self.assertEqual(actual_result, expected_result)
        else:
            raise ValueError("Rectangle has only 4 corners")

    def test_get_rectangle_diagonal(self):
        actual_result = rect_valid_value.get_rectangle_diagonal()
        expected_result = math.sqrt(math.pow(rect_valid_value.height, 2) +
                                    math.pow(rect_valid_value.width, 2))
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_circumscribed_circle(self):
        actual_result = rect_valid_value.get_radius_of_circumscribed_circle()
        expected_result = (math.sqrt(math.pow(rect_valid_value.height, 2) +
                                    math.pow(rect_valid_value.width, 2))) / 2
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle(self):
        actual_result = rect_valid_value.get_radius_of_inscribed_circle()
        if rect_valid_value.height == rect_valid_value.width:
            expected_result = rect_valid_value.height / 2
            self.assertEqual(actual_result, expected_result)
        else:
            raise ValueError("Can't inscribed circle in rectangle with such width and height")


if __name__ == "__main__":
    unittest.main()
