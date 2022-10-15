from Border import Border


class UpDownBorder(Border):
	def __init__(self, display, c):
		super().__init__(display)
		self.bc = c

	def getColums(self):
		return self.display.getColums()

	def getRows(self):
		return 2 + self.display.getRows()

	def getRowText(self, row):
		if row == 0:
			return self.bc*self.display.getColums()
		elif row == 1 + self.display.getRows():
			return self.bc*self.display.getColums()
		else:
			return self.display.getRowText(row - 1)


if __name__ == '__main__':
	from StringDisplay import StringDisplay
	ud = UpDownBorder(StringDisplay('hello QQ, GG'), '-')
	ud.show()