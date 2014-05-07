"""
>>> time python2.7 ./filename.py > /dev/null
real    0m17.911s
user    0m17.059s
sys 0m0.834s

>>> time pypy ./filename.py > /dev/null  # pypy2.2.1  gevent 1.1.0-dev
real    0m14.118s
user    0m9.993s
sys 0m0.787s

"""

from gevent.pool import Pool

SIZE = 655350

pool = Pool(SIZE)

def incr(n):
    b = n+1
    return b

for i in xrange(SIZE):
    pool.wait_available()
    pool.spawn(incr, i)

pool.join()
