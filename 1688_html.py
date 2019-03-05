import os
import random
import time

import mitmproxy as mitmproxy
import requests
from fake_useragent import UserAgent
from lxml import etree
from selenium  import webdriver
import pymysql
import fake_useragent


USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)"
]

chromedriver ="E:\chrome\chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get('https://login.1688.com/member/signin.htm?from=sm&Done=http://detail.1688.com/offer/538352556594.html')

#连接数据库
# connect=pymysql.connect(
#     host="192.168.1.142",
#     db="hui_cong",
#     user="root",
#     passwd="root",
#     charset='utf8',
#     use_unicode=True
# )
# cursor=connect.cursor()

# os.environ["webdriver.chrome.driver"] = chromedriver

# time.sleep(60)
# driver.get("https://login.1688.com/member/signin.htm?spm=a2609.11209760.0.d3.1ce57f9390Oy5O&Done=https%3A%2F%2Fre.1688.com%2F%3Fkeywords%3D1688%25C5%25FA%25B7%25A2%25CD%25F8%25D5%25BE%26cosite%3Dbaidujj%26location%3Dlanding_t4%26trackid%3D885688102460224166558396%26keywordid%3D66792614458%26format%3Dnormal")
# time.sleep(5)
#登陆
# driver.get("https://kuosidz.1688.com/page/offerlist.htm?spm=a2615.7691456.autotrace-paginator.7.27f46aa5CwO3Lh&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=wangpu_score&pageNum=99#search-bar")
# time.sleep(10)
# js="var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# response=driver.page_source
# print(response)


# 已经爬去过的和正在爬取的店铺url
# https://kuosidz.1688.com/?spm=b26110380.2178313.result.1.6c604bb70pgmtG
# https://apuresh.1688.com/?spm=a2615.7691456.autotrace-topNav.1.38266ff9f9OKMD
# https://shop93551je3259a7.1688.com/?spm=b26110380.2178313.result.23.6c604bb70pgmtG
# https://kuosidianzi.1688.com/?spm=b26110380.2178313.result.41.10b44bb7VZUvju
for i in range(99,110):
    time.sleep(20)
    url='https://apuresh.1688.com/page/offerlist.htm?spm=a2615.7691456.autotrace-paginator.3.21a46ff9GPSzsZ&showType=windows&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=timedown&pageNum='+str(i)+'#search-bar'
    # url='https://apuresh.1688.com/page/offerlist.htm?spm=a2615.7691456.autotrace-paginator.6.55696ff90iXLH3&showType=windows&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=timedown&pageNum=1'+str(i)+'#search-bar'

    driver.get(url)
    time.sleep(5)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    response = driver.page_source
    res=etree.HTML(response)
    url_list = res.xpath(".//div[@class='image']/a/@href")
    print(len(url_list))

    for url in url_list:
        driver.get(url)
        time.sleep(10)
        js = "var q=document.documentElement.scrollTop=500000"
        driver.execute_script(js)
        time.sleep(10)

        res1=driver.page_source
        res2=etree.HTML(res1)
        goods_names=res2.xpath(".//h1[@class='d-title']/text()")
        print(goods_names)
        goods_name=str(goods_names[0]).replace('/','_').replace('\\','_').replace('"','').replace('\t','').replace('?','')
        # path=os.getcwd()
        # print(path)
        img_href = res2.xpath('.//div[@class="desc-lazyload-container"]/p/img/@src')
        print(img_href)
        path1='F:\\html\\'+goods_name+'_'+str(i)+'.html'
        print(path1)
        print(img_href)

        with open(path1,'a+',encoding='utf-8') as f:
            f.write(url+'\\n')
            f.write(res1)

