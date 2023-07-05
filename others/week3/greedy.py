# Insert your Pr(text, profile) function here from Motifs.py.

# Write your ProfileMostProbableKmer() function here.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.

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

def Profile(Motifs):
    count = Count(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}

    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
             profile[symbol].append(count[symbol][j]/t)
    return profile

def Pr(Text, Profile):
    k = len(Text)
    score= 1
    for j in range(k):
        symbol = Text[j] 
        freq = Profile[symbol][j]
        score *= freq
    return score

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

def ScoreWrong(Motifs):
    count = Count(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    max_symbol = Consensus(Motifs)
    score = 0 
    for j in range(k):
        highScore = 0
        for symbol in "ACGT":
             j_score = count[symbol][j]
             if j_score > highScore:
                highScore = j_score
        score += t - highScore
    return score

def Score(Motifs):
    # Insert code here
    score = 0
    k = len(Motifs[0])
    count = Count(Motifs)
    max_symbol = Consensus(Motifs)
    sum1 = 0
    for j in range(k):
        m = 0
        for symbol in "ATCG":
            if count[symbol][j] > m:
                sum1 += count[symbol][j]
    for j in range(k):
        m = 0
        for symbol in "AGTC":
            if count[symbol][j] > m:
                m = count[symbol][j]
        score += m  
    return sum1-score

def ProfileMostProbableKmerWrong(text, k, profile):
    text = text+text[:k]
    mostN = 0
    mostMer = text[0:k]
    for i in range(len(text)-k+1):
        mer = text[i:i+k]
        pr = Pr(mer, profile)
        if pr > mostN:
            mostN = pr
            mostMer = mer
    return mostMer

def ProfileMostProbableKmer(text,k,profile):
    p=-1
    result=text[0:k]
    for i in range(len(text)-k+1):
        seq=text[i:i+k]
        pr=Pr(seq,profile)
        if pr>p:
            p=pr
            result=seq
    return result

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


profile = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}
profile2 = {
'A': [0.4, 0.3, 0.0,0.1,0.0,0.9],
'C': [ 0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
'G':  [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
'T':  [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}
# print(ProfileMostProbableKmer('TGCCGTGCC', 3, profile))

print(Pr('CAGTGA', profile2))

dna = ['GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA', 
        'TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA',
    'GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA',
    'GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC',
    'AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA',
    'AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA',
    'GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA',
    'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT']
# print(GreedyMotifSearch(dna, 4,8))
