from Border import Border


class SideBorder(Border):
	def __init__(self, display, c):
		super().__init__(display)
		self.bc = c

	def getColums(self):
		return 2 + self.display.getColums()

	def getRows(self):
		return self.display.getRows()

	def getRowText(self, row):
		return self.bc + self.display.getRowText(row) + self.bc


if __name__ == '__main__':
	from StringDisplay import StringDisplay
	sb = SideBorder(StringDisplay('hello QQ, GG'), '#')
	ss = SideBorder(sb, '*')
	sb.show()
	ss.show()