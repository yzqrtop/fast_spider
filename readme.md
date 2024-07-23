# 快速爬虫工具
> 仅通过设置config.json,快速爬取数据

# config.json介绍
```bash
{
  "url": "https://ying-zhang.github.io/misc/2022-ccf-list/", # 浏览器位置
  "table": { # 表格数据获取
    "head_xpath": "/html/body/article/table[3]/thead/tr", # 表头获取 
    "body_xpath": "/html/body/article/table[3]/tbody/tr", # 表内容获取
    "is_all_data": "yes", # 是否获取全部，默认全部
    "select_area": [ # 选择表格数据的范围，默认全部
      1,
      -1
    ]
  }
}
```

# 环境设置
```bash
pip install requests numpy pandas
```

# 运行
```bash
python main.py --config_set_path ./config/example_config.json
```