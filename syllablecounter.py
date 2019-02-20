import sys

syllablecounter = 0 
wordcounter = 0

for c in sys.stdin.read():
	if c in 'aeiouāēīōū': 
		syllablecounter = syllablecounter + 1
# a is the number of syllables

	if c == ' ' :
		wordcounter = wordcounter + 1

# b is the number of words

print (syllablecounter/wordcounter)
