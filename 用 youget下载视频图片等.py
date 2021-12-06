import sys
from you_get import common

url = input("请输入视频地址：")
DIR = input("请输入视频保存地址：")

sys.argv = ['you-get', '-o', DIR, url]
common.main()