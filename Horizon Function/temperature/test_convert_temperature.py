from unittest import TestCase

import convert_temperature

class TestConvertTemperature(TestCase):

    def test_that_convert_temperature_exists(self):
        convert_temperature.convert_fahrenheit_to_celsius_and_vice_versa(100)

    def test_that_temp_is_greater_than_threshold(self):
        number = 95
        expected = " Cold advisory"
        actual = convert_temperature.convert_fahrenheit_to_celsius_and_vice_versa(number , "F" , 100)
        self.assertEqual(actual , expected)

    def test_that_temp_is_less_than_threshold(self):
        number = 42
        expected = " Heat alert"
        actual = convert_temperature.convert_fahrenheit_to_celsius_and_vice_versa(number)
        self.assertEqual(actual , expected)
