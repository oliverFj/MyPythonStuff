"""
i = 0
while i < 4:
 print("i * i")
 i = i+1

i = 0
while i < 4:
 print("Hello")
 i = i+1

i = 0
while i < 5:
 print(i, 2 ** i)
 i = i+1


Task 3

for i in range(6):
 print(i)

i = 0
while i < 6:
 print(i)
 i = i+1



toppings = ""

print("Enter 'quit' to exit the program")


while True:
    topping = input("Which topping should be put on your pizza?")


    if topping == "quit":
        print("Expect your " + toppings + "pizza delivered in 10 minutes")
        break

    else:
        toppings = toppings+ " " + topping
        print ("Excellent choice! Your pizza now contains" + toppings)



customers = 0

stateofanalog = input("what has happened")

while True:

    if stateofanalog == "enter":
        customers = customers +1

    elif stateofanalog == "leave":
        customers = customers -1

    elif stateofanalog == "close":
        break

    else:
        print ("I didnt understand that")



def volume(length, width, height):
    params = length * width * height
    return params

print (volume(2,3,2))



def oh():
 print("Oh,", end=" ")
 that()
def that():
 print("that's the way, ", end = "")

def ilikeit():
 print("I like it, ", end ="")
 uhhuh()

def uhhuh():
 print("uh-huh, uh-huh")

oh()
uhhuh()
ilikeit()

for i in range(3):
    that()
    uhhuh()
    ilikeit()



def eur_to_dkk(amount):
    return amount * 7,46

def dkk_to_eur(amount):
    return amount / 7,46

print("100 Euro are " + str(eur_to_dkk(100)) + " DKK.")
print("21000 DKK are " + str(dkk_to_eur(21000)) + " Euro.")



def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3* number + 1
    return number

print (collatz(3))



print (4 == 4)



favorite_animals = ["cat","rat","bat","elephant"]

print (favorite_animals)

for animal in favorite_animals:
    print (animal)

animal_storage = ""

animal_storage = favorite_animals[1]
favorite_animals[1] = favorite_animals [2]
favorite_animals[2] = animal_storage

for animal in favorite_animals:
    print (animal)



favorite_cities = {}

favorite_cities["Tokyo"] = "Japan"
favorite_cities["Vancouver"] = "Canada"
favorite_cities["Basel"] = "Schweiz"

print("City Tokyo is in " + favorite_cities["Tokyo"])

for city in favorite_cities:
    print("The city " + city + " is in the country of " + favorite_cities[city])



birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have the birthday of ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')



dictionary {}
dictionary {"foo" : "42"}



values = [1, 2, 4, 10]

def f(val):
    return 4 * val

print (f(values[:2]))





def ituify(text):
    if text.endswith("IT"):
        return text
    else:
        return text + "IT"

thing = input()
print (ituify(thing))

"""


