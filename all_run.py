import unittest
from config.config import report_path,logging
from lib.HTMLTestRunner_PY2_PY3 import HTMLTestReportCN
from lib.send_mail import send_mail


# 发现并收集用例得到一个测试集合
all = unittest.defaultTestLoader.discover("./testcase") #当前文件夹下的所有用例
# 使用文本测试运行器，运行运行这个测试集合

if __name__=="__main__":
    # unittest.TextTestRunner(verbosity=1).run(all)
    logging.info("测试开始" + "=" * 50)
    with open(report_path,"wb") as f:
        HTMLTestReportCN(stream=f,title="接口测试报告",description="测试报告",tester="测试组").run(all)
    logging.info("测试结束" + "=" * 50)
    send_mail()