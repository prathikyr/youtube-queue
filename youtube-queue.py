#!/usr/bin/env python

import os
def main():
	command = 'youtube-dl --max-quality FORMAT '
	urlFile = open('urls', 'r')
	for eachLine in urlFile:
		command = command + str(eachLine)
		os.system(command)
	urlFile.close()
	
if __name__=="__main__":
	main()
