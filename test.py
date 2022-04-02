#to będzie plik na krórym będziemy pracowali z repo
def hello(name):
	return "Hello" + str(name)

def odejmij(a,b):
	return a-b

def pomnoz(a,b):
	return a*b

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

def podziel(a,b):
	wynik = float(a) / float(b)
	return wynik

pierwsza = input()
druga = input()

print (dodaj(pierwsza, druga))
