def hammingDistance(s, t):
    return len([a for (a,b) in zip(s,t) if a!=b])


def distanceBetweenPatternAndStrings (pattern,dna):
    def hamming(pattern,genome):
        return min([hammingDistance(pattern, genome[i:i + len(pattern)])
                    for i in range(len(genome)-len(pattern)+1)])
    return sum([hamming(pattern,motif) for motif in dna])

pattern = "ATATT"
file = open("C:/Users/iMan/Desktop/rosalind_ba2h.txt")
input = file.read()
dna = []
dna = input.split(" ")
print(distanceBetweenPatternAndStrings(pattern,dna))