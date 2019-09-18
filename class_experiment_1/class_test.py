#!/usr/bin/env python

class MyClass:
	
	mName = ""
	def __init__(self, name):
		self.mName = name;
	
	def printMyName(self):
		print "MyClass, name is "+self.mName
		

if __name__ == '__main__':
	print "In Main"
	m = MyClass("Mayur")
	m.printMyName()
