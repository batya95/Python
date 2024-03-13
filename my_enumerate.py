class Enumerate:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.index = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.iterable):
            return self.index, self.iterable[self.index]
        raise StopIteration


# Help on class enumerate in module builtins:

# class enumerate(object)
#  |  enumerate(iterable, start=0)
#  |
#  |  Return an enumerate object.
#  |
#  |    iterable
#  |      an object supporting iteration
#  |
#  |  The enumerate object yields pairs containing a count (from start, which
#  |  defaults to zero) and a value yielded by the iterable argument.
#  |
#  |  enumerate is useful for obtaining an indexed list:
#  |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.
#  |
