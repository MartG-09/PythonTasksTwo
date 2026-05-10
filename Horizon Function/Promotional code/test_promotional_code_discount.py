import unittest

import promotional_code_discount

class TestPromotionalCodeDiscount(unittest.TestCase):
    
    def test_that_promotional_code_discount_exists(self):
        promotional_code_discount.get_discounted_price("dog" , 200 , "")

    def test_that_save10_code_gives_10percent_discount(self):
        code = "Save10"
        expected = 180
        price = 200
        item = "dog"
        actual = promotional_code_discount.get_discounted_price(item , price , code)
        self.assertEqual(expected , actual)

    def test_that_halfoff_code_gives_50percent_discount(self):
        code = "halfoff"
        expected = 100
        price = 200
        item = "dog"
        actual = promotional_code_discount.get_discounted_price(item , price , code)
        self.assertEqual(expected , actual)

    def test_that_anyother_code_gives_0percent_discount(self):
        code = "myBol"
        expected = 200
        price = 200
        item = "dog"
        actual = promotional_code_discount.get_discounted_price(item , price , code)
        self.assertEqual(expected , actual)

    def test_that_price_less_thsn_0_raises_valueerror(self):
        with self.assertRaises(ValueError):
            promotional_code_discount.get_discounted_price("dog" , -100 , "Halfoff")

