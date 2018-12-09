import unittest,requests,json
from lib.read_excel import get_sheet,get_case
from lib.db import del_card
from config.config import data_path

class Testtianjiaka(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = get_sheet(data_path, "添加卡")

    def test_001tianjiakachenggong(self):
        """添加加油卡成功"""
        case_data = get_case(self.sheet,"test_001tianjiakachenggong")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url,json=data)
        self.assertEqual(res.json(),excepted_res)

    def test_002chongfutianjiaka(self):
        """重复添加加油卡"""
        case_data = get_case(self.sheet,"test_002chongfutianjiaka")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url,json=data)
        self.assertEqual(res.json(),excepted_res)
        del_card(7777777)




if __name__=="__main__":
    unittest.main(verbosity=2)
