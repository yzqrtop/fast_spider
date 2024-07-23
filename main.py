# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 16:21
# @Author  : yzqrtop
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_44077556?type=blog
import argparse

from models.collection_model import SPIDER_CONFIT_MODEL

if __name__ == '__main__':

    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='这是一个示例脚本。')
    # 添加参数
    parser.add_argument('--config_set_path', default="")
    # 解析参数
    args = parser.parse_args()
    SPIDER_CONFIT_MODEL(args.config_set_path)