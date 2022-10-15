from abc import ABC, abstractmethod

class AbstractDisplay(ABC):

	def __init__(self, n):
		self.n = n

	@abstractmethod
	def open(self):
		pass

	@abstractmethod
	def print(self):
		pass

	@abstractmethod
	def close(self):
		pass

	def display(self):
		self.open()	
		for i in range(self.n):
			self.print()
		self.close()

# if __name__ == '__main__':
# 	a = AbstractDisplay()