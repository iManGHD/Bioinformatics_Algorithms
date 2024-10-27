def trie_creator(patterns, root=1):
    next_node = root + 1
    Trie      = {root:{}}
    for Pattern in patterns:
        currentNode = root
        for currentSymbol in Pattern:
            if currentSymbol in Trie[currentNode]:
                currentNode = Trie[currentNode][currentSymbol]
            else:
                new_node                         = next_node
                Trie[new_node]                   = {}
                Trie[currentNode][currentSymbol] = new_node
                currentNode                      = new_node
                next_node                       += 1

    return Trie


def matchPrefix(text, trie):
    i      = iter(text)
    symbol = next(i)
    v      = min(trie.keys())
    path   = [v]
    while True:
        if len(trie[v])==0:
            return path
        elif symbol in trie[v]:
            w      = trie[v][symbol]
            try:
                symbol = next(i)
                v      = w
                path.append(v)
            except StopIteration:
                if len(trie[w])==0:
                    return path
                else:
                    return []
        else:
            return []

def match(text, trie):
    return [i for i in range(len(text)) if matchPrefix(text[i:], trie)]


file = open("C:/Users/iMan/desktop/rosalind_ba9b.txt","r")
text = file.read()
strings = []
strings = text.split("\n")
Trie = trie_creator(strings[1:])
Result = match(strings[0], Trie)

Output = ' '.join(str(n) for n in Result)
print(Output)