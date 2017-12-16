from sys import exit
def print_two(*args):
	arg1, arg2 =args
	print "arg1: %r , arg2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1: %r , arg2: %r" % (arg1,arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got no"

print_two("tes","test")
print_two_again("aaa",5)
print_one("bbbb")
print_none()

if 5 <10:
	print "test"
	exit(0)
elif 7 <10:
	print "aaaa"
else:
	print "aa"


count = [1,2,3,4,5]
list = ["test","test1","test2","test3"]

for number in count:
	print "this %d" % number
for listt in list:
	print "this %s" % listt
elements =[]

for i in range(0,6):
	print "aaa %d to list" % i
	elements.append(i)
for i in elements:
	print "%d" % i

i=0
numbers=[]
while i < 6:
	print "%d" % i
	numbers.append(i)
	i = i +1
	print "Number now" , numbers
	print "%d" % i

for num in numbers:
	print num


print list[1]

cities = [
 'CA': 'San Francisco',
 'MI': 'Detroit',
 'FL': 'Jacksonville'
 ]
 cities['NY'] = 'New York'

 print '-' * 10