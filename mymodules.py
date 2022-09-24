def PatternCount(text, pattern):
    count = 0
    for x in range(0,len(text)-len(pattern)+1) :
        if Extract(text, x, pattern) == pattern :
            count+=1
    return count

def Extract(text, position, pattern) :
    return text[position:position+len(pattern)]


def FrequentWords(text, k):
    maxValue=0
    word=''
    for x in range(0, len(text) -k+1):
        pattern = text[x:x+k+1]
        count = PatternCount(text, pattern)
        if  count > maxValue:
            maxValue=count
            word=pattern
    print(word)
    print(maxValue)

def SymbolToNumber(letter):
    return 'ACGT'.index(letter)

def NumberToSymbol(n):
    return 'ACGT'[n]

def Prefix(word):
    return word[:-1]

def Last(word):
    return word[-1]


def PatternToNumber(word):
    if word == '' :
        return 0
    return 4*PatternToNumber(Prefix(word))+SymbolToNumber(Last(word))


def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index // 4
    r = index % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern+symbol

def ComputingFrequencies(text, k):
    frequencyArray = [0]*(4**k-1)
    for i in range(0, len(text)-k+1) :
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyArray[j] = frequencyArray[j]+1
    return frequencyArray

def FasterFrequentWords(text, k):
    frequentPatterns = [] 
    frequencyArray = ComputingFrequencies(text, k)
    maxCount = max(frequencyArray)
    for i in range(0, 4**k-1) :
        if frequencyArray[i] == maxCount:
            pattern = NumberToPattern(i, k)
            frequentPatterns.append(pattern)
    return frequentPatterns
