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
            if self.is_collaborate_table(data=data,columns=columns):
                self.output_list_to_csv(data,columns)
            else:
                self.output_data_to_csv(data,OUTPUT_PATH+"/"+f"{str(time.time())}_table_body.csv")
                self.output_data_to_csv(columns,OUTPUT_PATH+"/"+f"{str(time.time())}_table_head.csv")


        print(f"------------anaysis finsh， please into {OUTPUT_PATH} to find the data---------------------")
    def find_root_len(self,data,root_i):
        if isinstance(data,list):
            return self.find_root_len(data[0],len(data))
        else:
            return root_i

    # 查看表头及表格内容是否列相同
    def is_collaborate_table(self,data,columns):
        data_i = self.find_root_len(data,len(data))
        columns_i = self.find_root_len(columns,len(columns))
        if data_i==columns_i:
            return True
        else:
            return False

    def output_list_to_csv(self,data,column,output_path:str="result.csv"):
        df_2d = pd.DataFrame(np.array(data),columns=column[0])
        df_2d.to_csv(output_path)

    def output_data_to_csv(self,data,output_path:str="result.csv"):
        def format_data(data):
            if isinstance(data,list):
                result = []
                for item in data:
                    if isinstance(item,list):
                        result.append(["<+>".join(item)])
                    else:
                        result.append([item])
                return result

            else:
                return [data]

        df_2d = pd.DataFrame(np.array(format_data(data)))
        df_2d.to_csv(output_path)
    def clear(self):
        self.sm.clear()


if __name__ == '__main__':
    scm = SPIDER_CONFIT_MODEL("")
    scm.process()