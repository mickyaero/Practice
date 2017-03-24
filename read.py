"""
#It imports the thing argv from the library already in the computer "sys"
from sys import argv

#Script here means that i will have to type the filename with the python command and passes this argument to the "filename"
script, filename = argv
#OPen the file and stores it in text variable
text = open(filename)

#prints the file
print "This is the file %r" %filename
#text.read(), reads the data in the file and it is then directly printed
print text.read()
#just another print statement
"""

print " Type filename again:"
#the "> " is just what you would like to show to the user to add an input, its just a bullet !!!!!!input is taken from the user in the running of the code and that is used further in the code, so basically the code halts here and takes the input, nice!!!
file_again = raw_input("> ")
#same stores the data in "text_again"
text_again = open(file_again)
#prints it
print text_again.read()
#closes the file
text_again.close()
