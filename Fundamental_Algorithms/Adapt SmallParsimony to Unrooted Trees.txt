import re
import random


class Tree(object):

    def __init__(self, N=-1, bidirectional=True):
        self.nodes = list(range(N))
        self.edges = {}
        self.bidirectional = bidirectional
        self.N = N

    def initialize_from(self, T):
        for node in T.nodes:
            if not node in self.nodes:
                self.nodes.append(node)
                if node in T.edges:
                    for a, w in T.edges[node]:
                        self.link(node, a, w)

    def link(self, start, end, weight=1):
        self.half_link(start, end, weight)
        if self.bidirectional:
            self.half_link(end, start, weight)

    def unlink(self,i,k):
        try:
            self.half_unlink(i,k)
            if self.bidirectional:
                self.half_unlink(k,i)
        except KeyError:
            print ('Could not unlink {0} from {1}'.format(i,k))
            self.print()

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

    def next_node(self):
        return len(self.nodes)

    def get_nodes(self):
        for node in self.nodes:
            yield(node)

    def is_leaf(self, v):
        return v in self.leaves

    def remove_backward_links(self,root):
        self.bidirectional = False
        for (child,_) in self.edges[root]:
            self.half_unlink(child,root)
            self.remove_backward_links(child)


class LabelledTree(Tree):

    def __init__(self, N=-1, bidirectional=True):
        super().__init__(N, bidirectional=bidirectional)
        self.labels = {}
        self.leaves = []

    def set_label(self, node, label):
        if not node in self.nodes:
            self.nodes.append(node)
        self.labels[node] = label

    def parse(N, lines, letters='ATGC', bidirectional=True):
        def get_leaf(string):
            for index, label in T.labels.items():
                if string == label:
                    return index
            return None

        T = LabelledTree(bidirectional=bidirectional)
        pattern = re.compile('(([0-9]+)|([{0}]+))->(([0-9]+)|([{0}]+))'.format(letters))

        for line in lines:
            m = pattern.match(line)
            if m:
                i = None

                if m.group(2) == None:
                    i = get_leaf(m.group(3))
                    if i == None:
                        i = len(T.labels)
                    T.set_label(i, m.group(3))

                    if not i in T.leaves:
                        T.leaves.append(i)

                if m.group(3) == None:
                    i = int(m.group(2))

                if m.group(5) == None:
                    j = get_leaf(m.group(6))
                    if j == None:
                        j = len(T.labels)
                        if not j in T.leaves:
                            T.leaves.append(j)
                        T.set_label(j, m.group(6))
                    T.link(i, j)

                if m.group(6) == None:
                    j = int(m.group(5))
                    T.link(i, j)

        return T

    def initialize_from(self, T):
        super().initialize_from(T)
        for node, label in T.labels.items():
            self.set_label(node, label)


def SmallParsimony(T, alphabet='ATGC'):

    def SmallParsimonyC(Character):
        def get_ripe():
            for v in T.get_nodes():
                if not processed[v] and v in T.edges:
                    for e, _ in T.edges[v]:
                        if e > v: continue
                        if not processed[e]: break

                    return v
            return None

        def calculate_s(symbol, v):

            def delta(i):
                return 0 if symbol == alphabet[i] else 1

            def get_min(e):
                return min(s[e][i] + delta(i) for i in range(len(alphabet)))

            return sum([get_min(e) for e, _ in T.edges[v]])

        def update_assignments(v, s):
            if not v in assignments.labels:
                assignments.labels[v] = ''
            index = 0
            min_s = float('inf')
            for i in range(len(s)):
                if s[i] < min_s:
                    min_s = s[i]
                    index = i
            assignments.set_label(v, assignments.labels[v] + alphabet[index])
            return alphabet[index]

        def backtrack(v, current_assignment):
            for v_next, _ in T.edges[v]:
                if T.is_leaf(v_next): continue
                if not v_next in assignments.labels:
                    assignments.labels[v_next] = ''
                min_score = min([s[v_next][i] for i in range(len(alphabet))])
                indices = [i for i in range(len(alphabet)) if s[v_next][i] == min_score]
                matched = False
                for i in indices:
                    if alphabet[i] == current_assignment:
                        matched = True
                        assignments.set_label(v_next, assignments.labels[v_next] + current_assignment)
                        backtrack(v_next, current_assignment)
                if not matched:

                    next_assignment = alphabet[indices[random.randrange(0, (len(indices)))]]
                    assignments.set_label(v_next, assignments.labels[v_next] + next_assignment)
                    backtrack(v_next, next_assignment)

        processed = {}
        s = {}
        for v in T.get_nodes():
            if T.is_leaf(v):
                processed[v] = True
                s[v] = [0 if symbol == Character[v] else float('inf') for symbol in alphabet]
            else:
                processed[v] = False

        v = get_ripe()
        while not v == None:
            processed[v] = True
            s[v] = [calculate_s(symbol, v) for symbol in alphabet]
            v_last = v
            v = get_ripe()

        backtrack(v_last, update_assignments(v_last, s[v_last]))
        return min([s[v_last][c] for c in range(len(alphabet))])

    assignments = LabelledTree(T.N)
    assignments.initialize_from(T)

    return sum([SmallParsimonyC([v[i] for l, v in T.labels.items()]) for i in range(len(T.labels[0]))]), assignments


def countMutations(s, t):
     return len([a for (a,b) in zip(s,t) if a!=b])

def print_assignments(assignments):
    assignments.nodes.sort()

    for node in assignments.nodes:
        if node in assignments.edges:
            for edge in assignments.edges[node]:
                end, weight = edge
                if node in assignments.labels and end in assignments.labels:
                    print('{0}->{1}:{2}'.format(assignments.labels[node],
                                                assignments.labels[end],
                                                countMutations(assignments.labels[node], assignments.labels[end])))

def AdaptSmallParsimonyToUnrootedTrees(N,T):

    def assign_root():

        a=T.nodes[len(T.nodes)-1]
        b,_=T.edges[a][0]
        T.unlink(a,b)
        c=T.next_node()
        T.link(c,a)
        T.link(c,b)
        return (a,b,c)
    
    a,b,root=assign_root()
    
    T.remove_backward_links(root)

    return a,b,root,T

                        
if __name__=='__main__':

    def parse(input):
        N=-1
        lines=[]
        for line in input:
            if N==-1:
                N=int(line.strip())
            else:
                lines.append(line.strip())
        return N,LabelledTree.parse(N,lines,bidirectional=True)
    
 
    with open('C:/Users/iMan/Desktop/Problem 8/rosalind_ba7g.txt') as f:
        N,T=parse(f)
        a,b,root,T1= AdaptSmallParsimonyToUnrootedTrees(N,T)
        score,assignments=SmallParsimony(T1)
        # This is the fixup at the emd of processing
        assignments.unlink(root,b)     
        assignments.unlink(root,a)
        assignments.link(a,b)
        
        print (score)
        print_assignments(assignments)