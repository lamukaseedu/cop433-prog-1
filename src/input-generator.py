import random

'''
This file can be run to write a valid input file for generated.in given some input n.
'''
n = int(input("Enter n: "))
with open("../data/generated.in", "w") as file:
  file.write(str(n))
  file.write("\n")
  numbers = list(range(1, n + 1))
  for i in range(0, 2 * n):
    random.shuffle(numbers) # Creates a random permutation of 1 to n for each preference list
    for j in range(0, n):
      file.write(str(numbers[j]))
      if (j != n - 1):
        file.write(" ")
    if (i != 2 * n - 1):
      file.write("\n")