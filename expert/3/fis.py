from collections import OrderedDict

from membership_functions import LMembershipFunction
from membership_functions import RMembershipFunction
from membership_functions import TrapezoidalMembershipFunction
from membership_functions import TriangularMembershipFunction
from rule import read_rule


class FIS:

    def read_fuzzy_var(self, filename):

        def read_values(line):
            return [float(x) for x in line.strip(" \n").split(' ')]

        def read_mf(line):
            values = read_values(line)
            count = len(values)

            if count == 2:
                a = values[0]
                b = values[1]

                if a < b:
                    return LMembershipFunction(a, b)
                return RMembershipFunction(a, b)
            elif count == 3:
                return TriangularMembershipFunction(values[0], values[1], values[2])
            
            return TrapezoidalMembershipFunction(values[0], values[1], values[2], values[3])

        _file = open(filename, 'r')
        lines = _file.readlines()
        var = OrderedDict()
        
        for line in lines:
            mf_name, mf_values = line.strip(" \n").split(':')
            var[mf_name] = read_mf(mf_values)

        _file.close()

        return var

    def print_fuzzy_var(self, name, var):
        print()
        print("%s:\n" % name)
        for mf_name, mf_values in var.items():
            print("%3s: %s" % (mf_name, mf_values))
        print()

    def __init__(self, error_filename, error_change_filename, output_filename, rules_filename):

        self.rules = []

        error = self.read_fuzzy_var(error_filename)
        error_change = self.read_fuzzy_var(error_change_filename)
        output = self.read_fuzzy_var(output_filename)

        # self.print_fuzzy_var("ERROR", error)
        # self.print_fuzzy_var("ERROR CHANGE", error_change)
        # self.print_fuzzy_var("OUTPUT", output)

        rules_file = open(rules_filename, 'r')
        lines = rules_file.readlines()
        rules_file.close()

        for line in lines:
            self.rules.append(read_rule(line, error, error_change, output))

        # print("RULES:\n")
        # i = 0
        # for rule in self.rules:
        #     i += 1
        #     print("%d) %s\n" % (i, rule))


    def sum_weights(self, x, y):

        if self.rules:
            return sum(rule.weight(x, y) for rule in self.rules)

        return 0

    def compute(self, x, y):

        weight_sum = self.sum_weights(x, y)

        if weight_sum:
            return sum(rule.weight(x, y) * rule.conclude(x, y) for rule in self.rules) / weight_sum

        return 0
