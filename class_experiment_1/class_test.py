#!/usr/bin/env python

class MyClass:
	
	mName = "abc"
	def __init__(self, name):
		self.mName = name
	
	def changeInstName(self, name):
		mName = name
		print "In changeInstName, mName: "+mName+" self.mName: "+self.mName
	
	def printMyName(self):
		print "MyClass, name is "+self.mName 
		

if __name__ == '__main__':
	print "In Main"
	m = MyClass("Mayur")
	m.printMyName()
	m.changeInstName("stuv")
	
	print ("Print 1 {}".format(m.__class__.mName))
	print ("Print 2 {}".format(m.mName))
	
	n = MyClass("One") 
	print "Print 1 {}".format(n.__class__.mName)
	print "Print 2  {}".format(n.mName)
