import collections


def read_data_from(file_name):
    with open(file_name) as f:
        data = f.readlines()

    for i in range(0, len(data)):
        data[i] = data[i].strip()

    return data


def prefix(string):
    return string[:len(string)-1]


def suffix(string):
    return string[1:]


def overlap(patterns):
    pat_len = len(patterns)
    pairs = {}
    for i in range(pat_len):
        for j in range(pat_len):
            if (i != j) and (suffix(patterns[i]) == prefix(patterns[j])):
                pairs[patterns[i]] = patterns[j]

    od = collections.OrderedDict(sorted(pairs.items()))
    for key in od.keys():
       print(str(key) + " -> " + str(od[key]))


if __name__ == "__main__":

    patterns = []
    file = open("C:/Users/iMan/desktop/rosalind_ba3c.txt","r")
    text = file.read()
    patterns = text.split("\n")
    overlap(patterns)