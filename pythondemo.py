# Print something in python
print("hello world")

# Assign a single variable
x = 1
print(x)
x = "hello"
print(x)

# Assign a list, types need not match
x = [1, 2, 3, "hello"]
# Python has built in printing for data strucutres
print(x)

# Create a dictionary (somewhat equivalent to a map in C++), but much more flexible
x = {
    "key": "stringvalue",
    1: "intvalue",
    ("tup", "le"): "tuplevalue"
}
print(x["key"])
print(x[1])
print(x[("tup", "le")])

# If statements in python
x = 1
if x == 0:
    print("x is 0")
elif x == 1:
    print("x is 1")
else:
    print("x is messed up")

# Loops in python

# While loop
x = True
ctr = 0
while x == True:
    print(ctr)
    ctr += 1
    if ctr == 5:
        x = False

# For loop
for i in range(0, 5):
    print(i)
for i in [0, 1, 2, 3, 4]:
    print(i)

# For each loop
l = ["line1", "line2", "line3", 1, 2, 3]
for item in l:
    print(item)

# Functions in python
def main():
    print("This is the main function")

def main2(x):
    print("This is the main function with param " + str(x))

# This checks if the current file is being executed or being
# used as a part of a library. The code inside this if only
# executes when the file is actually being run.
if __name__ == "__main__":
    main()
    main2(1000)

# Classes in python
class Student:
    def __init__(self, name, uniqname, id):
        self.name = name
        self.uniqname = uniqname
        self.id = id

    def getName(self):
        return self.name
    
    def printStudent(self):
        print(self.name + " has the uniqname " + self.uniqname + " and the id " + str(id))

x = Student("Joe Smith", "smithj", 12345678)
print(x.getName())
x.printStudent()