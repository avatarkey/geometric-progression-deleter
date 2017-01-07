#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time


dirpath = os.path.dirname(os.path.realpath(__file__))
files = []
del_files = []


#We scan the directory with file deleter.py
for roots, dirs, files in os.walk(dirpath):
	for name in files:
		files.append(name)

#We populate list "files" and sort it by the time modified
files = sorted(files, key=lambda x: time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(os.stat(x).st_mtime)))
files.reverse()


#We create a list of geometrical progression according to the number of files in the folder
geom_prog=[1]
li=1
while li<len(files):
	li *= 2
	if li < len(files):
		geom_prog.append(li)


#We populate a list of files to be deleted. 
#We leave only files which are numbered 1,2,4,8,16 etc and the last file in the folder
count = 0
for file in files:
	count += 1
	if count != 1 and count != len(files) and str(file) != str(sys.argv[0]):
		if count not in geom_prog:
			del_files.append(file)
		else:
			pass
print '=========================='
print 'The following files will be deleted:'
for x in del_files:
	print str(x)
print '=========================='
try:
	input("Press Enter to delete them, or Ctrl+C to cancel")
except SyntaxError:
	pass


#We delete these files by pushing Enter
for x in del_files:
	try:
		os.remove(x)
	except OSError:
		print "Some files were not deleted"

print 'The files have been successfully deleted' 
