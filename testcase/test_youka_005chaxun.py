import unittest,requests,json
from lib.read_excel import get_case,get_sheet
from config.config import data_path

class TestChaxun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = get_sheet(data_path,"查询卡")

    def test_chaxunchenggong(self):
        """查询成功"""
        case_data = get_case(self.sheet,"test_chaxunchenggong")
        url = case_data[4]
        excepted_res = json.loads(case_data[5])
        res = requests.get(url=url)
        dict = res.json()
        del dict['result']["cardBalance"]
        del dict['result']['consumptionDetails']
        del dict['result']['rechargeDetails']
        self.assertDictEqual(dict,excepted_res)

    def test_chaxunshibai(self):
        """卡号不存在"""
        case_data = get_case(self.sheet,"test_chaxunshibai")
        url = case_data[4]
        excepted_res = json.loads(case_data[5])
        res = requests.get(url=url)
        dict = res.json()
        self.assertDictEqual(dict,excepted_res)

if __name__=="__main":
    unittest.main(verbosity=2)