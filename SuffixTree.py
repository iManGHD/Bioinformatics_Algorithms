
# Suffix Tree

class Node:
    def __init__(self, sub="", children=None):
        self.sub = sub
        self.ch = children or []


class SuffixTree:
    def __init__(self, str):
        self.nodes = [Node()]
        for i in range(len(str)):
            self.addingSuffix(str[i:])

    def addingSuffix(self, suf):
        n = 0
        i = 0
        while i < len(suf):
            b = suf[i]
            x2 = 0
            while True:
                children = self.nodes[n].ch
                if x2 == len(children):
                    n2 = len(self.nodes)
                    self.nodes.append(Node(suf[i:], []))
                    self.nodes[n].ch.append(n2)
                    return
                n2 = children[x2]
                if self.nodes[n2].sub[0] == b:
                    break
                x2 = x2 + 1

            sub2 = self.nodes[n2].sub
            j = 0
            while j < len(sub2):
                if suf[i + j] != sub2[j]:
                    n3 = n2
                    n2 = len(self.nodes)
                    self.nodes.append(Node(sub2[:j], [n3]))
                    self.nodes[n3].sub = sub2[j:]
                    self.nodes[n].ch[x2] = n2
                    break
                j = j + 1
            i = i + j
            n = n2

    def printTreeEdges(self):
        if len(self.nodes) == 0:
            return

        def f(n, pre):
            children = self.nodes[n].ch
            if len(children) == 0 and n != 0:
                print(self.nodes[n].sub)
                return
            if n!= 0 :
             print(self.nodes[n].sub)
            for c in children[:-1]:
                f(c, pre)
            f(children[-1], pre )
        f(0, "")


if __name__ == '__main__':

    inputString = input()
    SuffixTree(inputString).printTreeEdges()
