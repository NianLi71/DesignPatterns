
class Singleton():
	def __init__(self):
		print('Singleton create a singleton.')
		pass

	def getInstance(self):
		return self

	def sayHi(self):
		print("Hi, I'm a singleton")

singleton = Singleton()

__all__ = ['singleton']

