import unittest

from homework import (
    task_1_search_elements_in_two_list,
    task_2_number_of_appears,
    task_3_check_integers_is_a_power_of_three,
    task_4_add_digit,
    task_5_push_zero_in_end,
    task_6_arith_progressing,
    task_7_find_number_does_not_occur_twice,
    task_8_find_missing_number,
    task_9_count_elements_until_a_tuple,
    task_10_reverse_string
)


class UnitTestCase(unittest.TestCase):
    def test_task_1_search_elements_in_two_list(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_result = [1, 2, 3, 5, 8, 13]
        self.assertEqual(task_1_search_elements_in_two_list(a, b),
                         expected_result)

    def test_task_2_number_of_appears(self):
        string = "I am a good developer. I am also a writer"
        self.assertEqual(task_2_number_of_appears(string), 5)

    def test_task_3_check_integers_is_a_power_of_three(self):
        num = 9
        self.assertTrue(task_3_check_integers_is_a_power_of_three(num))

    def test_task_3_check_integers_is_a_power_of_three_error(self):
        with self.assertRaises(ValueError):
            num = 0
            task_3_check_integers_is_a_power_of_three(num)

    def test_task_4_add_digit(self):
        self.assertEqual(task_4_add_digit(34), 7)
        self.assertEqual(task_4_add_digit(68), 5)

    def test_task_5_push_zero_in_end(self):
        list_int = [0, 2, 3, 4, 6, 7, 10]
        except_list_int = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(task_5_push_zero_in_end(list_int), except_list_int)

    def test_task_6_arith_progressing(self):
        list_int = [5, 7, 9, 11]
        list_int_false = [5, 7, 9, 14]
        self.assertTrue(task_6_arith_progressing(list_int))
        self.assertFalse(task_6_arith_progressing(list_int_false))

    def test_task_7_find_number_does_not_occur_twice(self):
        a = [5, 3, 4, 3, 4]
        self.assertEqual(task_7_find_number_does_not_occur_twice(a), 5)

    def test_task_8_find_missing_number(self):
        a = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(task_8_find_missing_number(a), 5)

    def test_task_9_count_elements_until_a_tuple(self):
        a = [1, 2, 3, (1, 2), 3]
        self.assertEqual(task_9_count_elements_until_a_tuple(a), 3)

    def test_task_10_reverse_string(self):
        string = "Hello World and Coders"
        reverse_string = "sredoC dna dlroW olleH"
        self.assertEqual(task_10_reverse_string(string), reverse_string)


if __name__ == "__main__":
    unittest.main()
