# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 16:24
# @Author  : yzqrtop
# @FileName: collection_model.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_44077556?type=blog
import os
import time

import numpy as np
import pandas as pd

from config.config import ROOT_PATH, OUTPUT_PATH
from tool.load_json_service import load_json
from tool.spider_service import SPIDER_MASTER

class SPIDER_CONFIT_MODEL():

    arg=None

    def __init__(self,arg=""):
        self.arg = load_json(arg)
        self.sm = SPIDER_MASTER()
        self.process()

    def __del__(self):
        self.clear()

    def process(self):
        self.sm.set_url(self.arg["url"])
        self.sm.read_web_value()

        if "table" in self.arg.keys():
            columns = self.sm.xpath_deconstruction(self.arg["table"]["head_xpath"])
            data = self.sm.xpath_deconstruction(self.arg["table"]["body_xpath"])
            self.output_list_to_csv(data,columns,OUTPUT_PATH+"/"+f"{str(time.time())}.csv")

        print(f"------------anaysis finsh， please into {OUTPUT_PATH} to find the data---------------------")


    def output_list_to_csv(self,data,columns:list,output_path:str="result.csv"):
        def is_nested_array(obj):
            if isinstance(obj,list):
                for item in obj:
                    if is_nested_array(item):
                        return True
                return True
            else:
                return False

        assert is_nested_array(columns) == True
        assert is_nested_array(data) == True
        assert type(output_path) == str

        df_2d= pd.DataFrame(np.array(data),columns=columns[0])
        df_2d.to_csv(output_path)

    def clear(self):
        self.sm.clear()


if __name__ == '__main__':
    scm = SPIDER_CONFIT_MODEL("")
    scm.process()