import pymysql
from config import config


def get_conn():
    conn = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           passwd=config.db_passwd,
                           db=config.db_db,
                           charset=config.db_charset)
    return conn

def db_query(sql):   # 查询
    config.logging.debug(sql)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    r = cur.fetchall()
    config.logging.debug(r)
    #print(r)
    cur.close()
    conn.close()
    return r

def db_change(sql): # 修改
    config.logging.debug(sql)                 #todo 使用logging方法
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()            # 提交修改
    except Exception as e:
        config.logging.error(repr(e))           #打印错误信息 todo logging
        conn.rollback()          #回滚修改
    finally:
        cur.close()
        conn.close()

def cardNumber(cardNumber):
    r = db_query("SELECT * FROM cardinfo WHERE cardNumber = '%d'"  %cardNumber)
    if r[4] == '0':   #余额等于0
        return True
    return False

def update_cardBalance(cardNumber):
    db_change("UPDATE cardinfo SET cardBalance = '0' WHERE cardNumber ='{}'" .format(cardNumber))  # 余额清零

def del_card(cardNumber):
    db_change("DELETE FROM cardinfo WHERE cardNumber = '{}'" .format(cardNumber))


if __name__=="__main__":
    pass
    #print(cardNumber(6666666667))
    print(del_card(6666666667))