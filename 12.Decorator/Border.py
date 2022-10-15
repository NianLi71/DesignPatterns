from Display import Display

class Border(Display):
	def __init__(self, display):
		self.display = display

# if __name__ == '__main__':
# 	b = Border(None)	# error, Border is still a Abstract class