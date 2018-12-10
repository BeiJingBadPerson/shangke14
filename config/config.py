import logging,os

# 数据库配置
db_host='115.28.108.130'
db_port=3306
db_user='test'
db_passwd='123456'
db_db='longtengserver'
db_charset='utf8'

# 邮件配置
server = "smtp.qq.com"  # smtp服务器 smtp.qq.com
sender = '378699049@qq.com'  # 发送方 378699049@qq.com
emailusername = "378699049@qq.com"  # 登录邮箱的用户名
emailpassword = "ajkxtszgxqaybijd"             # 登录邮箱的密码,请配置自己的 juhmbfvwzeuqcbbd
receiver = "378699049@qq.com" #  接收方,多个收件人以逗号隔开"beijinglixun@gmail.com,yy@qq.com"

# subject = '接口测试报告'
# body = "jie口测试报告"

#is_send_repoet = False


# 项目目录
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 数据目录
data_path = os.path.join(prj_path,'data','加油卡用例.xls')

# 报告目录
report_path = os.path.join(prj_path,'report','report.html')

# 日志配置
log_path = os.path.join(prj_path,'log','log.txt')
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_path,
                    )


if  __name__ == "__main__":
    pass
    logging.info("hello, world")
    logging.info("中文日志")
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # print(prj_path)
    # print(data_path)
    # print(report_file)
    # print(log_file)