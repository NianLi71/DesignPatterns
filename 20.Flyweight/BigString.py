from BigCharFactory import bigcharfactory

class BigString():
	def __init__(self, str):
		self.bcstr = []
		# self.bcfactory = BigCharFactory()	####BigCharFactory 需要用单例模式实现
		for c in str:
			self.bcstr.append(bigcharfactory.getBigChar(c))

	def ppt(self):
		for bc in self.bcstr:
			bc.BCprint()
