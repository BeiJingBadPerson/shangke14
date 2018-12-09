import unittest,requests,json
from lib.read_excel import get_case,get_sheet
from config.config import data_path

class Testchongzhi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = get_sheet(data_path,"充值")

    def test_chongzhichenggong(self):
        """充值成功"""
        case_data = get_case(self.sheet,"test_chongzhichenggong")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url,json=data)
        dict = res.json()
        dict.pop("result")
        self.assertDictEqual(dict,excepted_res,)


    def test_chongzhishibai(self):
        """加油卡号不存在"""
        case_data = get_case(self.sheet,"test_chongzhishibai")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url,json=data)
        self.assertDictEqual(res.json(),excepted_res,)


if __name__=="__main__":
    unittest.main(verbosity=2)