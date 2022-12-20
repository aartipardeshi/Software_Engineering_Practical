import emailotp
import unittest
import re


class TestOTP(unittest.TestCase):

    # Testcase for correct inputs
    def test_case1(self):
        email = 'pardeshiaarti49@gmail.com'
        emailotp.check(email)
        otp = emailotp.generate_otp(5)
        emailotp.otp_length(otp)
        emailotp.send_otp(email,otp)

    # Testcase for Invalid Email:
    def test_valid_email(self):
        email = 'pardeshi@aarti49@gmail.com'
        emailotp.check(email)
        otp = emailotp.generate_otp(5)
        emailotp.otp_length(otp)
        emailotp.send_otp(email, otp)

    # Testcase for Invalid otp length:
    def test_otp_length(self):
        email = 'pardeshiaarti49@gmail.com'
        emailotp.check(email)
        otp = emailotp.generate_otp(4)
        emailotp.otp_length(otp)
        emailotp.send_otp(email, otp)

    def test_random(self):
        x = emailotp.generate_otp(5)
        y = emailotp.generate_otp(5)
        self.assertNotEqual(x, y)


if __name__ == '__main__':
    unittest.main()
