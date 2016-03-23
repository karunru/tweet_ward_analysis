from collections import Counter
import MeCab
import sys
import csv

argvs = sys.argv
if (len(argvs) != 2):
	print('Usage: $ python %s filename' % argvs[0])
	exit()
 
tweetsfilename = argvs[1]
try:
        f = open(tweetsfilename,"r")
        tweets = f.readlines()
	# tweets = np.loadtxt(tweetsfilename,delimiter=",",usecols=(3,5))
except:
	print('faild to load %s' % tweetsfilename)
	exit()

# texts = (tw.encode('utf-8') for tw in tweets)
tagger = MeCab.Tagger('-Ochasen')
counter = Counter()

for text in tweets:
    text.encode('utf-8')
    nodes = tagger.parseToNode(text)
    while nodes:
        # if nodes.feature.split(',')[0] == '名詞' or nodes.feature.split(',')[0] == '動詞' :
        # print(nodes.feature)
        if nodes.feature.split(',')[0] == '名詞' :
            # word = nodes.surface.decode('utf-8')
            word = nodes.surface
            counter[word] += 1
        nodes = nodes.next
for word, cnt in counter.most_common():
    print(word,cnt)
