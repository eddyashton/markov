def pairs(s):
    return zip(s[:-1], s[1:])

def train_model(filename):
    model = {}
    with open(filename) as r:
        lines = (line.strip() for line in r.readlines())
        for line in lines:
            line = line.split(" ")
            for a, b in pairs(["\n"] + line + ["\n"]):
                if a not in model:
                    model[a] = {}

                if b not in model[a]:
                    model[a][b] = 0

                model[a][b] += 1

    return model
