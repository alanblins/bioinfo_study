import re
 # Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    window = n//2
    ExtendedGenome = Genome+Genome[0:window]

    array[0] = PatternCount(Genome[0:window], symbol)

    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1

        if ExtendedGenome[i+window-1] == symbol:
            array[i] = array[i]+1


    # your code here
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Text, Pattern):
    p = re.compile(rf"(?={Pattern})")
    return len(p.findall(Text))


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1])) 
