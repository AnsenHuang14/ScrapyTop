# -*- coding: utf-8 -*-. 
import sys
import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
def gen(*args):
	Categorylist = pd.read_csv('Category.txt',header=None).tolist()
	url_list = list()
	for cate in Categorylist:
		print 'https://play.google.com'+cate
def GetTopCategory():
	res=requests.get('https://play.google.com/store/apps')
	soup = BeautifulSoup(res.text.encode("utf-8"), "html.parser")
	total= soup.findAll('a',class_='child-submenu-link')
	url_list = list()
	cate_list = list()
	for url in total:
		cate = url['href'].split('/')
		cate = cate[len(cate)-1]
		cate_list.append(cate)
		url_list.append('https://play.google.com'+url['href'])
	return url_list,cate_list

def GetPkgurlList(url,number_of_app = 1000,num=120):
	urllist = list()
	i=1
	last_end_pkg_name =''
	for index in xrange(0,number_of_app,num):
		print i 
		form_data = {'start':str(index),'num':str(num)}
		res=requests.post(url+'/collection/topselling_free',form_data)
		soup = BeautifulSoup(res.text.encode("utf-8"), "html.parser")
		total= soup.find('div',class_='id-card-list card-list two-cards')
		if total != None:
			hrefs=total.find_all('div',class_='card no-rationale square-cover apps small')
			last_end_pkg_name = hrefs[len(hrefs)-1]['data-docid']
			if last_end_pkg_name in urllist:
				return list(set(urllist))
			for href in hrefs:
				urllist.append(href['data-docid'])
				# print i,href['data-docid']
				i+=1
		else :
			return list(set(urllist))

	return list(set(urllist))

def CrawlPackageByTopList():
	url_list,cate_list = GetTopCategory()
	pkg_list = list()
	lang = 'en'
	with open('./URL/top.txt', 'wb') as f:
		for i in xrange(len(url_list)):
			print i,'/',len(url_list)
			for pkg in GetPkgurlList(url_list[i]):
				content = 'https://play.google.com/store/apps/details?id='+pkg+'&hl='+lang
				f.write(content)
				f.write('\n')

if __name__ == '__main__':
	CrawlPackageByTopList()