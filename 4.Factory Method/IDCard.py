#-*- coding:utf-8 –*-

from Product import Product

class IDCard(Product):
	def __init__(self, owner):
		self.owner = owner
		print("Making {}'s ID card".format(owner))

	def use(self):
		print("Using {}'s ID card".format(self.owner))

	def getOwner(self):
		return self.owner