from pprint import pprint

l = [1, -2,3,10,-4,7,2,5]


def largest_seq(seq):
    # largest seq end with index
    sum_seq = {
        -1: [0, 0],
    }

    for index, item in enumerate(seq):
        if sum_seq[index-1][1] > 0:
            sum_seq[index] = [sum_seq[index-1][0], sum_seq[index-1][1] + seq[index]]
        else:
            sum_seq[index] = [index, seq[index]]
    return sum_seq

pprint(largest_seq(l))
