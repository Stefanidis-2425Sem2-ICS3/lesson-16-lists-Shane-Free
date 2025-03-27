#shane f
#lists
#March 25/25
#this code creates 100 numbers and averages them all
import random
import math
def list(): return random.randint(1,100)
bunchofnumbers = [list() for i in range (100) ]
print(bunchofnumbers)
average = sum(bunchofnumbers) / 100
print(average)