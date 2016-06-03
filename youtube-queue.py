#!/usr/bin/env python

import os
def main():
	url='youtube-dl --max-quality FORMAT '
	f=open('urls', 'r')
	for line in f:
		url=url+str(line)
		os.system(url)
	f.close()
if __name__=="__main__":
	main()
