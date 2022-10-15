from Observer import Observer

class DigitObserver(Observer):
	def update(self, generator):
		print('DigitObserver: {}'.format(generator.getNumber()))