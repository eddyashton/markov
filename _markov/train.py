def pairs(s):
    return zip(s[:-1], s[1:])


def train_model(filename):
    lines = open(filename).read().splitlines()

    model = {}
    for line in lines:
        for c1, c2 in pairs(line):
            if c2 not in model[c1]:
                model[c1][c2] = 0
            model[c1][c2] += 1
            print(c1, c2)
