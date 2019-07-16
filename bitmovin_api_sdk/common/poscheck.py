class PositionalArgumentsError(Exception):
    def __init__(self, f, n, message=None):
        super(PositionalArgumentsError, self).__init__()
        self.f = f
        self.n = n
        self.message = message

    def __str__(self):
        if self.n == 0:
            return "%s takes only keyword arguments" % self.f.__name__
        elif self.message:
            return self.message
        else:
            return 'all arguments to %s after the first %s must be keyword arguments' % (self.f.__name__, self.n)


def poscheck(f):
    return poscheck_except(0)(f)


def poscheck_model(f):
    error_message = """Models cannot be initialized using positional arguments. Use keyword arguments instead.

    Example:

    Wrong:
    encoding = Encoding('my encoding name', 'my encoding description')

    Correct:
    encoding = Encoding(name='my encoding name', description='my encoding description')
    """
    return poscheck_except(1, message=error_message)(f)


def poscheck_except(n, message=None):
    def helper(f):
        def checked_f(*args, **kwargs):
            if len(args) > n:
                if message:
                    raise PositionalArgumentsError(f, n, message=message)
                else:
                    raise PositionalArgumentsError(f, n)
            return f(*args, **kwargs)
        return checked_f
    return helper
