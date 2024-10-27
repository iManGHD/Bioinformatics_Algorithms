def betterBwMatch(lastColumn, patterns):

    def count(symbol, i):
        return sum([1 for ch in lastColumn[:i] if ch == symbol])

    def firstOccurence(ch):
        for i in range(len(FirstColumn)):
            if FirstColumn[i] == ch:
                return i

    def lastColumnContains(symbol, top, bottom):
        topIndex = None
        bottomIndex = None
        N = len(lastColumn)

        for i in range(top, N):
            if lastColumn[i] == symbol:
                bottomIndex = i
                break

        for i in range(bottom, -1, -1):
            if lastColumn[i] == symbol:
                topIndex = i
                break

        return topIndex, bottomIndex

    def match(Pattern):
        top = 0
        bottom = len(lastColumn) - 1
        while top <= bottom:
            if len(Pattern) > 0:
                symbol = Pattern[-1]
                Pattern = Pattern[:-1]
                topIndex, bottomIndex = lastColumnContains(symbol, top, bottom)
                if type(topIndex) == int and type(bottomIndex) == int:
                    top = FirstOccurences[symbol] + count(symbol, top)
                    bottom = FirstOccurences[symbol] + count(symbol, bottom + 1) - 1
                else:
                    return 0
            else:
                return bottom - top + 1
        return 0

    FirstColumn = sorted(lastColumn)
    FirstOccurences = {ch: firstOccurence(ch) for ch in FirstColumn}
    return [match(Pattern) for Pattern in patterns]


file = open("C:/Users/iMan/desktop/rosalind_ba9m.txt","r")
text = file.read()
strings = []
strings = text.split("\n")
Result = betterBwMatch(strings[0], strings[1].split())
output = ' '.join(str(i) for i in Result)
print(output)