# Write a program that prints the numbers from 1 to 100
# and for multiples of ‘3’ print “Fizz” instead of the
# number and for the multiples of ‘5’ print “Buzz”

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()