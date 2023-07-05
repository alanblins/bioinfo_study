import random
def RandomMotifs(Dna, k, t):
    k_mers = []
    for text in Dna:
        ran_pos = random.randint(1, len(text)-k-1)
        k_mers.append(text[ran_pos:ran_pos+k])
    return k_mers

    
