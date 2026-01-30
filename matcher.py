file = open("example.in")
n = int(file.readline())
print("n =", n)
print("Hospital preference lists:")
for i in range(0, n):
  print(file.readline().split())
print("Student preference lists:")
for i in range(0, n):
  print(file.readline().split())