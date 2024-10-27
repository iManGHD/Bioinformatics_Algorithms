from reference_tables import bases


def mostProbable(text, n, profile):

    def prob(kmer):
        p = 1
        for j in range(n):
            i = bases.find(kmer[j])
            p *= profile[i][j]
        return p

    def findMostProbable():
        probability = -1
        best = []
        for i in range(len(text) - n + 1):
            p = prob(text[i:i + n])
            if probability < p:
                probability = p
                best = text[i:i + n]
        return best

    return findMostProbable()


f = open("C:/Users/iMan/PycharmProjects/RosalindExercises/rosalind_ba2c.txt","r")
text = f.read()

k=7
string = "CGTTCCTTGCAGAGTTTACACAGCATAAAAGGATCCGCACAGAGGATACGTCAGCCAGTGGCAAACGGGCGTCTCTCGTGTCTTCGTCGTACTGACACAGCTATCTCCGTCATAGTAGGTTACTAGGTCCACAGTTACACGGCGAGGCCAGCTGCCAGAGCATCGCAATAACCGAATGCTTGTTAAGGCGTAGAGGGGCG"
T=[]
profileTable = text.split("\n")

rows_0 = profileTable[0].split()
rows_1 = profileTable[1].split()
rows_2 = profileTable[2].split()
rows_3 = profileTable[3].split()

for i in range(0, len(rows_0)):
    rows_0[i] = float(rows_0[i])

for i in range(0, len(rows_1)):
    rows_1[i] = float(rows_1[i])

for i in range(0, len(rows_2)):
    rows_2[i] = float(rows_2[i])

for i in range(0, len(rows_3)):
    rows_3[i] = float(rows_3[i])

T.insert(0,rows_0)
T.insert(1,rows_1)
T.insert(2,rows_2)
T.insert(3,rows_3)

print(mostProbable(string,k,T))