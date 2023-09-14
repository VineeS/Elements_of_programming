import collections

Interval = collections.namedtuple('Interval',('left','right'))

interval = [
    Interval(-4,-1),
    Interval(0,2),
    Interval(3,6),
    Interval(7,9),
    Interval(11,12),
    Interval(14,17),
]
new_interval = Interval(1,8)

def merge_interval(disjoint_interval, new_interval):
    i , result = 0,[]
    while (i< len(disjoint_interval) and new_interval.left > disjoint_interval[i].right):
        result.append(disjoint_interval[i])
        i+=1
    while (i< len(disjoint_interval) and new_interval.right >= disjoint_interval[i].left):
        new_interval = Interval(
            min(new_interval.left, disjoint_interval[i].left),
            max(new_interval.right, disjoint_interval[i].right)
        )
        print(new_interval)
        i+=1
    
    return result+[new_interval],disjoint_interval[i:]

print(merge_interval(interval, new_interval))