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

z = -87.7e100
print(float(z))