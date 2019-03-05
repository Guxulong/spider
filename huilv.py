# -*- coding: utf-8 -*
from flask import Flask, request

import requests
import  re
#!/usr/bin/python
#coding:utf-8


app=Flask(__name__)

@app.route('/api',methods=['GET'])
def hui_lv():
    country=request.args.get('country')
    print(country)
    if country=='usd' or country=='USD':
        url = 'http://hl.anseo.cn/cal_USD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h='0'+'\n'+huilv
        print(h)
        return h
    #欧元
    elif country == 'EUR' or country == 'eur':
        url = 'http://hl.anseo.cn/cal_EUR_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h
    #港币
    elif country == 'HKD' or country == 'hkd':
        url = 'http://hl.anseo.cn/cal_HKD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    # 英镑
    elif country == 'GBP' or country == 'gbp':
        url = 'http://hl.anseo.cn/cal_GBP_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h


    #日元
    elif country == 'JPY' or country == 'jpy':
        url = 'http://hl.anseo.cn/cal_JPY_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h
    #加元
    elif country == 'CAD' or country == 'cad':
        url = 'http://hl.anseo.cn/cal_CAD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h
    #韩元
    elif country == 'KRW' or country == 'krw':
        url = 'http://hl.anseo.cn/cal_KRW_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #澳元
    elif country == 'AUD' or country == 'aud':
        url = 'http://hl.anseo.cn/cal_AUD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #瑞郎
    elif country == 'chf' or country == 'CHF':
        url = 'http://hl.anseo.cn/cal_CHF_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #新加坡元
    elif country == 'sgd' or country == 'SGD':
        url = 'http://hl.anseo.cn/cal_SGD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #马来西亚币
    elif country == 'myr' or country == 'MYR':
        url = 'http://hl.anseo.cn/cal_MYR_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h
    #印尼
    elif country == 'idr' or country == 'IDR':
        url = 'http://hl.anseo.cn/cal_IDR_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #新西兰
    elif country == 'nzd' or country == 'NZD':
        url = 'http://hl.anseo.cn/cal_NZD_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #越南
    elif country == 'VND' or country == 'vnd':
        url = 'http://hl.anseo.cn/cal_VND_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #泰铢
    elif country == 'THB' or country == 'thb':
        url = 'http://hl.anseo.cn/cal_THB_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #菲律宾
    elif country == 'PHP' or country == 'php':
        url = 'http://hl.anseo.cn/cal_PHP_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h

    #人民币
    elif country == 'CNY' or country == 'cny':
        url = 'http://hl.anseo.cn/cal_CNY_To_CNY.aspx'
        res = requests.get(url)
        res1 = res.content.decode()
        # res2=re.search('<div id="result">',res1)
        res3 = re.findall(r'<div id="result">(.+?)人民币</p></div>', res1)[0]
        huilv = res3.split('</strong>')[1].split('</p>')[0]
        h = '0' + '\n' + huilv
        print(h)
        return h
    else:
        return '-1'+'</br>'+('输入的币种码不对')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8002)