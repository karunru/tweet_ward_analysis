import numpy as np
import sys
import csv

argvs = sys.argv
if (len(argvs) != 2):
	print('Usage: $ python %s filename' % argvs[0])
	exit()
 
tweetsfilename = argvs[1]
try:
        f = open(tweetsfilename,"r")
        tweets = list(csv.reader(f))
	# tweets = np.loadtxt(tweetsfilename,delimiter=",",usecols=(3,5))
except:
	print('faild to load %s' % tweetsfilename)
	exit()

for row in tweets:
    row[5] = row[5].replace("\n"," ")
    print(row[5])

f.close()
