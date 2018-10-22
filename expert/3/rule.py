from random import uniform

from membership_functions import MembershipFunction
from norm import mamdani_norm
from norm import sugeno_norm


class SugenoRuleConclusion:

    def __init__(self, p=None, q=None, r=None):

        if p:
            self.p = float(p)
        else:
            self.p = uniform(0.0, 1.0)
        if q:
            self.q = float(q)
        else:
            self.q = uniform(0.0, 1.0)
        if r:
            self.r = float(r)
        else:
            self.r = uniform(0.0, 1.0)

    def __repr__(self):
        return "%3f * x + %3f * y + %3f" % (self.p, self.q, self.r)

    def compute(self, x, y):
        return x * self.p + y * self.q + self.r


class Rule:

    def __init__(self, mfA, mfB, norm, conclusion):

        self.mfA = mfA
        self.mfB = mfB
        self.norm = norm
        self.conclusion = conclusion

    def __repr__(self):
        return "%s AND %s ---> %s" % (self.mfA, self.mfB, self.conclusion)

    def conclude(self, x, y):

        if isinstance(self.conclusion, MembershipFunction):
            return self.conclusion.peak()
        return self.conclusion.compute(x, y)

    def weight(self, x, y):

        return self.norm(self.mfA.compute(x), self.mfB.compute(y))


def read_rule(line, A, B, output):

    A_type, B_type, output_type = line.strip(" \n").split(' ')

    mfA = A[A_type]
    mfB = B[B_type]

    if ':' in output_type:
        norm = sugeno_norm
        conclusion = SugenoRuleConclusion(*output_type.strip(" \n").split(':'))
    else:
        norm = mamdani_norm
        conclusion = output[output_type]
    
    return Rule(mfA, mfB, norm, conclusion)
