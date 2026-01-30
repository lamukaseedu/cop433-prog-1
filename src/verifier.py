file = open("../data/example.in") # Name of input file goes here
n = file.readline() # Read n from first line
if n == "":
  print("Error! Input missing n")
  exit() # Terminate if file is empty
else:
  n = int(n)
hospital_lists = []
for i in range(1, n + 1): # Read hospital preference lists from next n lines
  line = file.readline()
  if line == "":
    print("Error! Input missing hospital line", i)
    exit()
  hospital_lists.append(line.split())
student_lists = []
for i in range(1, n + 1): # Read student preference lists from next n lines
  line = file.readline()
  if line == "":
    print("Error! Input missing student line", i)
    exit()
  student_lists.append(line.split())

file = open("../data/example.out") # Name of output file goes here
matchings = {}
for i in range(0, n): # Read matchings from the next n lines
  line = file.readline()
  if line == "":
    print("Error! Missing line", i)
    exit()
  matchings[line.split()[0]] = line.split()[1] # Create dictionary of matchings
