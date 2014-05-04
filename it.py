class countdown(object):

    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def next(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

for i in countdown(5):
    print i

print tuple(countdown(5))
