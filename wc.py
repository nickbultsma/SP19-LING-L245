import sys

linecounter = 0
tokencounter = 0
charcounter = 0

for c in sys.stdin.read():
	if c == '\n':
		linecounter = linecounter + 1
	if c == ' ': 
		tokencounter = tokencounter + 1
	charcounter = charcounter + 1
print(linecounter)
print(tokencounter)
print(charcounter)
