from BigChar import BigChar

class BigCharFactory():
	def __init__(self):
		self.pool = {}

	def getBigChar(self, charname):
		if charname not in self.pool:
			self.pool[charname] = BigChar(charname)

		return self.pool[charname]

	def getItemNum(self):
		return len(self.pool)

# singleton
bigcharfactory = BigCharFactory()

__all__ = ['bigcharfactory']