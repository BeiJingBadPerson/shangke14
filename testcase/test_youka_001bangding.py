import unittest,requests,json
from lib.read_excel import get_sheet,get_case
from config.config import data_path
from lib.case_log import case_log


class TestBangding(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = get_sheet(data_path,"绑定卡")


    def test_001tianjiakachenggong(self):
        """添加卡成功"""
        #log_case_info()
        case_data = get_case(self.sheet, "test_001tianjiakachenggong")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url, json=data)
        case_log(case_data[1],url,case_data[4],case_data[5],res.text)
        self.assertEqual(res.json(), excepted_res)


    def test_002bangdingchenggong(self):
        """绑定成功"""
        case_data = get_case(self.sheet, "test_002bangdingchenggong")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url, json=data)
        case_log(case_data[1],url,case_data[4],case_data[5],res.text)
        self.assertEqual(res.json(), excepted_res)

    def test_003chongfubangka(self):
        """重复绑定卡号"""
        case_data = get_case(self.sheet, "test_003chongfubangka")
        url = case_data[3]
        data = json.loads(case_data[4])
        excepted_res = json.loads(case_data[5])
        res = requests.post(url=url, json=data)
        case_log(case_data[1],url,case_data[4],case_data[5],res.text)
        self.assertEqual(res.json(), excepted_res)




