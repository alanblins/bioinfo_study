def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq.keys():
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1

    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] >= m:
            words.append(key)
    return words


print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
