# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Created on 2016-12-26

@author: Alibaba Open Platform

"""
import configparser
import datetime
import json

import os
import requests
import time

"""1. Import modules"""
import aop
import aop.api
import pymssql

#获取配置信息
path=os.getcwd()
path2=path+'\config.ini'
config = configparser.ConfigParser()
config.read(path2)
#获取到配置信息中的appkey和秘钥信息
appkey=config.get('default_config', 'appkey')
app_secret=config.get('default_config', 'app_secret')
refresh_token=config.get('default_config', 'refresh_token')
#获取到配置文件中的数据库信息
server=config.get('target', 'server')
user=config.get('target', 'user')
password=config.get('target', 'password')
database=config.get('target', 'database')

#连接数据库
conn=pymssql.connect(server=server,user = user,password=password,database=database)
cursor1=conn.cursor()

#### Default settings, begin
"""2. Remote server

Remote server is the server domain or ip. e.g. 'gw.open.1688.com' for 1688.

Set the default server by calling aop.set_default_server(remote_server).
You can also specify the server when newing an API request.
    e.g. req = aop.api.GetServerTimestampRequest(remote_server)

"""
aop.set_default_server('gw.open.1688.com')

"""3. Appkey and secret

Set the default appinfo by calling aop.set_default_appinfo(appkey, secret)
If you need to dynamically bind a different appinfo to the request, call req.set_appinfo(appkey, secret)

"""
aop.set_default_appinfo(appkey, app_secret) # default
#获取到access token



"""4.Timestamp

Timestamp is milliseconds since midnight, January 1, 1970 UTC and needed by some APIs
due to security concerns.

Timestamp generator is a function taking three arguments: appkey, secret, server domain.

Generally, there are three policy to generate the timestamp.
1) Use the local time every time.
    This is the default policy.
    Ensure that the time difference between your local machine and the server is tiny.
2) Use the server time every time. NOT RECOMMENDED!
    Just call aop.set_timestamp_generator(aop.get_server_timestamp).
    But remember that API '1/system/currentTimeMillis' will be called to get the server
    timestamp and there is a call limit for the API per 10-minutes.
3) Get the timestamp by the formula: timestamp = local_timestamp + timestamp_diff.
    "timestamp_diff" is the time difference between the server and the local that saved
    somewhere and periodically synchronized by calling aop.get_timestamp_diff(appkey, secret, server).
    e.g.
        1> periodically synchronize timestamp_diff:
            timestamp_diff = aop.get_timestamp_diff(appkey, secret, server)
        2> aop.set_timestamp_generator(lambda appkey, secret, server: timestamp_diff + aop.get_local_timestamp())

"""
# aop.set_timestamp_generator(custom_timestamp_generator)
#### Default settings, end
#调用1688的re接口
get_access_token=requests.get('https://gw.open.1688.com/openapi/param2/1/system.oauth2/getToken/'+appkey+'?grant_type=refresh_token&client_id='+appkey+'&client_secret='+app_secret+'&refresh_token='+refresh_token)
access_token=json.loads(get_access_token.content.decode())
acc=access_token.get('access_token')

#获取时间
# a=time.strftime("%Y-%m-%d", time.localtime())

#获取当前时间
now_time=datetime.datetime.now()
#处理格式
end_time=str(datetime.datetime.now()).split(' ')[0].replace('-','')
#获取30天前的时间
end_time1= now_time + datetime.timedelta(days=-30)
print(end_time)
#处理格式
start_time=str(end_time1).split(' ')[0].replace('-','')
#固定的时间字符串 因为要拼接成规定的java。date类型
fixed_time='211113000+0800'


"""5. New an API request"""
req = aop.api.AlibabaTradeGetSellerOrderListParam()
req.access_token =acc
# req.createEndTime =str(end_time)+fixed_time
# req.createStartTime = str(start_time)+fixed_time

req.createEndTime ='20190212182554000+0800'
req.createStartTime ='20180612182554000+0800'
req.isHis =' '
req.modifyEndTime = ' '
req.modifyStartTime = ' '
req.orderStatus = ' '
# req.page =4
req.pageSize =60
req.refundStatus = ' '
req.buyerMemberId = ' '
req.buyerRateStatus = ' '
req.tradeType = ' '
req.bizTypes = ' '
req.productName = ' '
req.needBuyerAddressAndPhone = ' '
req.needMemoInfo = ' '
req.sellerRateStatus = ' '
req.tousuStatus = ' '
# req = aop.api.AuthGetTokenRequest() # Use the default server that set by aop.set_default_server(remote_server)

"""6. Access token

