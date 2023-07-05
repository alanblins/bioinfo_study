#2 Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    skew = [0] 
    current = 0
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(0,len(Genome)):
        skew.append(current+score[Genome[i]])
        current = skew[-1]
    return skew
