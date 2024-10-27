import os
import sys

from Bio import SeqIO


def computelimblengths(n, j, D):
    return int(
        min([D[i][j] + D[j][k] - D[i][k] for i in range(n) for k in range(n) if j != k and k != i and i != j]) / 2)


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


def create_strings(problem=os.path.basename(sys.argv[0]).split('.')[0],
                   path=os.path.join(os.path.expanduser('~'), 'Downloads'),
                   ext=None,
                   fasta=False,
                   name=None):
    product = []
    with open("C:/Users/iMan/Desktop/rosalind_ba7b.txt", 'r') as f:
        if fasta:
            for record in SeqIO.parse(f, 'C:/Users/iMan/Desktop/rosalind_ba7b.txt'):
                product.append(str(record.seq))
        else:
            for line in f:
                product.append(line.strip())
    return product


if __name__ == '__main__':
    from helpers import read_matrix

    params, D = read_matrix(len_params=2)
    print(computelimblengths(params[0], params[1], D))