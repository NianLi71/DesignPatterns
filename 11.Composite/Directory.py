from Entry import Entry
from File import File

class Directory(Entry):
	def __init__(self, name):
		self.name = name
		self.dir = []

	def getName(self):
		return self.name

	def add(self, entry):
		self.dir.append(entry)

	def getSize(self):
		size = 0
		for d in self.dir:
			size += d.getSize()
		return size

	def printList(self, prefix=''):
		print(prefix + '/'+str(self))
		curPrefix = prefix + '/' +self.name   # don't forget the passed in prefix
		for d in self.dir:
			d.printList(curPrefix)	

if __name__ == '__main__':
	d = Directory('bin')
	d.add(Directory('lib'))
	d.add(File('test.py', 105))
	d.printList()