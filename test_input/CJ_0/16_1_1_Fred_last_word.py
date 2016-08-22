from base import *

class LastWordSolver (CodeJamSolver):
    def read_instance(self, f):
        return f.readline().strip()

    def solve_instance(self, input):
        # print input
        candidates = [input[0]]
        new = []
        for l in input[1:]:
            for c in candidates:
                new.append(l + c)
                new.append(c+l)
            candidates = new
            new = []

        return sorted(candidates)[-1]



if __name__ == '__main__':
    solver = LastWordSolver()
    solver.run()
    # print solver.solve_instance('JAM')
