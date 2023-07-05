
# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


# Insert your Count(Motifs) function here.

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    score = 0
    t = len(Motifs)
    count = Count(Motifs)
    consensus = Consensus(Motifs)
    k = len(consensus)
    for j in range(k):
        symbol = consensus[j] 
        freq = t-count[symbol][j]
        score += freq
    return score
