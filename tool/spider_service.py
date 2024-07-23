# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 14:47
# @Author  : yzqrtop
# @FileName: spider_service.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_44077556?type=blog
import os.path

import requests
from lxml import etree

from config.config import ROOT_PATH


class SPIDER_MASTER():
    url = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'content-type': "multipart/form-data; boundary=---011000010111000001101001"
    }

    def __init__(self, url="", username="user", password="123", appid="123", appkey="fds"):
        self.url = url
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self):
        page_text = ""
        try:
            page_text = requests.get(url=self.url, headers=self.headers).text
        except Exception as e:
            raise Exception(f"please check your network, make sure you can link the {self.url}")

        self.web_text = page_text
        self.web_tree = etree.HTML(page_text)
        self.save_web_value()

    def set_url(self,url):
        self.url = url

    def save_web_value(self):
        with open(f"{ROOT_PATH}/tool/temp_web_text.txt","w+",encoding="utf-8") as f:
            f.write(self.web_text)
        f.close()

    def read_web_value(self):
        if not os.path.exists(f"{ROOT_PATH}/tool/temp_web_text.txt"):
            self.request()

        with open(f"{ROOT_PATH}/tool/temp_web_text.txt","r+",encoding="utf-8") as f:
            self.web_text = f.read()

        f.close()
        self.web_tree = etree.HTML(self.web_text)

    def clear(self):
        if os.path.exists(f"{ROOT_PATH}/tool/temp_web_text.txt"):
            os.remove(f"{ROOT_PATH}/tool/temp_web_text.txt")

    def default_deep_path_data_return(self,elements):
        if type(elements) == etree._Element:
            if elements.text == None:
                return [i.text if i.text else "" for i in elements]
            return elements.text
        else:
            return_result = []
            for i in elements:
                return_result.append(self.default_deep_path_data_return(i))
            return return_result

    # 重要：解析获得单多级结构数据
    def xpath_deconstruction(self,xpath_val):
        result = self.web_tree.xpath(xpath_val)
        assert type(result) == list
        return self.default_deep_path_data_return(result)


