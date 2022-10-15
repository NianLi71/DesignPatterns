from StringDisplay import StringDisplay
from CharDisplay import CharDisplay

if __name__ == '__main__':
	c = CharDisplay('a')	#默认打印5次
	s = StringDisplay('Hello World.', 3)	# 打印3次

	c.display()
	s.display()