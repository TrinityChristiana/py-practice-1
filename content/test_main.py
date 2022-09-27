"""Tests for Python Practice 1"""
import unittest
from . import main


class TestSum(unittest.TestCase):
    """Test Suite for Python Practice 1"""

    def test_new_string(self):
        """Testing #1. create a string variable, it can contain anything"""

        self.assertIsInstance(main.NEW_STRING, str, "should be a string")

    def test_new_num(self):
        """Testing #2. create a number variable, it can be any number"""

        self.assertIsInstance(main.NEW_NUM, int, "should be a number")

    def test_new_bool(self):
        """Testing #3. create a boolean variable"""

        self.assertIsInstance(main.NEW_BOOL, bool, "should be a boolean")

    def test_new_subtract(self):
        """Testing #4. solve the following math problem"""

        self.assertTrue(main.NEW_SUBTRACT, "should be a boolean")

    def test_new_multiply(self):
        """Testing #5. Solve the following math problem"""

        self.assertTrue(main.NEW_MULTIPLY, "should be a boolean")

    def test_new_modulo(self):
        """Testing #6. Solve the following math problem"""

        self.assertTrue(main.NEW_MODULO, "should be a boolean")

    def test_return_string(self):
        """Testing #7. simply return the string provided: string"""

        string = "Code Tracker"
        self.assertEqual(main.return_string(string), string, "should return the string provided")

    def test_add(self):
        """Testing #8. int_x and int_y are numbers.
        add int_x and int_y together and return the value"""

        self.assertEqual(main.add(5, 5), 10, "should return the sum of the two arguments")
        self.assertEqual(main.add(-1, 5), 4, "should return the sum of the two arguments")

    def test_subtract(self):
        """Testing #9. subtract int_y from int_x and return the value"""

        self.assertEqual(main.subtract(5, 5), 0,
                         "should return the difference of the two arguments")
        self.assertEqual(main.subtract(-1, 5), -6,
                         "should return the difference of the two arguments")
        self.assertEqual(main.subtract(5, -5), 10,
                         "should return the difference of the two arguments")
        self.assertEqual(main.subtract(0, 0), 0,
                         "should return the difference of the two arguments")

    def test_multiply(self):
        """Testing #10. multiply int_x by int_y and return the value"""

        self.assertEqual(main.multiply(5, 5), 25,
                         "should return the product of the two arguments")
        self.assertEqual(main.multiply(10, -5), -50,
                         "should return the product of the two arguments")
        self.assertEqual(main.multiply(11, 0), 0,
                         "should return the product of the two arguments")

    def test_divide(self):
        """Testing #11. divide int_x by int_y and return the value"""
        self.assertEqual(main.divide(5, 5), 1,
                         "should return the quotient of the two arguments")
        self.assertEqual(main.divide(10, 5), 2,
                         "should return the quotient of the two arguments")
        self.assertEqual(main.divide(11, 2), 5.5,
                         "should return the quotient of the two arguments")

    def test_are_equal(self):
        """Testing #12. return true if int_x and int_y are the same otherwise return false"""

        self.assertTrue(main.are_equal(15, 15),
                        "should return true if the arguments are equal")
        self.assertFalse(main.are_equal(90, 50),
                         "should return true if the arguments are equal")
        self.assertTrue(main.are_equal("test", "test"),
                        "should return true if the arguments are equal")

    def test_are_same_length(self):
        """Testing #13. return true if the two strings have the same length
        otherwise return false"""

        self.assertFalse(main.are_same_length("hi", "there"),
                         "should return true if the arguments have the same length")
        self.assertTrue(main.are_same_length("javascript", "bumfuzzled"),
                        "should return true if the arguments have the same length")

    def test_less_than_ninety(self):
        """Testing #14. return true if the def argument: num , is less than ninety"""

        self.assertTrue(main.less_than_ninety(15),
                        "should return true if the argument is less than ninety")
        self.assertFalse(main.less_than_ninety(90),
                         "should return true if the argument is less than ninety")
        self.assertFalse(main.less_than_ninety(100),
                         "should return true if the argument is less than ninety")

    def test_greater_than_fifty(self):
        """Testing #15. return true if num is greater than fifty otherwise return false"""

        self.assertFalse(main.greater_than_fifty(15),
                         "should return true if the argument is greater than fifty")
        self.assertFalse(main.greater_than_fifty(50),
                         "should return true if the argument is greater than fifty")
        self.assertTrue(main.greater_than_fifty(60),
                        "should return true if the argument is greater than fifty")

    def test_get_remainder(self):
        """Testing #16. return the remainder from dividing int_x by int_y"""

        self.assertEqual(main.get_remainder(5, 5), 0,
                         "should return the division remainder of the two arguments")
        self.assertEqual(main.get_remainder(10, 5), 0,
                         "should return the division remainder of the two arguments")
        self.assertEqual(main.get_remainder(11, 2), 1,
                         "should return the division remainder of the two arguments")

    def test_is_even(self):
        """Testing #17. return true if num is even otherwise return false"""

        self.assertTrue(main.is_even(6),
                        "should return the bool true if the argument is even, false otherwise")
        self.assertFalse(main.is_even(7),
                         "should return the bool true if the argument is even, false otherwise")
        self.assertTrue(main.is_even(0),
                        "should return the bool true if the argument is even, false otherwise")

    def test_is_odd(self):
        """Testing #18. return true if num is odd otherwise return false"""

        self.assertFalse(main.is_odd(6),
                         "should return the bool true if the argument is odd, false otherwise")
        self.assertTrue(main.is_odd(7),
                        "should return the bool true if the argument is odd, false otherwise")
        self.assertFalse(main.is_odd(0),
                         "should return the bool true if the argument is odd, false otherwise")

    def test_square(self):
        """Testing #19. square num and return the new value"""

        self.assertEqual(main.square(6), 36,
                         "should return the argument after squaring it")
        self.assertEqual(main.square(7), 49,
                         "should return the argument after squaring it")
        self.assertEqual(main.square(0), 0,
                         "should return the argument after squaring it")
        self.assertEqual(main.square(-5), 25,
                         "should return the argument after squaring it")

    def test_cube(self):
        """Testing #20. cube num and return the new value"""

        self.assertEqual(main.cube(3), 27,
                         "should return the argument after cubing it")
        self.assertEqual(main.cube(0), 0,
                         "should return the argument after cubing it")
        self.assertEqual(main.cube(-5), -125,
                         "should return the argument after cubing it")

    def test_raise_to_power(self):
        """Testing #21. raise num to whatever power is passed in as exponent"""

        self.assertEqual(main.raise_to_power(2, 2), 4,
                         "should return the argument after raising it to the exponent's power")
        self.assertEqual(main.raise_to_power(2, 3), 8,
                         "should return the argument after raising it to the exponent's power")
        self.assertEqual(main.raise_to_power(0, 5), 0,
                         "should return the argument after raising it to the exponent's power")
        self.assertEqual(main.raise_to_power(10, 1), 10,
                         "should return the argument after raising it to the exponent's power")

    def test_round_number(self):
        """Testing #22. round num and return it"""

        self.assertEqual(main.round_number(1.5), 2, "should return the argument after rounding it")
        self.assertEqual(main.round_number(2), 2, "should return the argument after rounding it")
        self.assertEqual(main.round_number(0.1), 0, "should return the argument after rounding it")

    def test_round_up(self):
        """Testing #23. round num up and return it"""

        self.assertEqual(main.round_up(1.5), 2, "should return the argument after rounding it up")
        self.assertEqual(main.round_up(2), 2, "should return the argument after rounding it up")
        self.assertEqual(main.round_up(0.1), 1, "should return the argument after rounding it up")

    def test_add_exclamation_point(self):
        """Testing #24. add an exclamation point to the end of string and
        return the new string: 'hello world' -> 'hello world!'"""

        self.assertEqual(main.add_exclamation_point("hello world"), "hello world!",
                         "should add an exclamation point to the end of the string")
        self.assertEqual(main.add_exclamation_point("CodeTracker"), "CodeTracker!",
                         "should add an exclamation point to the end of the string")

    def test_combine_names(self):
        """Testing #25. return firstName and lastName combined as one
        string and separated by a space: 'Code', 'Tracker' -> 'Code Tracker'"""

        self.assertEqual(main.combine_names("hello", "world"), "hello world",
                         "should return the two strings combined into one with a space separating them")
        self.assertEqual(main.combine_names("Code", "Tracker"), "Code Tracker",
                         "should return the two strings combined into one with a space separating them")

    def test_get_greeting(self):
        """Testing #26. Take the name string and concatenate other
        strings onto it so it takes the following form: 'Sam' -> 'Hello Sam!'"""

        self.assertEqual(main.get_greeting("Ben"), "Hello Ben!",
                         "should return the string 'Hello {name}!'")
        self.assertEqual(main.get_greeting("CodeTracker"), "Hello CodeTracker!",
                         "should return the string 'Hello {name}!'")

    def test_get_rectangle_area(self):
        """Testing #27. return the area of the rectangle by using length and width"""

        self.assertEqual(main.get_rectangle_area(2, 2), 4, "should return the correct area")
        self.assertEqual(main.get_rectangle_area(3, 6), 18, "should return the correct area")
        self.assertEqual(main.get_rectangle_area(0, 2), 0, "should return the correct area")

    def test_get_triangle_area(self):
        """Testing #28. return the area of the triangle by using base and height"""
        self.assertEqual(main.get_triangle_area(2, 2), 2, "should return the correct area")
        self.assertEqual(main.get_triangle_area(0, 2), 0, "should return the correct area")


if __name__ == '__main__':
    unittest.main()
