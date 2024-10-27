import os
import sys


def create_strings(problem=os.path.basename(sys.argv[0]).split('.')[0],
                   path=os.path.join(os.path.expanduser('~'), 'Downloads'),
                   ext=None,
                   fasta=False,
                   name=None):
    product = []
    with open("C:/Users/iMan/Desktop/rosalind_ba7c.txt", 'r') as f:
        if fasta:
            for record in SeqIO.parse(f, 'C:/Users/iMan/Desktop/rosalind_ba7c.txt'):
                product.append(str(record.seq))
        else:
            for line in f:
                product.append(line.strip())
    return product


def read_matrix(problem=os.path.basename(sys.argv[0]).split('.')[0],
                path=os.path.join(os.path.expanduser('~'), 'Downloads'),
                ext=None,
                conv=int,
                len_params=1,
                name=None):
    params = []
    D = []
    for line in create_strings(problem=problem, path=path, ext=ext, name=name):
        if len(params) < len_params:
            params.append(int(line))
        else:
            D.append([conv(s) for s in line.split()])

    return (params, D)


class Tree(object):

    def __init__(self, n=-1, bidirectional=True):
        self.nodes = list(range(n))
        self.edges = {}
        self.bidirectional = bidirectional
        self.N = n

    def link(self,start,end,weight=1):
        self.half_link(start,end,weight)
        if self.bidirectional:
            self.half_link(end,start,weight)

    def half_link(self, a, b, weight=1):
        if not a in self.nodes:
            self.nodes.append(a)
        if a in self.edges:
            self.edges[a] = [(b0, w0) for (b0, w0) in self.edges[a] if b0 != b] + [(b, weight)]
        else:
            self.edges[a] = [(b, weight)]

    def half_unlink(self, a, b):
        links = [(e, w) for (e, w) in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
        else:
            print('Could not unlink {0} from {1}'.format(a, b))
            self.print()

    def are_linked(self, a, b):
        return len([e for (e, w) in self.edges[a] if e == b]) > 0

    def print_adjacency(self, includeNodes=False):
        print('-----------------')
        self.nodes.sort()
        if includeNodes:
            print(self.nodes)
        for node in self.nodes:
            if node in self.edges:
                for edge in self.edges[node]:
                    end, weight = edge
                    print('{0}->{1}:{2}'.format(node, end, weight))

    def next_node(self):
        return len(self.nodes)

    def unlink(self, i, k):
        try:
            self.half_unlink(i, k)
            if self.bidirectional:
                self.half_unlink(k, i)
        except KeyError:
            print('Could not unlink {0} from {1}'.format(i, k))
            self.print()

    def traverse(self, i, k, path=[], weights=[]):
        if not i in self.edges: return (False, [])
        if len(path) == 0:
            path = [i]
            weights = [0]

        for j, w in self.edges[i]:
            if j in path: continue
            path1 = path + [j]
            weights1 = weights + [w]
            if j == k:
                return (True, list(zip(path1, weights1)))
            else:
                found_k, test = self.traverse(j, k, path1, weights1)
                if found_k:
                    return (found_k, test)
        return (False, [])


def computeLimbLength(n, j, D):
    return int(min([D[i][j]+D[j][k]-D[i][k] for i in range(n) for k in range(n) if j!=k and k!=i and i!=j])/2)


def additivephylogeny(D, n, N=-1):

    def find_ikn(DD):
        for i in range(n):
            for k in range(n):
                if DD[i][k] == DD[i][n - 1] + DD[n - 1][k] and i != k:
                    return (i, k, n - 1, DD[i][n - 1])

    def get_Position_v(traversal):
        d = 0
        for l, w in traversal:
            d0 = d
            d += w
            if d == x: return (True, l, l, d0, d)
            if d > x: return (False, l_previous, l, d0, d)
            l_previous = l

        return (False, l_previous, l, d0, d)

    if N == -1:
        N = n
    if n == 2:
        T = Tree(N)
        T.link(0, 1, D[0][1])
        return T
    else:
        limbLength = computeLimbLength(n, n - 1, D)

        D_bald = [d_row[:] for d_row in D]
        for j in range(n - 1):
            D_bald[n - 1][j] -= limbLength
            D_bald[j][n - 1] = D_bald[n - 1][j]

        i, k, node, x = find_ikn(D_bald) 

        D_Trimmed = [D_bald[l][:-1] for l in range(n - 1)]

        T = additivephylogeny(D_Trimmed, n - 1, N)
        found_k, traversal = T.traverse(i, k)
        path, weights = zip(*traversal)

        found, l0, l1, d, d0 = get_Position_v(traversal)

        if found:
            v = l0  
            T.link(node, v, limbLength)
        else:
            v = T.next_node()
            weight_i = computeLimbLength(n, i, D)
            weight_k = computeLimbLength(n, k, D)
            T.unlink(l0, l1)
            T.link(v, l0, x - d)
            T.link(v, l1, d0 - x)

        T.link(node, v, limbLength) 

        return T


if __name__ == '__main__':

    params, D = read_matrix(name='Additive_Phylogeny')
    additivephylogeny(D, 22).print_adjacency()