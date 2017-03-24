#Comment should be above the line(sure???)
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#This  is asking whether you wnat to proceed or not, its very good, if you press enter you go forward else you do not, its excellent, the question mark is just fro the user to see!!!
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = line1+"\n"+line2+"\n"+line3+"\n"
print "I'm going to write these to the file."

target.write(line4)
"""
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

print "And finally, we close it."
target.close()
