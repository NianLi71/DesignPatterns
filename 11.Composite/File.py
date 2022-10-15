from Entry import Entry

class File(Entry):
	def __init__(self, name, size):
		self.name = name
		self.size = size

	def getName(self):
		return self.name

	def getSize(self):
		return self.size

	# def add(self, entry):
	# 	print("File can not include other entry!")

	def printList(self, prefix=""):
		print(prefix + '/'+str(self))

if __name__ == '__main__':
	f = File('a.txt', 1000)
	# f.add(File('b.txt', 10))
	f.printList()