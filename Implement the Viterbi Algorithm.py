# argmax = Returns the indices of the maximum values along an axis
from numpy import argmax


def Viterbi(xs, alphabet, States, Transition, Emission):

    def calculateproduct_weights(s_source=1):
        def product_weight(k, x):
            return max([s[-1][l] * Transition[(States[l], k)] * Emission[(k, x)] for l in range(len(States))])
        s=[]
        s.append([s_source * (1 / len(States)) * Emission[(k, xs[0])] for k in States])
        for x in xs[1:]:
            s.append([product_weight(k, x) for k in States])
        return s

    def backtrack(s):
        n = len(s) - 1
        #argmax = Returns the indices of the maximum values along an axis
        state = argmax(s[n])
        path = [States[state]]
        while True:
            ps = [s[n - 1][l] * Transition[(States[l], States[state])] for l in range(len(States))]
            state = argmax(ps)
            path.append(States[state])
            n -= 1
            if n <= 0: return path[::-1]

    return ''.join(backtrack(calculateproduct_weights()))


f = open("C:/Users/iMan/PycharmProjects/RosalindExercises/rosalind_ba10c.txt","r")
text = f.read()
input =[]
input = text.split("\n")
transition_Row_A = []
transition_Row_B = []
transition_Row_C = []
transition_Row_D = []
transition_Row_A = input[7].split()
transition_Row_B = input[8].split()

Transition = { ('A','A') : float(transition_Row_A[1]), ('A','B') : float(transition_Row_A[2]),
               ('B','A') : float(transition_Row_B[1]), ('B','B') : float(transition_Row_B[2])
               }
emission_Row_A = []
emission_Row_B = []
emission_Row_C = []
emission_Row_D = []
emission_Row_A = input[11].split()
emission_Row_B = input[12].split()


Emission = {('A','x') : float(emission_Row_A[1]), ('A','y') : float(emission_Row_A[2]), ('A','z') : float(emission_Row_A[3]),
            ('B','x') : float(emission_Row_B[1]), ('B','y') : float(emission_Row_B[2]), ('B','z') : float(emission_Row_B[3])
            }

print (Viterbi(input[0],'xyz','AB', Transition, Emission))