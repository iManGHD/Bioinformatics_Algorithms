import sys


def hammingDistance(s, t):
    return len([a for (a,b) in zip(s,t) if a!=b])


def distanceBetweenPatternAndStrings (pattern,dna):
    def hamming(pattern,genome):
        return min([hammingDistance(pattern, genome[i:i + len(pattern)])
                    for i in range(len(genome)-len(pattern)+1)])
    return sum([hamming(pattern,motif) for motif in dna])


def k_mers(k):
    if k<=0:
        return ['']
    else:
        result=[]
        for ks in k_mers(k-1):
            for l in ['T','G','C','A']:
                result.append(ks+l)
    return result


def medianString(k,dna):
    def findClosest(d):
        distance=sys.float_info.max
        closest=None
        for k_mer in k_mers(k):
            if distance>d(k_mer,dna):
                distance=d(k_mer,dna)
                closest=k_mer
        return closest
    return findClosest(distanceBetweenPatternAndStrings)


k=6
f = open("C:/Users/iMan/PycharmProjects/RosalindExercises/rosalind_ba2b.txt","r")
text = f.read()
dna =[]
dna = text.split("\n")
print(medianString(k,dna))