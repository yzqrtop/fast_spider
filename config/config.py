# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 17:56
# @Author  : yzqrtop
# @FileName: config.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_44077556?type=blog
import inspect
import os

path = inspect.getfile(inspect.currentframe())
ROOT_PATH = os.path.abspath(path)
ROOT_PATH = "\\".join(ROOT_PATH.split("\\")[:-2])
OUTPUT_PATH = ROOT_PATH+"/output"
