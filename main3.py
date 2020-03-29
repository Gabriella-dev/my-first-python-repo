# https://ocw.cs.pub.ro/courses/ii/lab/laborator1 - interesan
# https://www.w3schools.com/python/python_datatypes.asp - la fel de interesant

# my_string . foloseste ghilimele sau apostrof 
#       my_string = "Don't worry about aphostrophs"
print("Don't worry about apostrophes!")
#       my_string = 'Don\'t worry about apostrophes!'
print('Don\'t worry about apostrophes!')

a = 'hello,'
b = 'world!'
def myString(a, b):
    return a+" "+b
print(myString(a, b))
# sau/ or
print(a+" "+b)

#combinatia de numere cu cifre (str - in fata fiecarei variabile)
c = 10
def combinatie (a, b, c):
    return(str(a)+str(" ")+str(b)+str(c))
print(combinatie(a, b, c))

#wooowww
x = 5
x += 3
print(x)
# % Modulus - restul împărțirii operandului stâng la dreapta x % y (restul de x / y)
y = 15
y%=4
print(y)
# nu inteleg operatia pe care o efectueaza
# gata. inseamna 15 : 4 = cat e restul sau8 da-mi restul la aceasta impartire

x = 35e3
print(float(x))
# e este puterea 10 iar numarul de dupa e de cate ori la puterea 10 adica cati de zero dupa inclusiv la numerele cratiponale cmuta singur virgula 

# random - genereaza un numar aleatoriu in intervalul dat 
# randrange (start, stop, step) nu ia în considerare ultimul articol, 
# adică este exclusiv. De exemplu, randrange (10,20,1) 
# va returna orice număr aleatoriu de la 10 la 19 (exclusiv). 
# nu va selecta niciodată 20
# start = nr pornire
# stop = nr final
# step = step este o diferență între fiecare număr din secvență. 
# Etapa este parametrii opționali. 
# Valoarea implicită a pasului este 1 dacă nu este specificată.
#        - un argument nr generat intre 0 si 100
#        - doua argumente
#        - trei argumente
import random
print(random.randrange(100))
print(random.randrange(30, 70))
print(random.randrange(30, 70 ,3))
#Pentru a genera un număr float aleator, 
# utilizați funcția random.uniform () .
print(random.uniform(-1, 0))


# string
d = """Rana mea de Maramures, rana mea de alta tara
Cum ma lasi de unul singur, cum ma uiti, cum te-oi uita
Intr-un fotograf la Roma, moartea s-a retras sa moara
s-au smintit de tot poetii, eu nu vad faptura ta."""
print(d)

# String and Arrays
# - da-mi przitia literei 1 incepe numaratoarea de la0 si zero e pozitie
print(d[1])
# da-mi pozitiile literelor de la 10 la 15
print(d[10:15])
# pe negative index va incepe numaratoarea de la coada la cap si incepe de lanr mai mare la mai mic adica invers
print(d[-15:-10])

# String Length = lungimea sirurilor numara tot si pauze si tot
print(len(d))

# String Methods
# strip() muta spatiile albe de la inceput si sfarsit
print(d.strip())
# lower() - scrie cu  litere mici tot
print(d.lower())
# upper() - scrie tot cu litere mari
print(d.upper())
# replace() inlocuieste un sir cu altul, o litera cu alta
print(d.replace("m", "d"))
# split() - imparte sirul in subsiruri la separatorul pe care i-l dai de exemplu virgula
print(d.split(","))

# Check String
m = 'ing' in d
n = 'ing' not in d
print(m)
print(n)

# String Format
# nu putem combina numere cu litere decat folosind format()
# metoda format poate avea o multime de argumente
quantity = 3
itemo = 788 - orhidee
price = 47.30
my_order = "I want {} prices of item {} for {} £."
print(my_order.format(quantity, itemo, price))