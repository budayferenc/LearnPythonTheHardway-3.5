from sys import argv

script, input_file = argv

def print_all(f):
    # print the file contents
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_file, current_file)

current_line = current_line + 1
current_line(current_line, current_file)


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_cheese + 1000)


def print_args(*argv):
    size = len(argv)
    print(size)
    print("Hello! Welcome to use %r!" % argv[0])
    if size > 1:
        for i in range(1, size):
            print("The param %d is %r" % (i, argv[i]))
        return 0
    return -1


print_args(10, 20, 30)

print_args("print_args", 10, 20)

print_args("print_args", "Joseph", "Pan")

first_name = "Joseph"
last_name = "Pan"
print_args("print_args", first_name, last_name)

print_args("print_args", 5*4, 2.0/5)

print_args("print_args", '.'*10, '>'*3)

print_args("print_args", 10, 20, 30, 40, 50)

nums1 = (10, 20, 30)
nums2 = (40, 50, 60)
print_args("print_args", nums1, nums2)

nums3 = [70, 80, 90]
set1 = {"apple", "banana", "orange"}
dict1 = {'id': '0001', 'name': first_name+" "+last_name}
str1 = "Wow, so complicated!"
print_args("print args", nums1, nums2, nums3, set1, dict1, str1)

if print_args(cheese_and_crackers, print_args) != -1:
    print("You just send more than one parameter. Great!")