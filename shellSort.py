#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: shell_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
import randata
def shellSort(arr):
	print(arr)
	dist=int(len(arr)/2)
	while dist>0:
		print(dist)
		for i in range(dist,len(arr)):
			tmp=arr[i]
			j=i
			while j>=dist and tmp<arr[j-dist]:
				print(j,j-dist)
				arr[j]=arr[j-dist]
				j-=dist
			arr[j]=tmp
			print(arr)
		dist=int(dist/2)
	print(arr)