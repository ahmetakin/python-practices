from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copying %s to %s" % (from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "input file is %d bytes" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL- C to abort."

raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "done bitch"

out_file.close()
in_file.close()
