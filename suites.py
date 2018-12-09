import unittest
from testcase import test_youka_001bangding

smoke_suite = unittest.TestSuite()

smoke_suite.addTest(test_youka_001bangding.Testbangding("bangdingchenggong"))

# smoke_suite.addTest(test_reg.TestReg("test_reg_fail"))
#
#
# smoke_suite.addTests([test_login.Testuserlogin('test_login_normal'),
#                       test_login.Testuserlogin('test_login_password_wrong')])


if __name__=="__main__":
    unittest.TextTestRunner(verbosity=2).run(smoke_suite)