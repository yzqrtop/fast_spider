# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 14:56
# @Author  : yzqrtop
# @FileName: load_json.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_44077556?type=blog
import json


def load_json(path,mode="r+",encode="utf-8"):
    if path=="":
        return {}

    with open(path,mode=mode,encoding=encode)as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    load_json("../config/example_config.json")
