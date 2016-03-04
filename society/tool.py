 #-*- coding: utf-8 -*-
from store.models import Item
from xlwt import Workbook
import datetime

def save_mul_item(text):
    text=text.replace('\r\n', '')
    items = text.split(";")
    for item in items:
        content = item.split(" ")
        if len(content) == 3:
            #is unique ?
            try:
                Item.objects.create(
                    code=content[0],
                    name=content[1],
                    price=float(content[2])
                )
            except Exception as e:
                pass

def create_xls(data):
    work = Workbook(encoding='utf-8')
    work_sheet = work.add_sheet(u'活动账单')
    #head of table    
    work_sheet.write(0, 0, 'ID')
    work_sheet.write(0, 1, u'名字')
    work_sheet.write(0, 2, u'手机')
    work_sheet.write(0, 3, u'费用')
    work_sheet.write(0, 4, u'余额')
    work_sheet.write(0, 5, u'备注')
    i = 1
    total_price = 0
    for row in data:
        work_sheet.write(i, 0, str(i))
        work_sheet.write(i, 1, data[row]['name'])
        work_sheet.write(i, 2, data[row]['phone'])
        work_sheet.write(i, 3, data[row]['price'])
        work_sheet.write(i, 4, data[row]['balance'])
        work_sheet.write(i, 5, data[row]['bill_comment'])
        total_price += data[row]['price']
        i = i + 1
    work_sheet.write(i, 4, u'总价:')
    work_sheet.write(i, 5, total_price)
    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "download_xls/bill_%s.xls" % time_stamp
    work.save(file_name)
    return file_name
    #download_file(file_name)

def create_member_xls(data, bill_comment):
    work = Workbook(encoding='utf-8')
    work_sheet = work.add_sheet(u'会员详细活动统计')
    #head of table
    work_sheet.write(0, 0, 'ID')
    work_sheet.write(0, 1, u'名字')
    work_sheet.write(0, 2, u'手机')
    work_sheet.write(0, 3, u'余额')
    for i_act in range(0, len(bill_comment)):
        work_sheet.write(0, 4+i_act, bill_comment[i_act])
    i = 1
    for row in data:
        work_sheet.write(i, 0, str(i))
        work_sheet.write(i, 1, data[row]['name'])
        work_sheet.write(i, 2, data[row]['phone'])
        work_sheet.write(i, 3, data[row]['balance'])
        for i_act in range(0, len(bill_comment)):
            work_sheet.write(i, 4+i_act, data[row][bill_comment[i_act]])
        i = i+1

    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "download_xls/member_%s.xls" % time_stamp
    work.save(file_name)
    return file_name