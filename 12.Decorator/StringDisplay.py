from Display import Display

class StringDisplay(Display):
	def __init__(self, s):
		self.str = s

	def getColums(self):
		return len(self.str)

	def getRows(self):
		return 1

	def getRowText(self, row):
		if row == 0:
			return self.str
		else:
			return None

if __name__ == '__main__':
	s = StringDisplay('hello')
	s.show()