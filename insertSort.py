#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: insert_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
import randata
'''
被注释掉的部分是c语言数组普通的插入方式
未被注释的部分则是使用python列表的插入和删除特性改善的
'''
def insertSort(arr):
	print(arr)
	for i in range(1,len(arr)):
		j=i
		print(arr[i])
		while j>0 and arr[j-1]>arr[i]:
			j-=1
		print(j)
		arr.insert(j,arr[i])
		arr.pop(i+1)
		
		print(arr)
		
	print(arr)