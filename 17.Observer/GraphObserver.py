from Observer import Observer
import time

class GraphObserver(Observer):
	def update(self, generator):
		time.sleep(0.5)
		print('*'*generator.getNumber())