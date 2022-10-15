# -*- coding: UTF-8 -*-

from IDCardFactory import IDCardFactory
from IDCard import IDCard



def main():
	factory = IDCardFactory()
	card1 = factory.create('QiuQiu')
	card2 = factory.create('GuoGuo')

	card1.use()
	card2.use()

	card3 = factory.create('QiuQiu')
	for owner, n in factory.getOwners().items():
		print("{} has {} ID card(s).".format(owner, n))

if __name__ == '__main__':
	main()