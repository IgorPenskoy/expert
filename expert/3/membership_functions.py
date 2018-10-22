class MembershipFunction:

    def __repr__(self):
        return str([
            "%7.3f" % x for x in [
                getattr(self, attr, None) for attr in "abcd"
            ] if x is not None
        ])


class TriangularMembershipFunction(MembershipFunction):

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def compute(self, x):

        if self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif x == self.b:
            return 1
        elif self.b < x < self.c:
            return (self.c - x) / (self.c - self.b)

        return 0
    
    def peak(self):
        return (self.a + self.c) / 2


class RMembershipFunction(MembershipFunction):

    def __init__(self, c, d):

        self.c = c
        self.d = d

    def compute(self, x):

        if x <= self.c:
            return 1
        elif self.c < x < self.d:
            return (self.d - x) / (self.d - self.c)

        return 0

    def peak(self):
        return (self.c + self.d) / 2


class LMembershipFunction(MembershipFunction):

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def compute(self, x):

        if x <= self.a:
            return 0
        elif self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)

        return 1

    def peak(self):
        return (self.a + self.b) / 2


class TrapezoidalMembershipFunction(MembershipFunction):

    def __init__(self, a, b, c, d):

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def compute(self, x):

        if self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b <= x <= self.c:
            return 1
        elif self.c < x < self.d:
            return (self.d - x) / (self.d - self.c)

        return 0

    def peak(self):
        return (self.b + self.c) / 2
