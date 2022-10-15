from RandomNumberGenerator import RandomNumberGenerator
from DigitObserver import DigitObserver
from GraphObserver import GraphObserver

def main():
	rng = RandomNumberGenerator()

	digitObsv = DigitObserver()
	graphObsv = GraphObserver()

	rng.addObserver(digitObsv)
	rng.addObserver(graphObsv)

	rng.excute()

if __name__ == '__main__':
	main()