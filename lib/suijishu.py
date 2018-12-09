import string,random

field = string.ascii_letters + string.digits
def userName():    #数字字母随机数
    return "".join(random.sample(field,6))

def cardNumber():
    suiji = random.randint(100000000000, 999999999999)  # 数字随机数
    return suiji



if __name__=="main":
    print(userName())
    print(field)
    print(cardNumber)
