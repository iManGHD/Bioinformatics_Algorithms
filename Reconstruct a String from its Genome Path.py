#Reconstruct a String from its Genome Path

f = open("C:/Users/iMan/Desktop/rosalind_ba3b.txt", "r")
dna = f.read()
fragments = dna.split("\n")
k = len(fragments[0])

def reconstructlist(k, n, fragments, extract=lambda fragments, i: fragments[i]):
    result=[]
    for i in range(0,n,k):
        result.append(extract(fragments,i))
    target_len=n+k-1
    actual_len=len(result)*k
    overlap=target_len-actual_len
    if overlap>0:
        result.append(fragments[-1][k-overlap:k])
    return result


result = reconstructlist(k, len(fragments), fragments)
final = ''.join(result)
print(final)