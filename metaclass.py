class Meta(type):

    """
    """

    def __new__(mcs, name, bases, attrs):
        _init = attrs.get('__init__')
        print 'in class %s' % name

        def __init__(self, *args, **kwargs):
            if _init:
                print('in meta init %s' % str(args))
                _init(self, *args, **kwargs)
        attrs['__init__'] = __init__

        return type.__new__(mcs, name, bases, attrs)


class HasInit(object):
    __metaclass__ = Meta

    def __init__(self, *args, **kwargs):
        print('in HasInit init %s' % str(args))


class HasNoInit(object):
    __metaclass__ = Meta

    def __init__(self, *args, **kwargs):
        print('in HasNoInit init %s' % str(args))


if __name__ == '__main__':
    HasInit(1)
    HasInit(2)
    HasNoInit(1)
    HasNoInit(2)
