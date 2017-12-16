print("hello world") #hello

print ((3 + 4) + 2*3 ) % 2#calculation

print 3+4 > 7+8 #true or false


pi = 3.4

sayi = 50

sayi1 = 4

sayi3 = sayi + sayi1

sayi4 = (sayi+sayi1) * pi

print sayi4 , sayi3 , sayi1 , sayi , pi

isim="ahmet"

print "ve %s" % isim

print "Bunlar %d ve aaa" % sayi3

print "Bunlar %d ve %d ve %d" % (sayi,sayi1, pi * sayi1)

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print months

print "I am 6'2\" tall."

print 'I am 6\'2" tall.'

print "How old are you?",
age = raw_input()
height = raw_input("How tall are you? ")

print "So, you're %r old %r" % (age,height)


#
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's %r" % filename

print txt.read()


print "Enter again"

file_again= raw_input("> ")

txt_again= open(file_again)

print txt_again.read() #dostayı calıştırırken txt dosyasını yaz .py yanında