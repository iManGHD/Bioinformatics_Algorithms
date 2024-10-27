def getN(ch, row, column):
    n = 0
    i = 0
    while i <= row:
        if ch == column[i]:
            n += 1
        i += 1
    return n


def get_char(ch, column, seq):
    pos = 0
    count = 0
    for i in range(len(column)):
        if column[i] == ch:
            pos = i
            count += 1
            if count == seq:
                return pos, count


def lastToFirst(Transform, i):
    last = Transform
    first = sorted(Transform)
    ch = last[i]
    n = getN(ch,i,last)
    pos,count = get_char(ch,first,n)
    return pos

def bw_match(LastColumn, Patterns):
    def LastColumnContains(symbol, top, bottom):
        topIndex = None
        bottomIndex = None
        N = len(LastColumn)

        for i in range(top, N):
            if LastColumn[i] == symbol:
                bottomIndex = i
                break

        for i in range(bottom, -1, -1):
            if LastColumn[i] == symbol:
                topIndex = i
                break

        return topIndex, bottomIndex

    def match(Pattern):
        top = 0
        bottom = len(LastColumn) - 1
        while top <= bottom:
            if len(Pattern) > 0:
                symbol = Pattern[-1]
                Pattern = Pattern[:-1]
                topIndex, bottomIndex = LastColumnContains(symbol, top, bottom)
                if type(topIndex) == int and type(bottomIndex) == int:
                    top = lastToFirst(LastColumn, bottomIndex)
                    bottom = lastToFirst(LastColumn, topIndex)
                else:
                    return 0
            else:
                return bottom - top + 1
        return 0

    return [match(Pattern) for Pattern in Patterns]


file = open("C:/Users/iMan/desktop/rosalind_ba9l.txt","r")
text = file.read()
strings = []
strings = text.split("\n")
Result = bw_match(strings[0], strings[1].split())
output = ' '.join(str(i) for i in Result)
print(output)