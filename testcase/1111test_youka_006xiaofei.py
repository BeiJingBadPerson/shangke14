import unittest,requests
from lib.db import cardNumber,update_cardBalance
from config.config import data_path


class Testxiaofei(unittest.TestCase):

    def test_001xiaofeichenggong(self):
        """消费成功"""
        a = {"code":200,"msg":"消费成功!","success":True}
        url = "http://115.28.108.130:8080/gasStation/process"
        data = {
                "dataSourceId": "bHRz",
                "methodId": "04A",
                "CardUser": {
                    "userId":29
                },
                "CardInfo": {
                    "cardNumber": "6666666667",
                    "cardBalance": "5"
                }
            }
        res = requests.post(url=url,json=data)
        self.assertFalse(cardNumber(6666666667))
        self.assertDictEqual(res.json(),a)




    def test_002xiaofeishibai(self):
        """余额不足"""
        a = {"code":200,"msg":"对不起，您的余额不足，请充值!","success":False}
        url = "http://115.28.108.130:8080/gasStation/process"
        data = {
                "dataSourceId": "bHRz",
                "methodId": "04A",
                "CardUser": {
                    "userId":29
                },
                "CardInfo": {
                    "cardNumber": "6666666667",
                    "cardBalance": "9999999999"
                }
            }
        res = requests.post(url=url,json=data)
        self.assertDictEqual(res.json(),a)

        update_cardBalance(6666666667)    # 余额清零


if __name__=="__main__":
    unittest.main(verbosity=2)