def task_1_search_elements_in_two_list(list_a, list_b):
    """
    Take two lists, say for example these two:
    a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates).
    """
    temp = 0
    return list(set([a for a in list_a
                     for b in list_b
                     if a == b and temp != a]))


def task_2_number_of_appears(string):
    """
    Return the number of times that the letter “a” appears anywhere
    in the given string: “I am a good developer. I am also a writer”.
    :return: int
    """
    count = 0
    for s in string:
        if s == 'a':
            count += 1
    return count


def task_3_check_integers_is_a_power_of_three(num):
    """
    Check if a given positive integer is a power of three
    Input : 9
    Output : True
    :param num:
    :return:
    """
    if num == 0:
        raise ValueError("Введено некорректное значение")
    while num > 1:
        if num % 3 != 0:
            return False
        num //= 3
    return True


def task_4_add_digit(num):
    """
    Add the digits of a positive integer repeatedly until the result
    has a single digit.
    Input : 48
    Output : 3

    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    :param num:
    :return:
    """
    while True:
        return sum(int(digit) for digit in str(
            sum(int(digit) for digit in str(num))))


def task_5_push_zero_in_end(list_int):
    """
    Push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    :param list_int:
    :return:
    """
    i = 0
    while 0 in list_int:
        list_int.pop(0)
        i += 1
    for j in range(i):
        list_int.append(0)
    return list_int


def task_6_arith_progressing(list_int):
    """
    Check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    :param list_int:
    :return:
    """
    if len(list_int) < 2:
        return False
    dif = list_int[1] - list_int[0]
    index = 1
    while index < len(list_int) - 1:
        if list_int[index + 1] != list_int[index] + dif:
            return False
        index += 1
    return True


def task_7_find_number_does_not_occur_twice(list_int):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    :param list_int:
    :return:
    """
    for k, v in enumerate(list_int):
        if list_int.count(v) == 1:
            return v


def task_8_find_missing_number(list_int):
    """
    Find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    :param list_int:
    :return:
    """
    for num in range(list_int[0], list_int[-2]+1):
        if num not in list_int:
            return num


def task_9_count_elements_until_a_tuple(list_num):
    """
    To count the elements in a list until an element is a tuple.
    Input: [1,2,3,(1,2),3]
    Output: 3
    :param list_num:
    :return:
    """
    count = 0
    for i in range(len(list_num)):
        count += 1
        if isinstance(list_num[i], tuple):
            return count-1


def task_10_reverse_string(string):
    """
    Take the str parameter being passed and return the string
    in reversed order.
    :param string:
    :return:
    """
    return "".join(reversed(string))


def task_11_separate_num_to_hours_and_minutes(num):
    """
    Take the num parameter being passed and return the number of
    hours and minutes the parameter converts to
    (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    :return:
    """
    hours, minutes = divmod(num, 60)
    return "%d:%d" % (hours, minutes)


def task_12_largest_word_in_string(some_string):
    """
    Take the parameter being passed and return the largest word in
    the string. If there are two or more words that are the same length,
    return the first word from the string with that length. Ignore punctuation.
    Input:"fun&!! time"
    Output:time
    :param some_string:
    :return:
    """
    count = 0
    word = ''
    lst = some_string.split()
    for i in lst:
        if i.isalpha():
            if len(i) > count:
                count = len(i)
                word = i
    return word


def task_13_print_back_string():
    """
    Write a program (using functions!) that asks the user for a long
    string containing multiple words. Print back to the user the same
    string, except with the words in backwards order.
    Input: My name is Michele
    Outout: Michele is name My
    :param:
    :return:
    """
    return ' '.join(list(reversed(input().split())))


def task_14_fibonnaci_numbers():
    """
    Write a program that asks the user how many Fibonnaci numbers
    to generate and then generates them. Take this opportunity to
    think about how you can use functions. Make sure to ask the user
    to enter the number of numbers in the sequence to generate.
    :return:
    """
    fib = [1, 1]
    fib_1 = fib_2 = 1
    num = int(input())
    i = 0
    while i < num - 2:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        i += 1
        fib.append(fib_2)
    return fib


def task_15_generate_list_even_num(list_num):
    """
    List saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list
    that has only the even elements of this list in it.
    :param list_num:
    :return:
    """
    return [num for num in list_num if num % 2 == 0]


def task_16_add_numbers_from_1_to_input():
    """
    Add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program
    should return 10 because 1 + 2 + 3 + 4 = 10
    :return:
    """
    return sum([i for i in range(1, int(input()) + 1)])


def task_17_factorial_of_num(num):
    """
    Take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should
    return (4 * 3 * 2 * 1) = 24.
    :param num:
    :return:
    """
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial


def task_18_replace_letter_and_capitalize_vowel(some_string):
    """
    Take the str parameter being passed and modify it using the
    following algorithm. Replace every letter in the string
    with the letter following it in the alphabet
    (ie. cbecomes d, zbecomes a). Then capitalize every vowel
    in this new string (a, e, i, o, u) and finally return this
    modified string.
    Input: abcd
    Output: bcdE
    :param some_string:
    :return:
    """
    new_string = ''
    for letter in some_string:
        new_letter = chr(ord(letter) + 1)
        if new_letter in "aeiou":
            new_letter = new_letter.upper()
        new_string += new_letter
    return new_string


def task_19_letters_in_alphabetical_order(some_string):
    """
    Take the str string parameter being passed and return the string
    with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    :param some_string:
    :return:
    """
    new_str = ''
    lst = set([ord(i) for i in some_string if i.isalpha()])
    for i in lst:
        new_str += chr(i)
    return new_str


def task_20_compare_two_num(num1, num2):
    """
    Take both parameters being passed and return the true if num2 is
    greater than num1, otherwise return the false. If the parameter
    values are equal to each other then return the string -1
    :param num1:
    :param num2:
    :return:
    """
    if num2 > num1:
        return True
    elif num2 < num1:
        return False
    else:
        return -1