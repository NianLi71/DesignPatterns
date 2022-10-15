from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):
	def __init__(self, c, n=5):
		super().__init__(n)
		self.c = c

	def open(self):
		print("<<", end='')

	def close(self):
		print(">>")

	def print(self):
		print(self.c, end='')

if __name__ == '__main__':
	c = CharDisplay('a')
	c.display()