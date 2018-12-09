import unittest
from lib .db import del_card

class DB_qingli(unittest.TestCase):

    def test_youka_zzz(self):
        """数据清理"""
        del_card(6666666667)