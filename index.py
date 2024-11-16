print("Hello world")


list1 = (1,3,5,2,5,6,9)

new_list= sorted(list1)

# These methods allow you to define the behavior of objects in special cases, such as when you add two objects together or print them.


print(new_list)
print(dir(list1))

print("-------------------------------------------------------------------------------------------")

x = 100

if x > 10:
    print("Good morning")
elif x < 30:
    print("hello")
dayOfTheWeek = "Tuesday"

if dayOfTheWeek == "Monday":
    print("its monday")
elif dayOfTheWeek == "Tuesday":
    print("Its terrific Tuesday")
elif dayOfTheWeek == "Wednesday":
    print("Its Wednesday")
elif dayOfTheWeek == "Thursday":
    print("Its  Thursday")
elif dayOfTheWeek == "Friday":
    print("Its Friday")
elif dayOfTheWeek == "Saturday":
    print("Its saturday")
elif dayOfTheWeek == "Sunday":
    print("Its sunday")
else:
    print("Not valid")

print("-------------------------------------------------------------------------------------------")

name = "ravine"
print(dir(name))

# name.upper()
print(name.upper())

print(name.replace("ravine","kuria"))

print(name.__doc__)


print("-------------------------------------------------------------------------------------------")


for x in range(20,1,-2):
    print(x)

print("-------------------------------------------------------------------------------------------")
x = 1

while x <= 10:
    print(x)

    x +=1

player1 = 10
player2 = 10

from random import randint
print(randint(1,5))
i = 1
while True:
    print("Rounds",i)
    if player1<1:
        print("player 2 wins")
        break
    if player2<1:
        print("player 1 wins")
        break

    player1 -=randint(1,5)
    player2 -=randint(1,5)
    i+=1

print("-------------------------------------------------------------------------------------------")
# for item in enumerate()

