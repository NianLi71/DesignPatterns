from abc import ABC, abstractclassmethod

class NumberGenerator(ABC):
	def __init__(self):
		self.observers = []

	def addObserver(self, observer):
		self.observers.append(observer)

	def deleteObserver(self, observer):
		self.observers.remove(observer)

	def notifyObservers(self):
		for observer in self.observers:
			observer.update(self)


	@abstractclassmethod
	def getNumber(self):
		pass

	@abstractclassmethod
	def excute(self):
		pass

