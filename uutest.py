#coding:utf-8

#python 2.7

#Author bocy
#time 2016-7-22 15:02:31

from requests import get
import re

def get_str_count(url,strs):
	'''
	查找指定url中包含字符串str的次数
	'''
	res = get(url,timeout=5)
	if res.status_code is 200:
		content = res.text
		count = len(re.findall(strs,content))
		print url +"页面包含" + str(count)+ "个" + strs
	else:
		res.raise_for_status()

if __name__ == '__main__':
	url = "http://106.75.28.160/UCloud.txt"
	strs = "UCanUup"
	get_str_count(url,strs)
