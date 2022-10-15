from abc import ABC, abstractmethod

class Factory(ABC):
	def create(self, owner):
		p = self.createProduct(owner)
		self.registerProduct(p)
		return p

	@abstractmethod
	def createProduct(self, owner):
		pass

	@abstractmethod
	def registerProduct(self, product):
		pass