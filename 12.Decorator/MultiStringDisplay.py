from Display import Display

class MultiStringDisplay(Display):
	def __init__(self):
		self.str = []

	def add(self, s):
		self.str.append(s)

	def getColums(self):
		return len( max(self.str, key=lambda x: len(x)) )

	def getRows(self):
		return len(self.str)

	def getRowText(self, row):
		col = self.getColums()
		return self.str[row] + ' '*(col - len(self.str[row]))

if __name__ == '__main__':
	ms = MultiStringDisplay()
	ms.add('hi')
	ms.add('QiuQiu and GuoGuo')
	ms.add('how are you')
	ms.show()

	from FullBorder import FullBorder
	fb = FullBorder(ms)
	fb.show()

	from SideBorder import SideBorder
	sb = SideBorder(ms, '$')
	sb.show()