Two related APIs: AuthGetTokenRequest/AuthPostponeTokenRequest

References
---------
https://open.1688.com/api/sysAuth.htm

"""
# req.access_token = 'a1c21354-f4d8-43cc-86df-6f6db44d9910'


"""7. File upload (FileItem)

FileItem is used when the type of an API parameter is byte[].
And finally we will send a multipart request to the server.

Parameters
----------
filecontent: file-like-object(str/bytes/bytearray or an object that has read attribute)
    e.g. f = open('filepath', 'rb') ...  fileitem = aop.api.FileItem('filename', f)
    e.g. fileitem = aop.api.FileItem('filename', 'file_content_str')

"""
# req.file_item_param = aop.api.FileItem(filename, filecontent)


"""8. Other parameters"""
# req.other_param = param_json_value


"""9. Send the request

Raises
------
ApiError
    The remote server returned error and the error messages were successfully recognized.

AopError
    1) Failed before sending a request.
        e.g. Some of the required parameters missing.
    2) Failed to parse the returned results.

"""
result_list=[]
try:
    for i in range(1,5):
        req.page=i
        resp = req.get_response()
        result1=resp.get('result')
        if result1 !=[]:
            result_list.append(result1)



except aop.ApiError as e:
    print(e)
    # pass #log
except aop.AopError as e:
    print(e)
    # pass #log
except Exception as e:
    print(e)
    # pass #log
#拿到接口返回结果

# print(result)





#向国内物流ALIBABA_nativeLogistics导入
def prc_ALIBABA_nativeLogistics():

    for resu in result_list:
        result = resu
        for item in result:

            prc_nativeLogistics = ''
            address = ''
            area = ''
            areaCode = ''
            city = ''
            contactPerson = ''
            fax = ''
            mobile = ''
            province = ''
            telephone = ''
            zip = ''
            #取order_id
            prc_baseInfo = item.get('baseInfo')

            order_id = str(prc_baseInfo.get('id'))

            prc_nativeLogistics=item.get('nativeLogistics')


            address=prc_nativeLogistics.get('address')
            if address is None:
                address='None'
            area= prc_nativeLogistics.get('area')
            if area is None:
                area='None'
            areaCode= prc_nativeLogistics.get('areaCode')
            if areaCode is None:
                areaCode='None'
            city= prc_nativeLogistics.get('city')
            if city is None:
                city='None'
            contactPerson= prc_nativeLogistics.get('contactPerson')
            if contactPerson is None:
                contactPerson='None'
            fax= prc_nativeLogistics.get('fax')
            if fax is None:
                fax='None'
            mobile= prc_nativeLogistics.get('mobile')
            if mobile is None:
                mobile='None'
            province= prc_nativeLogistics.get('province')
            if province is None:
                province='None'
            telephone= prc_nativeLogistics.get('telephone')
            if telephone is None:
                telephone='None'
            zip= prc_nativeLogistics.get('zip')
            if zip is None:
                zip='None'
            insert_ALIBABA_nativeLogistics_sql="insert into ALI_BABA_nativeLogistics(order_id,address,area,areaCode,city,contactPerson,fax,mobile,province,telephone,zip)VALUES ("+"'"+order_id+"',"+"'"+address+"',"+"'"+area+"',"+"'"+areaCode+"',"+"'"+city+"',"+"'"+contactPerson+"',"+"'"+fax+"',"+"'"+mobile+"',"+"'"+province+"',"+"'"+telephone+"',"+"'"+zip+"')"
            cursor1.execute(insert_ALIBABA_nativeLogistics_sql)
            conn.commit()
            print('ALI_BABA_nativeLogistics插入成功')


    #向商品条目信息ALIBABA_productItems导入数据


def prc_ALIBABA_productItems():


    for resu in result_list:
        result = resu

        for item in result:

            # print(i)
            # print(item)
            cargoNumber = ''
            description = ''
            itemAmount = ''
            name = ''
            price = ''
            productID = ''
            productImgUrl = ''
            productSnapshotUrl = ''
            quantity = ''
            refund = ''
            skuID = ''
            sort = ''
            status = ''
            subItemID = ''
            type = ''
            unit = ''
            weight = ''
            weightUnit = ''
            # 取order_id
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))

            prc_nativeLogistics1 = item.get('productItems')
            prc_nativeLogistics2=list(prc_nativeLogistics1)

            #由于取出的对象prc_nativeLogistics1是个多维数组 所以要转为dict

            for prc_nativeLogistics_result in prc_nativeLogistics2:

                # prc_nativeLogistics=eval(str(prc_nativeLogistics2).strip('[').rstrip(']'))
                prc_nativeLogistics=prc_nativeLogistics_result
                cargoNumber = prc_nativeLogistics.get('cargoNumber')

                if cargoNumber is None  or cargoNumber=='':
                    cargoNumber = 'None'
                # print(cargoNumber)
                description = prc_nativeLogistics.get('description')

                if description is None  or description=='':
                    description = 'None'
                itemAmount = prc_nativeLogistics.get('itemAmount')
                if itemAmount is None  or itemAmount=='':
                    itemAmount = 'None'
                name = prc_nativeLogistics.get('name')
                if name is None  or name=='':
                    name = 'None'
                price = prc_nativeLogistics.get('price')
                if price is None  or price=='':
                    price = 'None'
                productID = prc_nativeLogistics.get('productID')

                if productID is None  or productID=='':
                    productID = 'None'
                productImgUrl = str(prc_nativeLogistics.get('productImgUrl')).replace('[','(').replace(']',')').replace("'",'')
                if productImgUrl is None  or productImgUrl=='':
                    productImgUrl = 'None'
                productSnapshotUrl = prc_nativeLogistics.get('productSnapshotUrl')
                if productSnapshotUrl is None  or productSnapshotUrl=='':
                    productSnapshotUrl = 'None'
                quantity = prc_nativeLogistics.get('quantity')
                if quantity is None  or quantity=='':
                    quantity = 'None'
                refund = prc_nativeLogistics.get('refund')
                if refund is None  or refund=='':
                    refund = 'None'
                skuID = prc_nativeLogistics.get('skuID')

                if skuID is None  or skuID=='':
                    skuID = 'None'
                sort = prc_nativeLogistics.get('sort')
                if sort is None  or sort=='':
                    sort = 'None'
                status = prc_nativeLogistics.get('status')
                if status is None  or status=='':
                    status = 'None'
                subItemID = prc_nativeLogistics.get('subItemID')

                if subItemID is None  or subItemID=='':
                    subItemID = 'None'
                type = prc_nativeLogistics.get('type')
                if type is None  or type=='':
                    type = 'None'
                unit = prc_nativeLogistics.get('unit')
                if unit is None  or unit=='':
                    unit = 'None'
                weight = prc_nativeLogistics.get('weight')
                if weight is None  or weight=='':
                    weight = 'None'
                weightUnit = prc_nativeLogistics.get('weightUnit')
                if weightUnit is None  or weightUnit=='':
                    weightUnit = 'None'
                insert_ALIBABA_productItems_sql = "insert into ALI_BABA_productItems(order_id,cargoNumber,description,itemAmount,name,price,productID,productImgUrl,productSnapshotUrl,quantity,refund,skuID,sort,status,subItemID,type,unit,weight,weightUnit)VALUES(" + "'" + order_id + "'," + "'" + str(cargoNumber) + "'," + "'" + str(description) + "'," + "'" + str(itemAmount) + "'," + "'" + str(name) + "'," + "'" + str(price) + "'," + "'" + str(productID) + "'," + "'" + str(productImgUrl) + "'," + "'" + str(productSnapshotUrl) + "'," + "'" + str(quantity) + "'," + "'" + str(refund) + "'," + "'" + str(skuID) + "'," + "'" + str(sort) + "'," + "'" + str(status) + "'," + "'" + str(subItemID) + "'," + "'" + str(type) + "'," + "'" + str(unit) + "'," + "'" + str(weight) + "'," + "'" + str(weightUnit) + "')"
                cursor1.execute(insert_ALIBABA_productItems_sql)
                conn.commit()
                print('ALI_BABA_productItems插入成功')


    # 向交易条款ALIBABA_tradeTerms导入数据


def prc_ALIBABA_tradeTerms():
    for resu in result_list:
        result = resu
        for item in result:
            payStatus = ''
            payTime = ''
            payWay = ''
            phasAmount = ''
            phase = ''
            phaseCondition = ''
            phaseDate = ''
            cardPay = ''
            expressPay=''

            # 取order_id
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))
            prc_tradeTerms1 =item.get('tradeTerms')

            # 由于取出的对象prc_tradeTerms1是个list 所以要转为dict
            if prc_tradeTerms1 != []:
                for prc_tradeTerms_result in prc_tradeTerms1:
                    prc_tradeTerms=prc_tradeTerms_result
                # prc_tradeTerms = eval(str(prc_tradeTerms1).strip('[').rstrip(']'))

                    payStatus = prc_tradeTerms.get('payStatus')
                    if payStatus is None  or payStatus=='':
                        payStatus = 'None'
                    payTime = prc_tradeTerms.get('payTime')
                    if payTime is None  or payTime=='':
                        payTime = 'None'
                    payWay = prc_tradeTerms.get('payWay')
                    if payWay is None  or payWay=='':
                        payWay = 'None'
                    phasAmount = prc_tradeTerms.get('phasAmount')
                    if phasAmount is None  or phasAmount=='':
                        phasAmount = 'None'
                    phase = prc_tradeTerms.get('phase')
                    if phase is None  or phase=='':
                        phase = 'None'
                    phaseCondition = prc_tradeTerms.get('phaseCondition')
                    if phaseCondition is None  or phaseCondition=='':
                        phaseCondition = 'None'
                    phaseDate = prc_tradeTerms.get('phaseDate')
                    if phaseDate is None  or phaseDate=='':
                        phaseDate = 'None'
                    cardPay = prc_tradeTerms.get('cardPay')
                    if cardPay is None   or cardPay=='':
                        cardPay = 'None'
                    expressPay = prc_tradeTerms.get('expressPay')

                    if expressPay is None  or expressPay=='':
                        expressPay = 'None'
                    insert_ALIBABA_tradeTerms_sql="insert into ALI_BABA_tradeTerms(order_id, payStatus, payTime, payWay, phasAmount, phase, phaseCondition, phaseDate,cardPay, expressPay)VALUES(" + "'" + order_id + "', " + "'" + str(payStatus) + "'," + "'" + str(payTime) + "'," + "'" + str(payWay) + "'," + "'" + str(phasAmount) + "'," + "'" + str(phase) + "'," + "'" + str(phaseCondition) + "'," + "'" + str(phaseDate) + "'," + "'" + str(cardPay) + "'," + "'" + str(expressPay) + "')"

                    cursor1.execute(insert_ALIBABA_tradeTerms_sql)
                    conn.commit()
                    print('ALI_BABA_tradeTerms插入成功')

        # conn.commit()

    # 向订单评价信息ALIBABA_orderRateInfo导入数据


def prc_ALIBABA_orderRateInfo():
    for resu in result_list:
        result = resu
        for item in result:
            buyerRateStatus=''
            sellerRateStatus=''
            # 取order_id
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))

            prc_orderRateInfo = item.get('orderRateInfo')
            buyerRateStatus = prc_orderRateInfo.get('buyerRateStatus')

            if buyerRateStatus is None or buyerRateStatus=='':
                buyerRateStatus = 'None'
            # print(cargoNumber)
            sellerRateStatus = prc_orderRateInfo.get('sellerRateStatus')
            # print(prc_orderRateInfo)
            if sellerRateStatus is None  or sellerRateStatus=='':
                sellerRateStatus = 'None'

            insert_ALIBABA_orderRateInfo_sql="insert into ALI_BABA_orderRateInfo(order_id, buyerRateStatus, sellerRateStatus)VALUES(" + "'" + order_id + "', " + "'" + str(buyerRateStatus) + "', " + "'" + str(sellerRateStatus) + "')"
            cursor1.execute(insert_ALIBABA_orderRateInfo_sql)
            conn.commit()
            print('ALI_BABA_orderRateInfo插入成功')


    # 向订单基础信息ALIBABA_baseInfo导入数据


def prc_ALIBABA_baseInfo():
    for resu in result_list:
        result = resu
        for item in result:
            order_id = ''
            businessType = ''
            buyerID = ''
            buyerSubID = ''
            completeTime = ''
            createTime = ''
            currency = ''
            modifyTime = ''
            payTime = ''
            receivingTime = ''
            refund = ''
            remark = ''
            sellerID = ''
            sellerMemo = ''
            sellerSubID = ''
            shippingFee = ''
            status = ''
            totalAmount = ''
            buyerRemarkIcon = ''
            sellerRemarkIcon = ''
            discount = ''
            tradeType = ''
            refundStatus = ''
            refundStatusForAs = ''
            refundPayment = ''
            idOfStr = ''
            alipayTradeId = ''
            buyerLoginId = ''
            sellerLoginId = ''
            buyerUserId = ''
            sellerUserId = ''
            buyerAlipayId = ''
            sellerAlipayId = ''
            confirmedTime = ''
            preOrderId = ''
            refundId = ''
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))
            allDeliveredTime = prc_baseInfo.get('allDeliveredTime')
            if allDeliveredTime is None or allDeliveredTime=='':
                allDeliveredTime = 'None'

            businessType = prc_baseInfo.get('businessType')
            if businessType is None or businessType=='':
                businessType = 'None'

            buyerID = prc_baseInfo.get('buyerID')
            if buyerID is None or buyerID=='':
                buyerID = 'None'

            buyerSubID = prc_baseInfo.get('buyerSubID')
            if buyerSubID is None or buyerSubID=='':
                buyerSubID = 'None'

            completeTime = prc_baseInfo.get('completeTime')
            if completeTime is None or completeTime=='':
                completeTime = 'None'

            createTime = prc_baseInfo.get('createTime')
            if createTime is None or createTime=='':
                createTime = 'None'

            currency = prc_baseInfo.get('currency')
            if currency is None or currency=='':
                currency = 'None'

            modifyTime = prc_baseInfo.get('modifyTime')
            if modifyTime is None or modifyTime=='':
                modifyTime = 'None'

            payTime = prc_baseInfo.get('payTime')
            if payTime is None or payTime=='':
                payTime = 'None'

            receivingTime = prc_baseInfo.get('receivingTime')
            if receivingTime is None or receivingTime=='':
                receivingTime = 'None'

            refund = prc_baseInfo.get('refund')
            if refund is None or refund=='':
                refund = 'None'

            remark = prc_baseInfo.get('remark')
            if remark is None or remark=='':
                remark = 'None'

            sellerID = prc_baseInfo.get('sellerID')
            if sellerID is None or sellerID=='':
                sellerID = 'None'

            sellerMemo = prc_baseInfo.get('sellerMemo')
            if sellerMemo is None or sellerMemo=='':
                sellerMemo = 'None'

            sellerSubID = prc_baseInfo.get('sellerSubID')
            if sellerSubID is None or sellerSubID=='':
                sellerSubID = 'None'

            shippingFee = prc_baseInfo.get('shippingFee')
            if shippingFee is None or shippingFee=='':
                shippingFee = 'None'

            status = prc_baseInfo.get('status')
            if status is None or status=='':
                status = 'None'

            totalAmount = prc_baseInfo.get('totalAmount')
            if totalAmount is None or totalAmount=='':
                totalAmount = 'None'

            buyerRemarkIcon = prc_baseInfo.get('buyerRemarkIcon')
            if buyerRemarkIcon is None or buyerRemarkIcon=='':
                buyerRemarkIcon = 'None'

            sellerRemarkIcon = prc_baseInfo.get('sellerRemarkIcon')
            if sellerRemarkIcon is None or sellerRemarkIcon=='':
                sellerRemarkIcon = 'None'

            discount = prc_baseInfo.get('discount')
            if discount is None or discount=='':
                discount = 'None'

            tradeType = prc_baseInfo.get('tradeType')
            if tradeType is None or tradeType=='':
                tradeType = 'None'

            refundStatus = prc_baseInfo.get('refundStatus')
            if refundStatus is None or refundStatus=='':
                refundStatus = 'None'

            refundStatusForAs = prc_baseInfo.get('refundStatusForAs')
            if refundStatusForAs is None or refundStatusForAs=='':
                refundStatusForAs = 'None'

            refundPayment = prc_baseInfo.get('refundPayment')
            if refundPayment is None or refundPayment=='':
                refundPayment = 'None'

            idOfStr = prc_baseInfo.get('idOfStr')
            if idOfStr is None or idOfStr=='':
                idOfStr = 'None'

            alipayTradeId = prc_baseInfo.get('alipayTradeId')
            if alipayTradeId is None or alipayTradeId=='':
                alipayTradeId = 'None'

            buyerLoginId = prc_baseInfo.get('buyerLoginId')
            if buyerLoginId is None or buyerLoginId=='':
                buyerLoginId = 'None'

            sellerLoginId = prc_baseInfo.get('sellerLoginId')
            if sellerLoginId is None or sellerLoginId=='':
                sellerLoginId = 'None'

            buyerUserId = prc_baseInfo.get('buyerUserId')
            if buyerUserId is None or buyerUserId=='':
                buyerUserId = 'None'

            sellerUserId = prc_baseInfo.get('sellerUserId')
            if sellerUserId is None or sellerUserId=='':
                sellerUserId = 'None'

            buyerAlipayId = prc_baseInfo.get('buyerAlipayId')
            if buyerAlipayId is None or buyerAlipayId=='':
                buyerAlipayId = 'None'

            sellerAlipayId = prc_baseInfo.get('sellerAlipayId')
            if sellerAlipayId is None or sellerAlipayId=='':
                sellerAlipayId = 'None'

            confirmedTime = prc_baseInfo.get('confirmedTime')
            if confirmedTime is None or confirmedTime=='':
                confirmedTime = 'None'

            preOrderId = prc_baseInfo.get('preOrderId')
            if preOrderId is None or preOrderId=='':
                preOrderId = 'None'

            refundId = prc_baseInfo.get('refundId')

            if refundId is None or refundId=='':
                refundId = 'None'
            insert_ALIBABA_baseInfo_sql="insert into ALI_BABA_baseInfo(order_id,businessType,buyerID,buyerSubID,completeTime,createTime,currency, modifyTime, payTime, receivingTime, refund,remark, sellerID, sellerMemo, sellerSubID, shippingFee,status, totalAmount, buyerRemarkIcon, sellerRemarkIcon, discount, tradeType,refundStatus, refundStatusForAs, refundPayment, idOfStr, alipayTradeId,buyerLoginId, sellerLoginId, buyerUserId, sellerUserId, buyerAlipayId,sellerAlipayId, confirmedTime, preOrderId, refundId)VALUES(" + "'" + order_id + "', " + "'" + str(businessType) + "', " + "'" + str(buyerID) + "'," + "'" + str(buyerSubID) + "', " + "'" + str(completeTime) + "', " + "'" + str(createTime) + "', "+ "'" + str(currency) + "'," + "'" + str(modifyTime) + "'," + "'" + str(payTime) + "'," + "'" + str(receivingTime) + "'," + "'" + str(refund) + "',"+ "'" + str(remark) + "'," + "'" + str(sellerID) + "'," + "'" + str(sellerMemo) + "'," + "'" + str(sellerSubID) + "'," + "'" + str(shippingFee) + "',"+ "'" + str(status) + "'," + "'" + str(totalAmount) + "'," + "'" + str(buyerRemarkIcon) + "'," + "'" + str(sellerRemarkIcon) + "'," + "'" + str(discount) + "'," + "'" + str(tradeType) + "',"+ "'" + str(refundStatus) + "'," + "'" + str(refundStatusForAs) + "'," + "'" + str(refundPayment) + "'," + "'" + str(idOfStr) + "'," + "'" + str(alipayTradeId) + "',"+ "'" + str(buyerLoginId) + "'," + "'" + str(sellerLoginId) + "'," + "'" + str(buyerUserId) + "'," + "'" + str(sellerUserId) + "'," + "'" + str(buyerAlipayId) + "',"+ "'" + str(sellerAlipayId) + "'," + "'" + str(confirmedTime) + "'," + "'" + str(preOrderId) + "'," + "'" + str(refundId) + "')"
            cursor1.execute(insert_ALIBABA_baseInfo_sql)
            conn.commit()
            print('ALI_BABA_baseInfo插入成功')


    # 向买家联系人ALIBABA_buyerContact导入数据


def prc_ALIBABA_buyerContact():
    for resu in result_list:
        result = resu
        for item in result:
            buyerContact_phone = ''
            buyerContact_fax = ''
            buyerContact_email = ''
            buyerContact_imInPlatform = ''
            buyerContact_name = ''
            buyerContact_mobile = ''
            buyerContact_companyName = ''
            prc_baseInfo=item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))

            buyerContact=prc_baseInfo.get('buyerContact')
            buyerContact_phone = buyerContact.get('phone')
            if buyerContact_phone =='' or buyerContact_phone is None:
                buyerContact_phone = 'None'

            buyerContact_fax = buyerContact.get('fax')
            if buyerContact_fax is None or buyerContact_fax=='':
                buyerContact_fax = 'None'

            buyerContact_email = buyerContact.get('email')
            if buyerContact_email is None or buyerContact_email=='':
                buyerContact_email = 'None'

            buyerContact_imInPlatform = buyerContact.get('imInPlatform')
            if buyerContact_imInPlatform is None or buyerContact_imInPlatform=='':
                buyerContact_imInPlatform = 'None'

            buyerContact_name = buyerContact.get('name')
            if buyerContact_name is None or buyerContact_name=='':
                buyerContact_name = 'None'

            buyerContact_mobile = buyerContact.get('mobile')
            if buyerContact_mobile is None or buyerContact_mobile=='':
                buyerContact_mobile = 'None'

                buyerContact_companyName = buyerContact.get('companyName')
            if buyerContact_companyName is None or buyerContact_companyName=='':
                buyerContact_companyName = 'None'
            insert_ALIBABA_buyerContact_sql="insert into ALI_BABA_buyerContact(order_id,phone,fax,email,imInPlatform,name,mobile,companyName)VALUES(" + "'" + order_id + "'," + "'" + str(buyerContact_phone) + "'," + "'" + str(buyerContact_fax) + "'," + "'" + str(buyerContact_email) + "'," + "'" + str(buyerContact_imInPlatform) + "'," + "'" + str(buyerContact_name) + "'," + "'" + str(buyerContact_mobile) + "'," + "'" + str(buyerContact_companyName) + "')"
            cursor1.execute(insert_ALIBABA_buyerContact_sql)
            conn.commit()
            print('ALI_BABA_buyerContact插入成功')


    # 向卖家联系人ALIBABA_sellerContact导入数据


def prc_ALIBABA_sellerContact():
    for resu in result_list:
        result = resu
        for item in result:
            sellerContact_phone = ''
            sellerContact_fax = ''
            sellerContact_email = ''
            sellerContact_imInPlatform = ''
            sellerContact_name = ''
            sellerContact_mobile = ''
            sellerContact_companyName = ''
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))
            sellerContact = prc_baseInfo.get('sellerContact')
            sellerContact_phone = sellerContact.get('phone')
            if sellerContact_phone == '' or sellerContact_phone is None:
                sellerContact_phone = 'None'

            sellerContact_fax = sellerContact.get('fax')
            if sellerContact_fax is None or sellerContact_fax=='':
                sellerContact_fax = 'None'

            sellerContact_email = sellerContact.get('mail')
            if sellerContact_email is None or sellerContact_email=='':
                sellerContact_email = 'None'

            sellerContact_imInPlatform = sellerContact.get('imInPlatform')
            if sellerContact_imInPlatform is None or sellerContact_imInPlatform=='':
                sellerContact_imInPlatform = 'None'

            sellerContact_name = sellerContact.get('name')
            if sellerContact_name is None or sellerContact_name=='':
                sellerContact_name = 'None'

            sellerContact_mobile = sellerContact.get('mobile')
            if sellerContact_mobile is None or sellerContact_mobile=='':
                sellerContact_mobile = 'None'

            sellerContact_companyName = sellerContact.get('companyName')
            if sellerContact_companyName is None or sellerContact_companyName=='':
                sellerContact_companyName = 'None'
            insert_ALIBABA_sellerContact_sql = "insert into ALI_BABA_sellerContact(order_id,phone,fax,email,imInPlatform,name,mobile,companyName)VALUES(" + "'" + order_id + "'," + "'" + str(sellerContact_phone) + "'," + "'" + str(sellerContact_fax) + "'," + "'" + str(sellerContact_email) + "'," + "'" + str(sellerContact_imInPlatform) + "'," + "'" + str(sellerContact_name) + "'," + "'" + str(sellerContact_mobile) + "'," + "'" + str(sellerContact_companyName) + "')"
            cursor1.execute(insert_ALIBABA_sellerContact_sql)
            conn.commit()
            print('ALI_BABA_sellerContact插入成功')



    # 向收件人信息ALIBABA_receiverInfo导入数据


def prc_ALIBABA_receiverInfo():
    for resu in result_list:
        result = resu
        for item in result:
            toFullName = ''
            toDivisionCode = ''
            toMobile = ''
            toPhone = ''
            toPost = ''
            toTownCode = ''
            toArea = ''
            prc_baseInfo = item.get('baseInfo')
            order_id = str(prc_baseInfo.get('id'))
            receiverInfo = prc_baseInfo.get('receiverInfo')
            toFullName = receiverInfo.get('toFullName')
            if toFullName is None or toFullName=='':
                toFullName = 'None'

            toDivisionCode = receiverInfo.get('toDivisionCode')
            if toDivisionCode is None or toDivisionCode=='':
                toDivisionCode = 'None'

            toMobile = receiverInfo.get('toMobile')
            if toMobile is None or toMobile=='':
                toMobile = 'None'

            toPhone = receiverInfo.get('toPhone')
            if toPhone is None or toPhone=='':
                toPhone = 'None'

            toPost = receiverInfo.get('toPost')
            if toPost is None or toPost=='' :
                toPost = 'None'

            toTownCode = receiverInfo.get('toTownCode')
            if toTownCode is None or toTownCode=='':
                toTownCode = 'None'

            toArea = receiverInfo.get('toArea')
            if toArea is None or toArea=='':
                toArea = 'None'
            insert_ALIBABA_receiverInfo_sql ="insert into ALI_BABA_receiverInfo(order_id,toFullName,toDivisionCode,toMobile,toPhone,toPost,toTownCode,toArea)VALUES(" + "'" + order_id + "'," + "'" + str(toFullName) + "'," + "'" + str(toDivisionCode) + "'," + "'" + str(toMobile) + "'," + "'" + str(toPhone) + "'," + "'" + str(toPost) + "'," + "'" + str(toTownCode) + "'," + "'" + str(toArea) + "')"
            cursor1.execute(insert_ALIBABA_receiverInfo_sql)
            conn.commit()
            print('ALI_BABA_receiverInfo插入成功')



ALIBABA_nativeLogistics=prc_ALIBABA_nativeLogistics()

ALIBABA_productItems=prc_ALIBABA_productItems()

ALIBABA_tradeTerms=prc_ALIBABA_tradeTerms()

ALIBABA_orderRateInfo=prc_ALIBABA_orderRateInfo()

ALIBABA_baseInfo=prc_ALIBABA_baseInfo()

ALIBABA_buyerContact=prc_ALIBABA_buyerContact()

ALIBABA_sellerContact=prc_ALIBABA_sellerContact()
#
ALIBABA_receiverInfo=prc_ALIBABA_receiverInfo()








