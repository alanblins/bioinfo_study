import re
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = []
    n = len(Genome)
    window = n//2
    ExtendedGenome = Genome+Genome[0:window]
    for i in range(n):
        count = PatternCount(ExtendedGenome[i:i+window], symbol)
        array.append(count)
    return array

# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
    p = re.compile(rf"(?=({Pattern}))")
    return len(p.findall(Text))

f = open("ecoli.txt", "r")
genome = f.read()

print(SymbolArray(genome,"C"))
