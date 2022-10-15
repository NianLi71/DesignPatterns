

# f = open('./bigchar/big2.txt')
# for line in f:
# 	print(line)

class BigChar():
	def __init__(self, charname):
		self.charname = charname
		self.str = ''
		f = open('./bigchar/big' + str(self.charname) + '.txt')
		for line in f:
			self.str += line
		f.close()

	def BCprint(self):
		print(self.str)

if __name__ == '__main__':
	bc = BigChar(8)
	bc.BCprint()
	c = BigChar('-')
	c.BCprint()