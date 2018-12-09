import xlrd

# 打开excel并返回工作表
def get_sheet(file,name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(name)
    return sheet

# 从工作表找到数据
def get_case(sheet,case_name):
    for i in range(1,sheet.nrows):
        if sheet.cell(i,1).value == case_name:
            return sheet.row_values(i)

if __name__=="__main__":
    sh = get_sheet("../data/加油卡用例.xls","添加卡")
    sh1 = get_sheet("../data/油卡查询.xlsx","查询卡")
    print(get_case(sh,"test_001tianjiakachenggong"))
    print(get_case(sh1,"test_chaxunshibai"))