import random

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

def Score2(Motifs):
    count = 0
    L = Consensus(Motifs)
    for i in Motifs:
        for chr1, chr2 in zip(i,L):
            if chr1 != chr2:
                count += 1
    return count

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

def ProfileWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            sumSymbol = 0
            for symbol2 in "ACGT":
                sumSymbol += count[symbol2][j]
            result = float(count[symbol][j])/float(sumSymbol)
            profile[symbol].append(float(result))
    return profile

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(float(1.0))
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Pr(Text, Profile):
    k = len(Text)
    score= 1
    for j in range(k):
        symbol = Text[j] 
        freq = Profile[symbol][j]
        score *= freq
    return score

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

def ConsensusPseudo(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
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

def ScorePseudo(Motifs):
    # Insert code here
    score = 0
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    max_symbol = ConsensusPseudo(Motifs)
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


def Motifs(Profile, Dna):
    k = len(Profile["A"])
    motifs = []
    for text in Dna:
        motifs.append(ProfileMostProbableKmer(text,k,Profile))
    return motifs

def RandomMotifs(Dna, k, t):
    k_mers = []
    for text in Dna:
        ran_pos = random.randint(0, len(text)-k-1)
        k_mers.append(text[ran_pos:ran_pos+k])
    return k_mers


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score2(M) < Score2(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

def Normalize(Probabilities):
    d = {}
    for k,v in Probabilities.items():
        d[k] = Probabilities[k]/sum(Probabilities.values())
    return d

def Normalize2(Probabilities):
    d =[] 
    for v in Probabilities:
        d.append(v/sum(Probabilities))
    return d

def WeightedDie(Probabilities):
    count = 0
    p = random.uniform(0,1)
    for keys,values in Probabilities.items():
        count = count+values
        if p < count:
            return keys

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for j in range(1,N):
        i = random.randint(0,t-1)
        ReducedMotifs = []
        for j in range(0,t):
            if j != i:
                ReducedMotifs.append(Motifs[j])
        Profile = ProfileWithPseudocounts(ReducedMotifs)
        Motif_i = ProfileGeneratedString(Dna[i], Profile, k)
        Motifs[i] = Motif_i
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs=Motifs
    return BestMotifs

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if ScorePseudo(Motifs) < ScorePseudo(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


input = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
input2 = ["GTACAACTGT","CAACTATGAA","TCCTACAGGA","AAGCAAGGGT","GCGTACGACC",
    "TCGTCAGCGT",
    "AACAAGGTCA",
    "CTCAGGCGTC",
    "GGATCCAGGT",
    "GGCAAGTACC"]
input3 = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
# print(Normalize(input3))
input4= [0.15, 0.6, 0.225, 0.225, 0.3]
print(Normalize2(input4))
# print(CountWithPseudocounts(input))
# print(ProfileWithPseudocounts(input2))

Dna =['AAGCCAAA', 'AATCCTGG','GCTACTTG','ATGTTTTG']
motifs = ["CCA","CCT","CTT","TTG"]

# print(Motifs(Profile(motifs), Dna))
