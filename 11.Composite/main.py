from Directory import Directory
from File import File

def main():

	print('Making root entries...')
	rootdir = Directory('root')
	bindir = Directory('bin')
	tmpdir = Directory('tmp')
	usrdir = Directory('usr')

	rootdir.add(bindir)
	rootdir.add(tmpdir)
	rootdir.add(usrdir)

	bindir.add(File('vi', 10000))
	bindir.add(File('latex', 20000))

	rootdir.printList()

	print("")
	print('Making user entries')
	yuki = Directory('yuki')
	hanako = Directory('hanako')
	tomura = Directory('tomura')
	usrdir.add(yuki)
	usrdir.add(hanako)
	usrdir.add(tomura)

	yuki.add(File("diary.html", 100))
	yuki.add(File('Composite.py',200))
	hanako.add(File('memo.tex',300))
	tomura.add(File('game.doc',400))
	tomura.add(File('junk.mail', 500))
	rootdir.printList()

if __name__ == '__main__':
	main()