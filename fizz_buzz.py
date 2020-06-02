# 1. Fizzbuzz (Choose whatever programming language you want for this)
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Done in python

def fizzbuzz(n):
    list1 = []
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            list1.append("FizzBuzz")

        elif i % 5 == 0:
           list1.append("Buzz")

        elif i % 3 == 0:
            list1.append("Fizz")

        else:
            list1.append(i)

    print(list1)

fizzbuzz([])
