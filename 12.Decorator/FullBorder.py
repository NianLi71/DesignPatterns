from Border import Border

class FullBorder(Border):
	def __init__(self, display):
		super().__init__(display)

	def getColums(self):
		return 2 + self.display.getColums()

	def getRows(self):
		return 2 + self.display.getRows()

	def getRowText(self, row):
		if row == 0:
			return '+' + '-'*self.display.getColums() + '+'
		elif row == self.display.getRows() + 1:
			return '+' + '-'*self.display.getColums() + '+'
		else:
			return '|' + self.display.getRowText(row - 1) + '|'

if __name__ == '__main__':
	from StringDisplay import StringDisplay
	fb = FullBorder(StringDisplay('good morning'))
	fb.show()