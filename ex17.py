from sys import argv
from os.path import exists

script, filefrom, fileto = argv

print "Copying files from %s to %s" %(filefrom, fileto)

infile = open(filefrom)
indata = infile.read()
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(fileto)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_data()

out_file = open(fileto, 'w')
outfile.write(indata)
print "Alright, all done."

out_file.close()
in_file.close()
