def Pr(Text, Profile):
    k = len(Text)
    score= 1
    for j in range(k):
        symbol = Text[j] 
        freq = Profile[symbol][j]
        # if freq > 0:
        score *= freq
    return score

profile = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}
print(Pr('TCGGGGATTTCC', profile))
print(Pr('ACGGGGATTACC', profile))
print(Pr('TCGTGGATTTCC', profile))
