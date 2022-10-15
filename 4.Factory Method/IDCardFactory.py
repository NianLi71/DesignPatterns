from Factory import Factory
from IDCard import IDCard
from collections import defaultdict

class IDCardFactory(Factory):
	def __init__(self):
		self.owners = defaultdict(int)

	def createProduct(self, owner):
		return IDCard(owner)

	def registerProduct(self, product):
		self.owners[product.getOwner()] += 1

	def getOwners(self):
		return self.owners