from pprint import pprint

l = [5,6,5,89,5,56,5]
l1 = [1, 0, 1]




def more_than_half(seq):
    times = 0
    candidate = None

    for item in seq:
        if times == 0:
            candidate = item
            times +=1
        else:
            if candidate == item:
                times +=1
            else:
                times -= 1
    return candidate

for item in (l, l1):
    print('more than half item for %s' % item)
    pprint(more_than_half(item))
