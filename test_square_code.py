import unittest


from square_code import cal_square


class Testcal_square(unittest.TestCase):
    def test_cal_square(self):
        self.assertEqual(cal_square(2), 4)

    def test_cal_square_zero(self):
        self.assertEqual(cal_square(0), 0)

    def test_cal_square_negative_integer(self):
        self.assertEqual(cal_square(-3), 9)

    def test_cal_square_float(self):
        self.assertEqual(cal_square(2.5), 6.25)


if __name__ == '__main__':
    unittest.main()
