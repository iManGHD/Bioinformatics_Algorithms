import numpy

from reference_tables import bases




def mostProbability(text, n, profile):
    def prob(kmer):
        p = 1
        for j in range(n):
            i = bases.find(kmer[j])
            p *= profile[i][j]
        return p

    def findMost():
        probability = -1
        best = []
        for i in range(len(text) - n + 1):
            p = prob(text[i:i + n])
            if probability < p:
                probability = p
                best = text[i:i + n]
        return best

    return findMost()



def greedyMotifSearch(k, t, dna):

    def count_occurrences_of_bases(motifs,initialise_counts=numpy.ones ):
        matrix = initialise_counts((len(bases), k), dtype=int)
        for kmer in motifs:
            for j in range(k):
                i = bases.find(kmer[j])
                matrix[i, j] += 1
        return matrix

    def profile(motifs):
        return count_occurrences_of_bases(motifs) / float(len(motifs))

    def score(motifs):
        matrix = count_occurrences_of_bases(motifs)
        total = 0
        for j in range(k):
            m = 0
            for i in range(len(bases)):
                if m < matrix[i, j]:
                    m = matrix[i, j]
            total += (len(bases) - m)
        return total

    bestMotifs = [genome[0:k] for genome in dna]
    for motif in [dna[0][i:i + k] for i in range(len(dna[0]) - k + 1)]:
        motifs = [motif]
        for i in range(1, t):
            motifs.append(mostProbability(dna[i], k, profile(motifs)))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

f = open("C:/Users/iMan/PycharmProjects/RosalindExercises/rosalind_ba2e.txt","r")
k=12
t=25
text = f.read()
dna=[]
dna = text.split("\n")
bestMotif=[]
bestMotif = greedyMotifSearch(k,t,dna)
for i in range(len(bestMotif)):
    print(bestMotif[i])