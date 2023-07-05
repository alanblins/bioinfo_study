def MinimumSkew(Genome):
    values = SkewArray(Genome)
    return [i for i,e in enumerate(values) if e == min(values)]

def MaxSkew(Genome):
    values = SkewArray(Genome)
    return [i for i,e in enumerate(values) if e == max(values)]



def SkewArray(Genome):
    skew = [0] 
    current = 0
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(0,len(Genome)):
        skew.append(current+score[Genome[i]])
        current = skew[-1]
    return skew

print(MaxSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))
