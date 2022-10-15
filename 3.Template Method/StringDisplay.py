from AbstractDisplay import AbstractDisplay

class StringDisplay(AbstractDisplay):
	def __init__(self, s, n=5):
		super().__init__(n)
		self.str = s
		self.len = len(s)

	def open(self):
		self.printLine()

	def close(self):
		self.printLine()

	def print(self):
		print("|{}|".format(self.str))

	def printLine(self):
		print('+' + '-'*self.len + '+')

