class SingletonMixin(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonMixin, cls).__new__(cls)
            return cls._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class SingletonClass(SingletonMixin):
    def __init__(self, *args, **kwargs):
        print "init %s %s" % (args, kwargs)


if __name__ == '__main__':
    a = SingletonClass('a')
    import ipdb;ipdb.set_trace()
    b = SingletonClass('b')
    print 'a is b %s' % (a is b, )
