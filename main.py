# this is an integer, it represents a number in Python
a = 5

# this is a string, it represents text in Python
b = "hello Mada"

# this is a list ("array" in other languages), it represents a list of items
nums = range(1, 101)
# print(nums)

# exercise: create a new list containing only the even numbers from the list above
even_nums = []
odd_nums = []

# loop through every number in the list, if the number is even add it to the new list of even numbers
for x in nums:
    if x % 2 == 0:
        even_nums.append(x)
    if (x % 2 == 0) and (x % 3 == 0):
        print(f'numarul {x} este divizibil cu 2 si cu 3')
    else:
        odd_nums.append(x)
print(even_nums)
print(odd_nums)


def say_hi(name):
    return f'Hello {name}'

say_hi('Gabi')






# # this is a simple function 
# c = 3
# d = 7

# def add(c, d):
#     return c+d

# add(1,2)

# def scade(num1,num2):
#     return num1-num2

# scade(42,12)
# print(scade(42,12))
# print(scade(30,6))

# def multiply(x,y):
#     return x*y

# multiply(57,34)
# print(multiply(57,34))

