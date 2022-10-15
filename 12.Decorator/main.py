from StringDisplay import *
from SideBorder import *
from FullBorder import *
from UpDownBorder import *
from MultiStringDisplay import *

def test_updown():
	b1 = StringDisplay('Hello, world.')
	b2 = UpDownBorder(b1, '-')
	b3 = SideBorder(b2, '*')

	b1.show()
	b2.show()
	b3.show()

	b4 = FullBorder(
			UpDownBorder(
				SideBorder(
					UpDownBorder(
						SideBorder(
							StringDisplay('hello China'), 
							'*'), 
						'='), 
					'|'), 
				'/')
		)
	b4.show()

def test_multiString():
	md = MultiStringDisplay()
	md.add('good morning')
	md.add('good afternoon')
	md.add('good night, see you tomorrow')
	md.show()

	d1 = SideBorder(md, '#')
	d1.show()

	d2 =FullBorder(md)
	d2.show()

def main():
	b1 = StringDisplay('Hello, world.')
	b2 = SideBorder(b1, '#')
	b3 = FullBorder(b2)

	b1.show()
	b2.show()
	b3.show()

	b4 = SideBorder(
			FullBorder(
				FullBorder(
					SideBorder(
							FullBorder( 
									StringDisplay("hello world!")
								), 
						'*')
					)
				), 
			'/')
	b4.show()

	test_updown()

	test_multiString()
	
if __name__ == '__main__':
	main()