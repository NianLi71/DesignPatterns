from BigString import BigString
from BigCharFactory import *

def main():
	bs = BigString('123-456')
	bs.ppt()
	print(bigcharfactory.getItemNum())

	b = BigString('999988')
	b.ppt()
	print(bigcharfactory.getItemNum())

	b1 = BigString('77889911223')
	b1.ppt()
	print(bigcharfactory.getItemNum())

	# will get an error
	# bcf = BigCharFactory()

if __name__ == '__main__':
	main()